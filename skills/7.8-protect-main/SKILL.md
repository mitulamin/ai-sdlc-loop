---
name: protect-main
description: "Use when any agent with git access. Amalgamated skill for principle 7.8 (Review and ship)."
principles: ["7.8"]
principle: "7.8 Never commit to main or force-push"
category: review-and-ship
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 3
link_only_sources: 1
---

# 7.8 Protect main

Principle 7.8 (Review and ship): Never commit to main or force-push

## When to use

Any agent with git access.

## Producer: dos and don'ts

Do:
- Work on branches; merge via PR
- Block push to main and force-push with hooks or branch protection

Don't:
- Commit directly to main
- Force-push shared branches

## Steps

1. Install guard hooks
2. Use branches
3. Merge via PR

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Attempt a push to main in a test: is it blocked?
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Pocock git-guardrails-claude-code (hooks that block push, reset --hard, clean and branch -D), Superpowers finishing-a-development-branch (verify, then choose merge, PR or discard) and Addy git-workflow-and-versioning (no force-pushing to shared branches) agree: work on branches and make the dangerous git commands impossible.

## Sources

3 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [michaelshimeles/AGENTS.md workflow template](https://github.com/michaelshimeles/rstack/blob/8ad39442fd64cf2b407249024c5310dda90f6283/AGENTS.md) (No licence)

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Review & ship
- Test order: slot 88 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
