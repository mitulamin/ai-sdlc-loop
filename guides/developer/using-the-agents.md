# Using the agents and commands

How to run the loop in this repo: who you talk to, what each agent and command does, the rules the loop follows, and how to keep it cheap. The agent and command files in [agents/](../../agents/README.md) and [commands/](../../commands/README.md) are the source of truth; this guide explains them. The [agents page](../../docs/agents.html) lists every agent and command with the skills it loads.

Sections:

- [Why the loop works this way](#why-the-loop-works-this-way)
- [Words used in this guide](#words-used-in-this-guide)
- [Before you start](#before-you-start)
- [The agents](#the-agents)
- [The commands](#the-commands)
- [What producers and reviewers load](#what-producers-and-reviewers-load)
- [The rules of the loop](#the-rules-of-the-loop)
- [The phase model and the Learn loop](#the-phase-model-and-the-learn-loop)
- [A worked example: one cycle](#a-worked-example-one-cycle)
- [Keeping token cost down](#keeping-token-cost-down)

## Why the loop works this way

The loop uses a coordinator model. The human talks only to a top-level coordinator, which starts new agents with blank contexts and fills each one with exactly the context it needs. Skills are layered: a short description is always in view, and the full skill is loaded only when a phase needs it. That layering is what makes the model cheap and reliable.

The aim is loops that run on their own from start to finish, come back to the human for feedback at the end, learn what they did not do well, and get better with each software project. Every mid-loop question to the human is a blocker that slows the process down, so the human stays out of each step. The human's judgement goes into the end-of-cycle review instead, and that review feeds the [Learn](../../docs/categories/learn.html) category.

## Words used in this guide

| Term | What it means here |
| --- | --- |
| Agent | An AI model run with a set of instructions (an agent file) and tools, doing one job. |
| Coordinator | The one agent the human talks to. It plans, writes briefs, starts other agents and decides what happens next. It does not do the phase work itself. |
| Phase | One stage of the loop, such as Plan or Verify. Each phase is run by a producer and checked by a reviewer. |
| Producer | The agent that does a phase's work, such as writing the plan or the code. |
| Adversarial reviewer | A separate agent whose job is to prove the producer's work fails. It is not a collaborator. |
| Skill | One folder in `skills/` per principle, with a `SKILL.md` that holds When to use, Do and Don't lists, Steps and adversarial reviewer checks. |
| Brief | A file the coordinator writes for an agent: the task, the acceptance criteria, the files to read, the skill IDs that apply, and where to write the output. |
| Fresh context | A new agent that has not seen the conversation so far. It cannot be misled by earlier mistakes because it never saw them. |
| Findings file | The file a reviewer writes. Its first line is `Verdict: PASS` or `Verdict: FAIL`, followed by each finding with its evidence. |
| P0 to P3 | Severity of a finding: P0 is security, data loss or correctness; P3 is a nit. Any P0 or P1 is a FAIL. |
| Cycle | One pass of the loop from the human's brief to the end-of-cycle review. |
| Held-out cases | Test cases a proposed change was not tuned on. A learned edit must help on these, not just on the case that prompted it. |
| Harness | Everything around the model: who starts which agent, with what context, who checks the work, and what is written to disk. |

## Before you start

- **A coding-agent tool that can start subagents and run slash commands.** The agent and command files are plain markdown with front matter. Load them the way your tool expects; this repo does not install them for you. Skill [8.10](../../docs/principles/8.10.html) says to use your tool's own isolation and features rather than work around them.
- **A project with a short always-on rules file.** The template's `AGENTS.md` is a starting point: run `scripts/new-project.sh` to create a project from it (see the [home page](../../docs/index.html)). Keep it to stack, commands, conventions and hard boundaries, as skill [8.2](../../docs/principles/8.2.html) says.
- **Somewhere for run files.** Briefs, outputs, findings files and the end-of-cycle `run-summary.md` are written to files, not pasted into the chat (skill [8.8](../../docs/principles/8.8.html)). Scores go in [data/scorecard.json](../../data/scorecard.json).
- **Principle IDs resolve through aliases.** Retired IDs are aliases of the principle they were merged into: 4.4 is now [4.1](../../docs/principles/4.1.html), 4.5 is [5.3](../../docs/principles/5.3.html), 9.4 is [5.1](../../docs/principles/5.1.html), 5.6 is [5.10](../../docs/principles/5.10.html) and 2.11 is [6.3](../../docs/principles/6.3.html). The coordinator resolves an alias before it briefs anyone with it.

## The agents

There is one coordinator, plus a producer and an adversarial reviewer for each phase. Each phase loads the skills whose phase in [data/skill-principle-map.json](../../data/skill-principle-map.json) is that phase, so a category can feed more than one phase.

| Phase | Producer (role) | Reviewer | Started by | Skills from |
| --- | --- | --- | --- | --- |
| Harness | [harness-producer](../../agents/harness-producer.md) (harness engineer) | [harness-reviewer](../../agents/harness-reviewer.md) | the coordinator | Agent operations |
| Plan | [plan-producer](../../agents/plan-producer.md) (planner) | [plan-reviewer](../../agents/plan-reviewer.md) | `/plan` | Plan and specify |
| Design | [design-producer](../../agents/design-producer.md) (architect) | [design-reviewer](../../agents/design-reviewer.md) | `/design` | Design and architecture |
| Build | [build-producer](../../agents/build-producer.md) (implementer) | [build-reviewer](../../agents/build-reviewer.md) | `/build` | Code craft, plus 5.4 |
| Verify | [verify-producer](../../agents/verify-producer.md) (tester) | [verify-reviewer](../../agents/verify-reviewer.md) | `/verify` | Verify (testing) |
| Debug | [debug-producer](../../agents/debug-producer.md) (debugger) | [debug-reviewer](../../agents/debug-reviewer.md) | `/verify` | Debug and observe |
| Secure | [secure-producer](../../agents/secure-producer.md) (security engineer) | [secure-reviewer](../../agents/secure-reviewer.md) | `/review` | Secure, plus 5.10 |
| Review & ship | [review-and-ship-producer](../../agents/review-and-ship-producer.md) (release manager) | [review-and-ship-reviewer](../../agents/review-and-ship-reviewer.md) | `/review`, `/ship` | Review and ship, plus 5.15 |
| Learn | [learn-producer](../../agents/learn-producer.md) (learner) | [learn-reviewer](../../agents/learn-reviewer.md) | `/retro` | Learn |

The [coordinator](../../agents/coordinator.md) loads the Agent operations skills itself, because they govern how every agent in the loop runs. It starts the Harness producer and reviewer at the start of a run, to set up or check the project's agent harness, and again when approved Learn edits are applied.

## The commands

You give a command to the coordinator, and only to the coordinator. It runs each phase's loop on its own and reports at the end of the cycle.

| Command | Phases it runs | What it is for |
| --- | --- | --- |
| [/plan](../../commands/plan.md) | Plan | Turn the brief into a spec and a plan with verifiable goals. |
| [/design](../../commands/design.md) | Design | Design the modules, contracts and decisions the plan needs. |
| [/build](../../commands/build.md) | Build | Implement the plan in small, safe steps that keep the build green. |
| [/verify](../../commands/verify.md) | Verify, then Debug | Prove the build works with tests and evidence, and find the root cause of what fails. |
| [/review](../../commands/review.md) | Secure, then Review & ship | Review the change for security and quality before it ships. |
| [/ship](../../commands/ship.md) | Review & ship | Get the reviewed change merged and released through the gates. |
| [/retro](../../commands/retro.md) | Learn | Turn the human's end-of-cycle feedback into proposed skill and check edits. |

Three details matter:

- `/verify` runs Debug only when the Verify output shows failing behaviour (a failing test, a bug or an unexpected result), and only for those failures. Then it runs Verify again on the fix.
- There is one Review & ship phase, so `/review` and `/ship` start the same Review & ship producer and reviewer, each on its own task. `/review` runs Secure first.
- `/retro` runs only after the human has given end-of-cycle feedback. The Harness phase has no command: the coordinator runs it.

## What producers and reviewers load

Every `SKILL.md` has the same sections, and the two roles load different ones on purpose.

- **Producers** load each skill's When to use, its Do and Don't lists together, and its Steps. Getting the dos and don'ts in one pass means the producer builds to them from the start, instead of finding out about a don't only when the reviewer fails it.
- **Reviewers** load only each skill's adversarial reviewer checks and its Don't list. A reviewer must not open the skills' `SKILL.md` files, because those hold the producer's Do lists. Without the Do lists, the reviewer cannot drift into grading taste or style; it hunts for breaches of the don'ts and known failure modes, and tests each acceptance criterion in the brief.

This split is principle [9.2](../../docs/principles/9.2.html): enforce standards at review, not by loading them all into the implementer's context. The separate reviewer itself is principle [7.1](../../docs/principles/7.1.html).

## The rules of the loop

1. **Fresh-context agents.** Every producer and reviewer starts in a new, blank context ([8.7](../../docs/principles/8.7.html)). The coordinator writes each one a brief to a file with exactly what the job needs ([8.1](../../docs/principles/8.1.html), [1.6](../../docs/principles/1.6.html)).
2. **The reviewer sees the result, not the reasoning.** It gets the brief's task and acceptance criteria and the producer's output, never the producer's transcript. The producer's report is a claim to test, not evidence.
3. **Findings go to files.** The reviewer writes only its findings file ([8.8](../../docs/principles/8.8.html)). The default verdict is FAIL until evidence shows otherwise. Every finding has a severity from P0 to P3 ([7.5](../../docs/principles/7.5.html)), the skill ID and check it breaks, and evidence: a file and line, or a command and its output. A check the reviewer could not run counts as a FAIL, because not run is not passed ([4.9](../../docs/principles/4.9.html)).
4. **Fix and re-review.** On a FAIL, the coordinator starts a new producer with the brief and the findings file, then a new reviewer.
5. **Three FAILs in a row stops the phase.** The coordinator records the phase as failed with its findings and notes it as a question about the approach, rather than trying a fourth time ([5.5](../../docs/principles/5.5.html)).
6. **Reviewers are never overruled.** The coordinator does not override a reviewer's FAIL.
7. **No mid-cycle questions to the human.** Agents send questions to the coordinator, even where a skill says to ask the human. The coordinator answers from the repo or the brief, or picks the recommended answer and records it as an assumption. The one exception is the interview at the very start of a project or epic, before any loop starts ([1.4](../../docs/principles/1.4.html)).
8. **The end of the cycle is the only exchange with the human.** The coordinator writes `run-summary.md` (what ran, each verdict and findings file, assumptions, open decisions), fills in [data/scorecard.json](../../data/scorecard.json), and asks for feedback.
9. **`/retro` proposes; the human approves.** The coordinator runs `/retro` on the feedback and closes with one report that gives the proposed edits and their results on held-out cases ([9.9](../../docs/principles/9.9.html)). An edit goes live only when the human approves it ([9.10](../../docs/principles/9.10.html)), every accepted or rejected edit is logged ([9.12](../../docs/principles/9.12.html)), and the Harness producer applies the approved edits at the start of the next run.

## The phase model and the Learn loop

Each phase repeats the same producer and reviewer pair. When the human dislikes the final result, the Learn loop turns that into a stricter check for the phase that let the problem through. As a flow:

1. **Phase producer.** Gets the phase's dos and don'ts together, in one pass, and produces the output.
2. **Adversarial reviewer.** Checks the output only against the don'ts and known failure modes. If a check fails, the work goes back to a new producer (step 1). If it passes, the loop moves to the next phase.
3. **Next phase.** The phases repeat this pair, in order, until the final result is ready.
4. **Human acceptance review.** At the end of the full cycle, the human judges the final result. This is not in-development code review. If the human likes it, it is accepted and the cycle ends.
5. **Learn 1: which phase, and how.** If the human dislikes it and explains why, the Learn skills find which phase let the problem through, and how.
6. **Learn 2: which do or don't rules.** They trace it to that phase's do and don't rules.
7. **Learn 3: harden that phase's checklist.** They propose new checks for that phase's adversarial reviewer, and a fix to the producer's rules where a rule was missing or wrong.
8. **Next run is stricter.** Once approved, the same failure is caught at its own phase instead of reaching the human.

If a mistake is mechanical, the fix is a lint, hook or CI check rather than another rule in a prompt ([9.1](../../docs/principles/9.1.html)).

## A worked example: one cycle

An illustration of a cycle on a small command-line app, the kind of project [Testing the skills](testing-the-skills.md) uses. The details are made up; the steps are the ones the loop follows.

1. **Brief.** You tell the coordinator: `/plan Add CSV import to the ledger CLI`. The coordinator sizes the task ([1.8](../../docs/principles/1.8.html)), picks the Plan skills that apply, and writes a brief to a file.
2. **Plan.** The plan producer writes a spec and a plan with a check for each step. The plan reviewer returns `Verdict: FAIL` with a P1 finding: there is no acceptance criterion for malformed rows. A new producer adds one, a new reviewer passes it, and the coordinator records both files.
3. **Design and build.** You run `/design`, then `/build`. Each phase runs its own producer and reviewer loop without asking you anything.
4. **Verify, then Debug.** `/verify` writes and runs the tests. One test fails on a file with a header row, so the Debug loop runs for that failure only: reproduce, find the root cause, fix, keep the test as a guard. Then Verify runs again and passes.
5. **Review and ship.** `/review` runs Secure, then Review & ship. `/ship` takes the reviewed change through the gates.
6. **End of cycle.** The coordinator writes `run-summary.md`, fills in the scorecard and asks for your feedback. You try the app and reply: blank lines in the CSV are skipped without a warning.
7. **Retro.** The coordinator runs `/retro`. The Learn skills ask what conditions allowed it ([9.5](../../docs/principles/9.5.html)), find that the Verify reviewer had no check for silent skips, and propose one small edit to one surface ([9.8](../../docs/principles/9.8.html)), tested on held-out cases. You approve it, it is logged, and the Harness producer applies it at the start of the next run.

## Keeping token cost down

Every token an agent reads costs time and money, and a crowded context makes the agent worse at its job. The biggest warning: the [sources](../../docs/sources.html) include very large catalogues, such as sickn33/agentic-awesome-skills and affaan-m/ECC, each with millions of tokens of skill text. Never load either wholesale. Even installing many of their skills costs you, because every installed skill's description sits in context on every turn.

1. **Keep the always-on file tiny.** An `AGENTS.md` or `CLAUDE.md` is paid for on every turn. Aim for 1,000 to 2,000 tokens with stack, commands, conventions and hard boundaries only ([8.2](../../docs/principles/8.2.html)).
2. **Put everything else in on-demand skills.** Only a skill's name and description are always loaded, about 100 words each; the body loads when the skill is triggered ([8.3](../../docs/principles/8.3.html)). Anthropic's skill-creator suggests keeping a `SKILL.md` under 500 lines.
3. **Use layers.** A few-line stub, a short rule set read when triggered, and the full reference read only when the short rules are not enough.
4. **Write descriptions carefully.** The description decides when a skill fires. A vague one misfires and loads a big body for nothing ([8.4](../../docs/principles/8.4.html)).
5. **Install few skills and subagents.** Descriptions add up: 300 skills at about 100 words each is roughly 40,000 tokens before any work. Pick the ones your stack needs.
6. **Push heavy work to subagents.** Reviews, audits and fact-finding in a fresh context keep the main thread small ([8.7](../../docs/principles/8.7.html)).
7. **Watch shared references.** Some small skills read large shared guides. Check what a skill reads, not just its own size.
8. **Cut output tokens too.** Terse answers and trimmed tool output save tokens; keep code, paths and errors verbatim ([8.9](../../docs/principles/8.9.html)).
