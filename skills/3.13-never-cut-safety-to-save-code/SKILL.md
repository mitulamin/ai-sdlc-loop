---
name: never-cut-safety-to-save-code
description: "Use when any simplification or minimalism pass. Amalgamated skill for principle 3.13 (Code craft)."
principles: ["3.13"]
principle: "3.13 Never cut boundary validation, data-loss handling or security to save code"
category: code-craft
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 3.13 Never cut safety to save code

Principle 3.13 (Code craft): Never cut boundary validation, data-loss handling or security to save code

## When to use

Any simplification or minimalism pass.

## Producer: dos and don'ts

Do:
- Keep boundary validation, error handling that prevents data loss, security checks and accessibility
- Treat removing any of these as a must-fix finding

Don't:
- Delete validation or error handling to make code shorter
- Swallow errors to simplify flow

## Steps

1. Simplify
2. Diff for removed checks
3. Restore any removed safety code
4. Reviewer audits the diff for removed guards

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a removed validation, catch or auth check
- Find an error swallowed silently
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

ponytail's 'never cut' list (validation at trust boundaries, data-loss handling, security, accessibility) and ponytail-audit's must-fix tier. The guard-rail that keeps 3.1 and 3.12 from going too far.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Build
- Test order: slot 62
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
