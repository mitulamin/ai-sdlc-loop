#!/usr/bin/env python3
"""Validate every data/*.json against data/schemas/<name>.schema.json.

Usage: scripts/validate-data.py

Needs the jsonschema package (pip install jsonschema). Exits 1 on any error,
including a data file that has no schema, and a schema that is not valid.
"""
import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:
    sys.exit("jsonschema is required: pip install jsonschema")

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SCHEMAS = DATA / "schemas"


def main():
    errors = []
    checked = 0
    for data_file in sorted(DATA.glob("*.json")):
        schema_file = SCHEMAS / f"{data_file.stem}.schema.json"
        if not schema_file.exists():
            errors.append(f"{data_file.relative_to(ROOT)}: no schema at {schema_file.relative_to(ROOT)}")
            continue
        try:
            schema = json.loads(schema_file.read_text(encoding="utf-8"))
            instance = json.loads(data_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{data_file.name}: invalid JSON ({e})")
            continue
        try:
            Draft202012Validator.check_schema(schema)
        except Exception as e:
            errors.append(f"{schema_file.relative_to(ROOT)}: not a valid schema ({e})")
            continue
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        for err in sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path)):
            where = "/".join(str(p) for p in err.absolute_path) or "(root)"
            errors.append(f"{data_file.relative_to(ROOT)} at {where}: {err.message}")
        checked += 1
    for schema_file in sorted(SCHEMAS.glob("*.schema.json")):
        name = schema_file.name[: -len(".schema.json")]
        if not (DATA / f"{name}.json").exists():
            print(f"note: {schema_file.relative_to(ROOT)} has no data file yet")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"validated {checked} data files against their schemas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
