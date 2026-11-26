# Importing this kit into the aidev repo

This kit replaces the 108-skill drafts. It contains 103 principles, 103 amalgamated skills (one per principle) and 5 aliases for merged duplicates. It already includes the duplicate merges and the licence cleanup, so it supersedes any earlier "dedupe" or "licence cleanup" instruction: do not run those again.

## 1. Unzip into the repo root

Everything lands in place, nothing needs moving:

| In the zip | In the repo | Notes |
|---|---|---|
| `skills/<id>-<slug>/SKILL.md` + `SOURCES.md` | same | 103 folders. Replace any existing `skills/` drafts. |
| `principles/<id>.md` | same | 103 files, one per principle. |
| `data/principles.json` | same | The index, with `aliases` for retired IDs. |
| `data/skill-principle-map.json` | same | Skill folder to principle, aliases, category, test app, phase, slot, licence status. Use this to wire everything by ID. |
| `data/mapping.json`, `data/licences.json` | same | Principle to source files; licence per repo and per source. |
| `scorecard.csv` | same, or convert to `data/scorecard.json` | One row per skill; filled during the test runs. |
| `MERGES.md`, `CREDITS.md`, `LICENSE.md`, `LICENSES/` | same | Text is CC BY-SA 4.0, code is GPLv3. |
| `scripts/validate.py` | same | Run in CI. |
| `README.md`, `IMPORT.md` | same | Merge the README with the repo's own if one exists. |

## 2. Licences

- Skills, principles, guides and data: CC BY-SA 4.0. Code, scripts, the docs site and CI: GPLv3. Put the split in the repo's root `LICENSE` or point it at `LICENSE.md`, and keep `LICENSES/`.
- Keep `CREDITS.md`. Do not copy any file from the link-only repos into the repo: they are only linked from "Further reading (link only)" sections.

## 3. Principles, aliases and skills

- IDs are not renumbered. Retired IDs resolve through `aliases` in `data/principles.json`: 4.4 to 4.1, 4.5 to 5.3, 9.4 to 5.1, 5.6 to 5.10, 2.11 to 6.3.
- Any agent, command, doc or test that mentions a retired ID must resolve it to the survivor. Search for `4.4`, `4.5`, `9.4`, `5.6` and `2.11` as principle IDs.
- Each principle has exactly one skill: look up `principle_id` in `data/skill-principle-map.json` to get the folder.

## 4. Wire agents and commands to skills by ID

- Each agent file declares the skills it loads and the principle IDs it can look up. Build those lists from the map: for the agent's phase, take the skills whose `category_id` or `phase` matches.
- Producers load the skill's dos and don'ts together. Reviewers load only the "Adversarial reviewer" section and the don'ts.
- Slash commands (/plan, /design, /build, /verify, /review, /ship, /retro) load the skills for their phase.

## 5. Docs site and CI

- Regenerate the docs site data from `data/` (principles, mapping, skill map, licences, scorecard). The site shows 103 principles with aliases noted, and licence status per source.
- CI must run `python3 scripts/validate.py` (expects 103 principles, 103 skills, 5 aliases, slots 1 to 103, no non-adaptable source in a main source list), plus the link checker and the SkillSpector scan of `skills/`.

## 6. Test runs

The test slot is in each skill's `SKILL.md` and in the map (`test_app`, `phase`, `slot`). Run order is by `slot`. See `README.md` for the three test apps, the loop and the scorecard.
