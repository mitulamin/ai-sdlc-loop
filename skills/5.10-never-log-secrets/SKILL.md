---
name: never-log-secrets
description: Use when any logging, tracing, error reporting or debug output. Amalgamated skill for principle 5.10 (Debug and observe).
principles: [5.10, 5.6]
principle: "5.10 Never log or display secrets, tokens or full personal data, including in debug output."
aliases: [5.6]
status: draft, untested
licence: CC-BY-SA-4.0
sources: 8
link_only_sources: 2
---

# 5.10 Never log secrets

Principle 5.10 (Debug and observe / Observability and logging): Never log or display secrets, tokens or full personal data, including in debug output.

Merged duplicates (aliases): 5.6. See MERGES.md.

## When to use

Any logging, tracing, error reporting or debug output.

## Producer: dos and don'ts

Do:
- Never log or display tokens, passwords, keys or full personal data
- Redact at the logger with an allow-list of fields
- Redact debug output, captured artifacts and transcripts before showing them
- Quote only the lines that carry the signal

Don't:
- Log or paste whole request bodies, headers or environments
- Rely on remembering to redact by hand

## Steps

1. Configure redaction at the logger
2. Add a test that logs a fake secret
3. Redact captured debug output before sharing
4. Reviewer greps logs and output

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a secret or personal data in logs, traces or debug output
- Find a log statement that dumps whole objects
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy observability-and-instrumentation and security-and-hardening, ciembor release-it, and the dash0 and ollygarden OpenTelemetry collector guidance on redaction agree; Pocock diagnosing-bugs and Superpowers diagnosing-superpowers add redaction of debug output and shared transcripts. Redacting secrets in debug output, formerly principle 5.6, is merged in.

## Sources

8 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [anthropics/scan-redactor](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/agents/scan-redactor.md) (Proprietary (Anthropic claude-security licence))
- [anthropics/attack-surface-redactor](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/agents/attack-surface-redactor.md) (Proprietary (Anthropic claude-security licence))

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Secure
- Test order: slot 73 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
