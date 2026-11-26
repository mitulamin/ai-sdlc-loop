#!/usr/bin/env python3
"""Check the kit layout that scripts/validate.py does not cover.

scripts/validate.py checks the data files, skill folders, aliases, slots,
licences and scorecard row count. This script adds:

- principles/ holds exactly one <id>.md per principle (103), and no file for a
  retired ID;
- skills/ has no folder for a retired ID, and every folder name starts with the
  ID of a live principle;
- scorecard.csv has one row per skill, with the same IDs as the principles,
  and no retired ID;
- every skills/*/SKILL.md starts with front matter that parses as YAML, with
  the keys the other scripts rely on;
- no skill folder holds a symlink or other non-regular file, and no SOURCES.md is empty;
- the alias map is exactly the five merges in MERGES.md (4.4, 4.5, 9.4, 5.6, 2.11);
- every data/*.json has a schema in data/schemas/ (and the reverse).

Usage: scripts/check-kit-layout.py

Needs PyYAML (pip install pyyaml). Exits 1 on any error.
"""
import csv
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
EXPECTED_PRINCIPLES = 103
EXPECTED_ALIASES = 5
RETIRED = {"4.4": "4.1", "4.5": "5.3", "9.4": "5.1", "5.6": "5.10", "2.11": "6.3"}
FRONT_MATTER_KEYS = ("name", "description", "principles", "principle", "aliases", "licence")

errors = []


def need(cond, msg):
    if not cond:
        errors.append(msg)


def main():
    index = json.loads((ROOT / "data" / "principles.json").read_text(encoding="utf-8"))
    ids = [p["id"] for p in index["principles"]]
    retired = set(RETIRED)
    need(index["aliases"] == RETIRED, f"data/principles.json: aliases are {index['aliases']}, expected {RETIRED}")
    need(len(set(ids)) == len(ids), "data/principles.json: duplicate principle IDs")
    need(not (set(ids) & retired), f"data/principles.json: retired IDs listed as principles: {sorted(set(ids) & retired)}")
    need(len(ids) == EXPECTED_PRINCIPLES, f"data/principles.json: expected {EXPECTED_PRINCIPLES} principles, got {len(ids)}")
    need(len(retired) == EXPECTED_ALIASES, f"data/principles.json: expected {EXPECTED_ALIASES} aliases, got {len(retired)}")

    files = sorted(p.name[:-3] for p in (ROOT / "principles").glob("*.md") if p.name != "README.md")
    need(len(files) == EXPECTED_PRINCIPLES, f"principles/: expected {EXPECTED_PRINCIPLES} principle files, got {len(files)}")
    need(set(files) == set(ids), f"principles/: files differ from principle IDs (missing {sorted(set(ids) - set(files))}, extra {sorted(set(files) - set(ids))})")
    for r in sorted(retired):
        need(not (ROOT / "principles" / f"{r}.md").exists(), f"principles/{r}.md exists for retired ID {r}")

    folders = sorted(p.name for p in (ROOT / "skills").iterdir() if p.is_dir())
    need(len(folders) == EXPECTED_PRINCIPLES, f"skills/: expected {EXPECTED_PRINCIPLES} folders, got {len(folders)}")
    prefix_ids = []
    for d in folders:
        m = re.match(r"^(\d+\.\d+)-[a-z0-9][a-z0-9-]*$", d)
        if not m:
            errors.append(f"skills/{d}: folder name is not <id>-<slug>")
            continue
        prefix_ids.append(m.group(1))
        if m.group(1) in retired:
            errors.append(f"skills/{d}: folder for retired ID {m.group(1)} (resolve it to {RETIRED[m.group(1)]})")
    need(sorted(prefix_ids) == sorted(ids), "skills/: folder IDs differ from principle IDs, or two folders share an ID")

    rows = list(csv.DictReader((ROOT / "scorecard.csv").open(encoding="utf-8", newline="")))
    sc_ids = [r["skill_id"] for r in rows]
    need(len(rows) == EXPECTED_PRINCIPLES, f"scorecard.csv: expected {EXPECTED_PRINCIPLES} rows, got {len(rows)}")
    need(sorted(sc_ids) == sorted(ids), "scorecard.csv: skill_id column differs from principle IDs")
    need(not (set(sc_ids) & retired), f"scorecard.csv: retired IDs present: {sorted(set(sc_ids) & retired)}")

    for d in folders:
        for f in sorted((ROOT / "skills" / d).rglob("*")):
            need(f.is_dir() or (f.is_file() and not f.is_symlink()), f"{f.relative_to(ROOT)}: not a regular file (SkillSpector skips symlinks)")
        sources = ROOT / "skills" / d / "SOURCES.md"
        need(sources.exists() and sources.stat().st_size > 0, f"skills/{d}/SOURCES.md is missing or empty")
        skill = ROOT / "skills" / d / "SKILL.md"
        if not skill.exists():
            continue
        m = re.match(r"^---\n(.*?)\n---\n", skill.read_text(encoding="utf-8"), re.S)
        if not m:
            errors.append(f"skills/{d}/SKILL.md: no front matter")
            continue
        try:
            fm = yaml.safe_load(m.group(1))
        except yaml.YAMLError as e:
            errors.append(f"skills/{d}/SKILL.md: front matter is not valid YAML ({str(e).splitlines()[0]})")
            continue
        if not isinstance(fm, dict):
            errors.append(f"skills/{d}/SKILL.md: front matter is not a mapping")
            continue
        for key in FRONT_MATTER_KEYS:
            need(key in fm, f"skills/{d}/SKILL.md: front matter lacks '{key}'")
        need(fm.get("name") == d.split("-", 1)[1], f"skills/{d}/SKILL.md: name '{fm.get('name')}' does not match the folder slug")

    data_stems = {p.stem for p in (ROOT / "data").glob("*.json")}
    schema_stems = {p.name[: -len(".schema.json")] for p in (ROOT / "data" / "schemas").glob("*.schema.json")}
    for s in sorted(data_stems - schema_stems):
        errors.append(f"data/{s}.json has no schema in data/schemas/")
    for s in sorted(schema_stems - data_stems):
        errors.append(f"data/schemas/{s}.schema.json has no data file")

    if errors:
        print("FAILED")
        for e in errors:
            print(f" - {e}")
        return 1
    print(f"OK: {len(files)} principle files, {len(folders)} skill folders, {len(retired)} aliases, {len(rows)} scorecard rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
