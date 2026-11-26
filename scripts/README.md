# scripts

| Script | What it does |
| --- | --- |
| `validate.py` | Checks the amalgamated-skills kit: 103 principles, 103 skill folders with `SKILL.md` and `SOURCES.md`, 5 aliases, slots 1 to 103, a licence line in every skill, no non-adaptable source in a main source list, 103 scorecard rows, and the licence files. Prints `OK: ...` or `FAILED` and exits 1. |
| `check-kit-layout.py` | Checks what `validate.py` does not: one `principles/<id>.md` per principle and none for a retired ID, no `skills/` folder or scorecard row for a retired ID, scorecard IDs match the principles, every `SKILL.md` front matter parses as YAML with the keys the scripts rely on, and every `data/*.json` has a schema. Needs `pip install pyyaml`. |
| `skillspector-scan.py` | Scans each `skills/<id>-<slug>/` with NVIDIA SkillSpector (static, `--no-llm`), failing on any finding not listed with a reason in `.github/skillspector-exceptions.yaml`. Needs `pip install skillspector`. Exits 2 if SkillSpector is not installed. |
| `build-principles.py` | Regenerates `principles/*.md` from `data/principles.json` and `data/skill-principle-map.json`. `--check` fails if anything is stale. |
| `refresh-sources.py` | Compares each pinned SHA in `data/sources.json` with the upstream head. `--pin` and `--repin` move pins. |
| `build-site.py` | Regenerates the static site in `docs/` from `data/` and `guides/developer/`. `--check` fails if anything is stale. |
| `validate-data.py` | Validates every `data/*.json` against `data/schemas/`. Needs `pip install jsonschema`. |
| `check-links.py` | Checks internal links in `docs/` and markdown, offline. |
| `new-project.sh` | `new-project.sh <target-dir> [profile]`. Copies the `template/` base, applies a profile (`solo` default, `small-team`, `large-org`) and runs `git init`. `--help` lists the profiles. |

Python 3, git and bash. Everything is standard library only except `validate-data.py` (`jsonschema`), `check-kit-layout.py` and `skillspector-scan.py` (`pyyaml`, plus `skillspector` for the scan). See [UPDATING.md](../UPDATING.md).
