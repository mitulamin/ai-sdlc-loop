---
name: correlation-ids
description: "Use when handling requests that cross functions, services or jobs. Amalgamated skill for principle 5.9 (Debug and observe)."
principles: ["5.9"]
principle: "5.9 Create a correlation ID at the boundary and attach it to every log line"
category: debug-and-observe
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 5.9 Correlation ids

Principle 5.9 (Debug and observe / Observability and logging): Create a correlation ID at the boundary and attach it to every log line

## When to use

Handling requests that cross functions, services or jobs.

## Producer: dos and don'ts

Do:
- Create or accept a correlation id at the entry point
- Propagate it through calls and jobs
- Include it in every log line and error response

Don't:
- Generate new ids mid-flow
- Drop the id at async boundaries

## Steps

1. Add middleware
2. Propagate
3. Log it
4. Reviewer follows one request through logs

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Is a correlation id created or accepted at every entry point?
- [ ] Is it carried through calls, jobs and async hops into every log line and error response?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Pick one request: can you trace all its logs?
- Find an async hop that loses the id
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy observability, ciembor release-it and OTel semantic conventions (ollygarden): create a correlation/trace id at the boundary and attach it everywhere.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Debug
- Test order: slot 68
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
