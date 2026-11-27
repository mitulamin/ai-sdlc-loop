---
name: orchestration-vs-services
description: "Use when adding a feature that coordinates several operations (e.g. create task + notify + audit). Amalgamated skill for principle 2.4 (Design and architecture)."
principles: ["2.4"]
principle: "2.4 Separate orchestration (business rules) from reusable service operations"
category: design-and-architecture
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 2.4 Orchestration vs services

Principle 2.4 (Design and architecture): Separate orchestration (business rules) from reusable service operations

## When to use

Adding a feature that coordinates several operations (e.g. create task + notify + audit).

## Producer: dos and don'ts

Do:
- Put each use case's flow in one function that calls the domain and shared services
- Extract shared mechanics (persistence, notification, formatting) into a service once two use cases need them
- Keep use-case rules out of the shared services
- Keep dependencies pointing one way: API, then use case, then service, then repository

Don't:
- Let services call each other into a web of hidden flows
- Extract a service for a single caller
- Let handlers or repositories hold the use-case rules

## Steps

1. Write the use-case function
2. Spot mechanics repeated across use cases
3. Extract them into a service
4. Reviewer checks the rules still live in the use-case function

## Related practices

Established practices this skill applies alongside its principle. Each has a self-check item and a reviewer check below.

- **Unix philosophy** ([guide](../../guides/developer/developer-guide.md#unix-philosophy)): make each service operation do one thing well, with a plain input and output, so use cases compose operations instead of one operation growing modes and flags. See also [2.1](../../principles/2.1.md), [3.5](../../principles/3.5.md).

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Does each use case's flow live in one function that calls the domain and the shared services?
- [ ] Are use-case rules kept out of shared services, handlers and repositories?
- [ ] Do dependencies point one way (API, use case, service, repository), and does every shared service have more than one caller?
- [ ] Unix philosophy: does each service operation do one thing well with a plain input and output, so use cases compose operations rather than switch one by mode?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a use-case rule hidden in a shared service
- Find a service with a single caller
- Find a dependency pointing the wrong way
- Unix philosophy: find a service operation that switches between several jobs by a mode or flag
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Fowler's PoEAA and Vernon's Implementing DDD (both via the ciembor rule books) describe a service or application layer that coordinates use cases over the domain; Clean Architecture (ciembor) calls these use cases; wshobson python-design-patterns keeps the dependency pointing API to service to repository; wshobson full-stack-feature lists the service layer's responsibilities. Amalgam: one function per use case holds the flow, shared technical mechanics are extracted into services only when two use cases need them. Evidence from clean sources is thin here, so this is a good candidate to drop or merge after testing.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [michaelshimeles/code-structure](https://github.com/michaelshimeles/rstack/blob/8ad39442fd64cf2b407249024c5310dda90f6283/code-structure/SKILL.md) (No licence)
- [michaelshimeles/AGENTS.md workflow template](https://github.com/michaelshimeles/rstack/blob/8ad39442fd64cf2b407249024c5310dda90f6283/AGENTS.md) (No licence)

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Design
- Test order: slot 47
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
