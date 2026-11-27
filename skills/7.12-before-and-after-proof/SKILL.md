---
name: before-and-after-proof
description: "Use when shipping any user-visible change: UI, CLI output, generated files. Amalgamated skill for principle 7.12 (Review and ship)."
principles: ["7.12"]
principle: "7.12 Attach before-and-after proof to each change you ship, such as test output, screenshots or measurements, so a reviewer can see the effect"
category: review-and-ship
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 7.12 Before and after proof

Principle 7.12 (Review and ship): Attach before-and-after proof to each change you ship, such as test output, screenshots or measurements, so a reviewer can see the effect

## When to use

Shipping any user-visible change: UI, CLI output, generated files.

## Producer: dos and don'ts

Do:
- Capture the 'before' first, on the base branch, at the start of the task
- Show the same screen, device or viewport, and state before and after; crop to the part that changed
- For non-UI changes show one short snippet or a before and after output pair, not a tour of every file
- Capture in a clean environment with a throwaway account; check the frame for private data
- Host images off the main branch (a non-merging branch) with a fresh path per capture
- Put the proof near the top of the PR body, and say when a state had to be set up with seed data
- For a new feature with no before, show the after on its own and say it is new

Don't:
- Ship a visible change with no proof
- Capture from a personal browser profile or device
- Overwrite an image at a path that has already been rendered (caches serve the stale picture)
- Commit screenshots to the main history
- Use whole-page screenshots when only one part changed

## Steps

1. Decide what the change touches (screens, states, output)
2. Capture the before on the base branch
3. Make the change and capture the after the same way
4. Publish the pair in the PR body, proof first
5. Reviewer checks the proof matches the change described

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Does each visible change have a before-and-after pair of the same screen, state and size, cropped to what changed, or an after alone marked as new?
- [ ] Was the proof captured in a clean environment, checked for private data, hosted off the main history, and put near the top of the PR body?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Check the before and after really show the same screen, state and size
- Find a visible change in the diff with no pair
- Find private data in a screenshot
- Find a claimed fix whose after shows the old behaviour
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

The MIT-licensed source skills agree: a UI change is shown with before and after screenshots of the same screen, device and state, and the 'before' is captured first; other changes are shown by one short snippet. They differ in mechanism: one hosts images on a non-merging branch with a fresh path per capture and a fixed PR body; one gets the 'before' by putting the changed files back to the base branch while the dev server hot-reloads; one pictures only the part that changed, on desktop and phone and in dark mode, and marks what changed; one uses scripts that capture base and feature branches and write a comparison report. Partial overlap with 4.9, which is the evidence for the agent itself.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Further reading (link only)

These sources have no usable licence for copying or adapting, so nothing in this skill is taken from them. Read them at the source:

- [michaelshimeles/before-and-after](https://github.com/michaelshimeles/rstack/blob/8ad39442fd64cf2b407249024c5310dda90f6283/before-and-after/SKILL.md) (PolyForm-Shield-1.0.0)
- [michaelshimeles/AGENTS.md workflow template](https://github.com/michaelshimeles/rstack/blob/8ad39442fd64cf2b407249024c5310dda90f6283/AGENTS.md) (No licence)
- [vercel-labs/before-and-after (Vercel Labs)](https://github.com/vercel-labs/before-and-after/blob/8306d34f459b6704e08e6adb5829fcddb0dc3557/skill/SKILL.md) (PolyForm Shield 1.0.0)

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Review & ship
- Test order: slot 92
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
