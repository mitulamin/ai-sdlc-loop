---
name: always-ask-never-tiers
description: "Use when setting up an agent's permissions for a project. Amalgamated skill for principle 6.2 (Secure)."
principles: ["6.2"]
principle: "6.2 Sort actions into always do, ask first and never do"
category: secure
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 1
link_only_sources: 0
---

# 6.2 Always ask never tiers

Principle 6.2 (Secure): Sort actions into always do, ask first and never do

## When to use

Setting up an agent's permissions for a project.

## Producer: dos and don'ts

Do:
- Write three lists: always (run tests), ask coordinator (add deps, migrations), never (push to main, touch secrets)
- Put them in the always-on rules file

Don't:
- Leave permissions implicit
- Route 'ask first' items to the human mid-loop

## Steps

1. Draft tiers
2. Add to rules
3. Enforce with hooks where possible
4. Reviewer audits transcript against tiers

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a never-action taken
- Find an ask-first action taken without asking
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy security-and-hardening only: sort agent actions into always do, ask first, never do. In the coordinator model 'ask first' goes to the coordinator, not the human.

## Sources

1 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Secure
- Test order: slot 75 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
