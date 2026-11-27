---
name: minimum-code
description: "Use when every implementation step. Amalgamated skill for principle 3.1 (Code craft)."
principles: ["3.1"]
principle: "3.1 When you write code, write the minimum that solves the stated problem, with no speculative features, options or hooks"
category: code-craft
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 3.1 Minimum code

Principle 3.1 (Code craft): When you write code, write the minimum that solves the stated problem, with no speculative features, options or hooks

## When to use

Every implementation step.

## Producer: dos and don'ts

Do:
- Implement only what the current acceptance check needs
- Prefer the standard library and existing code
- Delete code paths no test or requirement needs

Don't:
- Add options, hooks or generality nobody asked for
- Write 'future-proof' scaffolding

## Steps

1. Read the check
2. Write the least code to pass
3. Simplify once green
4. Reviewer tries to delete lines

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Does every line serve the current acceptance check, with no option, hook or generality nobody asked for?
- [ ] Did you use the standard library and existing code before writing new code?
- [ ] Once green, did you delete the code paths no test or requirement needs?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- List lines that can be deleted with all checks still green
- Find features not in the spec
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

ponytail (simplest solution, with lite, full and ultra levels and a 'never cut' list, see 3.13), Addy incremental-implementation and Addy code-simplification agree: write the smallest code that meets the acceptance check.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [multica-ai/CLAUDE.md (Karpathy guidelines)](https://github.com/multica-ai/andrej-karpathy-skills/blob/2c606141936f1eeef17fa3043a72095b4765b9c2/CLAUDE.md) (No LICENSE file (README claims MIT))

## Test plan

- Test app: App A (CLI tool)
- Phase: Build
- Test order: slot 19
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
