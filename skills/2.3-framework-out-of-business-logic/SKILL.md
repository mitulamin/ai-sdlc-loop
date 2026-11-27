---
name: framework-out-of-business-logic
description: "Use when structuring a web app or service with a framework, ORM or vendor SDK. Amalgamated skill for principle 2.3 (Design and architecture)."
principles: ["2.3"]
principle: "2.3 Keep framework, persistence and vendor details out of business logic, behind adapters"
category: design-and-architecture
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
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

## Related practices

Established practices this skill applies alongside its principle. Each has a self-check item and a reviewer check below.

- **Dependency inversion principle** (SOLID; [guide](../../guides/developer/quality-principles.md#dependency-inversion-principle)): the domain owns the interfaces it needs (a repository, a clock, a payment port), and the adapters for the framework, database or vendor implement them, so source dependencies point inward. This is programming to an interface, not an implementation; add the interface only when 2.5's test is met, a second implementation or a real test need. See also [2.2](../../principles/2.2.md), [2.5](../../principles/2.5.md).
- **Twelve-factor app** ([guide](../../guides/developer/quality-principles.md#operability)): for a service, keep config in the environment, treat databases, queues and caches as attached resources swapped by config, write logs to standard output as event streams, keep processes stateless and disposable, and keep build, release and run separate. It is a method for services, not a scorecard: apply the factors that fit. See also [6.4](../../principles/6.4.md), [5.8](../../principles/5.8.md).
- **Acyclic dependencies principle** ([guide](../../guides/developer/quality-principles.md#acyclic-dependencies-principle)): keep the dependency graph of modules and packages free of cycles, so each can be built, tested and released on its own. Break a cycle by moving the shared piece into a module both depend on, or by dependency inversion so one side depends on an abstraction; a cycle checker in CI keeps it that way. See also [2.4](../../principles/2.4.md).

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Are domain modules free of framework, ORM and vendor SDK imports?
- [ ] Do database, HTTP and vendor calls go through adapters, with framework types mapped to domain types at the edge?
- [ ] Does every port you added have a second implementation or a real test need?
- [ ] Dependency inversion principle: does the domain own each interface it depends on, with the adapters depending on the domain and never the reverse?
- [ ] Twelve-factor app: for a service, is config read from the environment, are backing services attached through config, do logs go to standard output, and is no state kept in the process that must survive a restart?
- [ ] Acyclic dependencies principle: is the dependency graph of the modules you touched free of cycles?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a domain file importing the framework or ORM
- Find business logic inside a handler
- Dependency inversion principle: find a domain module that imports a concrete adapter, or depends on an interface the adapter owns
- Twelve-factor app: find config or a backing-service address hard-coded in the code, or process state that is lost on restart
- Acyclic dependencies principle: find a cycle in the module or package dependency graph
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

ciembor clean-architecture, PoEAA and DDD rules agree: keep framework, persistence and vendor code at the edges behind adapters; wshobson architecture-patterns repeats hexagonal/ports-and-adapters. Amalgam keeps it pragmatic: adapters at real boundaries, not ceremonial layers (see 2.5).

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Design
- Test order: slot 46
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
