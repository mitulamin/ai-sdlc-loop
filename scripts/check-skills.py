#!/usr/bin/env python3
"""Check skills/ against data/principles.json and the skill data files.

Usage: scripts/check-skills.py

Standard library only. Exits 1 on any error. Checks:
- every active principle has exactly one skill folder skills/<id>-<slug>/ with SKILL.md and SOURCES.md
- data/skill-principle-map.json covers the same folders and principle ids, with aliases that
  match data/principles.json, and slots 1..N with no gaps
- each SKILL.md front matter names its principle id (and only active ids), its category and licence
- no retired id (an alias) appears as a principle id in skills, the map, mapping.json or taxonomy.json
- data/taxonomy.json phases and subgroups refer to real principle ids, categories and phases
- data/licences.json lists no non-adaptable source in a skill's main source list
- every repo a skill adapts from is listed in data/sources.json
- data/scorecard.json has one row per skill
- every agent file in agents/ declares the required output field from data/agent-contract.json
  (assumptions and open questions) in its front matter and has its section; skills carry no
  output contract, so there is nothing to check in them
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
NOT_ADAPTABLE = re.compile(r"No licen|No LICENSE|Proprietary|PolyForm|\bNC\b|\bND\b|-NC-|-ND-|-NC$|-ND$")


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def front_matter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    fm = {}
    for line in text[4:end].splitlines():
        key, sep, value = line.partition(": ")
        if sep:
            fm[key.strip()] = value.strip()
    return fm


def check_agents(errors):
    contract = load("agent-contract.json")["output_field"]
    key, heading = contract["key"], contract["heading"]
    files = sorted(p for p in (ROOT / "agents").glob("*.md") if p.name != "README.md")
    if not files:
        errors.append("agents/ has no agent files to check")
    for path in files:
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        fm = front_matter(text)
        if fm is None:
            errors.append(f"{rel}: no front matter, so it cannot declare the required output field {key}")
            continue
        try:
            declared = json.loads(fm.get("output_fields", "null"))
        except json.JSONDecodeError:
            declared = None
        if not isinstance(declared, list) or key not in declared:
            errors.append(f"{rel}: front matter must declare output_fields containing \"{key}\"")
        if f"\n## Required output field: {heading}\n" not in text:
            errors.append(f"{rel}: missing the section '## Required output field: {heading}'")
    return len(files)


def main():
    errors = []
    pdoc = load("principles.json")
    active = {p["id"]: p for p in pdoc["principles"] if p["status"] == "active"}
    aliases = {a: p["id"] for p in pdoc["principles"] for a in p.get("aliases", [])}
    cat_slugs = {c["slug"] for c in pdoc["categories"]}
    smap = load("skill-principle-map.json")["skills"]
    tax = load("taxonomy.json")
    mapping = load("mapping.json")["principles"]
    lic = load("licences.json")
    score = load("scorecard.json")["skills"]
    sources = load("sources.json")["repos"]
    known_repos = {f"{r['owner']}/{r['repo']}" for r in sources}

    folders = sorted(d.name for d in (ROOT / "skills").iterdir() if d.is_dir())
    by_pid = {}
    for d in folders:
        m = re.match(r"^([0-9]+\.[0-9]+)-[a-z0-9-]+$", d)
        if not m:
            errors.append(f"skills/{d}: folder name is not <id>-<slug>")
            continue
        by_pid.setdefault(m.group(1), []).append(d)
        for f in ("SKILL.md", "SOURCES.md"):
            if not (ROOT / "skills" / d / f).is_file():
                errors.append(f"skills/{d}/{f} missing")
    for pid in active:
        if len(by_pid.get(pid, [])) != 1:
            errors.append(f"principle {pid}: expected exactly one skill folder, found {by_pid.get(pid, [])}")
    for pid in by_pid:
        if pid in aliases:
            errors.append(f"skills/{by_pid[pid][0]}: {pid} is retired; use {aliases[pid]}")
        elif pid not in active:
            errors.append(f"skills/{by_pid[pid][0]}: {pid} is not an active principle")

    if {e["folder"].split("/")[-1] for e in smap} != set(folders):
        errors.append("data/skill-principle-map.json folders differ from skills/")
    if sorted(e["principle_id"] for e in smap) != sorted(active):
        errors.append("data/skill-principle-map.json principle ids differ from the active principles")
    if sorted(e["slot"] for e in smap) != list(range(1, len(smap) + 1)):
        errors.append("data/skill-principle-map.json slots must be 1..N with no gaps")
    phase_slugs = {p["slug"] for p in tax["phases"]}
    for e in smap:
        pid = e["principle_id"]
        if pid in active and sorted(e["aliases"]) != sorted(active[pid].get("aliases", [])):
            errors.append(f"map {pid}: aliases differ from data/principles.json")
        if pid in active and e["category"] != active[pid]["category"]:
            errors.append(f"map {pid}: category {e['category']} differs from data/principles.json")
        if e["phase"] not in phase_slugs:
            errors.append(f"map {pid}: phase {e['phase']} is not in data/taxonomy.json")
        skill = ROOT / e["folder"] / "SKILL.md"
        if not skill.is_file():
            continue
        fm = front_matter(skill.read_text(encoding="utf-8"))
        if fm is None:
            errors.append(f"{e['folder']}/SKILL.md: no front matter")
            continue
        try:
            ids = json.loads(fm.get("principles", "null"))
        except json.JSONDecodeError:
            ids = None
        if ids != [pid]:
            errors.append(f"{e['folder']}/SKILL.md: principles must be [\"{pid}\"] (quoted), got {fm.get('principles')}")
        if not fm.get("principle", "").startswith(f'"{pid} '):
            errors.append(f"{e['folder']}/SKILL.md: principle line does not start with {pid}")
        if fm.get("category") != e["category"]:
            errors.append(f"{e['folder']}/SKILL.md: category differs from the map")
        if fm.get("licence") != "CC-BY-SA-4.0":
            errors.append(f"{e['folder']}/SKILL.md: licence must be CC-BY-SA-4.0")
        desc = fm.get("description", "")
        if not (desc.startswith('"') and desc.endswith('"')):
            errors.append(f"{e['folder']}/SKILL.md: quote the description so the front matter is valid YAML")

    tax_ids = [i for p in tax["phases"] for i in p["principles"]]
    if sorted(tax_ids) != sorted(active):
        errors.append("data/taxonomy.json phases must cover each active principle exactly once")
    for p in tax["phases"]:
        for c in p["categories"]:
            if c not in cat_slugs:
                errors.append(f"taxonomy phase {p['slug']}: unknown category {c}")
    for g in tax["subgroups"]:
        if g["category"] not in cat_slugs:
            errors.append(f"taxonomy subgroup {g['slug']}: unknown category {g['category']}")
        for i in g["principles"]:
            if i not in active or active[i]["category"] != g["category"]:
                errors.append(f"taxonomy subgroup {g['slug']}: {i} is not an active principle in {g['category']}")

    if sorted(mapping) != sorted(active):
        errors.append("data/mapping.json principle ids differ from the active principles")
    if sorted(lic["skills"]) != sorted(active):
        errors.append("data/licences.json skills differ from the active principles")
    for pid, v in lic["skills"].items():
        for s in v["sources"]:
            if NOT_ADAPTABLE.search(s["licence"]):
                errors.append(f"{pid}: non-adaptable source in main list: {s['repo']}/{s['path']} ({s['licence']})")
            if s["repo"] not in known_repos:
                errors.append(f"{pid}: source repo {s['repo']} is not in data/sources.json")
    if sorted(r["skill_id"] for r in score) != sorted(active):
        errors.append("data/scorecard.json must have one row per active principle's skill")

    agent_count = check_agents(errors)

    if errors:
        print("\n".join(sorted(set(errors))))
        return 1
    print(f"skills OK: {len(folders)} skills, {len(active)} active principles, {len(aliases)} aliases; {agent_count} agent files declare the output field")
    return 0


if __name__ == "__main__":
    sys.exit(main())
