---
name: bound-everything
description: "Use when adding a list endpoint, cache, queue, worker pool or batch job. Amalgamated skill for principle 2.8 (Design and architecture)."
principles: ["2.8"]
principle: "2.8 Bound every queue, cache, pool and result set, and decide what happens when full"
category: design-and-architecture
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 2.8 Bound everything

Principle 2.8 (Design and architecture): Bound every queue, cache, pool and result set, and decide what happens when full

## When to use

Adding a list endpoint, cache, queue, worker pool or batch job.

## Producer: dos and don'ts

Do:
- Give every collection a max size and every query a limit/pagination
- Decide overflow: reject, drop oldest, block or shed load
- Expose the limit in the API contract

Don't:
- Return unbounded result sets
- Use unbounded in-memory caches or queues

## Steps

1. Find each growing structure
2. Set limits and overflow policy
3. Test at the limit
4. Reviewer tries to make it grow unbounded

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Does every queue, cache, pool and collection have a maximum size, and every query a limit or page size?
- [ ] Is the behaviour when full (reject, drop oldest, block or shed load) decided and stated in the contract?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a query with no LIMIT or page size
- Find a cache with no eviction
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

ciembor release-it and designing-data-intensive-applications: bound every queue, cache, pool and result set and decide the overflow behaviour; wshobson backend agents mention pagination. Amalgam: explicit limits and overflow policy in code and docs.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Design
- Test order: slot 51
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
