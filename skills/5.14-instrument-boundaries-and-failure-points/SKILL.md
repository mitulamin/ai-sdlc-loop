---
name: instrument-boundaries-and-failure-points
description: "Use when adding observability to outbound calls and entry points. Amalgamated skill for principle 5.14 (Debug and observe)."
principles: ["5.14"]
principle: "5.14 Instrument boundaries and failure points: latency, errors, saturation, retries, breaker state"
category: debug-and-observe
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 5.14 Instrument boundaries and failure points

Principle 5.14 (Debug and observe / Observability and logging): Instrument boundaries and failure points: latency, errors, saturation, retries, breaker state

## When to use

Adding observability to outbound calls and entry points.

## Producer: dos and don'ts

Do:
- Measure latency and errors at every boundary
- Expose retries, breaker state and pool saturation

Don't:
- Instrument only the happy path inside functions

## Steps

1. List boundaries
2. Add metrics/spans
3. Simulate failure and check signals
4. Reviewer verifies failure is visible

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Are latency and errors measured at every boundary?
- [ ] Are retries, breaker state and pool saturation exposed, so that an injected failure shows up in a signal?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Inject a failure: does any signal show it?
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

ciembor release-it, Addy observability and dash0 otel-instrumentation: instrument latency, errors, saturation, retries and breaker state at boundaries.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Debug
- Test order: slot 72
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
