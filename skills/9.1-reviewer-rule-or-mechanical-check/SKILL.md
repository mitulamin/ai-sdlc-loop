---
name: reviewer-rule-or-mechanical-check
description: "Use when end-of-run Learn step, after human feedback names a missed mistake. Amalgamated skill for principle 9.1 (Learn)."
principles: ["9.1"]
principle: "9.1 When the reviewer missed a mistake, give the reviewer a new rule; if the mistake is mechanical, build a lint, hook or CI check instead"
category: learn
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 9.1 Reviewer rule or mechanical check

Principle 9.1 (Learn): When the reviewer missed a mistake, give the reviewer a new rule; if the mistake is mechanical, build a lint, hook or CI check instead

## When to use

End-of-run Learn step, after human feedback names a missed mistake.

## Producer: dos and don'ts

Do:
- Classify the miss: judgement or mechanical
- Judgement: add one rule to the phase reviewer
- Mechanical: add a lint, hook or CI check

Don't:
- Add the rule to the implementer's always-on context

## Steps

1. Collect misses
2. Classify
3. Write rule or check
4. Validate on held-out case (9.9)

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Check the new rule would have caught the original miss
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Pocock retro: when the reviewer missed a mistake, add a reviewer rule; if mechanical, build a lint, hook or CI check. claude-reflect and git-guardrails show the hook route.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: All runs (harness and Learn)
- Phase: Learn
- Test order: slot 33
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
