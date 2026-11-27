---
name: sample-in-the-collector
description: "Use when configuring tracing for anything beyond local dev. Amalgamated skill for principle 5.13 (Debug and observe)."
principles: ["5.13"]
principle: "5.13 Sample in the collector pipeline, not the SDK"
category: debug-and-observe
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 5.13 Sample in the collector

Principle 5.13 (Debug and observe / Observability and logging): Sample in the collector pipeline, not the SDK

## When to use

Configuring tracing for anything beyond local dev.

## Producer: dos and don'ts

Do:
- Export all spans from the SDK
- Configure head/tail sampling in the collector pipeline

Don't:
- Hard-code sampling rates in application code

## Steps

1. Set SDK to always-on
2. Add collector sampling
3. Verify errors are always kept
4. Reviewer checks config location

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Does the SDK export all spans, with sampling configured only in the collector pipeline?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find sampling configured in app code
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

dash0 otel-instrumentation ('defer all sampling to the Collector') and otel-collector, ollygarden otel-collector. Amalgam: SDK exports everything; sampling policy lives centrally.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Debug
- Test order: slot 71
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
