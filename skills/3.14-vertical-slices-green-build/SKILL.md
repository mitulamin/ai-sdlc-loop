---
name: vertical-slices-green-build
description: "Use when implementing any multi-step feature. Amalgamated skill for principle 3.14 (Code craft)."
principles: ["3.14"]
principle: "3.14 Build in thin vertical slices, one at a time, each leaving the build green"
category: code-craft
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 3.14 Vertical slices green build

Principle 3.14 (Code craft): Build in thin vertical slices, one at a time, each leaving the build green

## When to use

Implementing any multi-step feature.

## Producer: dos and don'ts

Do:
- Build one end-to-end slice before widening
- Keep the build and tests green after each slice
- Commit per slice

Don't:
- Build all layers horizontally and integrate at the end
- Leave the build red between steps

## Steps

1. Pick the thinnest slice
2. Implement end to end
3. Run all checks; commit
4. Next slice

## Related practices

Established practices this skill applies alongside its principle. Each has a self-check item and a reviewer check below.

- **Gall's law** ([guide](../../guides/developer/developer-guide.md#galls-law)): a complex system that works grows from a simple system that worked. Make the first slice the simplest system that works end to end, then grow it slice by slice, rather than designing the whole and integrating at the end. See also [1.3](../../principles/1.3.md).

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Did you build one end-to-end slice before widening, with a commit per slice?
- [ ] Were the build and the tests green after every slice?
- [ ] Gall's law: was the first slice the simplest system that works end to end, with complexity added only by growing a working system?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a commit where the build was red
- Find layers built with no end-to-end path
- Gall's law: find a first slice that did not work end to end, or complexity built before the simple version worked
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy incremental-implementation and /build, Pocock to-tickets (tracer bullets) agree: one thin vertical slice at a time, build always green. PARTIAL overlap with 5.4 (stop the line) and 7.6 (small changes); kept as the build-time rule.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Build
- Test order: slot 63
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
