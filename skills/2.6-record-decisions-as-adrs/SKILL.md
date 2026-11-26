---
name: record-decisions-as-adrs
description: Use when choosing a database, framework, auth approach, API style or anything costly to reverse. Amalgamated skill for principle 2.6 (Design and architecture).
principles: [2.6]
principle: "2.6 Record significant decisions as ADRs"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 7
link_only_sources: 0
---

# 2.6 Record decisions as adrs

Principle 2.6 (Design and architecture): Record significant decisions as ADRs

## When to use

Choosing a database, framework, auth approach, API style or anything costly to reverse.

## Producer: dos and don'ts

Do:
- Write docs/adr/NNNN-title.md: context, decision, alternatives, consequences
- Keep it under a page
- Link the ADR from code or spec where the decision bites
- Supersede rather than edit old ADRs

Don't:
- Write ADRs for trivial choices
- Leave decisions only in chat or commit messages

## Steps

1. Detect a significant decision
2. Draft the ADR
3. Reviewer checks alternatives were real
4. Commit with the change

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a costly decision in the diff with no ADR
- Find an ADR whose alternatives are straw men
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy documentation-and-adrs, wshobson architecture-decision-records and Pocock improve-codebase-architecture/domain-modeling all record significant decisions; Addy adds detecting stale docs. Amalgam: a short ADR per irreversible or costly decision, written by the agent that made it.

## Sources

7 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Design
- Test order: slot 49 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
