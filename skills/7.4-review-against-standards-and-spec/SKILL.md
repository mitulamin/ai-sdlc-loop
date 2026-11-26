---
name: review-against-standards-and-spec
description: "Use when reviewing any change built from a spec. Amalgamated skill for principle 7.4 (Review and ship)."
principles: ["7.4"]
principle: "7.4 Review against both the standards and the spec, in parallel"
category: review-and-ship
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 4
link_only_sources: 0
---

# 7.4 Review against standards and spec

Principle 7.4 (Review and ship): Review against both the standards and the spec, in parallel

## When to use

Reviewing any change built from a spec.

## Producer: dos and don'ts

Do:
- Run a spec-compliance reviewer and a standards reviewer in parallel
- Spec reviewer checks every acceptance criterion and flags extras
- Merge findings

Don't:
- Review code quality only and miss that it built the wrong thing

## Steps

1. Dispatch both reviewers
2. Collect findings
3. Fix
4. Re-run the one whose area changed

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find an acceptance criterion not met
- Find built behaviour not in the spec
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Pocock code-review (standards and spec, in parallel) and Superpowers subagent-driven-development (spec reviewer then quality reviewer); Trail of Bits spec-compliance-checker. Amalgam: two parallel reviewers, spec and standards.

## Sources

4 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Review & ship
- Test order: slot 84 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
