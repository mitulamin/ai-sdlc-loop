---
name: validate-parameterise-encode
description: Use when handling any external input or rendering output. Amalgamated skill for principle 6.3 (Secure).
principles: [6.3, 2.11]
principle: "6.3 Validate all external input at the boundary, treat external API responses as untrusted too, parameterise queries and encode output."
aliases: [2.11]
status: draft, untested
licence: CC-BY-SA-4.0
sources: 16
link_only_sources: 0
---

# 6.3 Validate parameterise encode

Principle 6.3 (Secure): Validate all external input at the boundary, treat external API responses as untrusted too, parameterise queries and encode output.

Merged duplicates (aliases): 2.11. See MERGES.md.

## When to use

Handling any external input or rendering output.

## Producer: dos and don'ts

Do:
- Validate all external input at the boundary with a schema
- Treat external API and third-party responses as untrusted and validate them the same way
- Use parameterised queries only
- Encode output for its context (HTML, shell, SQL)
- Reject early with the standard error shape

Don't:
- Build SQL or shell commands by string concatenation
- Trust client-side validation
- Trust upstream payloads
- Validate only deep inside business logic

## Steps

1. List entry points and sinks
2. Add schema validation and parameterisation
3. Add injection and malformed-input tests
4. Reviewer attempts injection and fuzzes the boundary

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Attempt SQL, XSS and command injection on each input
- Find string-built queries
- Find a third-party response used without checks
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy security-and-hardening, agamm owasp-security, wshobson security-coder agents and xss-scan, plus Addy api-and-interface-design and ciembor release-it agree: validate input at the boundary, parameterise queries, encode output. Treating external API responses as untrusted, formerly principle 2.11, is merged in.

## Sources

16 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Secure
- Test order: slot 76 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
