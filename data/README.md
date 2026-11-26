# data

The machine-readable source of truth. Everything here is versioned (`schema_version`) and validated against `schemas/`.

| File | What it holds | Kind |
| --- | --- | --- |
| `principles.json` | The 103 principles, with sources, status, provenance, aliases for merged IDs and notes on how overlapping principles differ | Hand-written |
| `sources.json` | The 45 source repos, their role, licence and pinned commit | Hand-written, pins moved by `scripts/refresh-sources.py` |
| `changelog.json` | Machine-readable log of merges, drops, edits and pins | Hand-written |
| `notes/` | Hand-written overlays added to generated pages | Hand-written |
| `skill-principle-map.json` | One entry per skill: folder, principle, aliases, category, phase, test app, slot and licence status | Hand-written |
| `taxonomy.json` | Subgroups, the nine phases with their roles, agents and commands, the test apps and the run order | Hand-written |
| `mapping.json` | Each principle's source files, pinned | Hand-written |
| `licences.json` | The declared licence of every source repo and file (not this repo's licence) | Hand-written |
| `scorecard.json` | One row per skill for the test-app workflow; `runs` is empty until a skill is scored | Hand-written |
| `schemas/` | JSON schemas for the files above | Hand-written |

Still to come: `refresh/` (reports from each refresh).

How generated and hand-written content are kept apart: [UPDATING.md](../UPDATING.md).
