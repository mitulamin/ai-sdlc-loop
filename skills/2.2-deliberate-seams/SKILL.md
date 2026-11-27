---
name: deliberate-seams
description: "Use when before writing tests or adding an external dependency. Amalgamated skill for principle 2.2 (Design and architecture)."
principles: ["2.2"]
principle: "2.2 Choose seams deliberately; the seam is where tests and adapters attach"
category: design-and-architecture
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
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

## Related practices

Established practices this skill applies alongside its principle. Each has a self-check item and a reviewer check below.

- **Liskov substitution principle** (SOLID; [guide](../../guides/developer/quality-principles.md#liskov-substitution-principle)): every implementation behind a seam, test fakes included, honours the whole contract: it accepts what the interface accepts, keeps its guarantees and throws no new kind of error. A substitute that needs a type check or a special case at the call site breaks the seam. See also [2.9](../../principles/2.9.md).
- **Interface segregation principle** (SOLID; [guide](../../guides/developer/quality-principles.md#interface-segregation-principle)): shape each seam's interface for the client that uses it. Several small interfaces beat one fat one that ties callers to methods they never call. See also [2.1](../../principles/2.1.md).

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Is each seam named (I/O, clock, network, storage), with an interface that production code injects the real thing into?
- [ ] Does every external effect go through a seam?
- [ ] Do tests attach only at seams, so a refactor that keeps behaviour keeps them green?
- [ ] Liskov substitution principle: does every implementation, adapter and fake at a seam honour the whole contract, with no narrower input, weaker guarantee or unlisted error?
- [ ] Interface segregation principle: does each seam interface hold only the operations its client uses?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a test that breaks on a refactor that kept behaviour
- Find an external effect with no seam
- Liskov substitution principle: find an implementation or fake at a seam that rejects valid input, weakens a guarantee or throws an error the contract does not list
- Interface segregation principle: find a client that depends on interface methods it never calls
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Pocock codebase-design, tdd and improve-codebase-architecture define a seam as the place tests and adapters attach; others (Feathers' legacy code via ciembor) use the same idea for brownfield work. Amalgam: choose seams on purpose at design time and test through them.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App A (CLI tool)
- Phase: Design
- Test order: slot 18
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
