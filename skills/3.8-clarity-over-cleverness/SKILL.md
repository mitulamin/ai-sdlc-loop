---
name: clarity-over-cleverness
description: Use when after a task's tests pass, before review. Amalgamated skill for principle 3.8 (Code craft).
principles: [3.8]
principle: "3.8 Prefer clarity over cleverness"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 3
link_only_sources: 0
---

# 3.8 Clarity over cleverness

Principle 3.8 (Code craft): Prefer clarity over cleverness

## When to use

After a task's tests pass, before review.

## Producer: dos and don'ts

Do:
- Run a simplification pass with tests green
- Prefer explicit names and straightforward control flow
- Keep behaviour identical

Don't:
- Use dense one-liners or clever tricks to save lines
- Simplify without tests protecting behaviour

## Steps

1. Confirm tests green
2. Simplify
3. Re-run tests
4. Reviewer reads it cold

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a line a new engineer would need to puzzle over
- Confirm behaviour unchanged by tests
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy code-simplification and /code-simplify, Anthropic code-simplifier agents: prefer explicit, readable code; simplify after green. Amalgam: a simplification pass with behaviour locked by tests.

## Sources

3 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Test plan

- Test app: App A (CLI tool)
- Phase: Build
- Test order: slot 24 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
