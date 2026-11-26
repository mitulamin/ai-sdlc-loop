# Contributing

Small pull requests, one change each. Run `scripts/build-principles --check` before you push.

## Add or change a principle

1. Edit `data/principles.json`. Take the next number in the category, set `status` to `active`, and fill in `sources` and `provenance` (`origin`: `contributed`).
2. Every label in `sources` must be listed under `labels` for a repo in `data/sources.json`. Add the repo there first if it is new.
3. Run `scripts/build-principles`. Commit the generated `principles/` files.
4. Add an entry to `data/changelog.json` and `CHANGELOG.md`.

Do not renumber or delete principles. Merge or drop them by setting `status`. See [UPDATING.md](UPDATING.md).

## Add a source repo

Add it to `data/sources.json` with `role` `skill-source` or `curation-list`, `licence` `TBD`, and `pinned_sha` `null`. Then run `scripts/refresh-sources --repin owner/repo` once you have looked at it.

## Add a skill

Skills arrive in the next phase. The rules will be added here then: one skill per principle, `SKILL.md` plus `SOURCES.md`, sources pinned to a commit, licence and attribution kept.

## Rules

- Never hand-edit a file that starts with a `GENERATED` marker.
- Never install a curation list wholesale.
- Do not add anything that is internal to a company. This repo is public.
- Keep the licence and attribution of anything you borrow.
