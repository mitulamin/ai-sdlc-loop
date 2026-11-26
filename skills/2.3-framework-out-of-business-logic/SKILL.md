---
name: framework-out-of-business-logic
description: Use when structuring a web app or service with a framework, ORM or vendor SDK. Amalgamated skill for principle 2.3 (Design and architecture).
principles: [2.3]
principle: "2.3 Keep framework, persistence and vendor details out of business logic, behind adapters"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 5
link_only_sources: 0
---

# 2.3 Framework out of business logic

Principle 2.3 (Design and architecture): Keep framework, persistence and vendor details out of business logic, behind adapters

## When to use

Structuring a web app or service with a framework, ORM or vendor SDK.

## Producer: dos and don'ts

Do:
- Keep domain rules in plain modules with no framework imports
- Wrap DB, HTTP and vendor SDKs in adapters the domain calls through an interface
- Map framework types to domain types at the edge

Don't:
- Put business rules in controllers, ORM models or route handlers
- Add ports for things that have one implementation and no test need

## Steps

1. Identify domain rules
2. Place them in a framework-free module
3. Add adapters for persistence and external calls
4. Reviewer greps domain code for framework imports

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a domain file importing the framework or ORM
- Find business logic inside a handler
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

ciembor clean-architecture, PoEAA and DDD rules agree: keep framework, persistence and vendor code at the edges behind adapters; wshobson architecture-patterns repeats hexagonal/ports-and-adapters. Amalgam keeps it pragmatic: adapters at real boundaries, not ceremonial layers (see 2.5).

## Sources

5 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Design
- Test order: slot 46 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
