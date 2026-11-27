---
name: evidence-before-completion
description: "Use when before any agent reports a task done, fixed or passing. Amalgamated skill for principle 4.9 (Verify)."
principles: ["4.9"]
principle: "4.9 Do not claim the work is done until you have just run the verification and read its output"
category: verify
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 4.9 Evidence before completion

Principle 4.9 (Verify): Do not claim the work is done until you have just run the verification and read its output

## When to use

Before any agent reports a task done, fixed or passing.

## Producer: dos and don'ts

Do:
- Run the verification command fresh and paste its output
- Match evidence to the scope of the claim
- Report failures honestly

Don't:
- Claim done from memory of an earlier run
- Say 'should work'

## Steps

1. Identify the claim
2. Run the proving command
3. Attach output
4. Reviewer reruns it

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Did you run the verification command fresh, after the last change, and read its output?
- [ ] Does the evidence you show cover the full scope of each claim you make?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Rerun the evidence: does it reproduce?
- Find a claim broader than its evidence
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Superpowers verification-before-completion (no completion claim without fresh verification evidence), cc-sdd kiro-verify-completion (evidence matched to the scope of the claim) and caveman verify-and-stop (the smallest sufficient proof) agree. Partial overlap with 7.12, which is the reviewer-facing ship proof.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [michaelshimeles/evidence-driven-testing](https://github.com/michaelshimeles/rstack/blob/8ad39442fd64cf2b407249024c5310dda90f6283/evidence-driven-testing/SKILL.md) (No licence)

## Test plan

- Test app: App A (CLI tool)
- Phase: Verify
- Test order: slot 30
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
