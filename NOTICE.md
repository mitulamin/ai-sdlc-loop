# Licensing notes

The licence split is set in [LICENSE.md](LICENSE.md), with the full texts in [LICENSES/](LICENSES/). Why, and the plain-language reading, is in the README under [Licence](README.md#licence). This is not legal advice.

## GPL-3.0-only (code)

The text is in [LICENSES/GPL-3.0-only.txt](LICENSES/GPL-3.0-only.txt). It covers:

- `scripts/`
- the GitHub Pages site in `docs/`
- `data/schemas/`
- CI and tooling, including `.github/workflows/`

Do not replace or edit `LICENSE`, `LICENSE.md` or `LICENSES/` without a deliberate decision recorded in [CHANGELOG.md](CHANGELOG.md).

## CC BY-SA 4.0 (text)

The text is in [LICENSES/CC-BY-SA-4.0.txt](LICENSES/CC-BY-SA-4.0.txt). It covers:

- the skills in `skills/` (`SKILL.md` and `SOURCES.md`), the principles in `principles/`, and `guides/`
- the data files in `data/` (except `data/schemas/`) and `scorecard.csv`
- `README.md`, `IMPORT.md`, `MERGES.md`, `CREDITS.md`, `UPDATING.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `NOTICE.md`, `ATTRIBUTIONS.md`
- other markdown in this repo outside `template/`, including `agents/`, `commands/`, folder READMEs, `.github/PULL_REQUEST_TEMPLATE.md` and `.github/workflows/README.md`

Each file is under one licence.

## MIT (the template)

The text is in [template/LICENSE](template/LICENSE). It covers everything under `template/`, code and writing. A project created with `scripts/new-project.sh` copies the base from that folder plus the profile you pick, including `LICENSE`, and starts under MIT. It does not inherit GPL-3.0 or CC BY-SA 4.0.

## Borrowed material

The sources the skills were adapted from, with licence, copyright notice and pinned commit, are in [CREDITS.md](CREDITS.md). The licence of every source file, per repo and per skill, is in [data/licences.json](data/licences.json). Every project used or referenced in the research is listed in [ATTRIBUTIONS.md](ATTRIBUTIONS.md).

Content borrowed from other repos keeps its original licence. This repo does not relicense it. Each skill's `SOURCES.md` credits the exact files, linked at a pinned commit, with the licence of each.

Sources with no usable licence are link only: nothing from them is copied or adapted, and they appear only under "Further reading (link only)" in a skill's `SOURCES.md`. They are listed in the "Link only" section of [CREDITS.md](CREDITS.md). `scripts/validate.py` fails if one appears in a skill's main source list.
