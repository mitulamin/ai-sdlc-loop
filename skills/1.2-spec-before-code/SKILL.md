---
name: spec-before-code
description: "Use when any change bigger than a one-file fix, or any new feature/app. Amalgamated skill for principle 1.2 (Plan and specify)."
principles: ["1.2"]
principle: "1.2 Write a spec before code for non-trivial work, and gate each phase on human review"
category: plan-and-specify
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 1.2 Spec before code

Principle 1.2 (Plan and specify): Write a spec before code for non-trivial work, and gate each phase on human review

## When to use

Any change bigger than a one-file fix, or any new feature/app.

## Producer: dos and don'ts

Do:
- Write spec.md: goal, users, non-goals, acceptance criteria (testable), constraints, open questions
- Write acceptance criteria as numbered Given/When/Then lines, so every later check can cite one by its number
- Record the interview outcome in the spec as a decision sheet: for each decision the choice, who decided it, why, and its register id (log an interview answer in the register so it has one)
- Give every parked item a reason it can wait and a revisit trigger, the event that should bring it back
- Treat a decision the human has answered, through a register QUESTION or the interview, as locked, and carry it into the spec as answered
- Keep it to one or two pages; link out for detail
- Have an adversarial spec reviewer check it before planning starts
- Treat the spec as living: update it when the build teaches you something, except for locked decisions

Don't:
- Start coding before acceptance criteria exist
- Copy a heavyweight template and fill every section
- Pause the loop for human sign-off at each phase (the coordinator gates; the human reviews at the end)
- Reopen or override a locked decision silently; if the evidence contradicts it, raise [QUESTION: ...] or [BLOCKER: ...] with that evidence and leave the decision standing meanwhile
- Leave a choice open that affects behaviour, an interface, authorisation, the source of truth or rollout

## Steps

1. Draft spec.md from the brief, 1.1 assumptions and any answered decisions in the register
2. Spec reviewer attacks it: ambiguity, untestable criteria, missing non-goals, silent overrides
3. Revise until the reviewer passes or escalate one batched question
4. Hand the spec to planning (1.3, 1.6)

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Does the spec state the goal, users, non-goals, constraints and open questions, in one or two pages?
- [ ] Is every acceptance criterion numbered, written as Given/When/Then and checkable by a test or command?
- [ ] Is every item decided (choice, who decided, why, register id) or parked with a reason and a revisit trigger?
- [ ] Does the spec carry every locked decision as answered, with any contradicting evidence raised as a question or blocker rather than an override?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Every acceptance criterion must be numbered, written as Given/When/Then, and checkable by a test or command
- Exit test: every item in the spec is either decided, or parked with a reason and a revisit trigger; fail it if any open choice affects behaviour, an interface, authorisation, the source of truth or rollout
- Decision sheet: every decision shows the choice, who decided it, why, and its register id; fail a decision with a field missing or an id that is not in the register
- Locked decisions: compare the spec with the answered register entries and the interview outcome; flag any decision the spec changes, drops or narrows without a [QUESTION: ...] or [BLOCKER: ...] raised with evidence, as a silent override
- Find scope the code will need that the spec never mentions
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Several source files (Addy spec-driven-development, spec-kit specify, OpenSpec propose, cc-sdd requirements, Pocock to-spec, agent-os shape-spec) agree on a written spec as the source of truth; they differ on artefacts (spec.md vs proposal+tasks vs requirements/design/tasks). Amalgam: one short spec.md with goal, non-goals, acceptance criteria and open questions; the human gate moves to the coordinator's end-of-run review, per the independent-loop principle.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Plan
- Test order: slot 44
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
