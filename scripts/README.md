# scripts

| Script | What it does |
| --- | --- |
| `build-principles.py` | Regenerates `principles/*.md` from `data/principles.json`. `--check` fails if anything is stale. |
| `refresh-sources.py` | Compares each pinned SHA in `data/sources.json` with the upstream head. `--pin` and `--repin` move pins. |
| `build-site.py` | Regenerates the static site in `docs/` from `data/` and `guides/developer/`. `--check` fails if anything is stale. |
| `validate-data.py` | Validates every `data/*.json` against `data/schemas/`. Needs `pip install jsonschema`. |
| `check-skills.py` | Checks `skills/` against `data/principles.json` and `data/skill-principle-map.json`: one folder per principle with `SKILL.md` and `SOURCES.md`, matching front matter and aliases. Standard library only. |
| `check-links.py` | Checks internal links in `docs/` and markdown, offline. |
| `new-project.sh` | `new-project.sh <target-dir> [profile]`. Copies the `template/` base, applies a profile (`solo` default, `small-team`, `large-org`) and runs `git init`. `--help` lists the profiles. |

Python 3, git and bash. Everything is standard library only except `validate-data.py`, which needs `jsonschema`. See [UPDATING.md](../UPDATING.md).
