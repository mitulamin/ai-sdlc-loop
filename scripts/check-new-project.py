#!/usr/bin/env python3
"""Check that scripts/new-project.sh works for every harness in data/harnesses.json, and for none.

Usage: scripts/check-new-project.py

Standard library only; needs bash and git. Each run goes into a temporary folder, with HOME and
XDG_CONFIG_HOME pointed at an empty temporary folder, and fails if:
  - the script exits non-zero, or --help does not list every profile and harness
  - an unknown harness does not fail, or creates the target folder
  - anything is written outside the target (the fake home folder must stay empty)
  - the none harness writes any harness file (the result must match the template and profile)
  - a harness run is missing an agent, a command, a skill or its SOURCES.md, an extra file, the
    notice or the licence copy, or writes a file that the installer did not plan
  - a skill or command skill has a name that does not match its folder or a description over 1024
  - an installed file lacks the provenance comment, keeps the build-agents marker, keeps an
    unprefixed loop command, has a relative link that does not resolve inside the project, or links
    to an agent, command, skill or principle in the source repo instead of the installed copy
"""
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "new-project.sh"
LINK = re.compile(r"\]\(([^)\s]+)\)")


def load_installer():
    spec = importlib.util.spec_from_file_location("install_harness", ROOT / "scripts" / "install-harness.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run(args, env):
    return subprocess.run(["bash", str(SCRIPT)] + args, capture_output=True, text=True, env=env)


def files_under(folder):
    return {p.relative_to(folder).as_posix() for p in folder.rglob("*") if p.is_file() and ".git" not in p.relative_to(folder).parts}


def check_links(project, rel, text, errors, repo_url):
    base = (project / rel).parent
    installed = re.compile(re.escape(repo_url) + r"/(blob|tree)/[^/]+/(agents|commands|skills|principles)/")
    for target in LINK.findall(text):
        if installed.match(target):
            errors.append(f"{rel}: link {target} points at the source repo, not the installed copy")
            continue
        if re.match(r"^([a-z][a-z0-9+.-]*:|#)", target, re.I):
            continue
        path = target.split("#", 1)[0]
        resolved = (base / path).resolve()
        if not resolved.is_relative_to(project.resolve()):
            errors.append(f"{rel}: link {target} leaves the project")
        elif not resolved.exists():
            errors.append(f"{rel}: link {target} does not resolve")


def check_harness(mod, hid, project, errors):
    inst = mod.Installer(hid)
    planned = inst.plan()
    h = inst.h
    got = files_under(project)
    for rel in planned:
        if rel not in got:
            errors.append(f"{hid}: {rel} was not installed")
    base = files_under(project) - set(planned)
    stray = sorted(p for p in base for d in (h["skills"]["dir"], h["agents"]["dir"], h["commands"]["dir"], inst.shared) if p.startswith(d + "/"))
    if stray:
        errors.append(f"{hid}: unplanned files in harness folders: {', '.join(stray)}")
    kinds = {}
    for item in inst.items:
        kinds.setdefault(item.kind, []).append(item)
    agents = [p for p in (ROOT / "agents").glob("*.md") if p.name != "README.md"]
    commands = [p for p in (ROOT / "commands").glob("*.md") if p.name != "README.md"]
    skills = json.loads((ROOT / "data" / "skill-principle-map.json").read_text(encoding="utf-8"))["skills"]
    for kind, want in (("agent", len(agents)), ("command", len(commands)), ("skill", len(skills)), ("skill-sources", len(skills))):
        if len(kinds.get(kind, [])) != want:
            errors.append(f"{hid}: planned {len(kinds.get(kind, []))} {kind} files, expected {want}")
    if (project / inst.shared / "LICENSE-CONTENT").read_text(encoding="utf-8") != (ROOT / "LICENSE-CONTENT").read_text(encoding="utf-8"):
        errors.append(f"{hid}: {inst.shared}/LICENSE-CONTENT differs from LICENSE-CONTENT")
    for extra in h["extra_files"]:
        if "json" in extra:
            try:
                json.loads((project / extra["path"]).read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as e:
                errors.append(f"{hid}: {extra['path']} is not valid JSON ({e})")
    unprefixed = re.compile(r"(?<![\w/.-])/(" + "|".join(p.stem for p in commands) + r")(?![\w-])") if h["commands"]["prefix"] else None
    for item in inst.items:
        text = (project / item.dest).read_text(encoding="utf-8")
        front, body = mod.parse_front(text)
        if not body.lstrip().startswith(mod.PROVENANCE):
            errors.append(f"{hid}: {item.dest} lacks the provenance comment")
        if mod.MARKER_PREFIX in text:
            errors.append(f"{hid}: {item.dest} keeps the build-agents marker")
        if unprefixed and unprefixed.search(text):
            errors.append(f"{hid}: {item.dest} keeps an unprefixed loop command: {unprefixed.search(text).group(0)}")
        if item.kind == "command" and h["commands"]["arguments"] is not None and "$ARGUMENTS" in text:
            errors.append(f"{hid}: {item.dest} keeps $ARGUMENTS")
        if item.dest.endswith("/SKILL.md"):
            folder = item.dest.rsplit("/", 2)[-2]
            if front.get("name") != folder:
                errors.append(f"{hid}: {item.dest} name {front.get('name')!r} does not match its folder")
            if not front.get("description") or len(front["description"]) > 1024:
                errors.append(f"{hid}: {item.dest} needs a description of at most 1024 characters")
        expected_keys = {e["key"] for e in {"skill": h["skills"], "agent": h["agents"], "command": h["commands"]}.get(item.kind, {}).get("front_matter", [])
                         if "roles" not in e or item.role in e["roles"]}
        if item.kind in ("skill", "agent", "command"):
            missing = sorted(k for k in expected_keys - set(front) if not (k in ("tools", "permissions") or (k == "argument-hint" and not item.values.get("argument-hint"))))
            if missing:
                errors.append(f"{hid}: {item.dest} front matter lacks {', '.join(missing)}")
        check_links(project, item.dest, text, errors, mod.REPO_URL)
    check_links(project, f"{inst.shared}/NOTICE.md", (project / inst.shared / "NOTICE.md").read_text(encoding="utf-8"), errors, mod.REPO_URL)


def main():
    mod = load_installer()
    harnesses = [h["id"] for h in mod.load_harnesses()["harnesses"]]
    profiles = sorted(p.name for p in (ROOT / "template" / "profiles").iterdir() if (p / "profile.txt").exists())
    errors = []
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        home = tmp / "home"
        home.mkdir()
        env = dict(os.environ, HOME=str(home), XDG_CONFIG_HOME=str(home / ".config"))
        env.pop("PI_CODING_AGENT_DIR", None)

        help_out = run(["--help"], env)
        if help_out.returncode != 0:
            errors.append(f"--help exited {help_out.returncode}")
        for name in profiles + ["none"] + harnesses:
            if not re.search(rf"^  {re.escape(name)}\s", help_out.stdout, re.M):
                errors.append(f"--help does not list {name}")

        bad = run(["--harness", "no-such-harness", str(tmp / "bad")], env)
        if bad.returncode == 0 or (tmp / "bad").exists():
            errors.append("an unknown harness did not fail before creating the target")

        r = run([str(tmp / "base")], env)
        if r.returncode != 0:
            errors.append(f"none: exited {r.returncode}: {r.stderr.strip()}")
        base_files = files_under(tmp / "base")

        r = run([str(tmp / "none"), "--harness", "none"], env)
        if r.returncode != 0:
            errors.append(f"none: exited {r.returncode}: {r.stderr.strip()}")
        elif files_under(tmp / "none") != base_files:
            errors.append("none: the result differs from a run without --harness")

        for i, hid in enumerate(harnesses):
            profile = profiles[i % len(profiles)]
            target = tmp / hid
            args = ["--harness", hid, str(target), profile] if i % 2 == 0 else [str(target), profile, f"--harness={hid}"]
            r = run(args, env)
            if r.returncode != 0:
                errors.append(f"{hid}: exited {r.returncode}: {r.stderr.strip()}")
                continue
            if not (target / ".git").is_dir():
                errors.append(f"{hid}: no git repository")
            if not (target / "LICENSE").read_text(encoding="utf-8").startswith("MIT License"):
                errors.append(f"{hid}: LICENSE is not the template's MIT licence")
            check_harness(mod, hid, target, errors)

        leaked = sorted(p.relative_to(home).as_posix() for p in home.rglob("*"))
        if leaked:
            errors.append("files written outside the target, in the home folder: " + ", ".join(leaked))

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"new-project.sh works for none and every harness ({', '.join(harnesses)}), with nothing written outside the target")
    return 0


if __name__ == "__main__":
    sys.exit(main())
