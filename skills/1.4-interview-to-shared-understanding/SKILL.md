---
name: interview-to-shared-understanding
description: "Use when only at the very start of a project or epic, run by the top coordinator with the human. Amalgamated skill for principle 1.4 (Plan and specify)."
principles: ["1.4"]
principle: "1.4 Interview until there is shared understanding; ask each round of open decisions with a recommended answer"
category: plan-and-specify
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 1.4 Interview to shared understanding

Principle 1.4 (Plan and specify): Interview until there is shared understanding; ask each round of open decisions with a recommended answer

## When to use

Only at the very start of a project or epic, run by the top coordinator with the human.

## Producer: dos and don'ts

Do:
- Ground yourself first: read the repo, docs, brief and register, and open the interview with what you already know
- Infer the decision areas from this goal rather than a stock list of topics; a decision belongs in the tree only if this goal makes it matter
- Map open decisions as a tree; ask the top-level branches first
- Go one layer at a time, ordered by coupling: settle the decisions that others depend on before the ones they unlock
- Ask every question in one format: the question, the options, the recommended option first with the reason, and what changes if another option is picked
- Give a recommended answer and the reason with every question
- Batch a round of 3-7 questions; stop when answers stop changing the plan
- Write the outcome into the spec as a decision sheet: for each decision the choice, who decided it, why, and its register id (log each answer in the register so it has one)
- Park what can wait with a reason and a revisit trigger, the event that should bring it back
- Treat every answer as a locked decision from then on, and tell downstream agents which decisions are locked

Don't:
- Interview inside worker loops (workers get filled context instead)
- Ask questions whose answer is in the repo or docs
- Treat 'okay let's start' as agreement without checking open branches
- Anchor on the first option that comes to mind; weigh real alternatives before choosing what to recommend
- Apply a preference or default silently; declare it as [ASSUMPTION: ...]
- Reopen a locked decision without new evidence, or override it silently; raise [QUESTION: ...] or [BLOCKER: ...] with the evidence

## Steps

1. Coordinator reads the existing context, then lists decisions as a tree inferred from this goal
2. Order the layers by coupling and ask the first layer with recommendations
3. Fold answers in as locked decisions; ask the next layer only if branches remain
4. Freeze into spec.md with the decision sheet and the parked items

## Adversarial reviewer (fresh context, tries to prove the work fails)

- List any decision the build made that the interview never covered
- Exit test: every item is either decided, or parked with a reason and a revisit trigger; fail it if any open choice affects behaviour, an interface, authorisation, the source of truth or rollout
- Decision sheet: every decision shows the choice, who decided it, why, and its register id; every parked item shows a revisit trigger
- Find a question whose options were not led by a recommended one, or whose topic came from a stock list rather than this goal
- Find a preference or default that was applied without an [ASSUMPTION: ...] declaration
- Flag questions that a lookup could have answered
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Pocock grilling/grill-me/grill-with-docs, Superpowers brainstorming, Addy interview-me and idea-refine, and EGM brainstorm all interview the requester; Pocock maps a design tree and Addy detects false convergence. Amalgam for the coordinator model: the coordinator (not the worker) runs the interview once up front, asking each round with recommended answers.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [anthropics/doc-coauthoring](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/doc-coauthoring/SKILL.md) (No licence file in folder)

## Test plan

- Test app: App A (CLI tool)
- Phase: Plan
- Test order: slot 12
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
