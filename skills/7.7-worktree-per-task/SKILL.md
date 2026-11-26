---
name: worktree-per-task
description: "Use when starting any task, especially with parallel agents. Amalgamated skill for principle 7.7 (Review and ship)."
principles: ["7.7"]
principle: "7.7 One worktree and branch per task and per agent"
category: review-and-ship
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 7
link_only_sources: 2
---

# 7.7 Worktree per task

Principle 7.7 (Review and ship): One worktree and branch per task and per agent

## When to use

Starting any task, especially with parallel agents.

## Producer: dos and don'ts

Do:
- Create a worktree and branch per task
- Run setup and baseline tests in it
- Clean it up when merged

Don't:
- Let two agents edit the same checkout

## Steps

1. Create worktree
2. Baseline tests
3. Work
4. Finish and remove

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find two agents' changes interleaved in one working tree
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Superpowers using-git-worktrees (an isolated workspace per task, project setup and baseline tests, detect existing isolation and prefer native tools), finishing-a-development-branch (clean up when done) and dispatching-parallel-agents (parallel agents only for independent tasks) agree: one worktree and branch per task and per agent, so parallel agents never collide.

## Sources

7 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [michaelshimeles/new-feature](https://github.com/michaelshimeles/rstack/blob/8ad39442fd64cf2b407249024c5310dda90f6283/new-feature/SKILL.md) (No licence)
- [michaelshimeles/AGENTS.md workflow template](https://github.com/michaelshimeles/rstack/blob/8ad39442fd64cf2b407249024c5310dda90f6283/AGENTS.md) (No licence)

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Review & ship
- Test order: slot 87 of 103
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
