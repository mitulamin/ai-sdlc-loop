---
name: capture-corrections-batch-later
description: "Use when during and after runs. Amalgamated skill for principle 9.11 (Learn)."
principles: ["9.11"]
principle: "9.11 Capture corrections as they happen; process them later in a batch"
category: learn
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 9.11 Capture corrections batch later

Principle 9.11 (Learn): Capture corrections as they happen; process them later in a batch

## When to use

During and after runs.

## Producer: dos and don'ts

Do:
- Queue corrections and reviewer catches into a file as they occur
- Process the queue at end of run

Don't:
- Edit skills mid-run on each correction

## Steps

1. Capture
2. Queue
3. Batch process at end

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Was each correction and reviewer catch queued to a file as it happened?
- [ ] Was the queue processed at the end of the run, with no skill edited mid-run?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a correction in the transcript missing from the queue
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

claude-reflect (hooks queue corrections) and Kulaxyz self-learning: capture corrections as they happen; process them later in a batch.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: All runs (harness and Learn)
- Phase: Learn
- Test order: slot 42
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
