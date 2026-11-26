# Licence

This kit uses a split licence.

| What | Licence | Full text |
|---|---|---|
| Text: the skills (`skills/**/SKILL.md`, `SOURCES.md`), principles (`principles/`), guides, `README.md`, `IMPORT.md`, `MERGES.md`, `CREDITS.md` and the data files in `data/` | CC BY-SA 4.0 (Creative Commons Attribution-ShareAlike 4.0 International) | `LICENSES/CC-BY-SA-4.0.txt` |
| Also text, under the same licence: `scorecard.csv`, `UPDATING.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `NOTICE.md`, `ATTRIBUTIONS.md`, `agents/`, `commands/`, folder READMEs and the other markdown outside `template/` | CC BY-SA 4.0 | `LICENSES/CC-BY-SA-4.0.txt` |
| Code: scripts, the GitHub Pages site, CI and tooling (for example `scripts/`, `docs/`) | GNU GPL v3 only | `LICENSES/GPL-3.0-only.txt` |
| Also code, under the same licence: the JSON schemas in `data/schemas/` and the workflows in `.github/workflows/` | GNU GPL v3 only | `LICENSES/GPL-3.0-only.txt` |
| The project template: everything under `template/`, code and writing, so a project made with `scripts/new-project.sh` starts under MIT | MIT | `template/LICENSE` |

The root `LICENSE` file is a short pointer to this file. The principle statements shown on the generated site pages in `docs/` stay CC BY-SA 4.0 text.

Rules of thumb:
- If you reuse or adapt the text, you must credit it, link the licence, say what you changed, and share your version under CC BY-SA 4.0. Credit the original authors too: see `CREDITS.md`.
- If you reuse or adapt the code, you must keep it under GPLv3 when you distribute it.
- Every skill folder has a `SOURCES.md` with the licence of each source it draws on. Sources with no usable licence are listed under "Further reading (link only)": nothing was copied or adapted from them.

Why this split: CC BY-SA 4.0 can absorb text from MIT, Apache-2.0, CC BY and CC BY-SA sources, and is one-way compatible into GPLv3. It cannot absorb GPL text, non-commercial or no-derivatives text, PolyForm Shield, proprietary terms, or unlicensed files, which is why those are link only. See `state-of-ai-research/licences/repo-licences.md` for the review. This is a research summary, not legal advice.

Copyright (c) 2026 Shravi Limited and contributors.
