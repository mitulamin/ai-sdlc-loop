---
name: abstraction-only-for-benefit
description: "Use whenever an agent proposes a new layer, interface, base class or pattern. Amalgamated skill for principle 2.5 (Design and architecture)."
principles: ["2.5"]
principle: "2.5 At design time, add a layer, interface or abstraction only when you can name the concrete benefit it brings today"
category: design-and-architecture
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 2.5 Abstraction only for benefit

Principle 2.5 (Design and architecture): At design time, add a layer, interface or abstraction only when you can name the concrete benefit it brings today

## When to use

Whenever an agent proposes a new layer, interface, base class or pattern.

## Producer: dos and don'ts

Do:
- Name the concrete benefit now (second implementation, test seam, boundary)
- Prefer duplication twice before abstracting
- Delete abstractions that lost their reason

Don't:
- Add factories, strategies or generic layers for future needs
- Wrap a library in a facade with the same interface

## Steps

1. Proposer states the benefit in one line
2. Skeptic reviewer tries to delete it
3. Keep only if the benefit survives
4. Log the decision

## Related practices

Established practices this skill applies alongside its principle. Each has a self-check item and a reviewer check below.

- **Open-closed principle** (SOLID; [guide](../../guides/developer/quality-principles.md#open-closed-principle)): let new cases arrive as new code rather than as edits scattered through a working core, but only along an axis of change that is visible today, such as a second case in the spec or the code. YAGNI and this principle are the brake: no plugin system or extension point for a single case. See also [3.1](../../principles/3.1.md).
- **Composition over inheritance** ([guide](../../guides/developer/quality-principles.md#composition-over-inheritance)): build behaviour by combining small parts you can swap. Use inheritance only for a true is-a with a shared contract, where the Liskov substitution principle in 2.2 applies, never to reuse a handful of methods. See also [2.2](../../principles/2.2.md).

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Can you name, in one line, the concrete benefit each new layer, interface or abstraction brings today?
- [ ] If you remove each one in your head, does something break today, not only in a possible future?
- [ ] Did you tolerate a second copy and wait for a third before extracting shared code?
- [ ] Open-closed principle: is every extension point you added on an axis of change visible today, a second case in the spec or the code, with none built for a single case?
- [ ] Composition over inheritance: is every subclass you added a true is-a with a shared contract, with reuse otherwise done by composing small parts?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Remove the abstraction mentally: what breaks today?
- Find interfaces with one implementation and no test use
- Open-closed principle: find an extension point with one case and no second case in the spec
- Composition over inheritance: find a subclass that exists only to reuse methods, or that cannot honour its parent's contract
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

ponytail (YAGNI and 'simplest solution'), EGM zoom-out (a sceptical architect persona that favours minimalism and reuse) and Ousterhout's design rules (via ciembor) reject speculative layers. Overlaps 3.1 (minimum code) and 3.12 (no new dependencies) but is about structure, so it is kept separate.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [michaelshimeles/code-structure](https://github.com/michaelshimeles/rstack/blob/8ad39442fd64cf2b407249024c5310dda90f6283/code-structure/SKILL.md) (No licence)
- [multica-ai/CLAUDE.md (Karpathy guidelines)](https://github.com/multica-ai/andrej-karpathy-skills/blob/2c606141936f1eeef17fa3043a72095b4765b9c2/CLAUDE.md) (No LICENSE file (README claims MIT))

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Design
- Test order: slot 48
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
