---
name: match-existing-conventions
description: "Use when working in any existing codebase. Amalgamated skill for principle 3.3 (Code craft)."
principles: ["3.3"]
principle: "3.3 Match the existing style and conventions"
category: code-craft
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 2
link_only_sources: 1
---

# 3.3 Match existing conventions

Principle 3.3 (Code craft): Match the existing style and conventions

## When to use

Working in any existing codebase.

## Producer: dos and don'ts

Do:
- Read 2-3 neighbouring files before writing
- Copy naming, error handling, test layout and import style
- Record discovered conventions in the brief for later agents

Don't:
- Introduce a new style, pattern or library the codebase does not use
- Apply your preferred formatter over the project's

## Steps

1. Sample neighbouring code
2. List conventions
3. Write in that style
4. Reviewer diffs style against neighbours

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find code that looks foreign next to its neighbours
- Find a new dependency or pattern with an existing equivalent
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy code-simplification ('follow project conventions') and agent-os discover-standards (extract tribal knowledge from the codebase into a short standards file) agree. Amalgam: discover the conventions first, then inject them into the worker's brief.

## Sources

2 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [multica-ai/CLAUDE.md (Karpathy guidelines)](https://github.com/multica-ai/andrej-karpathy-skills/blob/2c606141936f1eeef17fa3043a72095b4765b9c2/CLAUDE.md) (No LICENSE file (README claims MIT))

## Test plan

- Test app: App C (brownfield bug-fix and refactor)
- Phase: Build
- Test order: slot 94 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
