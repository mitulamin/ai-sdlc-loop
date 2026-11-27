---
name: comments-explain-why
description: "Use when writing or reviewing comments and docstrings. Amalgamated skill for principle 3.7 (Code craft)."
principles: ["3.7"]
principle: "3.7 Comments explain why, never narrate what"
category: code-craft
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 3.7 Comments explain why

Principle 3.7 (Code craft): Comments explain why, never narrate what

## When to use

Writing or reviewing comments and docstrings.

## Producer: dos and don'ts

Do:
- Comment why: constraints, trade-offs, links to issues
- Keep public interface docs accurate
- Delete comments that restate the code

Don't:
- Narrate what each line does
- Leave commented-out code or stale TODOs

## Steps

1. Write code clear enough to skip 'what' comments
2. Add 'why' where non-obvious
3. Comment analyzer checks accuracy
4. Remove noise

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Does every comment explain why (a constraint, a trade-off, a link), not narrate what the code does?
- [ ] Are public interface docs accurate, with no commented-out code or stale TODOs left behind?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a comment that restates code
- Find a comment that no longer matches the code
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

ciembor clean-code and Ousterhout, plus Anthropic pr-review-toolkit comment-analyzer (finds stale or narrating comments). Amalgam: comments carry intent, constraints and gotchas only.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App A (CLI tool)
- Phase: Build
- Test order: slot 23
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
