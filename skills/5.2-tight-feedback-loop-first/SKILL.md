---
name: tight-feedback-loop-first
description: "Use when starting to debug anything non-trivial. Amalgamated skill for principle 5.2 (Debug and observe)."
principles: ["5.2"]
principle: "5.2 Build a tight, deterministic pass/fail feedback loop before hunting the bug"
category: debug-and-observe
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 5.2 Tight feedback loop first

Principle 5.2 (Debug and observe): Build a tight, deterministic pass/fail feedback loop before hunting the bug

## When to use

Starting to debug anything non-trivial.

## Producer: dos and don'ts

Do:
- Build a single command that shows pass/fail in seconds
- Make it deterministic (seed, fixed input)
- Reuse it for every hypothesis

Don't:
- Debug by re-running the whole app manually
- Hunt the bug before you can reproduce it reliably

## Steps

1. Write the repro command
2. Confirm it fails consistently
3. Hypothesise and test with it
4. Keep it as a test

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Run the loop 5 times: same result?
- Check how long one iteration takes
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Pocock diagnosing-bugs (build a fast deterministic pass/fail loop first) and Superpowers systematic-debugging. Amalgam: a one-command repro before hunting.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App C (brownfield bug-fix and refactor)
- Phase: Debug
- Test order: slot 100
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
