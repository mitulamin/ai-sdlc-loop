#!/usr/bin/env python3
"""Scan everything agent-facing that this repo ships with NVIDIA SkillSpector.

Usage: scripts/skillspector-scan.py [--jobs N]

SkillSpector (https://github.com/NVIDIA/SkillSpector, Apache-2.0, pip install
skillspector) does not take a baseline for a recursive scan, so this runs one
`skillspector scan` per target. The targets are:

  - each skill folder listed in data/skill-principle-map.json (and it verifies
    skills/ on disk matches the map);
  - agents/ and commands/ (the generated loop agents and slash commands);
  - template/ (the project template, including template/bootstrap/);
  - for each harness in data/harnesses.json, a throwaway install made by
    scripts/install-harness.py, minus the installed skill copies. That covers
    the files the installer writes that are not scanned any other way: the
    installed agents and commands as that harness reads them, its rules and
    settings files, and the shared reference pages. The installed skill copies
    differ from skills/ only in front matter and links, so the skills are scanned
    once, from skills/. A command that a harness installs as a skill folder is
    scanned, because it is not a copy of anything under skills/.

It runs static analysis only (--no-llm), so no text leaves the machine and no API
key is needed, and it fails on incomplete coverage (--fail-on-incomplete), for
example a SKILL.md whose front matter does not parse. It also fails unless
SkillSpector saw every file under a target, so a file type it skips cannot hide.
The model-assisted scan that runs before a release is scripts/skillspector-llm-scan.py.

Reviewed false positives are listed with non-empty reasons in
.github/skillspector-exceptions.yaml. SkillSpector's own baseline matches by
rule, file and matched text, so a second hit with the same text in the same file
would be suppressed silently. This script therefore matches the raw findings
itself, one finding at a time: an exception must match the rule id, the file,
the matched text and the full source line the finding sits on (`line`), and it
may suppress at most `max_per_file` findings in any one file (default 1). Any
finding left over fails the scan. Each exception must also suppress at least one
finding for every glob in its `target` list, or the scan fails, so the list
cannot go stale. Unknown keys in an exception are rejected.

Exits 0 when every target is clean, 1 on findings or stale exceptions, 2 when
SkillSpector cannot be run or inputs are invalid. It never reports a pass if
the scanner is missing.
"""
import argparse
import fnmatch
import json
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from skillspector_targets import (  # noqa: E402
    EXCEPTIONS, apply_exceptions, as_list, coverage_problem, dir_targets, find_scanner, harness_targets,
    load_exceptions, skill_targets,
)

TIMEOUT_SECONDS = 600


def scan(target, exceptions, tmp):
    """Return (name, exit code, unexplained findings, hits, coverage problem, error text).

    hits is the set of exception indexes that explained at least one finding.
    """
    name = target.name
    own = [(i, e) for i, e in enumerate(exceptions) if any(fnmatch.fnmatchcase(name, g) for g in as_list(e["target"]))]
    report = tmp / f"{name}.json"
    try:
        proc = subprocess.run(
            ["skillspector", "scan", str(target.path), "--no-llm", "--fail-on-incomplete",
             "--format", "json", "--output", str(report)],
            capture_output=True, text=True, timeout=TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        return name, 2, [], set(), None, f"timed out after {TIMEOUT_SECONDS}s"
    if not report.exists():
        return name, 2, [], set(), None, proc.stderr.strip() or proc.stdout.strip()
    data = json.loads(report.read_text(encoding="utf-8"))
    if not data.get("execution_successful"):
        return name, 2, [], set(), None, "SkillSpector reported execution_successful=false"
    unexplained, hits = apply_exceptions(target.path, data.get("issues", []), own)
    problem = coverage_problem(target, data.get("analysis_completeness"))
    if proc.returncode not in (0, 1):
        return name, 2, unexplained, hits, problem, proc.stderr.strip()
    # Exit code 1 is SkillSpector's own risk gate over all raw findings, which includes the
    # ones reviewed as false positives. This script's gate is unexplained findings and coverage.
    code = 1 if unexplained or problem else 0
    return name, code, unexplained, hits, problem, proc.stderr.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--only", metavar="GLOB", help="scan only the targets whose name matches (for working on exceptions; the staleness check is skipped)")
    args = ap.parse_args()

    _, version, err = find_scanner()
    if version:
        print(version)
    if err:
        print(err, file=sys.stderr)
        return 2
    exceptions, problems = load_exceptions()
    if problems:
        print("\n".join(f"{EXCEPTIONS.name}: {p}" for p in problems), file=sys.stderr)
        return 2

    skills, err = skill_targets()
    if err:
        print(err, file=sys.stderr)
        return 2
    dirs, err = dir_targets()
    if err:
        print(err, file=sys.stderr)
        return 2
    failed, broken = [], []
    hits_by_target = {}
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
            results = list(pool.map(lambda d: scan(d, exceptions, tmp), targets))
    for name, code, issues, hit, problem, err in results:
        hits_by_target[name] = hit
        if code == 2:
            broken.append((name, err))
        elif code != 0:
            failed.append((name, issues, problem, err))

    for name, err in broken:
        print(f"ERROR {name}: skillspector could not scan it: {err}", file=sys.stderr)
    for name, issues, problem, err in failed:
        print(f"FAIL {name}")
        for f in issues:
            loc = f.get("location", {})
            print(f"  {f.get('id')} {f.get('severity')} {f.get('pattern')} at {loc.get('file')}:{loc.get('start_line')}: {str(f.get('finding'))[:100]!r}")
        if problem:
            print(f"  {problem}")
        if not issues and not problem:
            print(f"  {err[:300]}")
    stale = []
    for i, e in enumerate(exceptions):
        for glob in ([] if args.only else as_list(e["target"])):
            if not any(i in hits_by_target[n] for n in hits_by_target if fnmatch.fnmatchcase(n, glob)):
                stale.append(e)
                print(f"STALE exception suppressed nothing for target glob {glob!r}: id={e['id']} path={e.get('path')} message={e.get('message')}")

    if broken:
        return 2
    if failed or stale:
        print(f"SkillSpector: {len(failed)} of {len(targets)} targets have unexplained findings or incomplete coverage, {len(stale)} stale exceptions")
        return 1
    if args.only:
        print(f"OK for --only {args.only!r}: {len(targets)} targets have no unexplained findings (not a full scan)")
        return 0
    print(f"OK: SkillSpector scanned {len(targets)} targets ({len(skills)} skills, {', '.join(d.name for d in dirs)}, {len(harnesses)} harness installs; static, --no-llm): "
          f"every file inspected, no unexplained findings, {len(exceptions)} reviewed exceptions, each in use")
    return 0


if __name__ == "__main__":
    sys.exit(main())
