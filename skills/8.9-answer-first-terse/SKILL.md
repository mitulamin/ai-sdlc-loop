---
name: answer-first-terse
description: "Use when agent-to-agent messages and reports. Amalgamated skill for principle 8.9 (Agent operations)."
principles: ["8.9"]
principle: "8.9 Answer first, cut ceremony, keep code and errors verbatim"
category: agent-operations
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 8.9 Answer first terse

Principle 8.9 (Agent operations): Answer first, cut ceremony, keep code and errors verbatim

## When to use

Agent-to-agent messages and reports.

## Producer: dos and don'ts

Do:
- Lead with the result
- Cut preamble and filler
- Quote code and errors verbatim

Don't:
- Paraphrase error messages
- Pad reports

## Steps

1. Draft
2. Cut to essentials
3. Keep verbatim bits

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Does each report lead with the result, with no preamble or padding?
- [ ] Are code and error messages quoted verbatim, not paraphrased?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a paraphrased error
- Measure tokens vs baseline
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

caveman family (caveman, ultracave, megacave, caveman-compress): answer first, cut filler, keep code and errors verbatim. Token-reduction rule for agent-to-agent traffic.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: All runs (harness and Learn)
- Phase: Harness
- Test order: slot 9
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
