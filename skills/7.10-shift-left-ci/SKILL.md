---
name: shift-left-ci
description: "Use when setting up a project's pipeline. Amalgamated skill for principle 7.10 (Review and ship)."
principles: ["7.10"]
principle: "7.10 Shift checks left and release in small, frequent batches, so problems show up early and each release carries little risk"
category: review-and-ship
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 7.10 Shift left ci

Principle 7.10 (Review and ship): Shift checks left and release in small, frequent batches, so problems show up early and each release carries little risk

## When to use

Setting up a project's pipeline.

## Producer: dos and don'ts

Do:
- Run lint, types, tests and security checks on every push
- Make the pipeline fast enough to run per commit
- Deploy small batches often

Don't:
- Leave checks to a release-time manual step

## Steps

1. Add CI
2. Order fast checks first
3. Keep under ~10 min
4. Reviewer breaks a test to see CI catch it

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Do lint, types, tests and security checks run on every push, fast enough to run per commit?
- [ ] Does the change ship as a small batch?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Introduce a deliberate failure: does CI catch it?
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy ci-cd-and-automation and shipping-and-launch: run checks as early as possible in CI and ship in small frequent batches.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [NousResearch/evolve_skill pipeline](https://github.com/NousResearch/hermes-agent-self-evolution/blob/0a929e3aa20e15cf04dc7c28492a7d41a5139125/README.md) (No LICENSE file (pyproject claims MIT))
- [anthropics/attack-surface-analysis](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/skills/attack-surface-analysis/SKILL.md) (Proprietary (Anthropic claude-security licence))

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Review & ship
- Test order: slot 90
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
