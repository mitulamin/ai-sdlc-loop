---
name: validate-parameterise-encode
description: "Use when handling any external input or rendering output. Amalgamated skill for principle 6.3 (Secure)."
principles: ["6.3"]
principle: "6.3 Validate all external input at the boundary, treat external API responses as untrusted too, parameterise queries and encode output."
category: secure
aliases: ["2.11"]
status: "draft, untested"
licence: CC-BY-SA-4.0
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

## Related practices

Established practices this skill applies alongside its principle. Each has a self-check item and a reviewer check below.

- **Robustness principle** ([guide](../../guides/developer/developer-guide.md#postels-law)): be conservative in what you send. At a trust boundary, be strict in what you accept: validate against the schema and reject malformed input with the standard error, rather than guess what it meant, as RFC 9413 advises. Tolerance belongs only where the contract allows it, such as ignoring unknown fields. See also [2.12](../../principles/2.12.md).

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Is all external input, third-party responses included, validated against a schema at the boundary?
- [ ] Are all queries parameterised and all output encoded for its context, with no SQL or shell built by concatenation?
- [ ] Is invalid input rejected early, with the standard error shape?
- [ ] Robustness principle: is everything you send strictly conformant, and is malformed input at a trust boundary rejected rather than guessed at or silently repaired?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Attempt SQL, XSS and command injection on each input
- Find string-built queries
- Find a third-party response used without checks
- Robustness principle: find malformed input at a trust boundary that is accepted or silently repaired instead of rejected
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy security-and-hardening, agamm owasp-security, wshobson security-coder agents and xss-scan, plus Addy api-and-interface-design and ciembor release-it agree: validate input at the boundary, parameterise queries, encode output. Treating external API responses as untrusted, formerly principle 2.11, is merged in.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Secure
- Test order: slot 76
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
