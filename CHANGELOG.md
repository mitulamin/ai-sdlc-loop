# Changelog

All notable changes to this repo. The machine-readable version of the data changes is in [data/changelog.json](data/changelog.json). Process: [UPDATING.md](UPDATING.md).

## Unreleased

### Wired agents and commands to skills by ID

Added:

- `scripts/build-agents.py`, which generates `agents/` and `commands/` from `data/skill-principle-map.json` and each skill's `SKILL.md`. `--check` fails if a generated file is stale, names a retired principle ID, or cites an unknown one.
- `agents/coordinator.md`: the only agent the human talks to. It loads the Harness skills (8.x) and can look up all 103 principles. It may interview the human once while taking the brief, at the start of a project (1.4), and not again until the end of the cycle. Loops run on their own, with at most three FAILs in a row per phase, and agents send questions to the coordinator, never the human. At the end of the cycle the human gives feedback. The coordinator runs `/retro` on it with the Learn skills (9.x), then closes with the proposed edits for the human to approve.
- A producer and a strictly adversarial reviewer for each of the nine phases in the map: Harness, Plan, Design, Build, Verify, Debug, Secure, Review & ship and Learn. A phase loads the skills whose phase is that phase, plus the skills in the phase's main category, so the Debug agents also load 5.4, 5.10 and 5.15. Producers load each skill's When to use, Do and Don't lists together, and Steps. Reviewers load only the adversarial reviewer checks and the Don't list, start with a FAIL verdict, fail on any P0 or P1 finding or any check they could not run, and write P0 to P3 findings to a file. Each agent's front matter lists `skills` (loaded) and `principles` (lookup: its skills, their partial-overlap partners and the Harness skills).
- `commands/plan.md`, `design.md`, `build.md`, `verify.md` (Verify, then Debug for what fails), `review.md` (Secure, then Review & ship), `ship.md` (Review & ship) and `retro.md` (Learn). Each one lists the skills for its phases. `/review` and `/ship` run the same Review & ship pair, because the map has one Review & ship phase. Harness has no command: the coordinator runs it.

Changed:

- `README.md`, `UPDATING.md`, `CONTRIBUTING.md` and `scripts/README.md` now say that `agents/` and `commands/` are generated, and list `scripts/build-agents.py --check` with the other pre-commit checks.

### Imported the amalgamated-skills-103 kit

The kit already contains the dedupe (108 principles to 103) and the licence cleanup, and supersedes the earlier drafts. See [IMPORT.md](IMPORT.md) and [MERGES.md](MERGES.md).

Added:

- `skills/<id>-<slug>/`: 103 amalgamated skills, one per principle, each with `SKILL.md` (when to use, producer dos and don'ts, steps, adversarial reviewer checks, source comparison, test slot) and `SOURCES.md` (sources pinned to a commit, with licences, and "Further reading (link only)").
- `data/skill-principle-map.json` (skill to principle, aliases, category, test app, phase, slot, licence status), `data/mapping.json` (principle to source files) and `data/licences.json` (licence per repo and per source), with JSON schemas.
- `scorecard.csv` (one row per skill), `CREDITS.md`, `IMPORT.md`, `LICENSE.md`, `LICENSES/` and `scripts/validate.py`, which prints `OK: 103 principles, 103 skills, 5 aliases, licences clean`.

Changed:

- `data/principles.json` is the kit's index: 103 principles, and an `aliases` map for the retired IDs (4.4 to 4.1, 4.5 to 5.3, 9.4 to 5.1, 5.6 to 5.10, 2.11 to 6.3). Survivors 4.1, 5.1, 5.3, 5.10 and 6.3 use the kit's merged statements. The 16 statements sharpened earlier for the overlapping pairs go back to the kit's wording, and the "how it differs" notes become the kit's `partial_overlap_with` field. `data/schemas/principles.schema.json` is now 2.0.0.
- `principles/<id>.md` is regenerated from the kit's data by `scripts/build-principles.py`, in the kit's layout. Retired IDs no longer have a file in `principles/`; they resolve through `aliases`, and the site keeps a redirect page for each.
- Licence: text is CC BY-SA 4.0 and code is GPL-3.0-only, set in `LICENSE.md` with the full texts in `LICENSES/`. `docs/` (the site) now sits with the code under GPL-3.0-only, `data/schemas/` and CI stay GPL-3.0-only, and `template/` stays MIT. `LICENSES/` holds the canonical plain-text legalcode. The root `LICENSE` is now a pointer to `LICENSE.md`; this is a deliberate change to `LICENSE`.
- README merged with the kit's README: the kit's dedup verdict, licence cleanup, test apps, run and scorecard sections, and links to `CREDITS.md`, `LICENSE.md` and `LICENSES/`.
- The five survivor skills' `principles:` front matter lists only the survivor; the retired ID stays in `aliases:`. Skill 8.5 says 103 skills instead of 108.
- `scripts/build-site.py` reads the kit's data (minimal change so the site still builds): sources come from each principle's primary files in `data/mapping.json`, each principle page links its skill, and the footer links `LICENSE.md` and `CREDITS.md`.
- `UPDATING.md`, `CONTRIBUTING.md`, `NOTICE.md`, `ATTRIBUTIONS.md`, `data/README.md`, `scripts/README.md` and `skills/README.md` describe the kit's layout and licences.

Removed:

- `LICENSE-CONTENT` (its CC BY-SA 4.0 text is now `LICENSES/CC-BY-SA-4.0.txt`).
- `principles/4.4.md`, `4.5.md`, `9.4.md`, `5.6.md` and `2.11.md` (alias stubs).

### Added

- Folder structure and placeholder READMEs for principles, skills, agents, commands, guides, docs, template and scripts.
- `README.md`, `UPDATING.md`, `CONTRIBUTING.md`, `NOTICE.md`.
- `data/principles.json`: 108 principles in 9 categories, imported from the initial research (run-1). No merges, no drops. The count is 103 after the dedupe listed under Changed.
- `data/sources.json`: the 41 source repos. Not pinned yet. Licences checked on 2026-11-26: 25 MIT, 6 Apache-2.0, 1 CC0-1.0, 1 CC-BY-SA-4.0, 3 with no licence file, and 5 described by their licence file (all rights reserved, CC BY-NC-ND 4.0, per-skill licences, Apache-2.0 text that GitHub reports as Other). Flags are in `ATTRIBUTIONS.md`.
- JSON schemas (version 1.0.0) for principles, sources and the data changelog in `data/schemas/`.
- `principles/<id>.md` for each principle, generated by `scripts/build-principles`.
- `scripts/refresh-sources.py` to compare pinned SHAs with upstream heads.
- `scripts/new-project.sh` and a minimal `template/`.
- `ATTRIBUTIONS.md`: links to all 41 source repos with their checked licences, and to works referenced but not sourced.

- Learning site in `docs/` (static, client-side JavaScript only, no build step to view, no trackers): a home page that walks the nine categories as a learning path, one page per category, one page per principle with sources linked through `data/sources.json`, a searchable, filterable and sortable table of all principles, a sources page, and the developer guide pages from `guides/developer/` (the guide is still a stub and the page says so). Generated by `scripts/build-site.py` from `data/` and `guides/developer/`, which also writes JSON copies to `docs/data/`.
- CI in `.github/workflows/ci.yml`: validates `data/*.json` against `data/schemas/` (`scripts/validate-data.py`), checks internal links in `docs/` and markdown (`scripts/check-links.py`), and fails if `principles/` or `docs/` are stale (`--check` on the two build scripts).

- Template profiles: `solo` (default), `small-team` and `large-org`, as small overlays in `template/profiles/`. One shared base, no copies. Solo skips gates and has no roles file. Small team adds a light review process and a short `ROLES.md`. Large org adds review gates, `ROLES.md` with owners and `.github/CODEOWNERS`.
- Base template now includes `CHANGELOG.md` and a basic pull request template, and `AGENTS.md` and `README.md` name the profile used.

### Changed

- Merged five duplicate principles, taking the count from 108 to 103 (dedupe pass by Rex). The old ID stays as an alias on the survivor, no other principle was renumbered, and the old principle pages redirect to the survivor. Details and reasons are in [MERGES.md](MERGES.md).
  - 4.4 into 4.1 (one test per cycle is a rule within red-green TDD).
  - 4.5 into 5.3 (the reproducing test is the first step of 5.3).
  - 9.4 into 5.1 (same technique, same source).
  - 5.6 into 5.10 (same rule).
  - 2.11 into 6.3 (same rule).
- Sharpened the wording of eight overlapping pairs that stay separate, and added a "how it differs" note to each principle: 2.14/3.5, 7.6/7.10, 7.1/8.7, 4.9/7.12, 3.14/5.4, 8.5/9.9, 8.1/8.3, 2.5/3.1.
- `data/schemas/principles.schema.json` is now version 1.1.0, with optional `aliases` and `distinct_from` fields. To migrate, set `schema_version` to `"1.1.0"` in `data/principles.json`; existing entries stay valid.
- `UPDATING.md` and `CONTRIBUTING.md`: a merged principle now leaves the list and lives on as an alias, instead of staying with a `merged` status.

- The site homepage is now a landing page (`docs/index.html`) that explains what the project is, who it is for, how the loop works, what you can do on the site and how to start a project from `template/`. Counts on it come from the data. The learning path moved to `docs/path.html`, and the nav and breadcrumbs on every generated page now start at Home. Generated by `scripts/build-site.py`.
- Renamed `scripts/build-principles` to `scripts/build-principles.py` so every script has an extension that matches its language. References in the README, CONTRIBUTING, UPDATING, the pull request template, the CI workflow and the generated `principles/` files are updated.
- The learning site's visible name is "AI SDLC Loop" (page titles, header and footer). The repo name and URLs are unchanged.

- `scripts/new-project.sh` takes a profile argument (`scripts/new-project.sh <target-dir> [profile]`, default `solo`), shows usage with `--help` or on bad input, and still refuses a target that is not empty. It copies the base, then applies the profile.

- Guides folder is `guides/developer/`. The guides cover everything, including what experienced developers already know.
- Split the licence. GPL-3.0 stays on the code (`scripts/`, `data/schemas/`, tooling; text in `LICENSE`). CC BY-SA 4.0 covers the writing, including `data/principles.json`, `data/sources.json`, `data/changelog.json` and `data/notes/` (full text in `LICENSE-CONTENT`). The README explains the choice.
- Everything under `template/` is MIT (`template/LICENSE`, copyright Shravi Limited and contributors, 2026). A project created with `scripts/new-project.sh` inherits MIT.
