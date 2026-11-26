---
name: severity-ranked-findings
description: Use when writing review findings. Amalgamated skill for principle 7.5 (Review and ship).
principles: [7.5]
principle: "7.5 Rank findings by severity (P0-P3)"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 36
link_only_sources: 1
---

# 7.5 Severity ranked findings

Principle 7.5 (Review and ship): Rank findings by severity (P0-P3)

## When to use

Writing review findings.

## Producer: dos and don'ts

Do:
- Tag each finding P0 (security/data loss/correctness) to P3 (nit)
- Block on P0/P1 only

Don't:
- Mix nits with blockers untagged

## Steps

1. Write finding
2. Assign severity
3. Decide block

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a mis-ranked finding (e.g. data loss as P2)
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

sanyuan code-review-expert (P0-P3 with merge-blocking rules); Trail of Bits review workers also rank. Amalgam: every finding carries P0-P3 and P0/P1 block.

## Sources

36 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [anthropics/attack-surface-analysis](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/skills/attack-surface-analysis/SKILL.md) (Proprietary (Anthropic claude-security licence))

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Review & ship
- Test order: slot 85 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
