---
name: blameless-five-whys
description: Use when end-of-run retro on any failure. Amalgamated skill for principle 9.5 (Learn).
principles: [9.5]
principle: "9.5 Ask what conditions allowed the failure, not who caused it (blameless, 5 whys)"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 3
link_only_sources: 0
---

# 9.5 Blameless five whys

Principle 9.5 (Learn): Ask what conditions allowed the failure, not who caused it (blameless, 5 whys)

## When to use

End-of-run retro on any failure.

## Producer: dos and don'ts

Do:
- Ask why five times toward conditions, not agents
- End with a system change

Don't:
- Conclude 'the agent made a mistake'

## Steps

1. State failure
2. 5 whys
3. Pick condition to change
4. Assign fix

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Check the conclusion names a changeable condition
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

wshobson postmortem-writing and steipete five: ask what conditions allowed the failure (blameless, 5 whys).

## Sources

3 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Test plan

- Test app: All three runs (harness and Learn)
- Phase: Learn
- Test order: slot 36 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
