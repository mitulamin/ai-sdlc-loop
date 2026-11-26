---
name: surgical-changes
description: "Use when any change to existing code. Amalgamated skill for principle 3.2 (Code craft)."
principles: ["3.2"]
principle: "3.2 Make surgical changes: every changed line traces to the request"
category: code-craft
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 3.2 Surgical changes

Principle 3.2 (Code craft): Make surgical changes: every changed line traces to the request

## When to use

Any change to existing code.

## Producer: dos and don'ts

Do:
- Check each hunk of the diff against the task; anything that does not serve it comes out
- Leave unrelated formatting, renames and refactors out
- Note other problems you see in the run log instead of fixing them

Don't:
- Reformat files you touched
- Fix 'while I'm here' issues in the same change

## Steps

1. Plan the smallest diff
2. Make it
3. Re-read the diff hunk by hunk against the task
4. Reviewer flags hunks that serve no part of the task

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a hunk unrelated to the task
- Find a drive-by rename
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

caveman surgical-patch (change the narrowest layer that owns the bug, preserve unrelated behaviour and user changes, no cleanup or renaming outside the fix), caveman cavecrew-builder, Addy incremental-implementation (thin, revertable increments) and Addy code-simplification agree: touch only what the task needs. Strongest in brownfield work.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [multica-ai/CLAUDE.md (Karpathy guidelines)](https://github.com/multica-ai/andrej-karpathy-skills/blob/2c606141936f1eeef17fa3043a72095b4765b9c2/CLAUDE.md) (No LICENSE file (README claims MIT))

## Test plan

- Test app: App C (brownfield bug-fix and refactor)
- Phase: Build
- Test order: slot 93
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
