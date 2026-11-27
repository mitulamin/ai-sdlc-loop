#!/usr/bin/env python3
"""Pre-release SkillSpector scan with the LLM analyzers on, and the record that goes with it.

Usage:
  scripts/skillspector-llm-scan.py --record release-scans/<tag>.md [--only GLOB] [--jobs N]
  scripts/skillspector-llm-scan.py --verify release-scans/<tag>.md

Run it before every release or tag, from a clean checkout of the commit you mean to release.
It scans the same targets as scripts/skillspector-scan.py (every skill, agents/, commands/,
template/ and a throwaway install for each harness) but without --no-llm, so SkillSpector sends
the text of those files to the model provider you configure. Do not run it if that is not
acceptable for the files being released. The steps and the record are in RELEASING.md.

Configuration is SkillSpector's own environment variables; this script adds none. It insists on
SKILLSPECTOR_PROVIDER being set, so a missing configuration cannot fall back to a provider you did
not choose, and the provider's credential must be in the environment (for example
ANTHROPIC_API_KEY for SKILLSPECTOR_PROVIDER=anthropic, or OPENAI_API_KEY for openai). Optionally
set SKILLSPECTOR_MODEL. Run `skillspector scan --help` for the full list of providers.

SkillSpector reports a degraded LLM stage (no key, a rejected key, a failed request) as a warning
and still exits 0 with static results only. This script treats that as a failure: a target counts
only if the LLM was requested, every LLM call succeeded, no semantic analyzer failed, every file
was inspected and the run succeeded. The exit code is 2 for a target that does not meet that.

--record writes a Markdown record with the commit, scanner version, provider and model, the
coverage of each target and every finding. A finding that an entry in
.github/skillspector-exceptions.yaml explains (same rule, file, matched text and source line)
is marked as covered by it. Every other finding is written as UNREVIEWED. Exit code 0 means no
unreviewed findings, 1 means there are some; a person then fixes the issue or replaces UNREVIEWED
in the record with one of the dispositions below, and --verify checks the record is complete.

Dispositions (replace UNREVIEWED with exactly one, followed by a reason):
  FIXED: <commit or PR that fixed it>
  FALSE POSITIVE: <why it is not an issue>
  ACCEPTED: <who accepted the risk, and why it ships anyway>

--verify exits 0 only when the record names a commit, says the scan completed, and no finding is
left UNREVIEWED or has a disposition without a reason.
"""
import argparse
import datetime
import fnmatch
import json
import os
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from skillspector_targets import (  # noqa: E402
    ROOT, apply_exceptions, as_list, coverage_problem, dir_targets, find_scanner, harness_targets, load_exceptions, skill_targets,
)

TIMEOUT_SECONDS = 1800
UNREVIEWED = "UNREVIEWED"
DISPOSITION = re.compile(r"^(FIXED|FALSE POSITIVE|ACCEPTED|COVERED BY STATIC EXCEPTION): \S")
SEMANTIC_PREFIX = "semantic_"


def llm_problem(data, proc):
    """Return why this report cannot count as a successful LLM-mode scan, or None."""
    meta = data.get("metadata", {})
    comp = data.get("analysis_completeness") or {}
    if not data.get("execution_successful"):
        return "SkillSpector reported execution_successful=false"
    if not meta.get("llm_requested"):
        return "the LLM was not requested"
    if not meta.get("llm_available"):
        return "no LLM provider was available (check SKILLSPECTOR_PROVIDER and its credential)"
    attempted, succeeded = meta.get("llm_calls_attempted", 0), meta.get("llm_calls_succeeded", 0)
    if meta.get("llm_degraded") or not attempted or succeeded != attempted:
        return f"LLM stage degraded: {succeeded} of {attempted} calls succeeded ({meta.get('llm_error', 'no detail')})"
    for a in comp.get("analyzer_statuses", []):
        if a.get("analyzer_id", "").startswith(SEMANTIC_PREFIX) and a.get("status") not in ("completed", "not_applicable"):
            return f"semantic analyzer {a['analyzer_id']} finished with status {a.get('status')}"
    if not comp.get("is_complete"):
        return f"incomplete coverage ({comp.get('coverage_percent')}%)"
    if "LLM stage degraded" in (proc.stderr or ""):
        return "SkillSpector warned that the LLM stage degraded"
    return None


def scan(target, tmp):
    """Return (target, report data or None, problem or None)."""
    report = tmp / f"{target.name}.json"
    try:
        proc = subprocess.run(
            ["skillspector", "scan", str(target.path), "--fail-on-incomplete", "--format", "json", "--output", str(report)],
            capture_output=True, text=True, timeout=TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        return target, None, f"timed out after {TIMEOUT_SECONDS}s"
    if not report.exists():
        return target, None, (proc.stderr.strip() or proc.stdout.strip())[:300]
    data = json.loads(report.read_text(encoding="utf-8"))
    return target, data, llm_problem(data, proc) or coverage_problem(target, data.get("analysis_completeness"))


def provider_summary(reports):
    seen = {}
    for data in reports:
        prov = data.get("metadata", {}).get("llm_provenance", {})
        adapter = prov.get("provider", {}).get("resolved_adapter", "unknown")
        for a in prov.get("analyzers", []):
            seen.setdefault((adapter, a.get("model", "unknown")), set()).add(a.get("analyzer_id"))
    return sorted(seen)


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True).stdout.strip()


def cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def record(args):
    if not os.environ.get("SKILLSPECTOR_PROVIDER"):
        print("SKILLSPECTOR_PROVIDER is not set. Set it to the provider you chose and export that provider's credential "
              "(see RELEASING.md); this script will not fall back to a default provider.", file=sys.stderr)
        return 2
    _, version, err = find_scanner()
    if err:
        print(err, file=sys.stderr)
        return 2
    exceptions, problems = load_exceptions()
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 2
    skills, err = skill_targets()
    dirs, err2 = dir_targets()
    if err or err2:
        print(err or err2, file=sys.stderr)
        return 2
    dirty = git("status", "--porcelain")
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        harnesses, err = harness_targets(tmp / "installs")
        if err:
            print(err, file=sys.stderr)
            return 2
        targets = skills + dirs + harnesses
        if args.only:
            targets = [x for x in targets if fnmatch.fnmatchcase(x.name, args.only)]
            if not targets:
                print(f"--only {args.only!r} matches no target", file=sys.stderr)
                return 2
        with ThreadPoolExecutor(max_workers=args.jobs) as pool:
            results = list(pool.map(lambda x: scan(x, tmp), targets))
        broken = [(x, p) for x, d, p in results if p]
        for x, p in broken:
            print(f"ERROR {x.name}: not a successful LLM-mode scan: {p}", file=sys.stderr)
        if broken:
            return 2
        rows = []
        for x, data, _ in results:
            own = [(i, e) for i, e in enumerate(exceptions) if any(fnmatch.fnmatchcase(x.name, g) for g in as_list(e["target"]))]
            unexplained, _hits = apply_exceptions(x.path, data.get("issues", []), own)
            ids = {id(f) for f in unexplained}
            for f in data.get("issues", []):
                loc = f.get("location", {})
                disp = UNREVIEWED if id(f) in ids else "COVERED BY STATIC EXCEPTION: same rule, file, text and line as an entry in .github/skillspector-exceptions.yaml"
                rows.append((x.name, f.get("id"), f.get("severity"), f"{loc.get('file')}:{loc.get('start_line')}",
                             f.get("finding"), f.get("explanation"), disp))
        reports = [d for _, d, _ in results]

    open_rows = [r for r in rows if r[6] == UNREVIEWED]
    models = provider_summary(reports)
    calls = sum(d["metadata"].get("llm_calls_succeeded", 0) for d in reports)
    lines = [
        "# SkillSpector LLM-mode scan record", "",
        f"- Commit: {git('rev-parse', 'HEAD')}" + (" (working tree has uncommitted changes)" if dirty else ""),
        f"- Date (UTC): {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M')}",
        f"- Scanner: {version}",
        f"- Provider and model: " + ("; ".join(f"{p} / {m}" for p, m in models) or "unknown"),
        f"- Targets scanned: {len(targets)} ({'all' if not args.only else 'only ' + args.only}); every file inspected: yes",
        f"- LLM calls succeeded: {calls}, failed: 0",
        "- Scan completed: yes",
        f"- Findings: {len(rows)} in total, {len(open_rows)} {UNREVIEWED}", "",
        "## Findings", "",
    ]
    if rows:
        lines += ["| Target | Rule | Severity | Where | Matched | Why SkillSpector flagged it | Disposition |", "| --- | --- | --- | --- | --- | --- | --- |"]
        lines += ["| " + " | ".join(cell(c) for c in r) + " |" for r in rows]
    else:
        lines.append("None.")
    out = Path(args.record)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {out}: {len(targets)} targets, {len(rows)} findings, {len(open_rows)} {UNREVIEWED}")
    return 1 if open_rows else 0


def verify(path):
    p = Path(path)
    if not p.is_file():
        print(f"{path}: no such record", file=sys.stderr)
        return 1
    text = p.read_text(encoding="utf-8")
    problems = []
    if not re.search(r"^- Commit: [0-9a-f]{7,40}", text, re.M):
        problems.append("no commit named")
    if "- Scan completed: yes" not in text:
        problems.append("the record does not say the scan completed")
    if "(all); every file inspected: yes" not in text:
        problems.append("the record is not of a full scan (it was made with --only, or a file was not inspected)")
    if "uncommitted changes" in text:
        problems.append("the scan ran on a working tree with uncommitted changes")
    in_table = False
    for n, line in enumerate(text.split("\n"), 1):
        if line.startswith("| Target |"):
            in_table = True
            continue
        if in_table and line.startswith("| ") and not line.startswith("| ---"):
            cells = re.split(r"(?<!\\)\|", line.strip().strip("|"))
            disposition = cells[-1].strip()
            if disposition == UNREVIEWED or not DISPOSITION.match(disposition):
                problems.append(f"line {n}: finding has no valid disposition ({disposition[:40]!r})")
    if problems:
        print("\n".join(f"{path}: {x}" for x in problems), file=sys.stderr)
        return 1
    print(f"OK: {path} names a commit, says the scan completed and has a disposition with a reason for every finding")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--record", metavar="PATH", help="run the scan and write the record here")
    mode.add_argument("--verify", metavar="PATH", help="check a record is complete")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--only", metavar="GLOB", help="scan only targets whose name matches (not for a release record)")
    args = ap.parse_args()
    if args.verify:
        return verify(args.verify)
    return record(args)


if __name__ == "__main__":
    sys.exit(main())
