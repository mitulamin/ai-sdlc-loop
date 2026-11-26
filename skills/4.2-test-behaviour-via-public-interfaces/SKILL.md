---
name: test-behaviour-via-public-interfaces
description: "Use when writing or reviewing tests. Amalgamated skill for principle 4.2 (Verify)."
principles: ["4.2"]
principle: "4.2 Test behaviour through public interfaces, not implementation details"
category: verify
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 7
link_only_sources: 0
---

# 4.2 Test behaviour via public interfaces

Principle 4.2 (Verify): Test behaviour through public interfaces, not implementation details

## When to use

Writing or reviewing tests.

## Producer: dos and don'ts

Do:
- Test through the public API or CLI
- Assert on outputs and observable effects
- Let tests survive internal refactors

Don't:
- Assert on private methods or internal call order
- Couple tests to data structures that may change

## Steps

1. Pick the behaviour
2. Call it through the interface
3. Assert outcome
4. Reviewer refactors internals mentally: do tests break?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a test that reaches into internals
- Find a test asserting how rather than what
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Pocock tdd (and tests.md), brooks-lint brooks-test, Addy test-engineer and Anthropic pr-test-analyzer agree: test observable behaviour through public interfaces. Amalgam ties to seams (2.2).

## Sources

7 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App A (CLI tool)
- Phase: Verify
- Test order: slot 27 of 103
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
