---
name: deliberate-seams
description: "Use when before writing tests or adding an external dependency. Amalgamated skill for principle 2.2 (Design and architecture)."
principles: ["2.2"]
principle: "2.2 Choose seams deliberately; the seam is where tests and adapters attach"
category: design-and-architecture
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 4
link_only_sources: 0
---

# 2.2 Deliberate seams

Principle 2.2 (Design and architecture): Choose seams deliberately; the seam is where tests and adapters attach

## When to use

Before writing tests or adding an external dependency.

## Producer: dos and don'ts

Do:
- Name the seams up front (I/O, clock, network, storage)
- Put an interface at each seam; inject the real thing in production
- Test behaviour at seams, not internal calls

Don't:
- Mock internal collaborators that are not seams
- Add a seam everywhere 'just in case'

## Steps

1. List external effects
2. Define one seam per effect
3. Write tests against seams
4. Reviewer checks no test reaches past a seam

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a test that breaks on a refactor that kept behaviour
- Find an external effect with no seam
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Pocock codebase-design, tdd and improve-codebase-architecture define a seam as the place tests and adapters attach; others (Feathers' legacy code via ciembor) use the same idea for brownfield work. Amalgam: choose seams on purpose at design time and test through them.

## Sources

4 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App A (CLI tool)
- Phase: Design
- Test order: slot 18 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
