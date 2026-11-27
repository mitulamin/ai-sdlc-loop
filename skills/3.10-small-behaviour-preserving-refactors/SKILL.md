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

## Related practices

Established practices this skill applies alongside its principle. Each has a self-check item and a reviewer check below.

- **Boy Scout rule** ([guide](../../guides/developer/quality-principles.md#the-boy-scout-rule)): leave the code you had to touch a little cleaner, such as a clearer name or a split function, but only in the lines the task already changes, and as its own refactor commit. 3.2's surgical scope wins: log anything wider instead of fixing it. See also [3.2](../../principles/3.2.md).

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Is each refactoring a named, behaviour-preserving step, with the tests run after it?
- [ ] Are refactor commits separate from behaviour changes, with tests covering the area before you start?
- [ ] Boy Scout rule: is every tidy-up limited to lines the task already changes, and in its own refactor commit?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a behaviour change hidden in a refactor commit
- Find a step that left tests red
- Boy Scout rule: find a tidy-up outside the lines the task changed, or one mixed into a behaviour commit
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
