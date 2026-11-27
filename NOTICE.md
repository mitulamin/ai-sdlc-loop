# Licensing notes

This repo uses three licences. Why, and the plain-language reading, is in the README under [Why GPLv3, and CC BY-SA for the writing](README.md#why-gplv3-and-cc-by-sa-for-the-writing). This is not legal advice.

## GPL-3.0 (code)

The text is in [LICENSE](LICENSE). It covers:

- `scripts/`
- `data/schemas/`
- tooling, including workflow files added later under `.github/workflows/`

Do not replace or edit LICENSE without a deliberate decision recorded in [CHANGELOG.md](CHANGELOG.md).

## CC BY-SA 4.0 (writing)

The text is in [LICENSE-CONTENT](LICENSE-CONTENT). It covers:

- markdown in this repo outside `template/`, including the principle statements and notes in `principles/`, `docs/` and `guides/`
- the data files in `data/` (except `data/schemas/`)

The data files hold the principle statements and the research record around them, so they sit with the writing. The schemas in `data/schemas/` stay under GPL-3.0. Each file is under one licence.

## MIT (the template)

The text is in [template/LICENSE](template/LICENSE). It covers everything under `template/`, code and writing. A project created with `scripts/new-project.sh` copies the base from that folder plus the profile you pick, including `LICENSE`, and starts under MIT. It does not inherit GPL-3.0. The copies of skills, agents and commands that the script installs with `--harness` are MIT too, like `template/`, except files adapted from share-alike sources, which keep CC BY-SA 4.0 and carry their notice and licence text. The sources of those copies, in `skills/`, `agents/` and `commands/` here, stay under CC BY-SA 4.0.

## Logo and brand images (all rights reserved)

The logo and brand image files in `docs/assets/brand/` (favicons, logos and social card images, in any format) are not covered by GPL-3.0, CC BY-SA 4.0 or MIT. They remain under plain copyright, all rights reserved, by Shravi Limited. None of the licences above gives permission to copy, modify or redistribute them.

## Borrowed material

Every project used or referenced, with links, roles and licences, is listed in [ATTRIBUTIONS.md](ATTRIBUTIONS.md).

Content borrowed from other repos keeps its original licence. This repo does not relicense it. Each borrowed file is credited in the `SOURCES.md` next to the skill that uses it, with the source link pinned to a commit and the source's licence.

The licence of each source repo is recorded in [data/sources.json](data/sources.json). All 45 were checked on 2026-11-26. Do not borrow from a repo whose licence is missing, restrictive or incompatible; the flags are in [ATTRIBUTIONS.md](ATTRIBUTIONS.md).

Principles in `data/principles.json` are short statements written for this repo. They name their sources but do not reproduce them.
