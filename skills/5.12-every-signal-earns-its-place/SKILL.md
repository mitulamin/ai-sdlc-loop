---
name: every-signal-earns-its-place
description: Use when reviewing instrumentation. Amalgamated skill for principle 5.12 (Debug and observe).
principles: [5.12]
principle: "5.12 Every signal should help detect, localise or explain a problem"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 4
link_only_sources: 0
---

# 5.12 Every signal earns its place

Principle 5.12 (Debug and observe / Observability and logging): Every signal should help detect, localise or explain a problem

## When to use

Reviewing instrumentation.

## Producer: dos and don'ts

Do:
- For each signal, name the question it answers
- Remove signals that answer none

Don't:
- Keep noisy logs and unused metrics 'just in case'

## Steps

1. Inventory signals
2. Map to detect/localise/explain
3. Prune
4. Reviewer challenges each signal

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a signal nobody would look at during an incident
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

dash0 otel-instrumentation/semantic-conventions/collector: every signal should help detect, localise or explain a problem. Amalgam: prune telemetry that does none.

## Sources

4 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Debug
- Test order: slot 70 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
