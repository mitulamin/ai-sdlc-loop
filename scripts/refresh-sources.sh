#!/usr/bin/env python3
"""Compare the pinned SHA of every source repo in data/sources.json with its upstream HEAD.

Usage:
  scripts/refresh-sources.sh                 print a status table, change nothing
  scripts/refresh-sources.sh --json FILE     also write the report as JSON
  scripts/refresh-sources.sh --pin           pin repos that have no pinned_sha yet (first run only)
  scripts/refresh-sources.sh --repin NAME... move the pin of the named repos (owner/repo) to upstream HEAD,
                                          only after you have reviewed the diff
  scripts/refresh-sources.sh --exit-code     exit 2 when anything changed or is missing

Statuses: unpinned, unchanged, changed, missing (git could not reach the repo: renamed, deleted or private).

This is a stub for the first step of the refresh playbook in UPDATING.md. It does not clone
repos, diff files, dedupe or re-score. It tells you which repos need that work.
Standard library and git only.
"""
import argparse
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "data" / "sources.json"


def upstream_head(url):
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
    try:
        out = subprocess.run(["git", "ls-remote", "--symref", url, "HEAD"], capture_output=True, text=True, timeout=60, env=env)
    except subprocess.TimeoutExpired:
        return None, None
    if out.returncode != 0:
        return None, None
    branch = sha = None
    for line in out.stdout.splitlines():
        if line.startswith("ref:"):
            branch = line.split()[1].removeprefix("refs/heads/")
        elif line.endswith("\tHEAD"):
            sha = line.split("\t")[0]
    return sha, branch


def inspect(repo):
    sha, branch = upstream_head(repo["url"])
    if sha is None:
        status = "missing"
    elif repo["pinned_sha"] is None:
        status = "unpinned"
    elif repo["pinned_sha"] == sha:
        status = "unchanged"
    else:
        status = "changed"
    entry = {"repo": f"{repo['owner']}/{repo['repo']}", "role": repo["role"], "status": status,
             "pinned_sha": repo["pinned_sha"], "upstream_sha": sha, "default_branch": branch}
    if status == "changed":
        entry["compare_url"] = f"{repo['url']}/compare/{repo['pinned_sha']}...{sha}"
    return entry


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", metavar="FILE")
    ap.add_argument("--pin", action="store_true")
    ap.add_argument("--repin", nargs="+", metavar="OWNER/REPO")
    ap.add_argument("--exit-code", action="store_true")
    args = ap.parse_args()

    doc = json.loads(SOURCES.read_text(encoding="utf-8"))
    with ThreadPoolExecutor(max_workers=8) as pool:
        report = list(pool.map(inspect, doc["repos"]))

    for e in report:
        short = (e["upstream_sha"] or "-")[:10]
        print(f"{e['status']:<10} {e['repo']:<55} {short}")
        if "compare_url" in e:
            print(f"{'':<11}{e['compare_url']}")
    counts = {}
    for e in report:
        counts[e["status"]] = counts.get(e["status"], 0) + 1
    print("\n" + ", ".join(f"{k}: {v}" for k, v in sorted(counts.items())))

    if args.json:
        Path(args.json).write_text(json.dumps({"date": date.today().isoformat(), "report": report}, indent=2) + "\n", encoding="utf-8")

    targets = set(args.repin or [])
    unknown = targets - {e["repo"] for e in report}
    if unknown:
        print("Unknown repo(s): " + ", ".join(sorted(unknown)), file=sys.stderr)
        return 1
    if args.pin or targets:
        by_name = {e["repo"]: e for e in report}
        changed = 0
        for repo in doc["repos"]:
            name = f"{repo['owner']}/{repo['repo']}"
            e = by_name[name]
            if e["upstream_sha"] is None:
                continue
            if (args.pin and repo["pinned_sha"] is None) or name in targets:
                repo["pinned_sha"] = e["upstream_sha"]
                repo["default_branch"] = e["default_branch"]
                repo["pinned_at"] = date.today().isoformat()
                changed += 1
        SOURCES.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Updated {changed} pin(s). Log it in data/changelog.json and CHANGELOG.md.")

    if args.exit_code and any(e["status"] in ("changed", "missing") for e in report):
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
