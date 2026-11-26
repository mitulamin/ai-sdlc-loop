# Licensing notes

This repo uses two licences. Why, and the plain-language reading, is in the README under [Why GPLv3, and CC BY-SA for the writing](README.md#why-gplv3-and-cc-by-sa-for-the-writing). This is not legal advice.

## GPL-3.0 (code)

The text is in [LICENSE](LICENSE). It covers:

- `scripts/`
- `data/schemas/`
- tooling, including workflow files added later under `.github/workflows/`
- code added later inside `template/`

Do not replace or edit LICENSE without a deliberate decision recorded in [CHANGELOG.md](CHANGELOG.md).

## CC BY-SA 4.0 (writing)

The text is in [LICENSE-CONTENT](LICENSE-CONTENT). It covers:

- `README.md`, `UPDATING.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `NOTICE.md`, `ATTRIBUTIONS.md`
- prose in `template/` (`README.md`, `AGENTS.md`, and later prose added there)
- principle statements and notes in `principles/`, `docs/` and `guides/`
- other markdown in this repo, including folder READMEs, `.github/PULL_REQUEST_TEMPLATE.md` and `.github/workflows/README.md`
- `data/principles.json`, `data/sources.json`, `data/changelog.json` and `data/notes/`

`data/principles.json` holds the principle statements, so it sits with the writing. `data/sources.json` and `data/changelog.json` are the research record around those statements, so they sit with the writing too. The schemas in `data/schemas/` stay under GPL-3.0. Each file is under one licence.

A project created from `template/` carries these licences with it. The GPL-3.0 duties apply when that project is distributed.

## Borrowed material

Every project used or referenced, with links, roles and licences, is listed in [ATTRIBUTIONS.md](ATTRIBUTIONS.md).

Content borrowed from other repos keeps its original licence. This repo does not relicense it. Each borrowed file is credited in the `SOURCES.md` next to the skill that uses it, with the source link pinned to a commit and the source's licence.

The licence of each source repo is recorded in [data/sources.json](data/sources.json). It reads `TBD` until someone has checked it. Do not borrow from a repo whose licence is `TBD` or incompatible.

Principles in `data/principles.json` are short statements written for this repo. They name their sources but do not reproduce them.
