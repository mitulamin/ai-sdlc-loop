#!/usr/bin/env python3
"""Validate the amalgamated-skills kit. Run from the kit root: python3 scripts/validate.py"""
import json, os, csv, sys, re
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
err = []
def need(c, m):
    if not c: err.append(m)
pj = json.load(open(f"{root}/data/principles.json"))
mp = json.load(open(f"{root}/data/skill-principle-map.json"))
lic = json.load(open(f"{root}/data/licences.json"))
ids = [p["id"] for p in pj["principles"]]
need(len(ids) == 103 == len(set(ids)), f"expected 103 unique principles, got {len(ids)}")
need(len(pj["aliases"]) == 5, f"expected 5 aliases, got {len(pj['aliases'])}")
for old, new in pj["aliases"].items():
    need(new in ids, f"alias {old} -> {new}: survivor missing")
    need(old not in ids, f"alias {old} must not also be a principle")
folders = sorted(d for d in os.listdir(f"{root}/skills") if os.path.isdir(f"{root}/skills/{d}"))
need(len(folders) == 103, f"expected 103 skill folders, got {len(folders)}")
for d in folders:
    for f in ("SKILL.md", "SOURCES.md"):
        need(os.path.exists(f"{root}/skills/{d}/{f}"), f"{d}/{f} missing")
sk = mp["skills"]
need(len(sk) == 103, f"skill map has {len(sk)} entries")
need(sorted(s["principle_id"] for s in sk) == sorted(ids), "every principle must have exactly one skill")
need({s["folder"].split("/")[-1] for s in sk} == set(folders), "map folders differ from skills/")
need(sorted(s["slot"] for s in sk) == list(range(1, 104)), "slots must be 1..103")
for s in sk:
    t = open(f"{root}/{s['folder']}/SKILL.md").read()
    need(f"principle: \"{s['principle_id']} " in t, f"{s['folder']}: principle id mismatch")
    need(re.search(r"^licence: CC-BY-SA-4.0$", t, re.M), f"{s['folder']}: licence line missing")
need(len(lic["skills"]) == 103, "licences.json must cover 103 skills")
for pid, v in lic["skills"].items():
    for s in v["sources"]:
        need(s["licence"] and "No licen" not in s["licence"] and "Proprietary" not in s["licence"] and "PolyForm" not in s["licence"] and "No LICENSE" not in s["licence"], f"{pid}: non-adaptable source in main list: {s['repo']}/{s['path']}")
rows = list(csv.DictReader(open(f"{root}/scorecard.csv")))
need(len(rows) == 103, f"scorecard has {len(rows)} rows")
for f in ("MERGES.md", "CREDITS.md", "LICENSE.md", "README.md", "IMPORT.md", "LICENSES/CC-BY-SA-4.0.txt", "LICENSES/GPL-3.0-only.txt"):
    need(os.path.exists(f"{root}/{f}"), f"{f} missing")
if err:
    print("FAILED"); [print(" -", e) for e in err]; sys.exit(1)
print("OK: 103 principles, 103 skills, 5 aliases, licences clean")
