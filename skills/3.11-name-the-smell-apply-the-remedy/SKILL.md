---
name: name-the-smell-apply-the-remedy
description: "Use when reviewing or cleaning code that feels wrong. Amalgamated skill for principle 3.11 (Code craft)."
principles: ["3.11"]
principle: "3.11 Name the code smell and apply its standard remedy"
category: code-craft
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 3.11 Name the smell apply the remedy

Principle 3.11 (Code craft): Name the code smell and apply its standard remedy

## When to use

Reviewing or cleaning code that feels wrong.

## Producer: dos and don'ts

Do:
- Name the smell (long method, feature envy, shotgun surgery...)
- Apply its catalogued remedy
- Cite the smell in the review comment or commit

Don't:
- Rewrite by taste without naming the problem
- Fix smells outside the task scope (log them instead)

## Steps

1. Scan the area
2. Name smells
3. Apply remedies under tests
4. Reviewer checks the smell is gone

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a smell the change introduced
- Find a remedy that is not the catalogued one without reason
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

refactoring-guru and Refactoring (ciembor), Pocock improve-codebase-architecture, sanyuan code-review-expert and brooks-lint brooks-review: identify the named smell and apply its standard remedy, so fixes are consistent and reviewable.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App C (brownfield bug-fix and refactor)
- Phase: Build
- Test order: slot 97
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
