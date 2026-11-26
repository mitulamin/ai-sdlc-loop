---
name: feature-flag-lifecycle
description: "Use when releasing behind a flag. Amalgamated skill for principle 7.11 (Review and ship)."
principles: ["7.11"]
principle: "7.11 Give feature flags a lifecycle that ends in removing them"
category: review-and-ship
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 5
link_only_sources: 0
---

# 7.11 Feature flag lifecycle

Principle 7.11 (Review and ship): Give feature flags a lifecycle that ends in removing them

## When to use

Releasing behind a flag.

## Producer: dos and don'ts

Do:
- Give each flag an owner, purpose and removal date
- Remove the flag and dead branch after rollout

Don't:
- Leave stale flags forever

## Steps

1. Add flag with metadata
2. Roll out
3. Remove
4. Reviewer lists flags past expiry

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a flag with no removal date
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy shipping-and-launch and deprecation-and-migration, wshobson deployment strategies: flags have an owner and an expiry that ends in removal.

## Sources

5 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Review & ship
- Test order: slot 91 of 103
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
