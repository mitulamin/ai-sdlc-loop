# scripts

| Script | What it does |
| --- | --- |
| `build-principles.py` | Regenerates `principles/*.md` from `data/principles.json`. `--check` fails if anything is stale. |
| `refresh-sources.py` | Compares each pinned SHA in `data/sources.json` with the upstream head. `--pin` and `--repin` move pins. |
| `build-agents.py` | Regenerates `agents/` (the coordinator and a producer and reviewer per phase) and `commands/` (the slash commands) from `data/skill-principle-map.json`, `data/taxonomy.json`, `data/principles.json` and `skills/`. Each lists its skills by ID. `--check` fails if anything is stale. |
| `build-site.py` | Regenerates the static site in `docs/` from `data/` and `guides/developer/`, and the agents page from the `build-agents.py` model (which also reads `skills/`). Guide links to files under `docs/` become site-relative links; see [guides/README.md](../guides/README.md). `--check` fails if anything is stale. |
| `validate-data.py` | Validates every `data/*.json` against `data/schemas/`. Needs `pip install jsonschema`. |
| `check-skills.py` | Checks `skills/` against `data/principles.json` and `data/skill-principle-map.json`: one folder per principle with `SKILL.md` and `SOURCES.md`, matching front matter and aliases. Standard library only. |
| `check-links.py` | Checks internal links in `docs/` and markdown, offline. |
| `skillspector-scan.py` | Scans every folder in `skills/` with NVIDIA SkillSpector (`--no-llm`) and matches each finding against `.github/skillspector-exceptions.yaml` by rule, file, text and source line (with a per-file cap), failing on unexplained findings or stale/reasonless exceptions. Needs `skillspector==2.13.7` and `pyyaml`. |
| `new-project.sh` | `new-project.sh <target-dir> [profile]`. Copies the `template/` base, applies a profile (`solo` default, `small-team`, `large-org`) and runs `git init`. `--help` lists the profiles. |

Python 3, git and bash. Everything is standard library only except `validate-data.py` (needs `jsonschema`) and `skillspector-scan.py` (needs `skillspector==2.13.7` and `pyyaml`). See [UPDATING.md](../UPDATING.md).
