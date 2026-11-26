---
name: three-failed-fixes-question-architecture
description: Use when when a third fix attempt for the same problem fails. Amalgamated skill for principle 5.5 (Debug and observe).
principles: [5.5]
principle: "5.5 After three failed fixes, question the architecture"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 1
link_only_sources: 0
---

# 5.5 Three failed fixes question architecture

Principle 5.5 (Debug and observe): After three failed fixes, question the architecture

## When to use

When a third fix attempt for the same problem fails.

## Producer: dos and don'ts

Do:
- Stop patching after three failed attempts
- Write what each attempt assumed and why it failed
- Escalate with a design question to the coordinator

Don't:
- Try a fourth and fifth variation of the same idea

## Steps

1. Count attempts
2. At three, write the failure summary
3. Escalate
4. Resume with the decision

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Count fix attempts in the transcript
- Check the escalation names the design assumption
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Superpowers systematic-debugging only: after three failed fixes, stop and question the design. Amalgam: an escalation trigger to the coordinator.

## Sources

1 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Test plan

- Test app: App C (brownfield bug-fix and refactor)
- Phase: Debug
- Test order: slot 102 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
