---
name: reports-to-files
description: "Use when any subagent producing findings or reports. Amalgamated skill for principle 8.8 (Agent operations)."
principles: ["8.8"]
principle: "8.8 Write reports to files, not into the chat"
category: agent-operations
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
sources: 5
link_only_sources: 0
---

# 8.8 Reports to files

Principle 8.8 (Agent operations): Write reports to files, not into the chat

## When to use

Any subagent producing findings or reports.

## Producer: dos and don'ts

Do:
- Write the report to a named file in the run folder
- Return the path and a 3-line summary

Don't:
- Paste long reports into the coordinator's context

## Steps

1. Write file
2. Return path+summary
3. Coordinator reads on demand

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a long report pasted inline
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

EGM review and synthesizer: write stage reports to files, not into the chat. Keeps coordinator context lean and creates an audit trail for Learn.

## Sources

5 licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: All three runs (harness and Learn)
- Phase: Harness
- Test order: slot 8 of 103
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
