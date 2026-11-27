---
name: dont-fight-the-harness
description: "Use when starting work in any harness (Cursor, Claude Code, Codex). Amalgamated skill for principle 8.10 (Agent operations)."
principles: ["8.10"]
principle: "8.10 Don't fight the harness: detect existing isolation and use native tools first"
category: agent-operations
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 8.10 Dont fight the harness

Principle 8.10 (Agent operations): Don't fight the harness: detect existing isolation and use native tools first

## When to use

Starting work in any harness (Cursor, Claude Code, Codex).

## Producer: dos and don'ts

Do:
- Detect existing worktrees, sandboxes and native tools first
- Use native tools over shell workarounds

Don't:
- Create nested worktrees or reimplement native features

## Steps

1. Detect environment
2. Choose native path
3. Proceed

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Did you detect and use the existing worktrees, sandboxes and native tools before reaching for a workaround?
- [ ] Did you avoid nested worktrees and reimplementing a native feature?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a workaround duplicating a native tool
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Superpowers using-git-worktrees (detect existing isolation) and using-superpowers (use native tools): detect what the harness already provides and use it.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: All runs (harness and Learn)
- Phase: Harness
- Test order: slot 10
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
