---
name: ledger-of-edits
description: "Use when every Learn decision. Amalgamated skill for principle 9.12 (Learn)."
principles: ["9.12"]
principle: "9.12 Keep a record of every accepted and rejected edit"
category: learn
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 9.12 Ledger of edits

Principle 9.12 (Learn): Keep a record of every accepted and rejected edit

## When to use

Every Learn decision.

## Producer: dos and don'ts

Do:
- Log date, change, evidence, decision and reason in a ledger file
- Include rejected edits

Don't:
- Keep only the accepted changes with no history

## Steps

1. Write entry
2. Commit ledger

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Does the ledger record the date, change, evidence, decision and reason for every edit, rejected ones included?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a decision missing from the ledger
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

muratcan self-improvement-loops, SkillOpt (adoption records) and Trail of Bits skill-improver: keep a record of every accepted and rejected edit.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: All runs (harness and Learn)
- Phase: Learn
- Test order: slot 43
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
