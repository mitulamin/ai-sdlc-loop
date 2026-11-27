# Contributing

Small pull requests, one change each. Run `scripts/build-principles.py --check` before you push.

## Add or change a principle

1. Edit `data/principles.json`. Take the next number in the category, set `status` to `active`, and fill in `sources` and `provenance` (`origin`: `contributed`).
2. Every label in `sources` must be listed under `labels` for a repo in `data/sources.json`. Add the repo there first if it is new.
3. Run `scripts/build-principles.py`. Commit the generated `principles/` files.
4. Add an entry to `data/changelog.json` and `CHANGELOG.md`.

Do not renumber principles. Drop one by setting `status` to `dropped`. Merge one by folding it into the survivor, listing the old ID in the survivor's `aliases` and `provenance.merged_from`, and adding a row to [MERGES.md](MERGES.md). See [UPDATING.md](UPDATING.md).

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

Then run `python scripts/check-new-project.py`, which CI also runs: it creates a project for every harness and fails if one breaks. If you change the template or the Cursor layout, also run `python scripts/check-bootstrap.py`, which CI runs too: it checks the Bootstrap for Cursor. Update the table in the README, `scripts/README.md` and `CHANGELOG.md`.

## Add or change a harness

The layout for each coding harness is data in `data/harnesses.json`, checked by `data/schemas/harnesses.schema.json`. To add a harness, add an entry and follow its current official docs: where it reads project skills, agents and commands, the file names and front matter, its tool names, and how a session reaches the coordinator. Link those docs in the entry. Keep every path inside the project, never in a user or global folder; the schema refuses an absolute path, `..` or `~`. Write a note for every concept the harness lacks and what you did instead. Then run `python scripts/validate-data.py`, `python scripts/check-new-project.py` and `scripts/build-site.py`, which regenerates the harness table and sections on the Use page.

## Add a skill

There is one skill per principle, in `skills/<id>-<slug>/`, with a `SKILL.md` and a `SOURCES.md`. The folder name is the principle ID and a short slug, and the ID is the survivor's ID if the principle was merged (the old ID goes in `aliases`).

- `SKILL.md` front matter has `principles: ["<id>"]` (quoted), `aliases`, `category` (the category slug), a quoted `description`, and `licence`. The statement matches `data/principles.json`.
- `SKILL.md` has the sections `scripts/build-agents.py` reads: When to use, `Producer: dos and don'ts` (a Do list, then a Don't list), Steps, Self-check and the adversarial reviewer checks, which end with the default-verdict line. The Self-check opens with the line every skill uses and lists `- [ ] ` items: questions the producer answers yes, no or N/A, with evidence, before it hands off.
- If an established practice that is not a principle here (SOLID, DRY, the Law of Demeter and the like) fits the skill, add it to the principle's `related_practices` in `data/principles.json` with the guide section that explains it and the principles it touches, then give the skill a Related practices entry (`- **<name>** (...)`, linking that guide section and those principles), a Self-check item `- [ ] <name>: ...` and a reviewer check `- <name>: ...`. `scripts/check-skills.py` fails if they drift. Put each practice in one skill only, next to the principle that brakes it where they pull against each other.
- `SOURCES.md` links every source file at a pinned commit, with its licence. Borrowed content keeps its own licence and attribution. Add the source repo to `data/sources.json` and `ATTRIBUTIONS.md` if it is new.
- Add the skill to `data/skill-principle-map.json` and, if it draws on new files, to `data/mapping.json`, `data/licences.json` and `CREDITS.md`.
- Run `python scripts/check-skills.py`, then `python scripts/build-principles.py` and `python scripts/build-site.py` so the principle page links the skill, and `python scripts/build-agents.py` so the agents and commands for its phase load it. Do not edit `agents/` or `commands/` by hand.

## Add a SkillSpector exception

CI scans everything agent-facing that this repo ships (skills, agents, commands, the template and what each harness install writes) with SkillSpector, and fails on any finding no entry explains. Read the finding in context first. If it is a real problem, fix the source: `agents/` and `commands/` are generated, so change `data/` or `scripts/build-agents.py`, not the generated file. Only for a genuine false positive, add an entry to `.github/skillspector-exceptions.yaml` with its rule, file, matched text, source line and a reason, as the header of that file describes. A model-assisted scan with SkillSpector's LLM analyzers runs on release candidates, not on pull requests, and a release is gated on it. To run it yourself: `export XAI_API_KEY=...` (or `NVIDIA_INFERENCE_KEY=...`) and `python scripts/skillspector-llm-scan.py --group <group> --record record.md` (`--list-groups` lists the groups; leave out `--group` to scan everything). See [RELEASING.md](RELEASING.md).

## Which licence your contribution is under

By contributing, you agree your contribution is licensed on the same split as the repo. This is not legal advice. The detail is in [NOTICE.md](NOTICE.md) and the README section [Why GPLv3, and CC BY-SA for the writing](README.md#why-gplv3-and-cc-by-sa-for-the-writing).

- A script, a schema, workflow tooling, or other program code is under GPL-3.0 ([LICENSE](LICENSE)). That includes `scripts/` and `data/schemas/`.
- Writing is under CC BY-SA 4.0 ([LICENSE-CONTENT](LICENSE-CONTENT)). That includes docs, guides, principle statements and notes, skill and agent markdown, and the data files in `data/` (except `data/schemas/`).
- Everything under `template/` is MIT ([template/LICENSE](template/LICENSE)), code and writing. A new project copied from it inherits MIT. So do the copies of skills, agents and commands that `scripts/new-project.sh --harness` installs, except files adapted from share-alike sources, which keep CC BY-SA 4.0. The sources of those copies in this repo stay CC BY-SA 4.0.
- Do not add material you cannot license that way. Borrowed files keep their own licence and their attribution.

## Credit your sources

If you use or reference a new project, add it to [ATTRIBUTIONS.md](ATTRIBUTIONS.md). The steps are at the bottom of that file.

## Rules

- Never hand-edit a file that starts with a `GENERATED` marker.
- Never install a curation list wholesale.
- Do not add anything that is internal to a company. This repo is public.
- Keep the licence and attribution of anything you borrow.
