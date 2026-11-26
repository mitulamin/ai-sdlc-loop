---
name: prune-rules-that-dont-change-behaviour
description: "Use when periodically, and when a rules file grows. Amalgamated skill for principle 9.3 (Learn)."
principles: ["9.3"]
principle: "9.3 Remove or clarify rules that don't change behaviour"
category: learn
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 1
link_only_sources: 0
---

# 9.3 Prune rules that dont change behaviour

Principle 9.3 (Learn): Remove or clarify rules that don't change behaviour

## When to use

Periodically, and when a rules file grows.

## Producer: dos and don'ts

Do:
- For each rule ask: what behaviour would change without it?
- Remove or rewrite rules with no effect

Don't:
- Keep adding rules forever

## Steps

1. List rules
2. Test removal on held-out tasks
3. Remove
4. Log

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a rule no transcript ever shows applied
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Pocock retro: remove or clarify rules that do not change behaviour. Few other files do this explicitly.

## Sources

1 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: All three runs (harness and Learn)
- Phase: Learn
- Test order: slot 35 of 103
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
