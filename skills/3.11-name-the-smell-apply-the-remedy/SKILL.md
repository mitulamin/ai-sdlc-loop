---
name: name-the-smell-apply-the-remedy
description: "Use when reviewing or cleaning code that feels wrong. Amalgamated skill for principle 3.11 (Code craft)."
principles: ["3.11"]
principle: "3.11 Name the code smell and apply its standard remedy"
category: code-craft
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 3.11 Name the smell apply the remedy

Principle 3.11 (Code craft): Name the code smell and apply its standard remedy

## When to use

Reviewing or cleaning code that feels wrong.

## Producer: dos and don'ts

Do:
- Name the smell (long method, feature envy, shotgun surgery...)
- Apply its catalogued remedy
- Cite the smell in the review comment or commit

Don't:
- Rewrite by taste without naming the problem
- Fix smells outside the task scope (log them instead)

## Steps

1. Scan the area
2. Name smells
3. Apply remedies under tests
4. Reviewer checks the smell is gone

## Related practices

Established practices this skill applies alongside its principle. Each has a self-check item and a reviewer check below.

- **DRY and the rule of three** ([guide](../../guides/developer/quality-principles.md#dry)): each piece of knowledge (a rule, a format, a constant) has one authoritative home, so one change of intent edits one place. Similar-looking code is only a clue: tolerate a second copy and extract on the third, which is 2.5's duplicate-twice brake. Name the smell (duplicated code, shotgun surgery) and apply its remedy. See also [2.5](../../principles/2.5.md).
- **Law of Demeter** ([guide](../../guides/developer/quality-principles.md#law-of-demeter)): a method talks to itself, its arguments, the objects it creates and its direct collaborators, not through a chain such as `order.customer().address().zip()`. The smell is message chains; the remedy is to hide the delegate or move the behaviour to the object that has the data. A short fluent chain over one value is fine. See also [2.1](../../principles/2.1.md).

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Did you name each smell you fixed and apply its catalogued remedy, citing it in the commit or review?
- [ ] Did you log, rather than fix, the smells outside the task's scope?
- [ ] DRY and the rule of three: does each piece of knowledge have one authoritative home, with a second copy tolerated and shared code extracted only at the third?
- [ ] Law of Demeter: does each method talk only to itself, its arguments, objects it creates and its direct collaborators, with no chain reaching through another object's internals?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a smell the change introduced
- Find a remedy that is not the catalogued one without reason
- DRY and the rule of three: find one piece of knowledge kept in two places that must change together, or a shared abstraction extracted from fewer than three copies
- Law of Demeter: find a call chain that reaches through one object into another's internals
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

refactoring-guru and Refactoring (ciembor), Pocock improve-codebase-architecture, sanyuan code-review-expert and brooks-lint brooks-review: identify the named smell and apply its standard remedy, so fixes are consistent and reviewable.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App C (brownfield bug-fix and refactor)
- Phase: Build
- Test order: slot 97
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
