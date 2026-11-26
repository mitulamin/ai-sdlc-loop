---
name: failure-modes-in-the-contract
description: "Use when writing or reviewing an API contract. Amalgamated skill for principle 2.15 (Design and architecture)."
principles: ["2.15"]
principle: "2.15 State failure modes, retryability, timeouts and versioning in the contract"
category: design-and-architecture
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 2.15 Failure modes in the contract

Principle 2.15 (Design and architecture / API design): State failure modes, retryability, timeouts and versioning in the contract

## When to use

Writing or reviewing an API contract.

## Producer: dos and don'ts

Do:
- For each operation list errors, whether it is retryable, expected latency/timeout
- State the versioning policy
- Keep the doc next to the contract

Don't:
- Leave callers to discover failure behaviour in production
- Version ad hoc

## Steps

1. Add failure/retry/timeout fields per operation
2. Add versioning section
3. Contract test failure cases
4. Reviewer plays an unhappy client

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find an error the code returns that the contract omits
- Find an operation with no retry guidance
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

ciembor release-it and Addy api design: state failure modes, retryability, timeouts and versioning in the contract. Overlaps 2.7 (design for failure) and 2.9 (contract first) but is about documenting them for callers.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Design
- Test order: slot 57
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
