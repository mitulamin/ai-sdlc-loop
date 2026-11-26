---
name: description-is-the-trigger
description: Use when writing or reviewing a skill's frontmatter. Amalgamated skill for principle 8.4 (Agent operations).
principles: [8.4]
principle: "8.4 The skill description is the trigger; put the 'when to use' there"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 11
link_only_sources: 0
---

# 8.4 Description is the trigger

Principle 8.4 (Agent operations): The skill description is the trigger; put the 'when to use' there

## When to use

Writing or reviewing a skill's frontmatter.

## Producer: dos and don'ts

Do:
- Write the description as 'Use when ...' with concrete triggers
- Test triggering with sample prompts

Don't:
- Describe what the skill is instead of when to use it

## Steps

1. Write description
2. Run trigger tests
3. Adjust

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Give 5 prompts that should and 5 that shouldn't trigger: check results
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Anthropic skill-creator, plugin-dev skill-development and skill-reviewer: the description decides when a skill fires, so 'when to use' goes there.

## Sources

11 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Test plan

- Test app: All three runs (harness and Learn)
- Phase: Harness
- Test order: slot 4 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
