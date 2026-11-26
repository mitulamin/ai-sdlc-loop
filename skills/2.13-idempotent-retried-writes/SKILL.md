---
name: idempotent-retried-writes
description: "Use when any create/charge/send operation a client or job may retry. Amalgamated skill for principle 2.13 (Design and architecture)."
principles: ["2.13"]
principle: "2.13 Make retried writes safe with idempotency keys derived from intent"
category: design-and-architecture
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 5
link_only_sources: 0
---

# 2.13 Idempotent retried writes

Principle 2.13 (Design and architecture / API design): Make retried writes safe with idempotency keys derived from intent

## When to use

Any create/charge/send operation a client or job may retry.

## Producer: dos and don'ts

Do:
- Require an idempotency key on retryable writes
- Derive it from intent (user+action+payload), not a random per-attempt id
- Store key and result; return the stored result on repeat

Don't:
- Rely on 'clients won't retry'
- Generate a new key per retry

## Steps

1. Identify retryable writes
2. Add key handling and storage
3. Test double-submit
4. Reviewer replays requests

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Submit the same request twice: are there two records?
- Find a write path reachable by retry without a key
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy api-and-interface-design and wshobson api-design-principles/background-jobs: make retried writes safe with idempotency keys derived from intent. Amalgam pairs with 2.7 (retries).

## Sources

5 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Design
- Test order: slot 55 of 103
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
