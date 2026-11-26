# scripts

| Script | What it does |
| --- | --- |
| `build-principles` | Regenerates `principles/*.md` from `data/principles.json`. `--check` fails if anything is stale. |
| `refresh-sources.py` | Compares each pinned SHA in `data/sources.json` with the upstream head. `--pin` and `--repin` move pins. |
| `new-project.sh` | `new-project.sh <target-dir> [profile]`. Copies the `template/` base, applies a profile (`solo` default, `small-team`, `large-org`) and runs `git init`. `--help` lists the profiles. |

Python 3 (standard library only), git and bash. See [UPDATING.md](../UPDATING.md).
