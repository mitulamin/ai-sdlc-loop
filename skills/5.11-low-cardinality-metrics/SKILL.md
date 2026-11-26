---
name: low-cardinality-metrics
description: "Use when defining metrics and labels. Amalgamated skill for principle 5.11 (Debug and observe)."
principles: ["5.11"]
principle: "5.11 Keep metric label cardinality low"
category: debug-and-observe
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 3
link_only_sources: 0
---

# 5.11 Low cardinality metrics

Principle 5.11 (Debug and observe / Observability and logging): Keep metric label cardinality low

## When to use

Defining metrics and labels.

## Producer: dos and don'ts

Do:
- Use bounded label values (status class, route template)
- Put high-cardinality data (user id, URL) in traces or logs

Don't:
- Label metrics with ids, emails or raw paths

## Steps

1. List labels
2. Check each is bounded
3. Move unbounded ones
4. Reviewer estimates series count

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find an unbounded label
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy observability and dash0/ollygarden otel-semantic-conventions: keep metric label cardinality low.

## Sources

3 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Debug
- Test order: slot 69 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
