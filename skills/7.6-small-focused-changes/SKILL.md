---
name: small-focused-changes
description: Use when opening a PR or commit. Amalgamated skill for principle 7.6 (Review and ship).
principles: [7.6]
principle: "7.6 Keep each change small and about one thing"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 2
link_only_sources: 0
---

# 7.6 Small focused changes

Principle 7.6 (Review and ship): Keep each change small and about one thing

## When to use

Opening a PR or commit.

## Producer: dos and don'ts

Do:
- One logical change per PR, ideally under ~300 changed lines
- Split refactors from features

Don't:
- Open giant mixed PRs

## Steps

1. Check diff size
2. Split if mixed
3. Write a focused description

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find two unrelated changes in one PR
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy git-workflow-and-versioning and code-review-and-quality: each change small and about one thing. PARTIAL overlap with 7.10 (small batches) and 3.14; proposed sharpening: 7.6 owns PR size, 7.10 owns pipeline/shift-left.

## Sources

2 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Review & ship
- Test order: slot 86 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
