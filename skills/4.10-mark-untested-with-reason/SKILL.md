---
name: mark-untested-with-reason
description: "Use whenever a check cannot be run. Amalgamated skill for principle 4.10 (Verify)."
principles: ["4.10"]
principle: "4.10 Mark anything you couldn't test as untested, with the reason; never skip silently"
category: verify
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 2
link_only_sources: 2
---

# 4.10 Mark untested with reason

Principle 4.10 (Verify): Mark anything you couldn't test as untested, with the reason; never skip silently

## When to use

Whenever a check cannot be run.

## Producer: dos and don'ts

Do:
- List every check you could not run, with the reason
- Surface it in the final report to the coordinator
- Suggest how it could be tested

Don't:
- Skip a test silently
- Report success on partially verified work

## Steps

1. Attempt each check
2. Record blocked ones
3. Add UNTESTED section
4. Reviewer checks the list is complete

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a claimed-tested item with no evidence
- Find skipped tests not listed
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Superpowers' cannot-verify reference (items the reviewer could not check from the diff must be resolved before a task is complete) and OpenSpec openspec-verify-change (mark a check as not verified with the specific reason, and carry on) both report what could not be verified instead of dropping it. Amalgam: an UNTESTED list with reasons in every report.

## Sources

2 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [michaelshimeles/evidence-driven-testing](https://github.com/michaelshimeles/rstack/blob/8ad39442fd64cf2b407249024c5310dda90f6283/evidence-driven-testing/SKILL.md) (No licence)
- [anthropics/patch-verifier](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/agents/patch-verifier.md) (Proprietary (Anthropic claude-security licence))

## Test plan

- Test app: App A (CLI tool)
- Phase: Verify
- Test order: slot 31 of 103
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
