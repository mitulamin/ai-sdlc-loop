# ai-sdlc-loop

A public starter for building your own learning agentic loops. Take it as a base, run it on your own work, and let it learn how you and your team build software.

It is a base, not a finished product. Fork it, copy it, strip out what you do not want, and let your own experience change it.

## Status

This repo is being built in phases. Right now it has the 103 principles as data and one file each, one amalgamated skill per principle (103, imported from the amalgamated-skills kit, see [IMPORT.md](IMPORT.md)), the skill-to-principle map, the licence record for every source, the list of 41 source repos, and the process for keeping all of it fresh. Wiring the agents and slash commands to the skills, and showing the skills on the website, come next. Each folder has a short README that says what will go in it.

## How this came about

At Shravi Limited we are building aidev, a software engineering team in a box. I wanted agents that do real software work end to end without me steering every step.

The ideas for that are scattered across dozens of public repos: skills, sub-agents, slash commands, rules files. Lots of them say the same thing in different words. Some contradict each other. Some are risky to install. And if you load them all, the descriptions alone eat your context window before the agent does anything useful.

So I had a research bot, Rex, read 41 public repos covering roughly 1,060 skills, sub-agents and commands. The result was 108 principles in 9 categories, and a dedupe pass merged five duplicates, leaving 103 (see [MERGES.md](MERGES.md)). This repo turns that research into something you can use, and something that can be redone as the field moves.

## What it aims to do

1. Give you a set of principles that are written down, numbered, and traceable to where they came from.
2. Turn each principle into one skill an agent can load when it needs it, with the sources and the dedupe notes next to it.
3. Give you agents and slash commands that use those skills and can look up the principles they rely on.
4. Let you start a new project from a template with all of that wired in.
5. Learn from every project, and get better each time.

The point is not my 103 principles. The point is the loop that produced them and the loop that keeps improving them. Swap in your own.

## From prompt to context to harness

I think of this as three steps.

**Prompt engineering** is writing a good instruction. It helps, but it is one message.

**Context engineering** is deciding what the model sees: which files, which spec section, which rules, nothing more. A lot of agent failures are context failures: too much loaded, or the wrong thing loaded.

**Harness engineering** is building the system around the model: who starts which agent, with what context, who checks the work, what gets written to disk, what gets learned afterwards. The model is one part. The harness is what makes it reliable.

This repo is mostly harness. Skills are layered so a short description is always in view and the full body only loads when it is needed. That keeps things cheap and predictable.

## The coordinator model

I only talk to one agent, the coordinator. It does not do the work itself. It plans, then starts new agents with blank contexts and gives each one exactly the context it needs for its job. When they finish, it reviews what came back and decides what happens next.

Blank contexts matter. An agent that has not seen the whole conversation cannot be misled by it, and it cannot carry earlier mistakes forward.

## Independent loops

Once a loop starts, it runs on its own. It does not come back to me at every step. It comes back at the end of a cycle, with the result and a request for feedback.

Every phase in the loop is a pair:

- a **producer**, which gets the dos and don'ts for that phase in one pass, and
- an **adversarial reviewer**, which checks only against the don'ts and known failure modes, and is strictly there to find problems.

After the last phase there is a human acceptance review. That is where my judgement goes, and only there.

## The Learn loop

The end-of-cycle review feeds the Learn category (principles 9.1 to 9.12). When I give feedback, the loop asks three things in order:

1. Which phase failed, and how?
2. Which do or don't rule was at fault?
3. How do we harden that phase's checklist so it is caught next time?

A change only goes live if it helps on cases held out from the one that caused it, and a human approves it. Every accepted and rejected edit is recorded. If a mistake is mechanical, the fix is a lint or a CI check, not another paragraph in a prompt.

## What is in the repo

| Path | What it holds |
| --- | --- |
| `skills/<id>-<slug>/` | One amalgamated skill per principle (103): `SKILL.md` (when to use, the producer's dos and don'ts together, steps, adversarial reviewer checks, how the sources compare, test slot) and `SOURCES.md` (every source file, pinned to a commit, with its licence, plus any link-only reading). |
| `principles/<id>.md` | One file per principle (103). Generated from `data/` by `scripts/build-principles.py`. |
| `data/principles.json` | The index of the 103 principles, with `aliases` for the 5 retired IDs. |
| `data/skill-principle-map.json` | Skill folder to principle, aliases, category, test app, phase, slot and licence status. The single source for wiring skills by ID. |
| `data/mapping.json`, `data/licences.json` | Principle to source files; licence per repo and per source. |
| `data/sources.json`, `data/changelog.json`, `data/schemas/` | The 41 research source repos and their pins, the machine-readable change log, and the JSON schemas. |
| `scorecard.csv` | One row per skill, filled in during the test runs. |
| `MERGES.md` | The five duplicate principles merged into survivors (108 to 103), and what was folded in. |
| `CREDITS.md` | The sources the skills were adapted from, with licence, copyright notice and pinned commit, and the link-only sources. |
| `LICENSE.md`, `LICENSES/` | The licence split and the full licence texts. |
| `IMPORT.md` | How the amalgamated-skills kit was imported. |
| `agents/` | The coordinator, and a producer and a strictly adversarial reviewer per phase, each declaring the skills it loads and the principle IDs it can look up. Generated from `data/skill-principle-map.json` by `scripts/build-agents.py`. |
| `commands/` | Slash commands for the main loop: `/plan`, `/design`, `/build`, `/verify`, `/review`, `/ship`, `/retro`, each loading the skills for its phases. Generated by `scripts/build-agents.py`. |
| `guides/developer/` | Plain-language guides to the principles. Coming. |
| `docs/` | The static website (GitHub Pages). |
| `template/` | The shared base a new project copies, and `template/profiles/` with the solo, small-team and large-org overlays. |
| `scripts/` | `validate.py` (checks the kit: 103 principles, 103 skills, 5 aliases, slots, licences), `build-principles.py`, `build-agents.py`, `build-site.py`, `validate-data.py`, `check-links.py`, `refresh-sources.py`, `new-project.sh`. |

## Dedup verdict
- 108 principles became 103. Five true duplicates were merged into survivors (IDs not renumbered; old IDs are aliases): 4.4 into 4.1, 4.5 into 5.3, 9.4 into 5.1, 5.6 into 5.10, 2.11 into 6.3. See `MERGES.md`.
- 8 partial overlaps remain as separate principles: 2.14/3.5, 7.6/7.10, 7.1/8.7, 4.9/7.12, 3.14/5.4, 8.5/9.9, 8.1/8.3, 2.5/3.1.
- Source files: 1,000 engineering items, of which 70 are identical copies (mostly wshobson agents repeated across plugins); copies are counted once.
- How files were mapped: a regex per principle over each file's name, description and body, kept only when the category also matched, plus primary files picked by hand from the sources the principle cites. Keyword matches are candidates and some big lists include loosely related files.

## Testing the skills

The test-app workflow comes after the import. Run order is by `slot` in `data/skill-principle-map.json`, and scoring is in `scorecard.csv`.

### Test apps
- Run 1, App A: CLI tool, greenfield (for example a `ledger` CLI that imports bank CSVs, categorises them by rules and prints monthly reports). 22 skills first.
- Run 2, App B: a small CRUD web app with auth, greenfield (for example "teamtasks": sign-up and login, projects and tasks, a REST API, SQLite or Postgres, a minimal UI). 49 skills first.
- Run 3, App C: brownfield. Fix one real open bug and do one small refactor in a small, well-tested open-source repo (for example pallets/click), as a PR on a fork. 11 skills first.
- Skills marked "All" (Agent operations and Learn, 21 skills) run in all three runs and are scored in each.

### How a run works (the coordinator model)
1. Mitul gives the brief to the top coordinator only.
2. The coordinator triages the brief (1.8) and loads only the skills for that run and phase. It briefs fresh, blank-context producer agents with the dos and don'ts plus the relevant context (8.1, 1.6).
3. Each phase has a strictly adversarial reviewer in a fresh context, using the skill's reviewer checks. Its default verdict is FAIL, and it writes findings to files (8.8).
4. Loops run on their own until the phase's checks pass. No human input during the run.
5. At the end, the coordinator fills in `scorecard.csv` from the transcripts and reviewer files, and writes `run-summary.md`.
6. Human feedback, about 30 minutes: Mitul tries the app, reads the summary, and marks each skill keep, merge or drop, with notes.
7. Learn step (9.x skills): corrections are queued (9.11) and grouped by mechanism (9.6). Small edits are proposed, one surface each (9.8), and tested on held-out tasks (9.9). Mitul approves them (9.10) and they are logged in `learn-ledger.md` (9.12). The next run uses the edited skills.

### Scorecard (`scorecard.csv`, one row per skill per run)
Each criterion is scored 0, 1 or 2: triggered, followed, reviewer_caught, outcome, cost. harm_flag is Y if the skill caused wrong work, a loop or bloat.
- KEEP: 7 or more out of 10 in at least two runs, with no harm flag.
- MERGE: its effect is indistinguishable from another skill's.
- DROP: it never triggered, or scored 4 or less in every run where it applied.
- The human note overrides any of these.

## Start a new project from the template

Clone it and run the script with a profile:

```bash
git clone https://github.com/mitulamin/ai-sdlc-loop
cd ai-sdlc-loop
scripts/new-project.sh ../my-new-project              # solo, the default
scripts/new-project.sh ../my-new-project small-team
scripts/new-project.sh ../my-new-project large-org
scripts/new-project.sh --help                         # usage and the list of profiles
```

The script copies the shared base from `template/`, applies the profile on top, and runs `git init`. It refuses a target folder that is not empty. Then edit the new project's `AGENTS.md` (stack, commands, conventions, boundaries), read its `PROCESS.md`, and start your first loop.

### Pick a profile

An individual and a large company share the same principles. What changes is ceremony: gates, roles, review and ownership. So there is one base template, and three profiles that switch that ceremony on or off. I did not make three separate trees.

| Profile | For | What you get on top of the base |
| --- | --- | --- |
| `solo` | One person | A short `PROCESS.md` with no gates. No roles file and no pull request template. |
| `small-team` | A few people | A light `PROCESS.md` (branch, pull request, one reviewer), a short `ROLES.md`, and the base pull request template. |
| `large-org` | Many people | `PROCESS.md` with review gates, a `ROLES.md` table with owners, `.github/CODEOWNERS`, and a pull request template with the gates as a checklist. |

Every profile starts from the same base: `README.md`, `AGENTS.md`, `CHANGELOG.md` and the MIT `LICENSE`. If you are unsure, start with `solo` or `small-team`. It is easier to add ceremony later than to remove it. The large-org profile is a starter, not a process manual.

Profiles live in `template/profiles/<name>/`. Each one is small: a `profile.txt`, an optional `omit` list of base files to leave out, and an `overlay/` folder of files to add or replace. The base is never copied into a profile. To add your own, see [CONTRIBUTING.md](CONTRIBUTING.md#add-or-change-a-template-profile).

You can also use this repo as a GitHub template (**Use this template** on the repo page), but then you get the whole repo, not a profile. The script is the intended route.

## How the repo stays alive

This is not a one-off. The research should be re-run about every six months, because the sources move, new ones appear and some disappear.

Every source file a skill was written from is pinned to a commit in its `SOURCES.md` and in `data/licences.json`. The research source repos are listed in `data/sources.json`, where repo-level pins are still to be set; `scripts/refresh-sources.py` compares each pin with the upstream head and tells you what changed. Principles record what was merged into them, skills list their sources, data files have schemas, and generated files are kept apart from hand-written ones so a refresh does not overwrite human edits. Every merge, drop and change is logged in `CHANGELOG.md` and `data/changelog.json`.

The full process is in [UPDATING.md](UPDATING.md).

## Make it yours

If you use this for yourself or your organisation, the intended path is: copy it, replace the principles and sources with the ones you trust, run your own projects through the loop, and let your own Learn loop reshape it. If you find something that would help everyone, send it back. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

Text is CC BY-SA 4.0 and code is GPLv3. The split, file by file, is in [LICENSE.md](LICENSE.md), and the full texts are in [LICENSES/](LICENSES/). Credits for every source the skills were adapted from are in [CREDITS.md](CREDITS.md).

| What | Licence | Full text |
| --- | --- | --- |
| Skills, principles, guides, the data in `data/`, `scorecard.csv`, and the other writing | CC BY-SA 4.0 | [LICENSES/CC-BY-SA-4.0.txt](LICENSES/CC-BY-SA-4.0.txt) |
| Scripts, the GitHub Pages site in `docs/`, CI, `data/schemas/` and other tooling | GPL-3.0-only | [LICENSES/GPL-3.0-only.txt](LICENSES/GPL-3.0-only.txt) |
| Everything under `template/` | MIT | [template/LICENSE](template/LICENSE) |

### Licence cleanup
- Text is CC BY-SA 4.0 and code is GPLv3 (`LICENSE.md`). Sources with no usable licence are link only and were not copied or adapted: michaelshimeles/rstack, multica-ai/andrej-karpathy-skills, NousResearch/hermes-agent-self-evolution, anthropics/skills doc-coauthoring, anthropics/claude-plugins-official plugins/claude-security (and, if ever cited, anthropics/claude-code, hesreallyhim/awesome-claude-code, travisvn/awesome-claude-skills and sickn33's bundled third-party skills).
- 24 skills had link-only sources. Their text was rewritten from clean sources where it leaned on them, the sources moved to "Further reading (link only)", and 7.12 was rebuilt from four MIT repos. See `CREDITS.md` and `data/licences.json`.

### Why GPLv3, and CC BY-SA for the writing

I am not a lawyer, and this is not legal advice. If you think this is the wrong licence for the intent, open an issue. I am open to discussing a better one.

I want the widest use, without restricting anyone. People should be able to include this in their own projects, and companies should be able to use it for private software development. I do not want someone to take this, add proprietary work on top, and lock that work into their own systems. If you benefit from open source, contribute back.

This is a tool for builders, not a consumer end product. I want it kept open rather than closed down into an end product.

MIT would have been my first choice. There is a clear push and pull between open and proprietary software today, and individuals' generosity is being used for financial gain. I want to back open source, so I chose GPLv3 for the code: `scripts/`, the GitHub Pages site in `docs/`, CI, `data/schemas/` and the tooling.

In short: private internal use and modification by a company is allowed, with no duty to publish, because the duties start when you distribute. Anyone who distributes a work that includes this code must release the whole combined work under GPLv3, with source. Hosted or SaaS use that never distributes the code does not start those duties. AGPL-3.0 is the licence that closes that gap. I could discuss it. I am not choosing it here.

Everything under `template/` is MIT, code and writing. The template is meant to be copied into a new project, and GPL would stop someone who wants to start an MIT project from using it. `scripts/new-project.sh` copies the base and the profile you pick, including that licence, so the new project starts under MIT.

The writing is CC BY-SA 4.0: the skills, the principles, the guides, the data files in `data/` and `scorecard.csv`, and the markdown in this repo outside `template/`. You can share and adapt it with attribution. Share-alike means derived text stays under CC BY-SA 4.0, so it stays open. CC BY-SA 4.0 can absorb text from MIT, Apache-2.0, CC BY and CC BY-SA sources, which is why the skills could be written from them.

Borrowed source repos keep their own licences. They are not relicensed here. The sources each skill adapts are credited in its `SOURCES.md` and in [CREDITS.md](CREDITS.md), the licensing notes are in [NOTICE.md](NOTICE.md), and every project I used or referenced is linked in [ATTRIBUTIONS.md](ATTRIBUTIONS.md).

## Sources

I never install the big curation lists wholesale. They overload context and contain files I would not trust. Anything borrowed gets scanned before it goes in.
