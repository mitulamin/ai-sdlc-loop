---
name: threat-model-first
description: "Use when before building auth, data handling or anything exposed to users. Amalgamated skill for principle 6.1 (Secure)."
principles: ["6.1"]
principle: "6.1 Threat-model before hardening"
category: secure
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 6.1 Threat model first

Principle 6.1 (Secure): Threat-model before hardening

## When to use

Before building auth, data handling or anything exposed to users.

## Producer: dos and don'ts

Do:
- List assets, actors, entry points and trust boundaries
- Run STRIDE over each boundary
- Rank threats and pick mitigations

Don't:
- Harden at random without knowing what you protect
- Write a model and never use it

## Steps

1. Draw data flow
2. STRIDE
3. Rank
4. Turn top threats into tasks and tests

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find an entry point missing from the model
- Find a top threat with no mitigation task
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy security-and-hardening ('threat model first'), wshobson threat-modeling-expert, stride-analysis-patterns and security-requirement-extraction, and Trail of Bits adversarial-modeler agree: list assets, entry points and trust boundaries, and rank threats before hardening.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [anthropics/threat-model](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/skills/threat-model/SKILL.md) (Proprietary (Anthropic claude-security licence))
- [anthropics/attack-surface-analysis](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/skills/attack-surface-analysis/SKILL.md) (Proprietary (Anthropic claude-security licence))
- [anthropics/attack-surface-verifier](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/agents/attack-surface-verifier.md) (Proprietary (Anthropic claude-security licence))
- [anthropics/attack-surface-stage](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/agents/attack-surface-stage.md) (Proprietary (Anthropic claude-security licence))
- [anthropics/attack-surface-redactor](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/agents/attack-surface-redactor.md) (Proprietary (Anthropic claude-security licence))
- [anthropics/claude-security](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/skills/claude-security/SKILL.md) (Proprietary (Anthropic claude-security licence))

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Secure
- Test order: slot 74
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
