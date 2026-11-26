---
name: contract-first
description: "Use when before building any API, CLI interface or module boundary other code will call. Amalgamated skill for principle 2.9 (Design and architecture)."
principles: ["2.9"]
principle: "2.9 Define the contract first"
category: design-and-architecture
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 11
link_only_sources: 0
---

# 2.9 Contract first

Principle 2.9 (Design and architecture / API design): Define the contract first

## When to use

Before building any API, CLI interface or module boundary other code will call.

## Producer: dos and don'ts

Do:
- Write the contract (OpenAPI, type signatures or CLI usage) first
- Review it with a consumer's eye before implementing
- Generate or check tests against the contract

Don't:
- Let the implementation define the API by accident
- Change the contract silently during build

## Steps

1. Draft the contract
2. Consumer-minded reviewer critiques it
3. Freeze v1
4. Implement and contract-test

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find an endpoint or flag in code that is not in the contract
- Find contract fields the code ignores
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy api-and-interface-design and wshobson api-design-principles/openapi-spec-generation agree: define the interface (OpenAPI or types) before implementation. Amalgam: the contract is the first artefact and the tests' reference.

## Sources

11 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Design
- Test order: slot 52 of 103
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
