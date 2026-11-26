---
name: size-process-to-task
description: "Use when at task intake, before loading planning skills. Amalgamated skill for principle 1.8 (Plan and specify)."
principles: ["1.8"]
principle: "1.8 Size the process to the task; skip ceremony for trivial changes"
category: plan-and-specify
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 4
link_only_sources: 1
---

# 1.8 Size process to task

Principle 1.8 (Plan and specify): Size the process to the task; skip ceremony for trivial changes

## When to use

At task intake, before loading planning skills.

## Producer: dos and don'ts

Do:
- Triage: trivial (one file, obvious), standard, or risky (security, data, public API)
- Trivial: skip spec, keep test and review
- Risky: full spec, design review and security pass
- Record the triage call in the run log

Don't:
- Run the full spec pipeline for a typo fix
- Skip tests or review because a task feels small

## Steps

1. Classify the task
2. Select the skill set for that class
3. Note the class in the run log
4. Re-triage if scope grows

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a 'trivial' change that touched risky areas
- Find ceremony that produced no decision or check
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy spec-driven-development has a 'when NOT to use' rule (single-line fixes, typo corrections), cc-sdd kiro-spec-quick is a lighter spec path and EGM lite is a lighter review path. Amalgam: an explicit triage rule the coordinator applies before it chooses which other skills to load.

## Sources

4 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [multica-ai/CLAUDE.md (Karpathy guidelines)](https://github.com/multica-ai/andrej-karpathy-skills/blob/2c606141936f1eeef17fa3043a72095b4765b9c2/CLAUDE.md) (No LICENSE file (README claims MIT))

## Test plan

- Test app: App A (CLI tool)
- Phase: Plan
- Test order: slot 16 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
