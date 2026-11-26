---
name: eval-skills-before-trusting
description: Use when before adopting any skill (including these 103). Amalgamated skill for principle 8.5 (Agent operations).
principles: [8.5]
principle: "8.5 Test skills with evals before trusting them"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 17
link_only_sources: 0
---

# 8.5 Eval skills before trusting

Principle 8.5 (Agent operations): Test skills with evals before trusting them

## When to use

Before adopting any skill (including these 103; five duplicates of the original 108 were merged, see MERGES.md).

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

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Check the grader did not know which run had the skill
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Anthropic skill-creator with its grader/comparator/analyzer agents (blind comparison) and wshobson eval-harness-first. PARTIAL overlap with 9.9; this is the pre-adoption eval. These test apps are its practical form.

## Sources

17 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Test plan

- Test app: All three runs (harness and Learn)
- Phase: Harness
- Test order: slot 5 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
