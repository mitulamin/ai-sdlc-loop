---
name: define-working-before-instrumenting
description: "Use when before adding logs, metrics or traces to a feature. Amalgamated skill for principle 5.7 (Debug and observe)."
principles: ["5.7"]
principle: "5.7 Define what 'working' means before instrumenting"
category: debug-and-observe
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 11
link_only_sources: 0
---

# 5.7 Define working before instrumenting

Principle 5.7 (Debug and observe / Observability and logging): Define what 'working' means before instrumenting

## When to use

Before adding logs, metrics or traces to a feature.

## Producer: dos and don'ts

Do:
- Write 2-4 indicators of 'working' (success rate, latency, freshness)
- Set a target for each
- Instrument to measure exactly those

Don't:
- Instrument everything and hope
- Add dashboards with no target

## Steps

1. Define SLIs
2. Set targets
3. Instrument
4. Reviewer maps each signal to an SLI

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a signal tied to no indicator
- Find an indicator with no signal
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy observability-and-instrumentation and wshobson slo-implementation/slo-implement: decide what 'working' means (SLIs/SLOs) before adding telemetry.

## Sources

11 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Debug
- Test order: slot 66 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
