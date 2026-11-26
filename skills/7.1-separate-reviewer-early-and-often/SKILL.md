---
name: separate-reviewer-early-and-often
description: "Use when after every task or slice, not only at the end. Amalgamated skill for principle 7.1 (Review and ship)."
principles: ["7.1"]
principle: "7.1 Review the work at the end of each phase, using a separate reviewer subagent that did not write it"
category: review-and-ship
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 35
link_only_sources: 0
---

# 7.1 Separate reviewer early and often

Principle 7.1 (Review and ship): Review the work at the end of each phase, using a separate reviewer subagent that did not write it

## When to use

After every task or slice, not only at the end.

## Producer: dos and don'ts

Do:
- Dispatch a fresh reviewer with the diff, the task and the spec excerpt
- Review after each task, before the next starts
- Fix blocking findings before moving on

Don't:
- Let the implementer review its own work
- Batch all review to the end

## Steps

1. Finish task
2. Dispatch reviewer
3. Fix findings
4. Re-review if changes were material

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Check the reviewer was a fresh context
- Find tasks merged without review
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Superpowers requesting-code-review (with code-reviewer.md) and subagent-driven-development, Pocock code-review and many wshobson code-reviewer copies (six identical files) agree: a separate reviewer subagent after each task. PARTIAL overlap with 8.7; proposed sharpening: 7.1 owns review, 8.7 owns fact-finding.

## Sources

35 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App A (CLI tool)
- Phase: Review & ship
- Test order: slot 32 of 103
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
