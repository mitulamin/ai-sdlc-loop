---
name: challenge-terms-with-scenarios
description: "Use when reviewing a domain model or glossary. Amalgamated skill for principle 2.19 (Design and architecture)."
principles: ["2.19"]
principle: "2.19 Challenge terms with edge-case scenarios while designing"
category: design-and-architecture
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 3
link_only_sources: 0
---

# 2.19 Challenge terms with scenarios

Principle 2.19 (Design and architecture / Domain modelling): Challenge terms with edge-case scenarios while designing

## When to use

Reviewing a domain model or glossary.

## Producer: dos and don'ts

Do:
- Write 5-10 concrete edge scenarios (empty, duplicate, concurrent, expired)
- Walk each through the model and note where terms break
- Update glossary/model

Don't:
- Validate only with the happy path
- Accept vague terms that pass because no one tested them

## Steps

1. Generate scenarios
2. Walk them
3. Fix model/terms
4. Record scenarios as tests

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Produce one scenario the model cannot express
- Find a term two scenarios use differently
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Pocock domain-modeling ('invent edge-case scenarios'), grill-with-docs and ForceInjection ddd-model-review. Amalgam: the design reviewer runs concrete edge scenarios against the glossary and model.

## Sources

3 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Design
- Test order: slot 61 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
