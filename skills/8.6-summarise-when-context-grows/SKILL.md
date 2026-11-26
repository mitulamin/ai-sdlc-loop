---
name: summarise-when-context-grows
description: "Use when a session nears its context budget or hands off. Amalgamated skill for principle 8.6 (Agent operations)."
principles: ["8.6"]
principle: "8.6 Summarise progress when the context gets long"
category: agent-operations
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 23
link_only_sources: 1
---

# 8.6 Summarise when context grows

Principle 8.6 (Agent operations): Summarise progress when the context gets long

## When to use

When a session nears its context budget or hands off.

## Producer: dos and don'ts

Do:
- Write a handoff file: goal, done, next, decisions, open issues
- Start the next agent from that file

Don't:
- Let context overflow and lose decisions

## Steps

1. Detect threshold
2. Write handoff
3. Restart fresh
4. Verify continuity

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a decision lost across a handoff
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy context-engineering, Pocock handoff/claude-handoff and muratcan context-compression: summarise progress into a handoff file when context gets long.

## Sources

23 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [anthropics/attack-surface-analysis](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/skills/attack-surface-analysis/SKILL.md) (Proprietary (Anthropic claude-security licence))

## Test plan

- Test app: All three runs (harness and Learn)
- Phase: Harness
- Test order: slot 6 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
