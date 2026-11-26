---
name: no-skippable-gates
description: Use when when lint, type check, tests or hooks fail. Amalgamated skill for principle 7.9 (Review and ship).
principles: [7.9]
principle: "7.9 No quality gate is skippable: fix the code, don't disable the check"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 4
link_only_sources: 0
---

# 7.9 No skippable gates

Principle 7.9 (Review and ship): No quality gate is skippable: fix the code, don't disable the check

## When to use

When lint, type check, tests or hooks fail.

## Producer: dos and don'ts

Do:
- Fix the cause of the failing check
- Block --no-verify and check-disabling via hooks

Don't:
- Disable, skip or loosen a check to get green

## Steps

1. Read the failure
2. Fix
3. Re-run
4. Reviewer diffs config for loosened checks

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a disabled rule, skip marker or --no-verify
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy ci-cd-and-automation and wshobson block-no-verify (hook): fix the code, don't disable the check.

## Sources

4 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Review & ship
- Test order: slot 89 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
