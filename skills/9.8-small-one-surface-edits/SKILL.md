---
name: small-one-surface-edits
description: "Use when proposing any learned change. Amalgamated skill for principle 9.8 (Learn)."
principles: ["9.8"]
principle: "9.8 Keep each learned edit small, to one surface, and keep behaviour that already passes"
category: learn
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 9.8 Small one surface edits

Principle 9.8 (Learn): Keep each learned edit small, to one surface, and keep behaviour that already passes

## When to use

Proposing any learned change.

## Producer: dos and don'ts

Do:
- Change one surface (one skill, one rule) per edit
- Keep a record of passing behaviour to preserve

Don't:
- Rewrite whole skills from one failure

## Steps

1. Pick surface
2. Draft small edit
3. Run regression set

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Does each learned edit change one surface, meaning one skill or one rule?
- [ ] Does the behaviour that already passed still pass?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find an edit touching several surfaces
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

muratcan self-improvement-loops (bounded proposals, preserve passing behaviour) and SkillOpt sleep: keep each learned edit small, to one surface.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: All runs (harness and Learn)
- Phase: Learn
- Test order: slot 39
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
