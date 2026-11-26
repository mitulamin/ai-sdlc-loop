---
name: command-query-separation
description: Use when writing functions that read or mutate state. Amalgamated skill for principle 3.6 (Code craft).
principles: [3.6]
principle: "3.6 Separate commands from queries; no hidden side effects"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 2
link_only_sources: 0
---

# 3.6 Command query separation

Principle 3.6 (Code craft): Separate commands from queries; no hidden side effects

## When to use

Writing functions that read or mutate state.

## Producer: dos and don'ts

Do:
- Name commands as verbs that return nothing (or a status)
- Make queries side-effect free
- Make side effects visible in names

Don't:
- Have a getter that writes, caches globally or logs to external systems silently
- Hide mutation in a function named like a query

## Steps

1. Classify each function
2. Split mixed ones
3. Test queries are pure
4. Reviewer hunts hidden side effects

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a query that mutates
- Find a side effect not implied by the name
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

ciembor clean-code and pragmatic-programmer: a function either changes state or returns data, not both; no hidden side effects. Mostly a reviewer rule.

## Sources

2 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Test plan

- Test app: App A (CLI tool)
- Phase: Build
- Test order: slot 22 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
