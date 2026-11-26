# data

The machine-readable source of truth. Everything here is versioned (`schema_version`) and validated against `schemas/`.

| File | What it holds | Kind |
| --- | --- | --- |
| `principles.json` | The 108 principles, with sources, status and provenance | Hand-written |
| `sources.json` | The 41 source repos, their role, licence and pinned commit | Hand-written, pins moved by `scripts/refresh-sources` |
| `changelog.json` | Machine-readable log of merges, drops, edits and pins | Hand-written |
| `notes/` | Hand-written overlays added to generated pages | Hand-written |
| `schemas/` | JSON schemas for the files above | Hand-written |

Still to come: `mapping.json` (principles to source files to skills), `scorecard.json`, `refresh/` (reports from each refresh).

How generated and hand-written content are kept apart: [UPDATING.md](../UPDATING.md).
