---
name: review-suites-for-mock-abuse
description: "Use when reviewing a test suite or a PR's tests. Amalgamated skill for principle 4.6 (Verify)."
principles: ["4.6"]
principle: "4.6 Review suites for mock abuse, brittleness and coverage illusions; coverage is not quality"
category: verify
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 4.6 Review suites for mock abuse

Principle 4.6 (Verify): Review suites for mock abuse, brittleness and coverage illusions; coverage is not quality

## When to use

Reviewing a test suite or a PR's tests.

## Producer: dos and don'ts

Do:
- Mock only at seams (system boundaries)
- Check tests would fail if the behaviour broke (mutation thinking)
- Treat coverage as a hint, not proof

Don't:
- Mock the unit under test's collaborators everywhere
- Accept high coverage as quality

## Steps

1. Scan tests for mocks
2. Mentally break the code: which tests fail?
3. List brittle/illusory tests
4. Fix or delete

## Related practices

Established practices this skill applies alongside its principle. Each has a self-check item and a reviewer check below.

- **Goodhart's law** ([guide](../../guides/developer/quality-principles.md#goodharts-law)): a measure that becomes a target stops being a good measure. Coverage, test counts and pass rates can all be met without the behaviour being checked, so treat each as a question and pair it with the outcome it stands for: tests that fail when the behaviour breaks. See also [5.7](../../principles/5.7.md).

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Are mocks used only at seams, never for internal modules?
- [ ] Would each test fail if the behaviour it covers were broken or deleted?
- [ ] Is every quality claim backed by tests that can fail, with coverage treated as a hint?
- [ ] Goodhart's law: is every metric you report, such as coverage, a test count or a pass rate, backed by the outcome it stands for rather than raised for its own sake?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Find a test that passes with the implementation deleted
- Find mocks of internal modules
- Goodhart's law: find a metric raised without the outcome it stands for, such as coverage from tests that assert nothing
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

brooks-lint brooks-test (both copies), Pocock tdd/mocking.md, Addy TDD and Anthropic pr-test-analyzer: review suites for over-mocking, brittleness and coverage illusions. Amalgam: an adversarial test-suite reviewer.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App C (brownfield bug-fix and refactor)
- Phase: Verify
- Test order: slot 98
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
