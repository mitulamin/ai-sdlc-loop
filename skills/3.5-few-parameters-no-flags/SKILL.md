---
name: few-parameters-no-flags
description: "Use when designing function signatures. Amalgamated skill for principle 3.5 (Code craft)."
principles: ["3.5"]
principle: "3.5 Keep parameter lists short: when a signature grows, introduce a named type for the concept or split the function"
category: code-craft
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 2
link_only_sources: 0
---

# 3.5 Few parameters no flags

Principle 3.5 (Code craft): Keep parameter lists short: when a signature grows, introduce a named type for the concept or split the function

## When to use

Designing function signatures.

## Producer: dos and don'ts

Do:
- Keep parameters to about three
- Replace boolean flags with two functions or an enum/options object
- Group related params into a value object

Don't:
- Add a bool param that switches behaviour
- Pass long positional argument lists

## Steps

1. Draft the signature
2. Check for flags and long lists
3. Refactor to concepts
4. Reviewer flags flag arguments

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a boolean param that changes behaviour
- Find a call site where argument order is easy to swap
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

ciembor clean-code and refactoring-guru (long parameter list, flag argument smells); wshobson refactor-clean repeats. Owns the 'no boolean flag parameters' rule (moved from 2.14).

## Sources

2 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App A (CLI tool)
- Phase: Build
- Test order: slot 21 of 103
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
