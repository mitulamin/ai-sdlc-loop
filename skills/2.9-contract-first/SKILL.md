---
name: contract-first
description: "Use when before building any API, CLI interface or module boundary other code will call. Amalgamated skill for principle 2.9 (Design and architecture)."
principles: ["2.9"]
principle: "2.9 Define the contract first"
category: design-and-architecture
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
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

## Related practices

Established practices this skill applies alongside its principle. Each has a self-check item and a reviewer check below.

- **Design by contract** ([guide](../../guides/developer/quality-principles.md#design-by-contract)): for each operation, state its preconditions, postconditions and invariants in the contract, and enforce them with checks or tests. A comment is not a contract unless something checks it. See also [2.15](../../principles/2.15.md).

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Was the contract (API schema, type signatures or CLI usage) written before the implementation?
- [ ] Does every endpoint, flag and field in the code appear in the contract, and every contract field in the code?
- [ ] Are tests generated from, or checked against, the contract?
- [ ] Design by contract: does each operation state its preconditions, postconditions and invariants, each enforced by code or a test?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find an endpoint or flag in code that is not in the contract
- Find contract fields the code ignores
- Design by contract: find a stated precondition, postcondition or invariant that no code or test enforces
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy api-and-interface-design and wshobson api-design-principles/openapi-spec-generation agree: define the interface (OpenAPI or types) before implementation. Amalgam: the contract is the first artefact and the tests' reference.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Design
- Test order: slot 52
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
