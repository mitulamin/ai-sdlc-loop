#!/usr/bin/env python3
"""Check that scripts/new-project.sh works for every harness in data/harnesses.json, and for none.

Usage: scripts/check-new-project.py

Standard library only; needs bash and git. Each run goes into a temporary folder, with HOME and
XDG_CONFIG_HOME pointed at an empty temporary folder, and fails if:
  - the script exits non-zero, or --help does not list every profile and harness
  - an unknown harness does not fail, or creates the target folder
  - anything is written outside the target (the fake home folder must stay empty)
  - the none harness writes any harness file (the result must match the template and profile)
  - a harness run is missing an agent, a command, a skill or its SOURCES.md, or an extra file, or
    writes a file that the installer did not plan
  - the project root holds anything but the template's MIT LICENSE as a licence or notice, or the
    shared folder holds a notice or a licence copy
  - a file has the wrong licence. The share-alike set is worked out here from data/sources.json and
    data/licences.json, not from the installer: a skill is share-alike if one of its sources is, and
    an agent if one of its skills is. Every other file must be MIT. A share-alike skill folder must
    hold NOTICE.md and a copy of LICENSE-CONTENT, no other folder may, and no MIT file may point at
    them. Each SOURCES.md must carry its sources' copyright lines and licence links, and a modified
    statement for Apache sources
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


def expected_licences(mod, inst):
    """Worked out from the data alone: {skill folder name: licence key}, and the set of share-alike skill ids."""
    lic = inst.licensing["licences"]
    sources = json.loads((ROOT / "data" / "sources.json").read_text(encoding="utf-8"))
    licences = json.loads((ROOT / "data" / "licences.json").read_text(encoding="utf-8"))
    share_keys = {k for k, v in lic.items() if v["kind"] == "share-alike"}
    share_repos = {f"{r['owner']}/{r['repo']}" for r in sources["repos"] if r["licence"] in share_keys}
    from_sources = {pid for r in share_repos for pid in licences["repos"][r]["adapted_in_skills"]}
    from_skills = {pid for pid, s in licences["skills"].items() if any(x["licence"].split()[0] in share_keys for x in s["sources"])}
    errors = []
    if from_sources != from_skills:
        errors.append("data/sources.json and data/licences.json disagree about which skills adapt a share-alike source: "
                      + ", ".join(sorted(from_sources ^ from_skills)))
    return from_skills, share_keys, errors


def check_licences(mod, inst, hid, project, errors):
    lic = inst.licensing["licences"]
    share_ids, share_keys, problems = expected_licences(mod, inst)
    errors += problems
    if len(share_keys) != 1:
        errors.append(f"{hid}: this check expects one share-alike licence, found {len(share_keys)}")
        return
    sa_key = next(iter(share_keys))
    sa = lic[sa_key]
    mit = inst.licensing["default"]
    licence_data = json.loads((ROOT / "data" / "licences.json").read_text(encoding="utf-8"))
    smap = {e["principle_id"]: e for e in json.loads((ROOT / "data" / "skill-principle-map.json").read_text(encoding="utf-8"))["skills"]}
    canonical = {a: pid for pid, e in smap.items() for a in e.get("aliases", [])}
    folders = {item.values["principle_id"]: item.dest.rsplit("/", 1)[0] for item in inst.items if item.kind == "skill"}

    root_names = sorted(p.name for p in project.iterdir())
    for name in root_names:
        if re.match(r"(licen[cs]e|notice|copying|copyright)", name, re.I) and name != "LICENSE":
            errors.append(f"{hid}: {name} at the project root; the root holds only the template's LICENSE")
    if (project / "LICENSE").read_bytes() != (ROOT / "template" / "LICENSE").read_bytes():
        errors.append(f"{hid}: LICENSE differs from template/LICENSE")
    for name in ("NOTICE.md", "LICENSE-CONTENT"):
        if (project / inst.shared / name).exists():
            errors.append(f"{hid}: {inst.shared}/{name} is written; the shared folder holds no notice or licence copy")

    allowed = {f"{folders[pid]}/{n}" for pid in share_ids for n in ("NOTICE.md", sa["text_file"])}
    for rel in sorted(files_under(project)):
        if rel.rsplit("/", 1)[-1] in ("NOTICE.md", sa["text_file"]) and rel not in allowed:
            errors.append(f"{hid}: {rel} is a notice or licence copy outside a share-alike skill folder")
    for rel in sorted(allowed):
        if not (project / rel).is_file():
            errors.append(f"{hid}: {rel} is missing from a share-alike skill folder")
    for pid in share_ids:
        copy = project / folders[pid] / sa["text_file"]
        if copy.is_file() and copy.read_bytes() != (ROOT / sa["text_file"]).read_bytes():
            errors.append(f"{hid}: {copy.relative_to(project)} differs from {sa['text_file']}")
        notice = project / folders[pid] / "NOTICE.md"
        if notice.is_file():
            text = notice.read_text(encoding="utf-8")
            for needle in (sa["name"], sa["url"], f"({sa['text_file']})", "trailofbits/skills", "Share-alike"):
                if needle not in text:
                    errors.append(f"{hid}: {notice.relative_to(project)} lacks {needle!r}")

    for item in inst.items:
        text = (project / item.dest).read_text(encoding="utf-8")
        front, body = mod.parse_front(text)
        header = body.lstrip().split("\n", 1)[0]
        if item.kind in ("skill", "skill-sources"):
            pid = item.values["principle_id"]
            is_sa = pid in share_ids
        elif item.kind == "agent":
            src_front, _ = mod.parse_front((ROOT / item.src).read_text(encoding="utf-8"))
            is_sa = any(canonical.get(s, s) in share_ids for s in src_front.get("skills", []))
        else:
            is_sa = False
        want = sa_key if is_sa else mit
        name = lic[want]["name"]
        if f"Licence: {name}," not in header:
            errors.append(f"{hid}: {item.dest} provenance comment does not state {name}")
        if item.kind == "skill" and front.get("license") != want:
            errors.append(f"{hid}: {item.dest} license is {front.get('license')!r}, expected {want}")
        if is_sa:
            if item.kind in ("skill", "skill-sources"):
                if "NOTICE.md in this skill folder" not in header:
                    errors.append(f"{hid}: {item.dest} header does not point at the skill folder's NOTICE.md")
            elif item.kind == "agent":
                m = re.search(r"see the notice at (\S+?)\. -->", header)
                if not m or not (project / m.group(1)).is_file() or m.group(1) not in allowed:
                    errors.append(f"{hid}: {item.dest} header does not point at an installed share-alike skill NOTICE.md")
        else:
            for needle in ("LICENSE-CONTENT", "NOTICE.md", "CC BY-SA 4.0", "CC-BY-SA"):
                if needle in text and not (item.kind == "skill-sources" and needle in ("CC BY-SA 4.0", "CC-BY-SA") and "not compatible with CC BY-SA" in text):
                    errors.append(f"{hid}: MIT file {item.dest} mentions {needle}")
        if item.kind == "skill-sources":
            check_source_notes(inst, hid, item, text, licence_data, is_sa, errors)


def check_source_notes(inst, hid, item, text, licence_data, is_sa, errors):
    lic = inst.licensing["licences"]
    pid = item.values["principle_id"]
    if "## Licence notices for the adapted sources" not in text:
        errors.append(f"{hid}: {item.dest} has no licence notices section")
        return
    section = text.split("## Licence notices for the adapted sources", 1)[1]
    for s in licence_data["skills"][pid]["sources"]:
        data = licence_data["repos"][s["repo"]]
        entry = lic[s["licence"].split()[0]]
        line = next((ln for ln in section.splitlines() if ln.startswith(f"- {s['repo']} (")), None)
        if line is None:
            errors.append(f"{hid}: {item.dest} has no notice for {s['repo']}")
            continue
        if data["licence_file"] not in line or f"({entry['name']})" not in line:
            errors.append(f"{hid}: {item.dest} notice for {s['repo']} lacks its licence or licence link")
        if entry["kind"] == "share-alike":
            continue
        for c in data.get("copyright", []):
            if c.lower().startswith("copyright") and c not in line:
                errors.append(f"{hid}: {item.dest} notice for {s['repo']} lacks {c!r}")
        if entry.get("modified_statement") and "Modified:" not in line:
            errors.append(f"{hid}: {item.dest} notice for {s['repo']} lacks the modified statement")
        if not entry.get("modified_statement") and "Modified:" in line:
            errors.append(f"{hid}: {item.dest} notice for {s['repo']} has an unneeded modified statement")


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
    check_licences(mod, inst, hid, project, errors)
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
    for rel in sorted(p for p in planned if p.endswith("/NOTICE.md")):
        check_links(project, rel, (project / rel).read_text(encoding="utf-8"), errors, mod.REPO_URL)


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
