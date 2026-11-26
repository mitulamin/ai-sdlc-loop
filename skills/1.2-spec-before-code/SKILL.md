---
name: spec-before-code
description: "Use when any change bigger than a one-file fix, or any new feature/app. Amalgamated skill for principle 1.2 (Plan and specify)."
principles: ["1.2"]
principle: "1.2 Write a spec before code for non-trivial work, and gate each phase on human review"
category: plan-and-specify
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 29
link_only_sources: 0
---

# 1.2 Spec before code

Principle 1.2 (Plan and specify): Write a spec before code for non-trivial work, and gate each phase on human review

## When to use

Any change bigger than a one-file fix, or any new feature/app.

## Producer: dos and don'ts

Do:
- Write spec.md: goal, users, non-goals, acceptance criteria (testable), constraints, open questions
- Keep it to one or two pages; link out for detail
- Have an adversarial spec reviewer check it before planning starts
- Treat the spec as living: update it when the build teaches you something

Don't:
- Start coding before acceptance criteria exist
- Copy a heavyweight template and fill every section
- Pause the loop for human sign-off at each phase (the coordinator gates; the human reviews at the end)

## Steps

1. Draft spec.md from the brief and 1.1 assumptions
2. Spec reviewer attacks it: ambiguity, untestable criteria, missing non-goals
3. Revise until the reviewer passes or escalate one batched question
4. Hand the spec to planning (1.3, 1.6)

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Every acceptance criterion must be checkable by a test or command
- Find scope the code will need that the spec never mentions
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Nine source files (Addy spec-driven-development, spec-kit specify, OpenSpec propose, cc-sdd requirements, Pocock to-spec, agent-os shape-spec) agree on a written spec as the source of truth; they differ on artefacts (spec.md vs proposal+tasks vs requirements/design/tasks). Amalgam: one short spec.md with goal, non-goals, acceptance criteria and open questions; the human gate moves to the coordinator's end-of-run review, per the independent-loop principle.

## Sources

29 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Plan
- Test order: slot 44 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
