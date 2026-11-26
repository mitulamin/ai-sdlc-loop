---
name: report-real-trust-boundary-issues
description: Use when running a security review. Amalgamated skill for principle 6.5 (Secure).
principles: [6.5]
principle: "6.5 Report only issues that cross a real trust boundary, with evidence, a safe reproduction and the smallest fix"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 21
link_only_sources: 2
---

# 6.5 Report real trust boundary issues

Principle 6.5 (Secure): Report only issues that cross a real trust boundary, with evidence, a safe reproduction and the smallest fix

## When to use

Running a security review.

## Producer: dos and don'ts

Do:
- Report only issues that cross a real trust boundary
- Give source evidence, a safe reproduction, priority and the smallest fix

Don't:
- Report theoretical issues with no reachable path
- Dump scanner output unfiltered

## Steps

1. Map boundaries
2. Find candidates
3. Prove reachability
4. Write finding with fix

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Try to show the finding is unreachable
- Check every finding has a reproduction
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Cloudflare security-audit (real trust boundary, evidence, safe reproduction, smallest fix) and Trail of Bits exploitability-verifier/fp-check/poc generator. Amalgam: findings must cross a real boundary and carry evidence.

## Sources

21 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [anthropics/attack-surface-analysis](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/skills/attack-surface-analysis/SKILL.md) (Proprietary (Anthropic claude-security licence))
- [anthropics/scan-verifier](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/agents/scan-verifier.md) (Proprietary (Anthropic claude-security licence))

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Secure
- Test order: slot 78 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
