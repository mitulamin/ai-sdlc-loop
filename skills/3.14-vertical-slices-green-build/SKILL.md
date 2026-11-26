---
name: vertical-slices-green-build
description: Use when implementing any multi-step feature. Amalgamated skill for principle 3.14 (Code craft).
principles: [3.14]
principle: "3.14 One thing at a time, in vertical slices, keeping the build green"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 8
link_only_sources: 0
---

# 3.14 Vertical slices green build

Principle 3.14 (Code craft): One thing at a time, in vertical slices, keeping the build green

## When to use

Implementing any multi-step feature.

## Producer: dos and don'ts

Do:
- Build one end-to-end slice before widening
- Keep the build and tests green after each slice
- Commit per slice

Don't:
- Build all layers horizontally and integrate at the end
- Leave the build red between steps

## Steps

1. Pick the thinnest slice
2. Implement end to end
3. Run all checks; commit
4. Next slice

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a commit where the build was red
- Find layers built with no end-to-end path
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy incremental-implementation and /build, Pocock to-tickets (tracer bullets) agree: one thin vertical slice at a time, build always green. PARTIAL overlap with 5.4 (stop the line) and 7.6 (small changes); kept as the build-time rule.

## Sources

8 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Build
- Test order: slot 63 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
