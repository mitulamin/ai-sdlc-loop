---
name: look-up-facts-ask-for-decisions
description: Use when whenever a question arises during planning or building. Amalgamated skill for principle 1.5 (Plan and specify).
principles: [1.5]
principle: "1.5 Look facts up yourself; only ask the human for decisions"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 4
link_only_sources: 0
---

# 1.5 Look up facts ask for decisions

Principle 1.5 (Plan and specify): Look facts up yourself; only ask the human for decisions

## When to use

Whenever a question arises during planning or building.

## Producer: dos and don'ts

Do:
- Classify each question: fact (look up) or decision (ask)
- Check the repo, README, docs and official sources first and cite them
- Send only decisions upward, batched, with a recommendation

Don't:
- Ask the human what version, API or convention the code already shows
- Answer facts from memory when a primary source is one lookup away

## Steps

1. Write the question down
2. Search repo and official docs
3. Record the answer with its source
4. Escalate only real decisions

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find any question sent to the coordinator that a file or doc answers
- Check citations exist and say what is claimed
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Pocock research and grilling, Superpowers brainstorming ('explore project context first') and Addy source-driven-development agree: facts come from the repo, docs and primary sources; only preferences go to the human. Amalgam adds Addy's 'cite the official doc' habit.

## Sources

4 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Test plan

- Test app: App A (CLI tool)
- Phase: Plan
- Test order: slot 13 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
