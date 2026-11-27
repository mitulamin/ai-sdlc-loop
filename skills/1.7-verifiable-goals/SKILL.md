---
name: verifiable-goals
description: "Use when writing any task, step or brief. Amalgamated skill for principle 1.7 (Plan and specify)."
principles: ["1.7"]
principle: "1.7 Turn every task into a verifiable goal, with a check for each step"
category: plan-and-specify
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 1.7 Verifiable goals

Principle 1.7 (Plan and specify): Turn every task into a verifiable goal, with a check for each step

## When to use

Writing any task, step or brief.

## Producer: dos and don'ts

Do:
- Rewrite vague asks as 'done when <command/test> passes'
- Write the goal's criteria as numbered Given/When/Then lines, and make each check name the criterion number it proves
- Prefer automated checks; describe manual checks precisely when unavoidable
- Loop until the check passes, independently

Don't:
- Accept 'make it better' without a measurable target
- Declare done because the code looks right

## Steps

1. For each task write the success check
2. Run it to confirm it fails now
3. Build until it passes
4. Record the evidence

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a goal whose check could pass while the goal is unmet
- Find tasks with no check
- Find a check that names no criterion, a criterion no check names, or a criterion that is not numbered Given/When/Then
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy planning-and-task-breakdown (small tasks with explicit acceptance criteria), Addy spec-driven-development (testable success criteria) and spec-kit checklist and analyze agree: attach a runnable check to every task before work begins. Amalgam: every task and step carries a pass/fail check.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [multica-ai/CLAUDE.md (Karpathy guidelines)](https://github.com/multica-ai/andrej-karpathy-skills/blob/2c606141936f1eeef17fa3043a72095b4765b9c2/CLAUDE.md) (No LICENSE file (README claims MIT))

## Test plan

- Test app: App A (CLI tool)
- Phase: Plan
- Test order: slot 15
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
