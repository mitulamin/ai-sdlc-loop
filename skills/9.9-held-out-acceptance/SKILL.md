---
name: held-out-acceptance
description: "Use when accepting a learned change. Amalgamated skill for principle 9.9 (Learn)."
principles: ["9.9"]
principle: "9.9 Accept a rule change coming out of a retrospective only if it measurably improves results on held-out cases it was not tuned on"
category: learn
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 6
link_only_sources: 1
---

# 9.9 Held out acceptance

Principle 9.9 (Learn): Accept a rule change coming out of a retrospective only if it measurably improves results on held-out cases it was not tuned on

## When to use

Accepting a learned change.

## Producer: dos and don'ts

Do:
- Test on held-in (the failure) and held-out (unseen) tasks
- Accept only if held-out does not regress and held-in improves

Don't:
- Accept because the triggering case now passes

## Steps

1. Split tasks
2. Run before/after
3. Compare
4. Decide

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Check held-out tasks were unseen by the proposer
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

muratcankoylan self-improvement-loops (a held-in split checks the targeted weakness, a held-out split the proposer never sees checks for regressions) and SkillOpt sleep (a change is kept only if it improves a held-out replay score; nothing goes live until adopted) agree. Partial overlap with 8.5, which is the pre-adoption eval.

## Sources

6 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [NousResearch/evolve_skill pipeline](https://github.com/NousResearch/hermes-agent-self-evolution/blob/0a929e3aa20e15cf04dc7c28492a7d41a5139125/README.md) (No LICENSE file (pyproject claims MIT))

## Test plan

- Test app: All three runs (harness and Learn)
- Phase: Learn
- Test order: slot 40 of 103
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
