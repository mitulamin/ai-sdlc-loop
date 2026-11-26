---
name: domain-glossary
description: "Use when starting a domain with business terms, or when names drift. Amalgamated skill for principle 2.16 (Design and architecture)."
principles: ["2.16"]
principle: "2.16 Keep a glossary of the domain language; one term per concept, used in code and tests"
category: design-and-architecture
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 2.16 Domain glossary

Principle 2.16 (Design and architecture / Domain modelling): Keep a glossary of the domain language; one term per concept, used in code and tests

## When to use

Starting a domain with business terms, or when names drift.

## Producer: dos and don'ts

Do:
- Keep a glossary file: term, definition, code name
- Use the same term in code, tests, UI and docs
- Resolve synonyms to one term

Don't:
- Let each agent invent names
- Use generic names (data, item, manager) for domain concepts

## Steps

1. Extract terms from spec
2. Write glossary
3. Inject into worker briefs
4. Reviewer greps for synonyms

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find two names for one concept
- Find a glossary term missing from code
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Pocock domain-modeling (CONTEXT.md glossary), ciembor DDD/Distilled (ubiquitous language) and ForceInjection ddd-contexts agree on one term per concept used in code and tests. Amalgam: a GLOSSARY section the coordinator injects into every worker's context.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Design
- Test order: slot 58
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
