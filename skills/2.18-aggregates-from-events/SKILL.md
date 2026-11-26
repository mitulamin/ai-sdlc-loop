---
name: aggregates-from-events
description: "Use when modelling state changes with business rules (e.g. task assignment, status transitions). Amalgamated skill for principle 2.18 (Design and architecture)."
principles: ["2.18"]
principle: "2.18 Derive aggregates from events and commands"
category: design-and-architecture
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 7
link_only_sources: 0
---

# 2.18 Aggregates from events

Principle 2.18 (Design and architecture / Domain modelling): Derive aggregates from events and commands

## When to use

Modelling state changes with business rules (e.g. task assignment, status transitions).

## Producer: dos and don'ts

Do:
- List domain events and the commands that cause them
- Group by the invariant that must hold together; that is the aggregate
- Change one aggregate per transaction

Don't:
- Design tables first and call them aggregates
- Make huge aggregates that lock everything

## Steps

1. Event-storm briefly
2. Find invariants
3. Draw aggregate boundaries
4. Reviewer tests invariants under concurrency

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find an invariant enforced outside its aggregate
- Find a transaction spanning two aggregates
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

ForceInjection ddd-discover/ddd-aggregates/ddd-domain-interactions and Vernon's IDDD (ciembor): derive aggregates from events and commands, guard invariants inside the aggregate. Amalgam: a quick event list, then aggregates sized to invariants.

## Sources

7 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Design
- Test order: slot 60 of 103
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
