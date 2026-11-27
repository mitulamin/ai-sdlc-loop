---
name: load-only-needed-context
description: "Use whenever the coordinator briefs a worker. Amalgamated skill for principle 8.1 (Agent operations)."
principles: ["8.1"]
principle: "8.1 At task time, give the agent only the context that task needs, such as the relevant spec section"
category: agent-operations
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 8.1 Load only needed context

Principle 8.1 (Agent operations): At task time, give the agent only the context that task needs, such as the relevant spec section

## When to use

Whenever the coordinator briefs a worker.

## Producer: dos and don'ts

Do:
- Include only the spec section, files and standards for this task
- Point to files rather than pasting whole repos
- Track a context budget

Don't:
- Dump the whole spec, history and all skills into every agent

## Steps

1. Select task
2. Pick relevant context
3. Brief worker
4. Review what was unused

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Does each brief hold only the spec section, files and standards its task needs, pointing to files rather than pasting them?
- [ ] Did the worker have everything it needed, and use what it was given?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find context in the brief the worker never used
- Find needed context missing
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy context-engineering, agent-os inject-standards and muratcan context-optimization/fundamentals: load only the relevant spec section and standards. Core coordinator duty when filling blank-context agents.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: All runs (harness and Learn)
- Phase: Harness
- Test order: slot 1
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
