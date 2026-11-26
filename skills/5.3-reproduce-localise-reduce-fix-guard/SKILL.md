---
name: reproduce-localise-reduce-fix-guard
description: "Use when fixing a reported bug. Amalgamated skill for principle 5.3 (Debug and observe)."
principles: ["5.3"]
principle: "5.3 Reproduce the bug with a failing test first, then localise, reduce, fix, keep the test as a guard, and verify end to end."
category: debug-and-observe
aliases: ["4.5"]
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 5.3 Reproduce localise reduce fix guard

Principle 5.3 (Debug and observe): Reproduce the bug with a failing test first, then localise, reduce, fix, keep the test as a guard, and verify end to end.

Merged duplicates (aliases): 4.5. See MERGES.md.

## When to use

Fixing a reported bug.

## Producer: dos and don'ts

Do:
- Reproduce the bug with a failing test first
- Localise it (bisect, logs, narrowing)
- Reduce it to the minimal case
- Fix, keep the test as a guard, and verify end to end

Don't:
- Fix first and add a test later, or never
- Skip straight to fixing without a reproduction
- Close the bug without an end-to-end check

## Steps

1. Reproduce in a failing test and confirm it is red
2. Localise and reduce
3. Fix until the test passes
4. Keep the test as a guard and verify end to end

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Revert the fix: does the guard test fail?
- Check end-to-end evidence exists
- Find a bug-fix commit with no reproducing test
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy debugging-and-error-recovery gives the full sequence; Pocock diagnosing-bugs, Superpowers systematic-debugging and Trail of Bits reproduce-bug cover parts; Addy test-driven-development has a 'prove it' pattern for bug fixes; wshobson smart-fix and issue repeat the flow. The reproducing test first, formerly principle 4.5, is merged in as step one.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [multica-ai/CLAUDE.md (Karpathy guidelines)](https://github.com/multica-ai/andrej-karpathy-skills/blob/2c606141936f1eeef17fa3043a72095b4765b9c2/CLAUDE.md) (No LICENSE file (README claims MIT))

## Test plan

- Test app: App C (brownfield bug-fix and refactor)
- Phase: Debug
- Test order: slot 101
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
