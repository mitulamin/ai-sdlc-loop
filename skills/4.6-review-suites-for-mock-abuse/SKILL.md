---
name: review-suites-for-mock-abuse
description: Use when reviewing a test suite or a PR's tests. Amalgamated skill for principle 4.6 (Verify).
principles: [4.6]
principle: "4.6 Review suites for mock abuse, brittleness and coverage illusions; coverage is not quality"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 5
link_only_sources: 0
---

# 4.6 Review suites for mock abuse

Principle 4.6 (Verify): Review suites for mock abuse, brittleness and coverage illusions; coverage is not quality

## When to use

Reviewing a test suite or a PR's tests.

## Producer: dos and don'ts

Do:
- Mock only at seams (system boundaries)
- Check tests would fail if the behaviour broke (mutation thinking)
- Treat coverage as a hint, not proof

Don't:
- Mock the unit under test's collaborators everywhere
- Accept high coverage as quality

## Steps

1. Scan tests for mocks
2. Mentally break the code: which tests fail?
3. List brittle/illusory tests
4. Fix or delete

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a test that passes with the implementation deleted
- Find mocks of internal modules
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

brooks-lint brooks-test (both copies), Pocock tdd/mocking.md, Addy TDD and Anthropic pr-test-analyzer: review suites for over-mocking, brittleness and coverage illusions. Amalgam: an adversarial test-suite reviewer.

## Sources

5 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Test plan

- Test app: App C (brownfield bug-fix and refactor)
- Phase: Verify
- Test order: slot 98 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
