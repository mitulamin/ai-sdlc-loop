---
name: bounded-contexts
description: "Use when a domain with distinct sub-areas (e.g. auth vs tasks vs billing). Amalgamated skill for principle 2.17 (Design and architecture)."
principles: ["2.17"]
principle: "2.17 Split the domain into bounded contexts and map how they relate"
category: design-and-architecture
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 2.17 Bounded contexts

Principle 2.17 (Design and architecture / Domain modelling): Split the domain into bounded contexts and map how they relate

## When to use

A domain with distinct sub-areas (e.g. auth vs tasks vs billing).

## Producer: dos and don'ts

Do:
- Name each context and what it owns
- Draw the context map (who calls whom, translation points)
- Keep models separate per context

Don't:
- Share one giant model across contexts
- Run full strategic DDD for a tiny app

## Steps

1. List subdomains
2. Define contexts and owners
3. Map relations
4. Reviewer finds leaked models

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a type used across contexts without translation
- Find a context with no clear owner
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

ciembor DDD and DDD Distilled, ForceInjection ddd-contexts/ddd-context-map/ddd-subdomains: split the domain into bounded contexts and map relationships. For small apps, the amalgam keeps it light: name contexts and their integration, skip heavy ceremony.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Design
- Test order: slot 59
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
