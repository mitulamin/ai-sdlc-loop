---
name: design-for-failure
description: "Use when any call over a network, to a DB, queue or third-party API. Amalgamated skill for principle 2.7 (Design and architecture)."
principles: ["2.7"]
principle: "2.7 Design for failure: explicit timeouts, bounded retries with backoff, circuit breakers, bulkheads"
category: design-and-architecture
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 4
link_only_sources: 0
---

# 2.7 Design for failure

Principle 2.7 (Design and architecture): Design for failure: explicit timeouts, bounded retries with backoff, circuit breakers, bulkheads

## When to use

Any call over a network, to a DB, queue or third-party API.

## Producer: dos and don'ts

Do:
- Set an explicit timeout on every outbound call
- Retry only idempotent operations, with capped exponential backoff and jitter
- Add a circuit breaker where a dependency can hang
- Isolate resources so one slow dependency cannot exhaust all

Don't:
- Rely on library default timeouts (often infinite)
- Retry non-idempotent writes blindly

## Steps

1. List outbound calls
2. Assign timeout, retry and breaker policy
3. Implement and test failure paths with fakes
4. Reviewer injects a hanging dependency

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a call with no timeout
- Find a retry loop with no cap or on a non-idempotent write
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

ciembor release-it (Nygard) is the main source: timeouts, bounded retries with backoff, circuit breakers, bulkheads; wshobson error-handling-patterns and backend-architect agents repeat parts. Amalgam: every outbound call gets a timeout and a retry policy, decided at design time.

## Sources

4 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Design
- Test order: slot 50 of 103
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
