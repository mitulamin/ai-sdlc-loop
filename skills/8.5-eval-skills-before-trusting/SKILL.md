---
name: eval-skills-before-trusting
description: "Use when before adopting any skill (including the skills in this repo). Amalgamated skill for principle 8.5 (Agent operations)."
principles: ["8.5"]
principle: "8.5 Run a new or changed skill against evals before you rely on it"
category: agent-operations
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 8.5 Eval skills before trusting

Principle 8.5 (Agent operations): Run a new or changed skill against evals before you rely on it

## When to use

Before adopting any skill (including the skills in this repo).

## Producer: dos and don'ts

Do:
- Run tasks with and without the skill
- Grade blind with a comparator agent
- Adopt only on a measurable win

Don't:
- Adopt skills on star count or vibes

## Steps

1. Pick eval tasks
2. Run A/B
3. Blind grade
4. Record result

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Was each new or changed skill run against evals with and without it, graded blind, and adopted only on a measurable win?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Check the grader did not know which run had the skill
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Anthropic skill-creator with its grader/comparator/analyzer agents (blind comparison) and wshobson eval-harness-first. PARTIAL overlap with 9.9; this is the pre-adoption eval. These test apps are its practical form.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: All runs (harness and Learn)
- Phase: Harness
- Test order: slot 5
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
