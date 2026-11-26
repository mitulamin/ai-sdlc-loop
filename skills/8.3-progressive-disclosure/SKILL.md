---
name: progressive-disclosure
description: Use when writing any skill. Amalgamated skill for principle 8.3 (Agent operations).
principles: [8.3]
principle: "8.3 Progressive disclosure: short description always, body on trigger, references on demand"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 6
link_only_sources: 0
---

# 8.3 Progressive disclosure

Principle 8.3 (Agent operations): Progressive disclosure: short description always, body on trigger, references on demand

## When to use

Writing any skill.

## Producer: dos and don'ts

Do:
- Keep SKILL.md body short; move detail to reference files
- Link references from the body with when-to-read notes

Don't:
- Put everything in one huge SKILL.md

## Steps

1. Draft body
2. Split references
3. Check token size

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Measure body tokens; find reference-worthy detail inline
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Anthropic skill-creator and plugin-dev skill-development, Stratos core and muratcan context-fundamentals: short description always loaded, body on trigger, references on demand. PARTIAL overlap with 8.1.

## Sources

6 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Test plan

- Test app: All three runs (harness and Learn)
- Phase: Harness
- Test order: slot 3 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
