---
name: short-always-on-rules-file
description: "Use when setting up any repo for agents. Amalgamated skill for principle 8.2 (Agent operations)."
principles: ["8.2"]
principle: "8.2 Keep one short always-on rules file: stack, commands, conventions, boundaries"
category: agent-operations
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 19
link_only_sources: 2
---

# 8.2 Short always on rules file

Principle 8.2 (Agent operations): Keep one short always-on rules file: stack, commands, conventions, boundaries

## When to use

Setting up any repo for agents.

## Producer: dos and don'ts

Do:
- Keep one always-on rules file (AGENTS.md or CLAUDE.md): stack, build and test commands, conventions, never-do list
- Keep it short enough that every line changes agent behaviour
- Move detail into on-demand skills

Don't:
- Let the rules file grow into a manual
- Keep stale commands or conventions

## Steps

1. Draft the file
2. Trim lines that change nothing
3. Test that a fresh agent can build and test from it alone
4. Prune on a schedule (9.3)

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a line no agent behaviour depends on
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy context-engineering (Level 1: a rules file that persists across sessions), the agents.md README, Anthropic claude-md-improver (scores commands, architecture clarity, conciseness and currency) and caveman init agree: one short always-on rules file with the stack, the commands, the conventions and the boundaries.

## Sources

19 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [michaelshimeles/AGENTS.md workflow template](https://github.com/michaelshimeles/rstack/blob/8ad39442fd64cf2b407249024c5310dda90f6283/AGENTS.md) (No licence)
- [multica-ai/CLAUDE.md (Karpathy guidelines)](https://github.com/multica-ai/andrej-karpathy-skills/blob/2c606141936f1eeef17fa3043a72095b4765b9c2/CLAUDE.md) (No LICENSE file (README claims MIT))

## Test plan

- Test app: All three runs (harness and Learn)
- Phase: Harness
- Test order: slot 2 of 103
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
