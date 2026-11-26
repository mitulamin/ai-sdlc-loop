---
name: surface-assumptions
description: "Use when starting any task where the brief leaves a choice open (scope, data shape, library, behaviour). Amalgamated skill for principle 1.1 (Plan and specify)."
principles: ["1.1"]
principle: "1.1 State assumptions; when something is unclear, stop and ask rather than pick silently"
category: plan-and-specify
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 7
link_only_sources: 2
---

# 1.1 Surface assumptions

Principle 1.1 (Plan and specify): State assumptions; when something is unclear, stop and ask rather than pick silently

## When to use

Starting any task where the brief leaves a choice open (scope, data shape, library, behaviour).

## Producer: dos and don'ts

Do:
- Write an ASSUMPTIONS block (numbered, one line each) before the first edit
- Mark each assumption as safe-default or needs-decision
- Send needs-decision items to the coordinator in one batch, each with your recommended answer
- Proceed on safe defaults and record them in the run log

Don't:
- Silently pick an interpretation and bury it in code
- Ask the human mid-loop for things you can look up (see 1.5)
- Ask one question at a time across many turns

## Steps

1. Read the brief and list every open choice
2. Classify: safe default vs decision
3. Batch decisions to the coordinator with recommendations
4. Record the answers in the spec/run log, then build

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a behaviour in the output that rests on an unstated assumption
- Check every needs-decision item got an answer before code that depends on it
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy spec-driven-development (a numbered 'assumptions I'm making' list the human corrects), Addy interview-me, Superpowers brainstorming (proposes approaches with trade-offs), spec-kit clarify (bounded clarification questions) and EGM brainstorm all stop to surface open points before work starts. Amalgam: one numbered assumptions list split into safe defaults and real decisions, with the decisions batched to the coordinator so loops stay independent.

## Sources

7 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [multica-ai/CLAUDE.md (Karpathy guidelines)](https://github.com/multica-ai/andrej-karpathy-skills/blob/2c606141936f1eeef17fa3043a72095b4765b9c2/CLAUDE.md) (No LICENSE file (README claims MIT))
- [anthropics/doc-coauthoring](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/doc-coauthoring/SKILL.md) (No licence file in folder)

## Test plan

- Test app: App A (CLI tool)
- Phase: Plan
- Test order: slot 11 of 103
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
