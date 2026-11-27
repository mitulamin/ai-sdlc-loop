---
name: small-functions-one-level
description: "Use when writing or reviewing functions. Amalgamated skill for principle 3.4 (Code craft)."
principles: ["3.4"]
principle: "3.4 Keep functions small and at one level of abstraction"
category: code-craft
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 3.4 Small functions one level

Principle 3.4 (Code craft): Keep functions small and at one level of abstraction

## When to use

Writing or reviewing functions.

## Producer: dos and don'ts

Do:
- Keep each function to one job at one level of abstraction
- Extract steps into well-named helpers when a function mixes levels
- Aim for functions that fit on one screen

Don't:
- Split into trivial one-line functions that hurt readability
- Mix I/O, parsing and business rules in one function

## Steps

1. Write the function
2. Read it top-down: is each line the same level?
3. Extract mixed levels
4. Reviewer flags mixed-level functions

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Does each function do one job at one level of abstraction, with I/O, parsing and business rules kept apart?
- [ ] Does each function fit on one screen, without being split into trivial one-line helpers?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a function doing I/O and rules together
- Find a function longer than one screen without reason
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

ciembor clean-code and code-complete: small functions at one level of abstraction. Few agent skill files implement it directly; it is mainly a reviewer rule.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App A (CLI tool)
- Phase: Build
- Test order: slot 20
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
