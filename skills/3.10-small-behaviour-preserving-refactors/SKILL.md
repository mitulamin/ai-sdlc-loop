---
name: small-behaviour-preserving-refactors
description: "Use when restructuring existing code. Amalgamated skill for principle 3.10 (Code craft)."
principles: ["3.10"]
principle: "3.10 Refactor in small behaviour-preserving steps, kept separate from feature changes"
category: code-craft
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 3.10 Small behaviour preserving refactors

Principle 3.10 (Code craft): Refactor in small behaviour-preserving steps, kept separate from feature changes

## When to use

Restructuring existing code.

## Producer: dos and don'ts

Do:
- Refactor in steps of a few minutes, running tests after each
- Keep refactor commits separate from behaviour changes
- Use named refactorings (extract, inline, move)

Don't:
- Mix a refactor and a feature in one commit
- Refactor without tests covering the area

## Steps

1. Ensure coverage of the area
2. Apply one named refactoring
3. Run tests and commit
4. Repeat; reviewer checks no behaviour diff

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a behaviour change hidden in a refactor commit
- Find a step that left tests red
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Fowler's Refactoring and refactoring-guru (ciembor), Addy code-simplification, Pocock improve-codebase-architecture, caveman safe-refactor and wshobson tdd-refactor/refactor-clean agree: small steps, tests green each step, separate from features.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App C (brownfield bug-fix and refactor)
- Phase: Build
- Test order: slot 96
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
