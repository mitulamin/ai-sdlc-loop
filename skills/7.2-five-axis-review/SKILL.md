---
name: five-axis-review
description: "Use when every code review. Amalgamated skill for principle 7.2 (Review and ship)."
principles: ["7.2"]
principle: "7.2 Review on five axes: correctness, readability, architecture, security, performance"
category: review-and-ship
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 7.2 Five axis review

Principle 7.2 (Review and ship): Review on five axes: correctness, readability, architecture, security, performance

## When to use

Every code review.

## Producer: dos and don'ts

Do:
- Score each of the five axes with findings
- Note which axes were not applicable and why

Don't:
- Review only style
- Skip security or performance silently

## Steps

1. Read diff
2. Go axis by axis
3. Write findings
4. Summarise verdict

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Does the review cover correctness, readability, architecture, security and performance, each with findings or a reason it does not apply?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find an axis with no comment and no 'n/a' reason
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy code-review-and-quality, code-reviewer agent and /review, plus steipete pr-review (multiple perspectives): review correctness, readability, architecture, security, performance.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Review & ship
- Test order: slot 82
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
