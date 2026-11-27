---
name: tdd-for-skills
description: "Use when before editing any skill based on a failure. Amalgamated skill for principle 9.7 (Learn)."
principles: ["9.7"]
principle: "9.7 Before hardening a skill, reproduce the failure as a baseline scenario and record the agent's excuses; then close the loophole and re-test"
category: learn
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 9.7 Tdd for skills

Principle 9.7 (Learn): Before hardening a skill, reproduce the failure as a baseline scenario and record the agent's excuses; then close the loophole and re-test

## When to use

Before editing any skill based on a failure.

## Producer: dos and don'ts

Do:
- Run a baseline scenario without the fix and record the rationalisations
- Patch the skill to close each excuse
- Re-run until compliant

Don't:
- Edit a skill without seeing it fail first

## Steps

1. Red: scenario fails
2. Green: patch
3. Refactor: close loopholes
4. Re-test

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Was the failure reproduced as a baseline scenario, with the agent's excuses recorded, before the skill was edited?
- [ ] Was the scenario run again after the edit until the agent complied?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Check a baseline failure was recorded before the edit
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Superpowers writing-skills and testing-skills-with-subagents: reproduce the failure as a pressure scenario, record the agent's excuses, then patch and re-test.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: All runs (harness and Learn)
- Phase: Learn
- Test order: slot 38
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
