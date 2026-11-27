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

## Related practices

Established practices this skill applies alongside its principle. Each has a self-check item and a reviewer check below.

- **Fail fast** ([guide](../../guides/developer/quality-principles.md#fail-fast)): detect invalid input, broken invariants and missing config at the point of entry, at startup or at the boundary, and fail loudly rather than carry on with data that is already wrong. Failing fast is for operators and developers: users still get a controlled, consistent error. See also [6.3](../../principles/6.3.md), [2.7](../../principles/2.7.md).

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Does the change keep every boundary validation, data-loss guard, security check and accessibility feature?
- [ ] Is every error handled or propagated, with none swallowed to simplify the flow?
- [ ] Fail fast: are invalid input, broken invariants and missing config caught at startup or at the boundary and reported loudly, with users still given a controlled error?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a removed validation, catch or auth check
- Find an error swallowed silently
- Fail fast: find invalid input, a broken invariant or missing config that the code carries on with instead of reporting at entry
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
