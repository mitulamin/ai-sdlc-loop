---
name: no-secrets-in-code
description: Use when configuring credentials or writing client-side checks. Amalgamated skill for principle 6.4 (Secure).
principles: [6.4]
principle: "6.4 Never commit secrets; never trust client-side validation"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 5
link_only_sources: 0
---

# 6.4 No secrets in code

Principle 6.4 (Secure): Never commit secrets; never trust client-side validation

## When to use

Configuring credentials or writing client-side checks.

## Producer: dos and don'ts

Do:
- Load secrets from env or a secrets manager
- Add .env to .gitignore and a secret scanner to CI
- Re-validate everything server-side

Don't:
- Hard-code keys, even in tests
- Rely on browser validation for security

## Steps

1. Set up secret loading
2. Add scanning
3. Server-side checks
4. Reviewer scans history

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Run a secret scan on the diff and history
- Bypass the client and hit the API directly
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy security-and-hardening and wshobson secrets-management: never commit secrets; never trust client-side validation.

## Sources

5 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Secure
- Test order: slot 77 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
