# Contributing

Small pull requests, one change each. Run `scripts/build-principles.py --check`, `scripts/build-agents.py --check` and `scripts/validate.py` before you push.

## Add or change a principle

1. Edit `data/principles.json`. Take the next number in the category and fill in `statement`, `category`, `category_name`, `skill` and `skill_folder`.
2. Add the matching entry to `data/skill-principle-map.json` (folder, principle, category, test app, phase, slot and licence status), the source files to `data/mapping.json` and `data/licences.json`, and a row to `scorecard.csv`.
3. Run `scripts/build-principles.py`. Commit the generated `principles/` files. Then run `scripts/validate.py`.
4. Add an entry to `data/changelog.json` and `CHANGELOG.md`.

Do not renumber principles. Merge one by folding it into the survivor: move the old ID to the top-level `aliases` map and to the survivor's `aliases` list (with its old statement), record the survivor's old wording in `previous_statement`, and add a section to [MERGES.md](MERGES.md). See [UPDATING.md](UPDATING.md).

## Add a source repo

Add it to `data/sources.json` with `role` `skill-source` or `curation-list`, `licence` `TBD`, and `pinned_sha` `null`. Then run `scripts/refresh-sources.py --repin owner/repo` once you have looked at it.

## Add or change a template profile

The base lives in `template/`. A profile is a small overlay in `template/profiles/<name>/`, never a copy of the base.

- `profile.txt`: one line, shown in the script usage.
- `omit` (optional): base files to leave out, one path per line, relative to the project root.
- `overlay/` (optional): files to add or replace. Same paths as in the new project.

Put something in the base only if every profile needs it. Put it in an overlay if it is ceremony: a gate, a role, a review rule, an ownership file. Use `@PROFILE@` where a file should name the profile. Keep profiles short, and keep everything under `template/` MIT.

To check a change, run the script once per profile into a temp folder and look at the result:

```bash
for p in solo small-team large-org; do scripts/new-project.sh "$(mktemp -d)/x" "$p"; done
```

Then update the table in the README, `scripts/README.md` and `CHANGELOG.md`.

## Add a skill

One skill per principle, in `skills/<id>-<slug>/`, with `SKILL.md` (front matter with `principle:` and `licence: CC-BY-SA-4.0`) and `SOURCES.md` (every source file pinned to a commit, with its licence). A source with no usable licence goes under "Further reading (link only)" and nothing from it is copied or adapted. Register the folder in `data/skill-principle-map.json`, then run `scripts/build-agents.py` to wire it into the agents and commands for its phase, and `scripts/validate.py`.

## Which licence your contribution is under

By contributing, you agree your contribution is licensed on the same split as the repo. This is not legal advice. The split is set in [LICENSE.md](LICENSE.md), the detail is in [NOTICE.md](NOTICE.md), and the reasons are in the README section [Licence](README.md#licence).

- A script, a schema, the site in `docs/`, CI, or other program code is under GPL-3.0-only ([LICENSES/GPL-3.0-only.txt](LICENSES/GPL-3.0-only.txt)). That includes `scripts/`, `docs/`, `data/schemas/` and `.github/workflows/`.
- Text is under CC BY-SA 4.0 ([LICENSES/CC-BY-SA-4.0.txt](LICENSES/CC-BY-SA-4.0.txt)). That includes skills, principles, guides, agent and command markdown, the data files in `data/` and `scorecard.csv`.
- Everything under `template/` is MIT ([template/LICENSE](template/LICENSE)), code and writing. A new project copied from it inherits MIT.
- Do not add material you cannot license that way. Borrowed files keep their own licence and their attribution.

## Credit your sources

If you adapt a new source in a skill, add it to that skill's `SOURCES.md`, to `data/licences.json` and to [CREDITS.md](CREDITS.md). If you use or reference a new project, add it to [ATTRIBUTIONS.md](ATTRIBUTIONS.md). The steps are at the bottom of that file.

## Rules

- Never hand-edit a file that starts with a `GENERATED` marker.
- Never install a curation list wholesale.
- Do not add anything that is internal to a company. This repo is public.
- Keep the licence and attribution of anything you borrow.
