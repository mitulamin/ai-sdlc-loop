---
name: enforce-standards-at-review
description: "Use when deciding where a standard lives. Amalgamated skill for principle 9.2 (Learn)."
principles: ["9.2"]
principle: "9.2 Enforce standards at review, not by loading them into the implementer's context"
category: learn
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 2
link_only_sources: 0
---

# 9.2 Enforce standards at review

Principle 9.2 (Learn): Enforce standards at review, not by loading them into the implementer's context

## When to use

Deciding where a standard lives.

## Producer: dos and don'ts

Do:
- Put enforcement checklists in reviewer briefs
- Give producers only the short dos and don'ts

Don't:
- Load full standards into every implementer

## Steps

1. Sort standards
2. Assign to reviewer briefs
3. Measure implementer context

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a long standards doc in an implementer brief
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Pocock retro and agent-os index-standards: keep standards in the reviewer's context, not loaded into every implementer. Matches producers-get-dos-and-donts, reviewers-enforce.

## Sources

2 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: All three runs (harness and Learn)
- Phase: Learn
- Test order: slot 34 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
