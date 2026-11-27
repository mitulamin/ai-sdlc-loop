---
name: approve-on-improved-health
description: "Use when deciding whether to approve. Amalgamated skill for principle 7.3 (Review and ship)."
principles: ["7.3"]
principle: "7.3 Approve when a change improves code health, not when it is perfect"
category: review-and-ship
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
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

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Does the verdict rest on whether the change improves code health, with no block based only on preference?
- [ ] Are nits labelled non-blocking, and is nothing approved with an open blocker?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a block based only on preference
- Find an approval with an open blocker
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy code-review-and-quality (Google's standard: approve when the change improves code health). Balances strictly adversarial reviewers so loops terminate.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Review & ship
- Test order: slot 83
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
