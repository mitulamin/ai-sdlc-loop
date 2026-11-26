---
name: group-failures-by-mechanism
description: "Use when learn step with several failures. Amalgamated skill for principle 9.6 (Learn)."
principles: ["9.6"]
principle: "9.6 Group failures by the mechanism behind them, not by error text"
category: learn
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 1
link_only_sources: 0
---

# 9.6 Group failures by mechanism

Principle 9.6 (Learn): Group failures by the mechanism behind them, not by error text

## When to use

Learn step with several failures.

## Producer: dos and don'ts

Do:
- Cluster failures by cause mechanism
- Fix one mechanism per edit

Don't:
- Group by error message

## Steps

1. List failures
2. Cluster by mechanism
3. Rank
4. Fix top cluster

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find two clusters with the same mechanism
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

muratcan self-improvement-loops: group failures by the mechanism behind them, not by error text.

## Sources

1 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: All three runs (harness and Learn)
- Phase: Learn
- Test order: slot 37 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
