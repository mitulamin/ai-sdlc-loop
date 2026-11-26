---
name: tests-as-production-code
description: "Use when writing or maintaining tests. Amalgamated skill for principle 4.8 (Verify)."
principles: ["4.8"]
principle: "4.8 Treat tests as production code: readable and deterministic"
category: verify
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 4
link_only_sources: 0
---

# 4.8 Tests as production code

Principle 4.8 (Verify): Treat tests as production code: readable and deterministic

## When to use

Writing or maintaining tests.

## Producer: dos and don'ts

Do:
- Make tests deterministic: fixed clock, seeds, no real network
- Name tests as behaviour sentences
- Keep arrange-act-assert clear

Don't:
- Use sleeps or real time
- Share mutable state between tests

## Steps

1. Write test
2. Run it 10x
3. Fix nondeterminism
4. Reviewer reads names as a spec

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find sleeps, random or wall-clock use in tests
- Find order-dependent tests
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

ciembor clean-code, brooks-lint brooks-test and Superpowers writing-good-tests: tests readable, deterministic, independent. Amalgam: flaky tests are bugs.

## Sources

4 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App A (CLI tool)
- Phase: Verify
- Test order: slot 29 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
