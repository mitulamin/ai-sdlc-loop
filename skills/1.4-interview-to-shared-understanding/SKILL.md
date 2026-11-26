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
- Map open decisions as a tree; ask the top-level branches first
- Give a recommended answer and the reason with every question
- Batch a round of 3-7 questions; stop when answers stop changing the plan
- Write the outcome into the spec

Don't:
- Interview inside worker loops (workers get filled context instead)
- Ask questions whose answer is in the repo or docs
- Treat 'okay let's start' as agreement without checking open branches

## Steps

1. Coordinator lists decisions as a tree
2. Ask round 1 with recommendations
3. Fold answers in; ask the next round only if branches remain
4. Freeze into spec.md

## Adversarial reviewer (fresh context, tries to prove the work fails)

- List any decision the build made that the interview never covered
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
