"""What the SkillSpector scans cover and how reviewed exceptions apply, shared by
skillspector-scan.py and skillspector-llm-scan.py.

A target is one folder handed to one `skillspector scan`: a skill folder, agents/,
commands/, template/, or a throwaway install for one harness (minus the installed skill
copies, which differ from skills/ only in front matter and links). Needs PyYAML for the exceptions.
"""
import fnmatch
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
SKILL_MAP = ROOT / "data" / "skill-principle-map.json"
HARNESSES = ROOT / "data" / "harnesses.json"
INSTALLER = ROOT / "scripts" / "install-harness.py"
SCANNER_VERSION = "2.13.7"
DIR_TARGETS = ("agents", "commands", "template")
HARNESS_PREFIX = "harness-"
EXCEPTIONS = ROOT / ".github" / "skillspector-exceptions.yaml"
EXCEPTION_KEYS = {"target", "id", "path", "message", "line", "max_per_file", "reason"}


@dataclass(frozen=True)
class Target:
    name: str
    path: Path


def count_files(path):
    return sum(1 for p in path.rglob("*") if p.is_file())


def skill_targets():
    """Return (targets, error): one target per skill folder, checked against the skill map."""
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
        return [], "skills/ does not match data/skill-principle-map.json (" + "; ".join(parts) + ")"
    return [Target(n, ROOT / "skills" / n) for n in sorted(expected)], None


def dir_targets():
    """Return (targets, error) for agents/, commands/ and template/; each must exist and hold files."""
    targets = []
    for name in DIR_TARGETS:
        path = ROOT / name
        if not path.is_dir() or not count_files(path):
            return [], f"{name}/ is missing or has no files to scan"
        targets.append(Target(name, path))
    return targets, None


def harness_targets(tmp):
    """Install every harness in data/harnesses.json under tmp and return (targets, error).

    Each target is the install minus the installed skill copies. When a harness installs its
    loop commands as skill folders (a commands dir equal to its skills dir), the folders that
    start with the commands prefix are kept, because they are not copies of anything in skills/.
    """
    doc = json.loads(HARNESSES.read_text(encoding="utf-8"))
    targets = []
    for h in doc["harnesses"]:
        dest = tmp / h["id"]
        dest.mkdir(parents=True)
        proc = subprocess.run([sys.executable, str(INSTALLER), str(dest), h["id"]], capture_output=True, text=True)
        if proc.returncode != 0:
            return [], f"install-harness.py failed for {h['id']}: {(proc.stderr or proc.stdout).strip()[:300]}"
        skills_dir = dest / h["skills"]["dir"]
        if h["commands"]["dir"] == h["skills"]["dir"]:
            keep = h["commands"].get("prefix", "")
            for child in skills_dir.iterdir():
                if child.is_dir() and not (keep and child.name.startswith(keep)):
                    shutil.rmtree(child)
        else:
            shutil.rmtree(skills_dir)
        if not count_files(dest):
            return [], f"the {h['id']} install has no files to scan"
        targets.append(Target(HARNESS_PREFIX + h["id"], dest))
    return targets, None


def find_scanner():
    """Return (path to skillspector, version line, error)."""
    exe = shutil.which("skillspector")
    if not exe:
        return None, None, f"skillspector is not installed: pip install 'skillspector=={SCANNER_VERSION}'"
    # Rich styles the version even when piped if FORCE_COLOR is set to any value, so drop ANSI escapes.
    version = re.sub(r"\x1b\[[0-9;]*m", "", subprocess.run([exe, "--version"], capture_output=True, text=True).stdout).strip()
    if SCANNER_VERSION not in version:
        return exe, version, f"expected SkillSpector {SCANNER_VERSION}; the reviewed exceptions only apply to that version"
    return exe, version, None


def coverage_problem(target, completeness):
    """Return a message when SkillSpector did not inspect every file under the target, else None."""
    files = count_files(target.path)
    if not completeness:
        return "SkillSpector reported no coverage figures"
    if completeness.get("total_components") != files:
        return f"SkillSpector saw {completeness.get('total_components')} components but the target holds {files} files"
    if not completeness.get("is_complete", True):
        return (f"incomplete coverage ({completeness.get('coverage_percent')}%): "
                f"{json.dumps(completeness.get('ledger_exceptions', []))[:600]}")
    return None


def as_list(value):
    return value if isinstance(value, list) else [value]


def glob_match(value, pattern):
    return fnmatch.fnmatchcase(value.lower(), pattern.lower())


def source_line(root, location):
    """Return the stripped text of the line a finding points at, or None."""
    file, number = location.get("file"), location.get("start_line")
    if not file or not isinstance(number, int) or number < 1:
        return None
    try:
        lines = (root / file).read_text(encoding="utf-8").split("\n")
    except (OSError, UnicodeDecodeError):
        return None
    return lines[number - 1].strip() if number <= len(lines) else None


def apply_exceptions(root, issues, own):
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
        line = source_line(root, loc)
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
        for key in ("target", "id", "line", "reason"):
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
        if "target" in e:
            globs = e["target"] if isinstance(e["target"], list) else [e["target"]]
            if not globs or any(not isinstance(g, str) or not g.strip() for g in globs):
                problems.append(f"exception #{n} 'target' must be a non-empty glob or list of non-empty globs")
        for key in e:
            if key not in EXCEPTION_KEYS:
                problems.append(f"exception #{n} has unknown key '{key}': {e}")
    return exceptions, problems
