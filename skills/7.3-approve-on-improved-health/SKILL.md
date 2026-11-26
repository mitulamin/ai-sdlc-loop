---
name: approve-on-improved-health
description: Use when deciding whether to approve. Amalgamated skill for principle 7.3 (Review and ship).
principles: [7.3]
principle: "7.3 Approve when a change improves code health, not when it is perfect"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 1
link_only_sources: 0
---

# 7.3 Approve on improved health

Principle 7.3 (Review and ship): Approve when a change improves code health, not when it is perfect

## When to use

Deciding whether to approve.

## Producer: dos and don'ts

Do:
- Approve when the change improves overall health and has no blocking findings
- Label nits as non-blocking

Don't:
- Block on preferences or perfection
- Approve changes that make health worse

## Steps

1. Classify findings blocking/non-blocking
2. Decide
3. Record reason

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a block based only on preference
- Find an approval with an open blocker
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy code-review-and-quality (Google's standard: approve when the change improves code health). Balances strictly adversarial reviewers so loops terminate.

## Sources

1 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Review & ship
- Test order: slot 83 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
