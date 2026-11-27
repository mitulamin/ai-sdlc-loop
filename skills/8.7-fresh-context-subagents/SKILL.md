---
name: fresh-context-subagents
description: "Use when any investigation or review that would pollute the main context. Amalgamated skill for principle 8.7 (Agent operations)."
principles: ["8.7"]
principle: "8.7 Send fact-finding and bulk reading to fresh-context subagents and take back only a short summary, so the main context stays small"
category: agent-operations
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 8.7 Fresh context subagents

Principle 8.7 (Agent operations): Send fact-finding and bulk reading to fresh-context subagents and take back only a short summary, so the main context stays small

## When to use

Any investigation or review that would pollute the main context.

## Producer: dos and don'ts

Do:
- Dispatch a fresh subagent with a precise brief
- Get back a short report or file path
- Use parallel agents for independent questions

Don't:
- Do long investigations in the coordinator's own context

## Steps

1. Write brief
2. Dispatch
3. Read report
4. Decide

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Did fact-finding and bulk reading go to fresh subagents with precise briefs?
- [ ] Did you take back only a short report or a file path?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Check the coordinator's context stayed small
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Pocock chief-of-staff, Superpowers subagent-driven-development and dispatching-parallel-agents, EGM review (goldfish) and Cloudflare security-audit: fresh-context subagents for fact-finding and review. The core of the coordinator model; PARTIAL overlap with 7.1.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: All runs (harness and Learn)
- Phase: Harness
- Test order: slot 7
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
