---
name: structured-logs
description: Use when adding any logging. Amalgamated skill for principle 5.8 (Debug and observe).
principles: [5.8]
principle: "5.8 Use structured logs with consistent levels"
aliases: []
status: draft, untested
licence: CC-BY-SA-4.0
sources: 6
link_only_sources: 0
---

# 5.8 Structured logs

Principle 5.8 (Debug and observe / Observability and logging): Use structured logs with consistent levels

## When to use

Adding any logging.

## Producer: dos and don'ts

Do:
- Log key-value/JSON events with a consistent schema
- Use levels consistently (error = needs action)
- Include context fields (ids, operation)

Don't:
- Log free-text strings with values concatenated
- Log at error for expected conditions

## Steps

1. Pick logger and schema
2. Add events at boundaries
3. Check levels
4. Reviewer parses logs as JSON

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find an unstructured log line
- Find an error-level log for a non-error
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy observability-and-instrumentation, ciembor release-it and wshobson python-observability: structured (JSON) logs with consistent levels.

## Sources

6 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE.md and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Debug
- Test order: slot 67 of 103
- Record results in ../../scorecard.csv (criteria in ../../README.md)
