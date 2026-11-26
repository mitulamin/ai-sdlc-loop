# data

The machine-readable source of truth. Every data file is validated against `schemas/` by `scripts/validate-data.py`, and the kit files are cross-checked by `scripts/validate.py`.

| File | What it holds | Kind |
| --- | --- | --- |
| `principles.json` | The index of the 103 principles: statement, category, subgroup, skill folder, previous wording, partial overlaps, and `aliases` for the 5 retired IDs | From the amalgamated-skills kit |
| `skill-principle-map.json` | One entry per skill: folder, principle, aliases, category, test app, phase, slot and licence status. The single source for wiring skills by ID | From the kit |
| `mapping.json` | Principle to source files (pinned to a commit, with licence) and link-only sources | From the kit |
| `licences.json` | The licence split, the licence of each source repo, and per skill the adapted and link-only sources | From the kit |
| `sources.json` | The 41 research source repos, their role, licence and pinned commit | Hand-written, pins moved by `scripts/refresh-sources.py` |
| `changelog.json` | Machine-readable log of imports, merges, drops, edits and pins | Hand-written |
| `notes/` | Hand-written notes | Hand-written |
| `schemas/` | JSON schemas for the files above | Hand-written |

The kit files carry a `version` date instead of a `schema_version`; the schema version is in each schema's description. Do not hand-edit principle statements: change them in the kit data and regenerate `principles/` with `scripts/build-principles.py`.

Still to come: `scorecard.json` (the scorecard is `../scorecard.csv` for now), `refresh/` (reports from each refresh).

How generated and hand-written content are kept apart: [UPDATING.md](../UPDATING.md).
