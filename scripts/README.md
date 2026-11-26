# scripts

| Script | What it does |
| --- | --- |
| `validate.py` | Checks the amalgamated-skills kit: 103 principles, 103 skill folders with `SKILL.md` and `SOURCES.md`, 5 aliases, slots 1 to 103, a licence line in every skill, no non-adaptable source in a main source list, 103 scorecard rows, and the licence files. Prints `OK: ...` or `FAILED` and exits 1. |
| `build-principles.py` | Regenerates `principles/*.md` from `data/principles.json` and `data/skill-principle-map.json`. `--check` fails if anything is stale. |
| `build-agents.py` | Regenerates `agents/` (the coordinator, and a producer and an adversarial reviewer per phase) and `commands/` (`/plan` to `/retro`) from `data/skill-principle-map.json` and the skills' `SKILL.md`. A phase loads the skills whose phase or category matches it. Producers get each skill's Do and Don't lists together; reviewers get only the reviewer checks and the Don't list. `--check` fails if anything is stale, or if a generated file names a retired or unknown principle ID. |
| `refresh-sources.py` | Compares each pinned SHA in `data/sources.json` with the upstream head. `--pin` and `--repin` move pins. |
| `build-site.py` | Regenerates the static site in `docs/` from `data/` and `guides/developer/`. `--check` fails if anything is stale. |
| `validate-data.py` | Validates every `data/*.json` against `data/schemas/`. Needs `pip install jsonschema`. |
| `check-links.py` | Checks internal links in `docs/` and markdown, offline. |
| `new-project.sh` | `new-project.sh <target-dir> [profile]`. Copies the `template/` base, applies a profile (`solo` default, `small-team`, `large-org`) and runs `git init`. `--help` lists the profiles. |

Python 3, git and bash. Everything is standard library only except `validate-data.py`, which needs `jsonschema`. See [UPDATING.md](../UPDATING.md).
