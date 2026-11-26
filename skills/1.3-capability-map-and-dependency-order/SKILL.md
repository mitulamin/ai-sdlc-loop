---
name: capability-map-and-dependency-order
description: Use when after the spec, before any implementation of a multi-part feature or app. Amalgamated skill for principle 1.3 (Plan and specify).
principles: [1.3]
principle: "1.3 Break big asks into a capability map and build modules in dependency order"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 17
link_only_sources: 0
---

# 1.3 Capability map and dependency order

Principle 1.3 (Plan and specify): Break big asks into a capability map and build modules in dependency order

## When to use

After the spec, before any implementation of a multi-part feature or app.

## Producer: dos and don'ts

Do:
- List capabilities (what the system can do), then the modules each needs
- Order tasks blockers-first; mark which can run in parallel
- Make each task a thin vertical slice with an acceptance check
- Write tasks.md the implementer agents can pick up cold

Don't:
- Plan horizontally (all models, then all routes, then all UI)
- Create tasks with no verifiable done condition
- Plan beyond what one run can deliver without a wayfinder milestone

## Steps

1. Derive capabilities from spec acceptance criteria
2. Map capability to modules and dependencies
3. Emit tasks.md in dependency order with checks
4. Plan reviewer checks ordering, gaps and parallel safety

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a task that depends on a later task
- Find an acceptance criterion no task covers
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy planning-and-task-breakdown, Pocock to-tickets/wayfinder, spec-kit tasks and cc-sdd tasks all break work into ordered units; Pocock insists on tracer-bullet vertical slices, spec-kit on dependency-ordered tasks.md. Amalgam: a capability map, then tasks in dependency order where each task is a vertical slice with its own check.

## Sources

17 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Plan
- Test order: slot 45 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
