---
name: no-tautological-tests
description: Use when writing assertions. Amalgamated skill for principle 4.3 (Verify).
principles: [4.3]
principle: "4.3 No tautological tests that recompute the expected value the way the code does"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 2
link_only_sources: 0
---

# 4.3 No tautological tests

Principle 4.3 (Verify): No tautological tests that recompute the expected value the way the code does

## When to use

Writing assertions.

## Producer: dos and don'ts

Do:
- Use literal, hand-worked expected values
- Derive expectations from the spec, not the implementation

Don't:
- Call the function under test (or copy its logic) to build the expected value
- Snapshot whatever the code outputs and call it correct

## Steps

1. Work an example by hand
2. Assert the literal
3. Reviewer checks the expected-value source

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find an expected value computed by the same logic
- Find a snapshot never reviewed
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Pocock tdd and tests.md: never compute the expected value the same way the code does. Unique to Pocock; kept as a reviewer check.

## Sources

2 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Test plan

- Test app: App A (CLI tool)
- Phase: Verify
- Test order: slot 28 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
