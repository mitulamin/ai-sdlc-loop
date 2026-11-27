---
name: always-ask-never-tiers
description: "Use when setting up an agent's permissions for a project. Amalgamated skill for principle 6.2 (Secure)."
principles: ["6.2"]
principle: "6.2 Sort actions into always do, ask first and never do"
category: secure
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 6.2 Always ask never tiers

Principle 6.2 (Secure): Sort actions into always do, ask first and never do

## When to use

Setting up an agent's permissions for a project.

## Producer: dos and don'ts

Do:
- Write three lists: always (run tests), ask coordinator (add deps, migrations), never (push to main, touch secrets)
- Put them in the always-on rules file

Don't:
- Leave permissions implicit
- Route 'ask first' items to the human mid-loop

## Steps

1. Draft tiers
2. Add to rules
3. Enforce with hooks where possible
4. Reviewer audits transcript against tiers

## Related practices

Established practices this skill applies alongside its principle. Each has a self-check item and a reviewer check below.

- **Least privilege** ([guide](../../guides/developer/developer-guide.md#least-privilege)): give each agent, service, token and user role only the access its task needs, scoped and time-limited where the platform allows: read-only by default, write access only where the task writes. See also [6.4](../../principles/6.4.md).

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Are the always, ask-first and never lists written in the always-on rules file?
- [ ] Did you take no never-action, and no ask-first action without the coordinator's answer?
- [ ] Least privilege: does each agent, service account, token and user role have only the access and scopes its task uses?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a never-action taken
- Find an ask-first action taken without asking
- Least privilege: find a token, role, account or agent tool with more access than its task uses
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Addy security-and-hardening only: sort agent actions into always do, ask first, never do. In the coordinator model 'ask first' goes to the coordinator, not the human.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Secure
- Test order: slot 75
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
