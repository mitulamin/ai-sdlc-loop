---
name: audit-dependencies-before-release
description: "Use when before release, or when dependencies change. Amalgamated skill for principle 6.8 (Secure)."
principles: ["6.8"]
principle: "6.8 Audit dependencies against the lockfile before each release"
category: secure
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 9
link_only_sources: 0
---

# 6.8 Audit dependencies before release

Principle 6.8 (Secure): Audit dependencies against the lockfile before each release

## When to use

Before release, or when dependencies change.

## Producer: dos and don'ts

Do:
- Run the ecosystem audit (npm audit, pip-audit) against the lockfile
- Check new deps for maintenance and typosquatting
- Pin and commit the lockfile

Don't:
- Release with known high-severity vulnerabilities unaddressed
- Install unpinned packages in CI

## Steps

1. Run audit
2. Triage results
3. Upgrade or document
4. Reviewer re-runs the audit

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Re-run audit: any high/critical left?
- Find unpinned installs
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy security-and-hardening, Trail of Bits supply-chain-risk-auditor and wshobson deps-audit/security-dependencies: audit deps against the lockfile before each release.

## Sources

9 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App C (brownfield bug-fix and refactor)
- Phase: Secure
- Test order: slot 103 of 103
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
