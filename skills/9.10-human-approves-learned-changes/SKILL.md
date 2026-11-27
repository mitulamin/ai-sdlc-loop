---
name: human-approves-learned-changes
description: "Use when end of each run. Amalgamated skill for principle 9.10 (Learn)."
principles: ["9.10"]
principle: "9.10 A human approves each learned change before it goes live"
category: learn
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 9.10 Human approves learned changes

Principle 9.10 (Learn): A human approves each learned change before it goes live

## When to use

End of each run.

## Producer: dos and don'ts

Do:
- Present each proposed change with evidence in one review batch
- Apply only approved changes

Don't:
- Auto-apply learned edits to live skills

## Steps

1. Batch proposals
2. Human reviews
3. Apply approved
4. Log all

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Is each proposed change presented with its evidence, in one batch, for the human to approve?
- [ ] Were only approved changes applied to live skills?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a live change with no approval record
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

claude-reflect /reflect (approval per fix), Anthropic hookify conversation-analyzer, SkillOpt adopt and caveman-learn: a human approves each learned change. This is the one human touchpoint in the loop.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: All runs (harness and Learn)
- Phase: Learn
- Test order: slot 41
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
