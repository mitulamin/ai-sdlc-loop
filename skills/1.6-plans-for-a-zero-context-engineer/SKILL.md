---
name: plans-for-a-zero-context-engineer
description: "Use when the coordinator hands a task to a fresh implementer agent. Amalgamated skill for principle 1.6 (Plan and specify)."
principles: ["1.6"]
principle: "1.6 Write plans for an engineer who has never seen the codebase: exact files, small tasks"
category: plan-and-specify
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 1.6 Plans for a zero context engineer

Principle 1.6 (Plan and specify): Write plans for an engineer who has never seen the codebase: exact files, small tasks

## When to use

When the coordinator hands a task to a fresh implementer agent.

## Producer: dos and don'ts

Do:
- Name exact file paths, functions and the test file for each step
- Keep steps 2-5 minutes of work each, with the command that proves it
- Include the relevant spec excerpt, not the whole spec
- State conventions the code must match

Don't:
- Write 'implement the feature' with no file paths
- Assume the implementer knows earlier conversation
- Bundle unrelated changes into one step

## Steps

1. Pick the task from tasks.md
2. Write the step list with paths, tests and commands
3. Readiness reviewer simulates a zero-context engineer and lists blockers
4. Fix blockers, then dispatch

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Try to execute step 1 knowing only the plan: what is missing?
- Find steps with no verification command
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Superpowers writing-plans/executing-plans, spec-kit plan and EGM implementation-readiness agree a plan must be executable by someone who has never seen the code: exact files, small tasks, the test to write, the command to run. This is the core of filling blank-context agents' context in the coordinator model.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App A (CLI tool)
- Phase: Plan
- Test order: slot 14
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
