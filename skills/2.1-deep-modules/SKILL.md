---
name: deep-modules
description: "Use when designing a new module or reviewing one that feels shallow (many small pass-through pieces). Amalgamated skill for principle 2.1 (Design and architecture)."
principles: ["2.1"]
principle: "2.1 Design deep modules: a lot of behaviour behind a small interface"
category: design-and-architecture
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
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

## Related practices

Established practices this skill applies alongside its principle. Each has a self-check item and a reviewer check below.

- **Single responsibility principle** (SOLID; [guide](../../guides/developer/quality-principles.md#single-responsibility-principle)): give each module one reason to change: one business actor or decision it answers to. It is about isolating change, not about tiny classes, so keep the module deep. See also [3.4](../../principles/3.4.md).
- **Loose coupling and high cohesion** ([guide](../../guides/developer/quality-principles.md#loose-coupling-and-high-cohesion)): put work that changes together in one module, and keep the links between modules few, explicit and stable. A module that must know another's tables, retries or sequencing is coupled however tidy the folders look. See also [2.17](../../principles/2.17.md).

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Is each module's interface much simpler than what it hides, and hard to misuse?
- [ ] Can every caller use each module without knowing its internal data structures or sequencing?
- [ ] Did you merge pass-through layers rather than add tiny classes that do almost nothing?
- [ ] Single responsibility principle: does each module have one reason to change, so that a change for one business reason edits one module?
- [ ] Loose coupling and high cohesion: does work that changes together live together, with each module using only a few explicit, stable interfaces of the others?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a module whose interface is nearly as complex as its implementation
- Find a caller that must know internals
- Single responsibility principle: find a module that changes for two unrelated reasons
- Loose coupling and high cohesion: find a module that must know another module's internals, tables or sequencing to work
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Pocock codebase-design (with DEEPENING.md), improve-codebase-architecture, setup-ts-deep-modules and ciembor's Philosophy of Software Design rules all push deep modules: much behaviour behind a small interface. Pocock adds a deepening workflow and dependency-cruiser enforcement.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App A (CLI tool)
- Phase: Design
- Test order: slot 17
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
