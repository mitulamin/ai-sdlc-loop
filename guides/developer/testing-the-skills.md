# Testing the skills

Each of the 103 principles has one amalgamated skill. Before any of them is trusted, it is tried out on three small app builds run by the coordinator and its agents, and scored keep, merge or drop. This guide explains the test apps, the run order, how a run works and how the scorecard is filled in.

The live data is on the [skills page](../../docs/skills.html), which lists every skill with its slot, phase, test app, licence status and score. The machine-readable sources are [data/skill-principle-map.json](../../data/skill-principle-map.json) (slots, phases and test apps), [data/taxonomy.json](../../data/taxonomy.json) (phases, test apps and the run order) and [data/scorecard.json](../../data/scorecard.json) (scores and verdicts).

Sections:

- [Words used in this guide](#words-used-in-this-guide)
- [Where things stand](#where-things-stand)
- [Merges and aliases](#merges-and-aliases)
- [The three test apps](#the-three-test-apps)
- [Run order](#run-order)
- [How each run works](#how-each-run-works)
- [The keep, merge or drop scorecard](#the-keep-merge-or-drop-scorecard)
- [A worked scoring example](#a-worked-scoring-example)
- [Caveats](#caveats)

## Words used in this guide

| Term | What it means here |
| --- | --- |
| Amalgamated skill | One skill per principle, written by combining the matching skill files from the source repos into a single `SKILL.md`. |
| Slot | A skill's place in the test run order, from 1 to 103. |
| Test app | The small project a skill is first exercised on: A, B or C. Skills tagged All are exercised on every app. |
| Run | One build of one test app through the loop, from brief to end-of-cycle review. |
| Greenfield | A new project started from nothing. |
| Brownfield | Work on an existing codebase someone else wrote. |
| Scorecard | The record of how each skill did on each run, kept in `data/scorecard.json`. |
| Verdict | The decision for a skill after the runs: keep, merge or drop. |
| Harm flag | A yes or no mark for a skill that caused wrong work, a loop or bloat during a run. |
| Alias | A retired principle ID that now points to the principle it was merged into. |

## Where things stand

There are 103 principles in 9 categories and one skill for each, drawn from 45 source repos. Every source repo is pinned to a full 40-character commit SHA in [data/sources.json](../../data/sources.json), and the [sources page](../../docs/sources.html) lists them with their licences.

All 103 skills are drafts and none has been run yet, so every row in the scorecard is empty. The skills page shows the current count as runs are scored.

Each skill also has a licence status. Clean means every source could be adapted. Rewritten means some sources were link only, so the skill text was written in this repo's own words and those sources moved to Further reading. One skill, 7.12, was rebuilt from MIT-licensed sources. The status is on each skill's row on the skills page and on its principle page.

## Merges and aliases

The research produced 108 principles; five duplicates were merged into survivors, leaving 103. The five merges were approved by Mitul, the repo's owner. Principle IDs were never renumbered: a retired ID stays as an alias on its survivor, and its old page redirects there. Do not treat a retired ID as a live principle.

| Retired ID | Merged into | Survivor |
| --- | --- | --- |
| 4.4 | [4.1](../../docs/principles/4.1.html) | Write one failing test first and watch it fail, then write the minimal code to pass; one seam per cycle, never all tests up front. |
| 4.5 | [5.3](../../docs/principles/5.3.html) | Reproduce the bug with a failing test first, then localise, reduce, fix, keep the test as a guard, and verify end to end. |
| 9.4 | [5.1](../../docs/principles/5.1.html) | No fixes without root-cause investigation first: trace back to the original trigger, not where the symptom showed up. |
| 5.6 | [5.10](../../docs/principles/5.10.html) | Never log or display secrets, tokens or full personal data, including in debug output. |
| 2.11 | [6.3](../../docs/principles/6.3.html) | Validate all external input at the boundary, treat external API responses as untrusted too, parameterise queries and encode output. |

Each retired principle's dos, don'ts, steps, reviewer checks and sources were folded into its survivor without repeats. The reasons and dates are in [MERGES.md](../../MERGES.md).

Some pairs overlap without being duplicates, so they were kept as separate skills with sharper wording: 2.14 and 3.5, 7.6 and 7.10, 7.1 and 8.7, 4.9 and 7.12, 3.14 and 5.4, 8.5 and 9.9, 8.1 and 8.3, and 2.5 and 3.1. These are the pairs most likely to earn a merge verdict if the runs cannot tell their effects apart.

## The three test apps

Each app is small on purpose: big enough to exercise its skills for real, small enough to run often.

### App A: a CLI tool, greenfield (run 1)

A new `ledger` command-line tool that imports bank CSV files, sorts transactions into categories by rules, and prints monthly reports. It exercises planning, deep modules and seams, code craft and test-driven development, and the harness skills are set up here.

- **Skills scored first here:** 22, plus the 21 that apply on every run
- **Size:** about 1 to 2 days of agent time

### App B: a small CRUD web app with auth, greenfield (run 2)

`teamtasks`: sign-up and login, projects and tasks, a REST API on SQLite or Postgres, and a minimal UI. CRUD means create, read, update and delete, the four basic operations on stored records. It exercises specs and task breakdown, domain-driven design, API design, designing for failure, security, OpenTelemetry instrumentation, CI and shipping.

- **Skills scored first here:** 49
- **Size:** about 2 to 3 days of agent time

### App C: a brownfield fix and refactor (run 3)

Fix one real open bug and do one small refactor in a small, well-tested open-source repo (for example pallets/click), as a pull request on a fork. It exercises debugging, surgical changes, Chesterton's fence, refactoring, test-suite review and a dependency audit.

- **Skills scored first here:** 11
- **Size:** about half a day to 1 day

### Skills tagged All

The 21 skills tagged All are the Agent operations skills (the harness, 8.1 to 8.10) and the Learn skills (9.1 to 9.12, without the retired 9.4). They run in all three builds and get a score in each one. That adds up: 22 + 49 + 11 + 21 = 103.

## Run order

This is the run order as written in [data/taxonomy.json](../../data/taxonomy.json):

Skills are tested in slot order (1 to 103, see data/skill-principle-map.json): Agent operations (the harness) first, then the three test apps in order (A, B, C). Each app run walks Plan, Design, Build and Verify, then Debug, Secure and Review as needed. Learn is exercised on the first run (slots 33-43) so the retrospective is tested early. Skills tagged All apply on every run.

In slot terms, from [data/skill-principle-map.json](../../data/skill-principle-map.json):

| Slots | Skills | Test app |
| --- | --- | --- |
| 1 to 10 | Agent operations (Harness phase) | All |
| 11 to 32 | Plan, Design, Build, Verify, and 7.1 from Review & ship | A |
| 33 to 43 | Learn | All |
| 44 to 92 | Plan, Design, Build, Verify, Debug, Secure, Review & ship | B |
| 93 to 103 | Build, Verify, Debug, and 6.8 from Secure | C |

Slots were renumbered after the merges so they run 1 to 103 without gaps. Principle IDs were not.

## How each run works

1. **Brief the coordinator only.** The human gives the brief to the top coordinator. Nobody else talks to the human.
2. **Triage and load.** The coordinator sizes the task ([1.8](../../docs/principles/1.8.html)) and loads only that run's skills for each phase. It briefs fresh, blank-context producers with the dos and don'ts plus the context they need ([8.1](../../docs/principles/8.1.html), [1.6](../../docs/principles/1.6.html)).
3. **Independent loops per phase.** Each phase runs until its checks pass: Plan, Design, Build, Verify, Debug, Secure, then Review & ship. Nobody asks the human anything mid-run.
4. **Adversarial reviewer per phase.** Each reviewer is a fresh agent using the skill's reviewer checks. Its default verdict is FAIL, and it writes findings to files with P0 to P3 severity ([8.8](../../docs/principles/8.8.html), [7.5](../../docs/principles/7.5.html)).
5. **The coordinator scores the run.** It fills in [data/scorecard.json](../../data/scorecard.json) from the transcripts and reviewer files, and writes `run-summary.md`.
6. **Human feedback at the end.** About 30 minutes: the human tries the app, reads the summary, and marks each skill keep, merge or drop, with notes.
7. **Learn.** Corrections are queued ([9.11](../../docs/principles/9.11.html)) and grouped by mechanism ([9.6](../../docs/principles/9.6.html)). Small edits are proposed, one surface each ([9.8](../../docs/principles/9.8.html)), and checked on held-out tasks ([9.9](../../docs/principles/9.9.html)). The human approves them ([9.10](../../docs/principles/9.10.html)) and they are logged ([9.12](../../docs/principles/9.12.html)). The next run uses the edited skills.

[Using the agents and commands](using-the-agents.md) explains the agents and commands that carry out these steps.

## The keep, merge or drop scorecard

Each skill has one row in `data/scorecard.json`, in slot order. Each run adds an entry to that row's `runs`. Five criteria score 0, 1 or 2, so a run's total is out of 10, and a separate harm flag is yes or no.

| Criterion | Field | What a 2 looks like | Evidence |
| --- | --- | --- | --- |
| Triggered | `triggered` | Loaded at the right moment: its description fired or the coordinator chose it | Transcript |
| Followed | `followed` | The producer did what the dos and don'ts say | Transcript, diff |
| Reviewer caught | `reviewer_caught` | The reviewer used its checks and found or confirmed something real | Reviewer file |
| Outcome | `outcome` | A defect was prevented or caught, there were fewer loops, or the artefact was better | Tests, run summary |
| Cost | `cost` | The tokens and time were worth it | Usage log |
| Harm flag | `harm_flag` | Yes if it caused wrong work, a loop or bloat | Reviewer, human |

A score of 1 means partly: for example, the skill loaded but late, or the producer followed some of the rules. A 0 means not at all.

The verdict rules:

- **Keep:** 7 or more out of 10 in at least two runs, with no harm flag.
- **Merge:** its effect cannot be told apart from another skill's.
- **Drop:** never triggered, or scored 4 or less in every run where it applied.
- **The human's end-of-run note overrides any score.** It is stored as `human_note` on the run, and the final decision as `verdict`.

## A worked scoring example

Suppose skill 5.8 (structured logs) is first scored on App B. It triggered when the producer added logging (2). The producer used structured logs with levels but skipped one endpoint (1). The reviewer's check caught the missing endpoint (2). The fix made a failing request easy to trace (2). It cost little (2). That is 9 out of 10 with no harm, and the run entry looks like this:

```
{
  "run_id": "run-2-app-b",
  "date": "2026-12-03",
  "scores": {
    "triggered": 2,
    "followed": 1,
    "reviewer_caught": 2,
    "outcome": 2,
    "cost": 2
  },
  "total": 9,
  "harm_flag": false,
  "evidence_link": "runs/run-2-app-b/review-debug.md",
  "human_note": ""
}
```

One run is not enough for a keep: the rule needs 7 or more in at least two runs. A skill tagged All, such as 8.8 (reports to files), gets an entry on every app, so it reaches two runs sooner. A skill that never triggers on any run where it applied is dropped, whatever its other scores.

## Caveats

- The amalgamated drafts were written by reading the matching passages in their primary sources, not every line of every file. Treat them as starting drafts for the test runs.
- Some skills have thin clean evidence. 2.4 (separate orchestration from reusable service operations) is the likeliest drop.
- Source mapping started from keyword matches, so some skills cite loosely related files. Each skill's `SOURCES.md` lists what it was built from.
- The licence checks are a research check, not legal advice.
