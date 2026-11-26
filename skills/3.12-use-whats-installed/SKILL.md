---
name: use-whats-installed
description: "Use whenever a new package or library seems needed. Amalgamated skill for principle 3.12 (Code craft)."
principles: ["3.12"]
principle: "3.12 Use what's installed; never add a dependency for a few lines"
category: code-craft
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 2
link_only_sources: 0
---

# 3.12 Use whats installed

Principle 3.12 (Code craft): Use what's installed; never add a dependency for a few lines

## When to use

Whenever a new package or library seems needed.

## Producer: dos and don'ts

Do:
- Check stdlib, platform features and existing deps first
- Justify any new dependency in one line (size, maintenance, licence)
- Prefer a few lines of own code over a tiny package

Don't:
- Add a package for a one-liner
- Add a second library that duplicates an installed one

## Steps

1. Search existing deps
2. Decide
3. Justify new deps in the PR
4. Reviewer challenges every added dependency

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a new dependency replaceable by stdlib or an existing one
- Check licence and maintenance of new deps
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

ponytail and ponytail-audit are the source: stdlib, platform, or an installed dependency before anything new; never add a dependency for a few lines. Shares its file with 3.13 but is a separate rule.

## Sources

2 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App A (CLI tool)
- Phase: Build
- Test order: slot 25 of 103
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
