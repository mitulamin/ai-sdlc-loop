---
name: red-green-tdd
description: "Use when implementing any feature or fix. Amalgamated skill for principle 4.1 (Verify)."
principles: ["4.1"]
principle: "4.1 Write one failing test first and watch it fail, then write the minimal code to pass; one seam per cycle, never all tests up front."
category: verify
aliases: ["4.4"]
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 4.1 Red green tdd

Principle 4.1 (Verify): Write one failing test first and watch it fail, then write the minimal code to pass; one seam per cycle, never all tests up front.

Merged duplicates (aliases): 4.4. See MERGES.md.

## When to use

Implementing any feature or fix.

## Producer: dos and don'ts

Do:
- Write one failing test for the next behaviour and watch it fail for the right reason
- Pick one seam and one behaviour per cycle
- Write the minimum code to pass
- Refactor with tests green
- Repeat: one test, one implementation per cycle

Don't:
- Write code before a failing test exists
- Write a batch of tests up front, then all the code (horizontal slicing)
- Test several seams in one cycle

## Steps

1. Choose the seam and the next behaviour
2. Red: write one test, run it, see the expected failure
3. Green: write the minimal code
4. Refactor, then repeat
5. Reviewer checks test-first order in the history

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find code with no test that failed first
- Find a test that passed on its first run (never red)
- Find a commit that adds many tests before any code
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Superpowers test-driven-development (iron law: no code without a failing test), Addy test-driven-development, Pocock tdd (one seam, one test, one minimal implementation per cycle) and the wshobson tdd-cycle, tdd-red, tdd-green and tdd-refactor commands agree on red-green-refactor. Pocock's vertical-slice rule, formerly principle 4.4, is merged in as the cycle rule: never write all the tests up front.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App A (CLI tool)
- Phase: Verify
- Test order: slot 26
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
