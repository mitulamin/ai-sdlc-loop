---
name: independent-finding-verification
description: Use when before any security finding is reported. Amalgamated skill for principle 6.6 (Secure).
principles: [6.6]
principle: "6.6 Have a separate agent verify each finding before it is reported"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 13
link_only_sources: 2
---

# 6.6 Independent finding verification

Principle 6.6 (Secure): Have a separate agent verify each finding before it is reported

## When to use

Before any security finding is reported.

## Producer: dos and don'ts

Do:
- Dispatch a fresh verifier with only the claim and the code
- Verifier tries to prove the finding wrong
- Report only verified findings

Don't:
- Let the finder verify their own finding
- Share the finder's reasoning with the verifier

## Steps

1. Finder writes claim
2. Fresh verifier attacks it
3. Keep verified, drop refuted
4. Log both

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Check verifier context excluded finder reasoning
- Count findings dropped as false positives
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Cloudflare security-audit runs separate hunter and verifier agents, each with its own working folders, and asks for an independent verifier when a finding is replaced; Trail of Bits fp-check does a structured false-positive check. Amalgam: a fresh verifier tries to refute each finding before it is reported. Giving the verifier only the claim, the code and the reproduction steps, not the finder's reasoning, is our own hardening of that idea, not something the sources prescribe.

## Sources

13 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [anthropics/attack-surface-verifier](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/agents/attack-surface-verifier.md) (Proprietary (Anthropic claude-security licence))
- [anthropics/scan-verifier](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/agents/scan-verifier.md) (Proprietary (Anthropic claude-security licence))

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Secure
- Test order: slot 79 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
