---
name: command-query-separation
description: "Use when writing functions that read or mutate state. Amalgamated skill for principle 3.6 (Code craft)."
principles: ["3.6"]
principle: "3.6 Separate commands from queries; no hidden side effects"
category: code-craft
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 3.6 Command query separation

Principle 3.6 (Code craft): Separate commands from queries; no hidden side effects

## When to use

Writing functions that read or mutate state.

## Producer: dos and don'ts

Do:
- Name commands as verbs that return nothing (or a status)
- Make queries side-effect free
- Make side effects visible in names

Don't:
- Have a getter that writes, caches globally or logs to external systems silently
- Hide mutation in a function named like a query

## Steps

1. Classify each function
2. Split mixed ones
3. Test queries are pure
4. Reviewer hunts hidden side effects

## Related practices

Established practices this skill applies alongside its principle. Each has a self-check item and a reviewer check below.

- **Principle of least astonishment** ([guide](../../guides/developer/quality-principles.md#principle-of-least-astonishment)): names, defaults and errors behave as a careful caller would expect: a getter does not write, similar calls behave alike, and errors share one shape. See also [2.10](../../principles/2.10.md).

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Is each function either a command (named as a verb, returning nothing or a status) or a query with no side effects?
- [ ] Is every side effect visible in the function's name?
- [ ] Principle of least astonishment: would a careful caller predict what each name, default and error does, with no surprise writes and no difference between similar calls?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a query that mutates
- Find a side effect not implied by the name
- Principle of least astonishment: find a name, default or error that behaves differently from what a careful caller would expect
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

ciembor clean-code and pragmatic-programmer: a function either changes state or returns data, not both; no hidden side effects. Mostly a reviewer rule.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App A (CLI tool)
- Phase: Build
- Test order: slot 22
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
