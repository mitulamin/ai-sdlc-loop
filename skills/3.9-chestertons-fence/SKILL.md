---
name: chestertons-fence
description: "Use when before deleting or rewriting code you did not write. Amalgamated skill for principle 3.9 (Code craft)."
principles: ["3.9"]
principle: "3.9 Understand why code exists before removing it (Chesterton's fence)"
category: code-craft
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 3.9 Chestertons fence

Principle 3.9 (Code craft): Understand why code exists before removing it (Chesterton's fence)

## When to use

Before deleting or rewriting code you did not write.

## Producer: dos and don'ts

Do:
- Check git blame, linked issues and tests for the code's reason
- Write a characterization test before changing legacy behaviour
- Record the reason in the commit when you remove it

Don't:
- Delete 'dead-looking' code without checking callers and history
- Rewrite legacy code wholesale

## Steps

1. Find the code's history
2. Search callers
3. Add characterization tests
4. Remove or change with evidence

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Ask: what did this code protect against?
- Find a deletion with no history check
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy code-simplification (Chesterton's fence), Feathers' Working Effectively with Legacy Code (ciembor) and Trail of Bits audit-prep agree: know why code exists before removing it.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App C (brownfield bug-fix and refactor)
- Phase: Build
- Test order: slot 95
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
