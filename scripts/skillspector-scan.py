#!/usr/bin/env python3
"""Scan every skills/<id>-<slug>/ folder with NVIDIA SkillSpector.

Usage: scripts/skillspector-scan.py [--jobs N]

SkillSpector (https://github.com/NVIDIA/SkillSpector, Apache-2.0, pip install
skillspector) does not take a baseline for a recursive scan, so this runs one
`skillspector scan` per skill folder listed in data/skill-principle-map.json
(and verifies skills/ on disk matches the map). It runs static analysis only
(--no-llm), so no skill text leaves the machine and no API key is needed, and
it fails on incomplete coverage (--fail-on-incomplete), for example a SKILL.md
whose front matter does not parse.

Reviewed false positives are listed with non-empty reasons in
.github/skillspector-exceptions.yaml. SkillSpector's own baseline matches by
rule, file and matched text, so a second hit with the same text in the same file
would be suppressed silently. This script therefore matches the raw findings
itself, one finding at a time: an exception must match the rule id, the file,
the matched text and the full source line the finding sits on (`line`), and it
may suppress at most `max_per_file` findings in any one file (default 1). Any
finding left over fails the scan. Each exception must also suppress at least one
finding for every glob in its `skill` list, or the scan fails, so the list
cannot go stale. Unknown keys in an exception are rejected.

Exits 0 when every skill is clean, 1 on findings or stale exceptions, 2 when
SkillSpector cannot be run or inputs are invalid. It never reports a pass if
the scanner is missing.
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
SKILL_MAP = ROOT / "data" / "skill-principle-map.json"
SCANNER_VERSION = "2.13.7"
TIMEOUT_SECONDS = 600
EXCEPTION_KEYS = {"skill", "id", "path", "message", "line", "max_per_file", "reason"}


def as_list(value):
    return value if isinstance(value, list) else [value]


def glob_match(value, pattern):
    return fnmatch.fnmatchcase(value.lower(), pattern.lower())


def source_line(skill_dir, location):
    """Return the stripped text of the line a finding points at, or None."""
    file, number = location.get("file"), location.get("start_line")
    if not file or not isinstance(number, int) or number < 1:
        return None
    try:
        lines = (skill_dir / file).read_text(encoding="utf-8").split("\n")
    except (OSError, UnicodeDecodeError):
        return None
    return lines[number - 1].strip() if number <= len(lines) else None


def apply_exceptions(skill_dir, issues, own):
    """Split findings into (unexplained, hits).

    A finding is explained by an exception only when the id matches exactly and
    the `path`, `message` and `line` globs (if given) match that finding's file,
    matched text and source line, and the exception has not already explained
    `max_per_file` findings in that file. hits is the set of exception indexes
    that explained at least one finding.
    """
    used = {}
    unexplained, hits = [], set()
    for f in issues:
        loc = f.get("location", {})
        line = source_line(skill_dir, loc)
        for i, e in own:
            if f.get("id") != e["id"]:
                continue
            if "path" in e and not glob_match(str(loc.get("file")), e["path"]):
                continue
            if "message" in e and not glob_match(str(f.get("finding")), e["message"]):
                continue
            if line is None or not glob_match(line, e["line"]):
                continue
            key = (i, loc.get("file"))
            if used.get(key, 0) >= e.get("max_per_file", 1):
                continue
            used[key] = used.get(key, 0) + 1
            hits.add(i)
            break
        else:
            unexplained.append(f)
    return unexplained, hits


def scan(skill_dir, exceptions, tmp):
    """Return (name, exit code, unexplained findings, hits, completeness, error text).

    hits is the set of exception indexes that explained at least one finding.
    """
    name = skill_dir.name
    own = [(i, e) for i, e in enumerate(exceptions) if any(fnmatch.fnmatchcase(name, g) for g in as_list(e["skill"]))]
    report = tmp / f"{name}.json"
    try:
        proc = subprocess.run(
            ["skillspector", "scan", str(skill_dir), "--no-llm", "--fail-on-incomplete",
             "--format", "json", "--output", str(report)],
            capture_output=True, text=True, timeout=TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        return name, 2, [], set(), None, f"timed out after {TIMEOUT_SECONDS}s"
    if not report.exists():
        return name, 2, [], set(), None, proc.stderr.strip() or proc.stdout.strip()
    data = json.loads(report.read_text(encoding="utf-8"))
    completeness = data.get("analysis_completeness")
    if not data.get("execution_successful"):
        return name, 2, [], set(), completeness, "SkillSpector reported execution_successful=false"
    unexplained, hits = apply_exceptions(skill_dir, data.get("issues", []), own)
    incomplete = bool(completeness) and not completeness.get("is_complete", True)
    if proc.returncode not in (0, 1):
        return name, 2, unexplained, hits, completeness, proc.stderr.strip()
    code = 1 if unexplained or incomplete or proc.returncode == 1 else 0
    return name, code, unexplained, hits, completeness, proc.stderr.strip()


def load_exceptions():
    data = yaml.safe_load(EXCEPTIONS.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("exceptions"), list):
        return [], [f"{EXCEPTIONS.name} must contain a top-level 'exceptions' list"]
    exceptions = data["exceptions"]
    problems = []
    for n, e in enumerate(exceptions):
        if not isinstance(e, dict):
            problems.append(f"exception #{n} is not a mapping: {e}")
            continue
        for key in ("skill", "id", "line", "reason"):
            if key not in e:
                problems.append(f"exception #{n} lacks '{key}': {e}")
        if "id" in e and (not isinstance(e["id"], str) or not e["id"].strip()):
            problems.append(f"exception #{n} 'id' must be a non-empty string")
        if "reason" in e and (not isinstance(e["reason"], str) or not e["reason"].strip()):
            problems.append(f"exception #{n} 'reason' must be a non-empty string")
        if "line" in e and (not isinstance(e["line"], str) or not e["line"].strip()):
            problems.append(f"exception #{n} 'line' must be a non-empty glob on the source line")
        if "max_per_file" in e and (type(e["max_per_file"]) is not int or e["max_per_file"] < 1):
            problems.append(f"exception #{n} 'max_per_file' must be an integer of at least 1")
        if "skill" in e:
            globs = e["skill"] if isinstance(e["skill"], list) else [e["skill"]]
            if not globs or any(not isinstance(g, str) or not g.strip() for g in globs):
                problems.append(f"exception #{n} 'skill' must be a non-empty glob or list of non-empty globs")
        for key in e:
            if key not in EXCEPTION_KEYS:
                problems.append(f"exception #{n} has unknown key '{key}': {e}")
    return exceptions, problems


def load_skills():
    map_doc = json.loads(SKILL_MAP.read_text(encoding="utf-8"))
    expected = {Path(e["folder"]).name for e in map_doc["skills"]}
    on_disk = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
    if expected != on_disk:
        missing = sorted(expected - on_disk)
        extra = sorted(on_disk - expected)
        parts = []
        if missing:
            parts.append(f"missing on disk: {missing}")
        if extra:
            parts.append(f"not in {SKILL_MAP.relative_to(ROOT)}: {extra}")
        return None, "skills/ does not match data/skill-principle-map.json (" + "; ".join(parts) + ")"
    return sorted((ROOT / "skills" / name for name in expected), key=lambda p: p.name), None


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

    skills, err = load_skills()
    if err:
        print(err, file=sys.stderr)
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
