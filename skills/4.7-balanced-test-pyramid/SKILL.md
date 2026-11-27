---
name: balanced-test-pyramid
description: "Use when planning tests for an app. Amalgamated skill for principle 4.7 (Verify)."
principles: ["4.7"]
principle: "4.7 Balance the test pyramid by size and cost"
category: verify
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 4.7 Balanced test pyramid

Principle 4.7 (Verify): Balance the test pyramid by size and cost

## When to use

Planning tests for an app.

## Producer: dos and don'ts

Do:
- Default to fast unit tests
- Add integration tests at real boundaries (DB, HTTP)
- Keep a handful of end-to-end tests for critical journeys

Don't:
- Rely mainly on slow, flaky end-to-end tests
- Skip integration tests at the DB boundary

## Steps

1. List behaviours
2. Assign each the cheapest test that proves it
3. Check suite time
4. Reviewer audits the mix

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Is most behaviour covered by fast unit tests, with integration tests at real boundaries such as the database and HTTP?
- [ ] Are end-to-end tests kept to the critical journeys, with no behaviour covered only end to end?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a behaviour only covered by e2e
- Find a boundary with no integration test
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy test-driven-development and test-engineer, wshobson test-automator/tdd-orchestrator: many fast small tests, fewer integration, few end-to-end. Amalgam: size tests by cost.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Verify
- Test order: slot 65
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
