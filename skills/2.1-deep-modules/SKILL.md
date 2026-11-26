---
name: deep-modules
description: "Use when designing a new module or reviewing one that feels shallow (many small pass-through pieces). Amalgamated skill for principle 2.1 (Design and architecture)."
principles: ["2.1"]
principle: "2.1 Design deep modules: a lot of behaviour behind a small interface"
category: design-and-architecture
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 5
link_only_sources: 0
---

# 2.1 Deep modules

Principle 2.1 (Design and architecture): Design deep modules: a lot of behaviour behind a small interface

## When to use

Designing a new module or reviewing one that feels shallow (many small pass-through pieces).

## Producer: dos and don'ts

Do:
- Design the interface first; keep it small and hard to misuse
- Hide decisions likely to change inside the module
- Merge shallow pass-through layers into deeper ones
- Consider enforcing module boundaries with a dependency rule

Don't:
- Split code into many tiny classes that each do almost nothing
- Leak internal data structures through the interface

## Steps

1. Sketch the interface (design it twice, compare)
2. Implement behind it
3. Reviewer scores depth: interface size vs behaviour hidden
4. Deepen or merge where shallow

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a module whose interface is nearly as complex as its implementation
- Find a caller that must know internals
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Pocock codebase-design (with DEEPENING.md), improve-codebase-architecture, setup-ts-deep-modules and ciembor's Philosophy of Software Design rules all push deep modules: much behaviour behind a small interface. Pocock adds a deepening workflow and dependency-cruiser enforcement.

## Sources

5 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App A (CLI tool)
- Phase: Design
- Test order: slot 17 of 103
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
