---
name: simple-by-default-opt-in-complexity
description: Use when designing a public API, config or CLI. Amalgamated skill for principle 2.14 (Design and architecture).
principles: [2.14]
principle: "2.14 Simple by default, complexity opt-in; avoid boolean flag parameters"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 3
link_only_sources: 0
---

# 2.14 Simple by default opt in complexity

Principle 2.14 (Design and architecture / API design): Simple by default, complexity opt-in; avoid boolean flag parameters

## When to use

Designing a public API, config or CLI.

## Producer: dos and don'ts

Do:
- Make the common case work with zero config and sensible defaults
- Put advanced options in a separate, opt-in layer
- Keep the primary constructor to 3-4 params

Don't:
- Force every caller to set options most never need
- Expose every knob at the top level

## Steps

1. List the common use case
2. Design the zero-config path
3. Layer advanced options
4. Reviewer writes the hello-world call

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Count steps for the common case
- Find an option every caller must set to the same value
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Stratos core (layered API: zero-config first layer, advanced layers opt-in), Ousterhout and Clean Code. PARTIAL overlap with 3.5 on flag parameters: proposed sharpening is to leave flag parameters to 3.5 and keep this about layered defaults.

## Sources

3 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Design
- Test order: slot 56 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
