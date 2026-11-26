#!/usr/bin/env python3
"""Scan every skills/<id>-<slug>/ folder with NVIDIA SkillSpector.

Usage: scripts/skillspector-scan.py [--jobs N]

SkillSpector (https://github.com/NVIDIA/SkillSpector, Apache-2.0, pip install
skillspector) does not take a baseline for a recursive scan, so this runs one
`skillspector scan` per skill folder. It runs static analysis only (--no-llm),
so no skill text leaves the machine and no API key is needed, and it fails on
any finding (--fail-on-findings) and on incomplete coverage
(--fail-on-incomplete), for example a SKILL.md whose front matter does not
parse. Reviewed false positives are listed with reasons in
.github/skillspector-exceptions.yaml. Each exception must suppress at least one
finding for every glob in its `skill` list, or the scan fails, so the list
cannot go stale. Unknown keys in an exception are rejected.

Exits 0 when every skill is clean, 1 on findings, 2 when SkillSpector cannot
be run. It never reports a pass if the scanner is missing.
"""
import argparse
import fnmatch
import json
import re
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
EXCEPTIONS = ROOT / ".github" / "skillspector-exceptions.yaml"
SCANNER_VERSION = "2.13.7"
EXPECTED_SKILLS = 103
TIMEOUT_SECONDS = 600
EXCEPTION_KEYS = {"skill", "id", "path", "message", "reason"}


def as_list(value):
    return value if isinstance(value, list) else [value]


def scan(skill_dir, exceptions, tmp):
    """Return (name, exit code, issues, hits, completeness, error text).

    hits is the set of exception indexes that suppressed at least one finding.
    Each rule's reason starts with its index, which SkillSpector echoes back as
    the suppression reason, so a suppressed finding is attributed to the rule
    that actually matched it.
    """
    name = skill_dir.name
    own = [(i, e) for i, e in enumerate(exceptions) if any(fnmatch.fnmatchcase(name, g) for g in as_list(e["skill"]))]
    rules = []
    for i, e in own:
        rule = {"id": e["id"], "reason": f"EXCEPTION-{i}: " + " ".join(e["reason"].split())}
        for key in ("path", "message"):
            if key in e:
                rule[key] = e[key]
        rules.append(rule)
    baseline = tmp / f"{name}.baseline.yaml"
    baseline.write_text(yaml.safe_dump({"version": 2, "rules": rules}), encoding="utf-8")
    report = tmp / f"{name}.json"
    try:
        proc = subprocess.run(
            ["skillspector", "scan", str(skill_dir), "--no-llm", "--fail-on-findings", "--fail-on-incomplete",
             "--baseline", str(baseline), "--show-suppressed", "--format", "json", "--output", str(report)],
            capture_output=True, text=True, timeout=TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        return name, 2, [], set(), None, f"timed out after {TIMEOUT_SECONDS}s"
    if not report.exists():
        return name, 2, [], set(), None, proc.stderr.strip() or proc.stdout.strip()
    data = json.loads(report.read_text(encoding="utf-8"))
    if not data.get("execution_successful"):
        return name, 2, [], set(), data.get("analysis_completeness"), "SkillSpector reported execution_successful=false"
    hits = set()
    for s in data.get("suppressed", []):
        m = re.match(r"EXCEPTION-(\d+): ", s.get("suppression_reason", ""))
        if m:
            hits.add(int(m.group(1)))
    return name, proc.returncode, data.get("issues", []), hits, data.get("analysis_completeness"), proc.stderr.strip()


def load_exceptions():
    data = yaml.safe_load(EXCEPTIONS.read_text(encoding="utf-8"))
    exceptions = data["exceptions"]
    problems = []
    for n, e in enumerate(exceptions):
        for key in ("skill", "id", "reason"):
            if key not in e:
                problems.append(f"exception #{n} lacks '{key}': {e}")
        for key in e:
            if key not in EXCEPTION_KEYS:
                problems.append(f"exception #{n} has unknown key '{key}': {e}")
    return exceptions, problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=4)
    args = ap.parse_args()

    exe = shutil.which("skillspector")
    if not exe:
        print(f"skillspector is not installed: pip install 'skillspector=={SCANNER_VERSION}'", file=sys.stderr)
        return 2
    version = subprocess.run([exe, "--version"], capture_output=True, text=True).stdout.strip()
    print(version)
    if SCANNER_VERSION not in version:
        print(f"expected SkillSpector {SCANNER_VERSION}; the reviewed exceptions only apply to that version", file=sys.stderr)
        return 2
    exceptions, problems = load_exceptions()
    if problems:
        print("\n".join(f"{EXCEPTIONS.name}: {p}" for p in problems), file=sys.stderr)
        return 2

    skills = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
    if len(skills) != EXPECTED_SKILLS:
        print(f"expected {EXPECTED_SKILLS} skill folders, found {len(skills)}", file=sys.stderr)
        return 2
    failed, broken = [], []
    hits_by_skill = {}
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        with ThreadPoolExecutor(max_workers=args.jobs) as pool:
            results = list(pool.map(lambda d: scan(d, exceptions, tmp), skills))
    for name, code, issues, hit, completeness, err in results:
        hits_by_skill[name] = hit
        if code == 2:
            broken.append((name, err))
        elif code != 0:
            failed.append((name, issues, completeness, err))

    for name, err in broken:
        print(f"ERROR {name}: skillspector could not scan it: {err}", file=sys.stderr)
    for name, issues, completeness, err in failed:
        print(f"FAIL {name}")
        for f in issues:
            loc = f.get("location", {})
            print(f"  {f.get('id')} {f.get('severity')} {f.get('pattern')} at {loc.get('file')}:{loc.get('start_line')}: {str(f.get('finding'))[:100]!r}")
        if completeness and not completeness.get("is_complete", True):
            print(f"  incomplete coverage ({completeness.get('coverage_percent')}%): {json.dumps(completeness.get('ledger_exceptions', []))[:600]}")
        if not issues and not (completeness and not completeness.get("is_complete", True)):
            print(f"  {err[:300]}")
    stale = []
    for i, e in enumerate(exceptions):
        for glob in as_list(e["skill"]):
            if not any(i in hits_by_skill[n] for n in hits_by_skill if fnmatch.fnmatchcase(n, glob)):
                stale.append(e)
                print(f"STALE exception suppressed nothing for skill glob {glob!r}: id={e['id']} path={e.get('path')} message={e.get('message')}")

    if broken:
        return 2
    if failed or stale:
        print(f"SkillSpector: {len(failed)} of {len(skills)} skills have unexplained findings, {len(stale)} stale exceptions")
        return 1
    print(f"OK: SkillSpector scanned {len(skills)} skills (static, --no-llm): no unexplained findings, {len(exceptions)} reviewed exceptions, each in use")
    return 0


if __name__ == "__main__":
    sys.exit(main())
