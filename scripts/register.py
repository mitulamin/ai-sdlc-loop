#!/usr/bin/env python3
"""Write to, read and validate the shared surface register (append-only JSON Lines).

Usage:
  scripts/register.py add --agent A --phase P --type assumption|question --text T --impact I --urgency U
                          [--recommendation R] [--register PATH]
  scripts/register.py update --ref ID --status S [--note N] [--answer A] [--by coordinator|human]
                             [--agent A] [--phase P] [--register PATH]
  scripts/register.py ingest FILE [--agent A] [--phase P] [--register PATH]
  scripts/register.py list [--open] [--register PATH]
  scripts/register.py check [--register PATH]

Standard library only. The format, the allowed values and the default path come from
data/agent-contract.json. Lines are only ever appended, in one write each, so agents running
at the same time do not overwrite each other. `ingest` appends each declare line found in a
findings or report file (for agents that have no shell). `list` reads the log and shows each
entry with its current status; the register file itself stays readable without this script.
"""
import argparse
import json
import os
import re
import secrets
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTRACT = json.loads((ROOT / "data" / "agent-contract.json").read_text(encoding="utf-8"))["register"]


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def new_id():
    return "r-" + datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S") + "-" + secrets.token_hex(2)


def append(path, records):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records).encode("utf-8")
    fd = os.open(path, os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o644)
    try:
        os.write(fd, data)
    finally:
        os.close(fd)


def validate(rec, known_ids=None):
    """Return the problems with one register line."""
    errs = []
    event = rec.get("event")
    spec = CONTRACT["events"].get(event)
    if spec is None:
        return [f"event must be one of {sorted(CONTRACT['events'])}"]
    for k in spec["required"]:
        if not isinstance(rec.get(k), str) or not rec[k].strip():
            errs.append(f"{k} is required and must be a non-empty string")
    allowed = set(spec["required"]) | set(spec.get("optional", []))
    for k in rec:
        if k not in allowed:
            errs.append(f"unexpected field {k}")
    if errs:
        return errs
    if not re.fullmatch(CONTRACT["id_pattern"], rec["id"]):
        errs.append(f"id {rec['id']!r} does not match {CONTRACT['id_pattern']}")
    if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", rec["ts"]):
        errs.append(f"ts {rec['ts']!r} is not UTC RFC 3339 (YYYY-MM-DDTHH:MM:SSZ)")
    if rec["status"] not in CONTRACT["statuses"]["values"]:
        errs.append(f"status must be one of {CONTRACT['statuses']['values']}")
    if event == "declare":
        if rec["type"] not in CONTRACT["types"]:
            errs.append(f"type must be one of {CONTRACT['types']}")
        for k in ("impact", "urgency"):
            if rec[k] not in CONTRACT[k]["values"]:
                errs.append(f"{k} must be one of {CONTRACT[k]['values']}")
        if rec["status"] != "open":
            errs.append("a declared entry starts as open")
    else:
        if "by" in rec and rec["by"] not in CONTRACT["by"]:
            errs.append(f"by must be one of {CONTRACT['by']}")
        if known_ids is not None and rec["ref"] not in known_ids:
            errs.append(f"ref {rec['ref']} is not an earlier declared entry")
    return errs


def read(path):
    """Yield (line number, record or None, parse error) for each non-blank line."""
    for n, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
            yield n, rec if isinstance(rec, dict) else None, None if isinstance(rec, dict) else "not a JSON object"
        except json.JSONDecodeError as e:
            yield n, None, f"invalid JSON ({e.msg})"


def declare_record(a):
    rec = {"id": new_id(), "event": "declare", "ts": now(), "agent": a["agent"], "phase": a["phase"],
           "type": a["type"], "text": a["text"], "impact": a["impact"], "urgency": a["urgency"], "status": "open"}
    if a.get("recommendation"):
        rec["recommendation"] = a["recommendation"]
    return rec


def cmd_add(args):
    rec = declare_record(vars(args))
    errs = validate(rec)
    if errs:
        sys.exit("; ".join(errs))
    append(args.register, [rec])
    print(rec["id"])
    return 0


def cmd_update(args):
    path = Path(args.register)
    ids = {r["id"] for _, r, e in read(path) if r and r.get("event") == "declare"} if path.exists() else set()
    rec = {"id": new_id(), "event": "update", "ts": now(), "agent": args.agent or args.by or "coordinator",
           "phase": args.phase or "all", "ref": args.ref, "status": args.status}
    for k in ("note", "answer", "by"):
        if getattr(args, k):
            rec[k] = getattr(args, k)
    errs = validate(rec, ids)
    if errs:
        sys.exit("; ".join(errs))
    append(path, [rec])
    print(rec["id"])
    return 0


def cmd_ingest(args):
    recs, bad = [], []
    for n, line in enumerate(Path(args.file).read_text(encoding="utf-8").splitlines(), 1):
        s = line.strip()
        if not s.startswith("{"):
            continue
        try:
            raw = json.loads(s)
        except json.JSONDecodeError:
            continue
        if not isinstance(raw, dict) or raw.get("type") not in CONTRACT["types"]:
            continue
        rec = {"id": new_id(), "event": "declare", "ts": now(), "status": "open",
               "agent": args.agent or raw.get("agent"), "phase": args.phase or raw.get("phase")}
        rec.update({k: raw[k] for k in ("type", "text", "impact", "urgency", "recommendation") if k in raw})
        errs = validate(rec)
        if errs:
            bad.append(f"{args.file}:{n}: " + "; ".join(errs))
        else:
            recs.append(rec)
    if bad:
        sys.exit("\n".join(bad))
    append(args.register, recs)
    print(f"appended {len(recs)} entries")
    return 0


def current(path):
    entries, latest = {}, {}
    for _, rec, _ in read(path):
        if not rec:
            continue
        if rec.get("event") == "declare":
            entries[rec["id"]] = rec
        elif rec.get("event") == "update" and rec.get("ref") in entries:
            latest[rec["ref"]] = rec
    return entries, latest


def cmd_list(args):
    if not Path(args.register).exists():
        print("no register yet")
        return 0
    entries, latest = current(args.register)
    scale = {"high": 0, "medium": 1, "low": 2}
    rows = []
    for i, e in entries.items():
        status = latest[i]["status"] if i in latest else e["status"]
        if args.open and status not in ("open", "surfaced"):
            continue
        rows.append((scale.get(e["impact"], 3), scale.get(e["urgency"], 3), e["ts"], i, status, e))
    for _, _, _, i, status, e in sorted(rows):
        print(f"{i}  {status:9}  {e['type']:10}  impact={e['impact']:6} urgency={e['urgency']:6} {e['agent']} ({e['phase']}): {e['text']}")
    return 0


def cmd_check(args):
    if not Path(args.register).exists():
        print("no register yet")
        return 0
    errors, ids = [], set()
    for n, rec, err in read(args.register):
        if err:
            errors.append(f"line {n}: {err}")
            continue
        for p in validate(rec, ids):
            errors.append(f"line {n}: {p}")
        if rec.get("event") == "declare" and isinstance(rec.get("id"), str):
            if rec["id"] in ids:
                errors.append(f"line {n}: duplicate id {rec['id']}")
            ids.add(rec["id"])
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"{args.register}: {len(ids)} entries, valid")
    return 0


def main():
    default = CONTRACT["default_path"]
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = p.add_subparsers(dest="cmd", required=True)

    def common(sp):
        sp.add_argument("--register", default=default, help=f"register path (default {default})")
        return sp

    a = common(sub.add_parser("add"))
    a.add_argument("--agent", required=True)
    a.add_argument("--phase", required=True)
    a.add_argument("--type", required=True, choices=CONTRACT["types"])
    a.add_argument("--text", required=True)
    a.add_argument("--impact", required=True, choices=CONTRACT["impact"]["values"])
    a.add_argument("--urgency", required=True, choices=CONTRACT["urgency"]["values"])
    a.add_argument("--recommendation")
    u = common(sub.add_parser("update"))
    u.add_argument("--ref", required=True)
    u.add_argument("--status", required=True, choices=CONTRACT["statuses"]["values"])
    u.add_argument("--note")
    u.add_argument("--answer")
    u.add_argument("--by", choices=CONTRACT["by"])
    u.add_argument("--agent")
    u.add_argument("--phase")
    i = common(sub.add_parser("ingest"))
    i.add_argument("file")
    i.add_argument("--agent")
    i.add_argument("--phase")
    ls = common(sub.add_parser("list"))
    ls.add_argument("--open", action="store_true", help="only entries still open or surfaced")
    common(sub.add_parser("check"))
    args = p.parse_args()
    return {"add": cmd_add, "update": cmd_update, "ingest": cmd_ingest, "list": cmd_list, "check": cmd_check}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
