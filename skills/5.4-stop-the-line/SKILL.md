---
name: stop-the-line
description: "Use whenever a test or build goes red during work. Amalgamated skill for principle 5.4 (Debug and observe)."
principles: ["5.4"]
principle: "5.4 When a test fails or the build breaks, stop and fix it before writing anything new"
category: debug-and-observe
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 2
link_only_sources: 0
---

# 5.4 Stop the line

Principle 5.4 (Debug and observe): When a test fails or the build breaks, stop and fix it before writing anything new

## When to use

Whenever a test or build goes red during work.

## Producer: dos and don'ts

Do:
- Stop feature work and fix the red first
- If not yours, report it to the coordinator with evidence

Don't:
- Keep adding code on a red build
- Mark failing tests skip to proceed

## Steps

1. Notice red
2. Halt
3. Fix or escalate
4. Resume when green

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find commits made on top of a red build
- Find newly skipped tests
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy debugging-and-error-recovery and incremental-implementation: don't build on a failing test or broken build. PARTIAL overlap with 3.14 (keep the build green); kept as the response rule when it goes red.

## Sources

2 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Build
- Test order: slot 64 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
