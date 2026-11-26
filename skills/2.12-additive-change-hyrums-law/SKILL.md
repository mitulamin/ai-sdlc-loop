---
name: additive-change-hyrums-law
description: Use when changing any public API, CLI flag, file format or behaviour others may rely on. Amalgamated skill for principle 2.12 (Design and architecture).
principles: [2.12]
principle: "2.12 Prefer adding over changing; assume every observable behaviour is depended on (Hyrum's law)"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 18
link_only_sources: 0
---

# 2.12 Additive change hyrums law

Principle 2.12 (Design and architecture / API design): Prefer adding over changing; assume every observable behaviour is depended on (Hyrum's law)

## When to use

Changing any public API, CLI flag, file format or behaviour others may rely on.

## Producer: dos and don'ts

Do:
- Prefer adding a new field/endpoint over changing an old one
- Deprecate with a notice and timeline before removal
- Keep a compatibility test for old behaviour

Don't:
- Rename or change semantics in place
- Remove behaviour without a deprecation period

## Steps

1. Classify the change: additive or breaking
2. If breaking, design the additive path
3. Write compat tests
4. Reviewer lists who could break

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find an observable behaviour change not in the changelog
- Find a removed field with no deprecation
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy api-and-interface-design and deprecation-and-migration lead; wshobson ADRs and Anthropic version-delta-analyst touch compatibility. Amalgam: assume every observable behaviour is depended on; add, deprecate, then remove.

## Sources

18 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Design
- Test order: slot 54 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
