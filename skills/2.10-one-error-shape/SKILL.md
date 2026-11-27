---
name: one-error-shape
description: "Use when building any HTTP API or CLI error output. Amalgamated skill for principle 2.10 (Design and architecture)."
principles: ["2.10"]
principle: "2.10 Use one consistent error shape across endpoints"
category: design-and-architecture
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 2.10 One error shape

Principle 2.10 (Design and architecture / API design): Use one consistent error shape across endpoints

## When to use

Building any HTTP API or CLI error output.

## Producer: dos and don'ts

Do:
- Define one error shape: code, message, details, correlation id
- Map all exceptions to it in one place
- Document error codes in the contract

Don't:
- Return different error formats per endpoint
- Leak stack traces to clients

## Steps

1. Define the envelope
2. Add a central error mapper
3. Test each endpoint's failure path
4. Reviewer diffs error bodies across endpoints

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Do all endpoints return one error shape, with a code, message, details and correlation id?
- [ ] Are exceptions mapped to that shape in one place, with no stack trace reaching a client?
- [ ] Are the error codes documented in the contract?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find two endpoints with different error shapes
- Find a raw exception reaching the client
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy api-and-interface-design and wshobson api-design-principles/error-handling-patterns call for one consistent error format (e.g. RFC 9457 problem details). Amalgam: one error envelope, mapped centrally.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Design
- Test order: slot 53
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
