---
name: root-cause-before-fix
description: "Use when any bug, test failure or unexpected behaviour. Amalgamated skill for principle 5.1 (Debug and observe)."
principles: ["5.1"]
principle: "5.1 No fixes without root-cause investigation first: trace back to the original trigger, not where the symptom showed up."
category: debug-and-observe
aliases: ["9.4"]
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 5.1 Root cause before fix

Principle 5.1 (Debug and observe): No fixes without root-cause investigation first: trace back to the original trigger, not where the symptom showed up.

Merged duplicates (aliases): 9.4. See MERGES.md.

## When to use

Any bug, test failure or unexpected behaviour.

## Producer: dos and don'ts

Do:
- State the root cause in one sentence before writing a fix
- Trace the bad value back to the original trigger, not where the symptom showed up
- Fix at the source; add defence in depth if useful
- In Learn, trace an agent failure to its original trigger the same way

Don't:
- Patch the symptom where the error appears
- Try random changes until the test passes

## Steps

1. Gather evidence
2. Trace backwards to the trigger
3. State the root cause
4. Fix at the source; reviewer challenges the causal chain

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Can you state the root cause in one sentence, traced back to the original trigger?
- [ ] Does the fix change the source of the bad value, so it would also protect another caller?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Ask: would this fix prevent the same bug from another caller?
- Find a fix with no stated cause
- Check the trigger, not the symptom, was fixed
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Superpowers systematic-debugging (with root-cause-tracing.md), Addy debugging-and-error-recovery, cc-sdd kiro-debug, steipete five and the wshobson debugger agents agree: no fix without a root cause. Tracing back to the original trigger, formerly principle 9.4, is the same technique and is merged in. The Learn step reuses it when analysing why an agent failed.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App C (brownfield bug-fix and refactor)
- Phase: Debug
- Test order: slot 99
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
