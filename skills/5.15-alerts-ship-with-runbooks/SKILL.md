---
name: alerts-ship-with-runbooks
description: "Use when adding an alert. Amalgamated skill for principle 5.15 (Debug and observe)."
principles: ["5.15"]
principle: "5.15 Every alert ships with a minimal runbook"
category: debug-and-observe
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 6
link_only_sources: 0
---

# 5.15 Alerts ship with runbooks

Principle 5.15 (Debug and observe / Observability and logging): Every alert ships with a minimal runbook

## When to use

Adding an alert.

## Producer: dos and don'ts

Do:
- Write a runbook: meaning, first checks, mitigation, owner
- Link it from the alert

Don't:
- Add alerts nobody knows how to handle

## Steps

1. Define alert
2. Write runbook
3. Link
4. Reviewer does a dry run

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Follow the runbook cold: does it work?
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy observability and wshobson incident-runbook-templates/on-call-handoff-patterns: every alert ships with a minimal runbook.

## Sources

6 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Review & ship
- Test order: slot 81 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
