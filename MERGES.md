# Merges: 108 principles to 103

Approved by Mitul on 26 Nov 2026. A duplicate was merged into its survivor. IDs are not renumbered: the old ID stays valid as an alias (see `data/principles.json`, `aliases`). Nothing from the duplicates was lost: dos, don'ts, steps, reviewer checks and sources were folded into the survivor with repeats removed.

| Duplicate | Survivor | Alias resolves to |
|---|---|---|
| 4.4 | 4.1 | 4.1 |
| 4.5 | 5.3 | 5.3 |
| 9.4 | 5.1 | 5.1 |
| 5.6 | 5.10 | 5.10 |
| 2.11 | 6.3 | 6.3 |

## 4.4 into 4.1

- Duplicate 4.4: One seam, one test, one minimal implementation per cycle; never write all tests first
- Survivor 4.1 before: Write a failing test first and watch it fail
- Survivor 4.1 now: Write one failing test first and watch it fail, then write the minimal code to pass; one seam per cycle, never all tests up front.
- Why: 4.1 already requires a failing test first; 4.4 is the same TDD cycle taken one test at a time.
- Skill folder removed: `skills/4.4-one-seam-one-test-per-cycle` (now `skills/4.1-red-green-tdd`)
- Folded in: dos (2), don'ts (2), steps (4), reviewer checks (1); repeats removed. The duplicate's source files (1) are all in the survivor's SOURCES.md (1 present; link-only ones appear under Further reading).

The duplicate's content, for the record:

- Do: Pick one seam and one behaviour per cycle; Write a single test, then the code for it
- Don't: Write all tests first (horizontal); Test several seams in one cycle

## 4.5 into 5.3

- Duplicate 4.5: Start every bug fix with a test that reproduces it
- Survivor 5.3 before: Reproduce, localise, reduce, fix, guard against recurrence, verify end to end
- Survivor 5.3 now: Reproduce the bug with a failing test first, then localise, reduce, fix, keep the test as a guard, and verify end to end.
- Why: 5.3 starts with reproducing the bug; a bug fix that begins with a reproducing test is that step.
- Skill folder removed: `skills/4.5-bug-fix-starts-with-repro-test` (now `skills/5.3-reproduce-localise-reduce-fix-guard`)
- Folded in: dos (3), don'ts (1), steps (4), reviewer checks (1); repeats removed. The duplicate's source files (8) are all in the survivor's SOURCES.md (8 present; link-only ones appear under Further reading).

The duplicate's content, for the record:

- Do: Write a test that reproduces the bug and fails; Fix until it passes; Keep it as a regression test
- Don't: Fix first and add a test later (or never)

## 9.4 into 5.1

- Duplicate 9.4: Trace back to the original trigger, not the place the symptom showed up
- Survivor 5.1 before: No fixes without root-cause investigation first
- Survivor 5.1 now: No fixes without root-cause investigation first: trace back to the original trigger, not where the symptom showed up.
- Why: Tracing to the original trigger is the technique inside 5.1's root-cause step.
- Skill folder removed: `skills/9.4-trace-to-original-trigger` (now `skills/5.1-root-cause-before-fix`)
- Folded in: dos (1), don'ts (1), steps (3), reviewer checks (1); repeats removed. The duplicate's source files (2) are all in the survivor's SOURCES.md (2 present; link-only ones appear under Further reading).

The duplicate's content, for the record:

- Do: Trace back to the first wrong value or decision
- Don't: Stop at where the symptom surfaced

## 5.6 into 5.10

- Duplicate 5.6: Redact secrets in any debug output you show
- Survivor 5.10 before: Never log secrets, tokens or full personal data
- Survivor 5.10 now: Never log or display secrets, tokens or full personal data, including in debug output.
- Why: 5.10 forbids secrets in any output; debug output is one case of it.
- Skill folder removed: `skills/5.6-redact-secrets-in-debug-output` (now `skills/5.10-never-log-secrets`)
- Folded in: dos (1), don'ts (1), steps (3), reviewer checks (1); repeats removed. The duplicate's source files (7) are all in the survivor's SOURCES.md (7 present; link-only ones appear under Further reading).

The duplicate's content, for the record:

- Do: Redact tokens, passwords, keys and personal data before printing
- Don't: Paste raw env or headers into output

## 2.11 into 6.3

- Duplicate 2.11: Validate input at the boundary; treat external responses as untrusted too
- Survivor 6.3 before: Validate all external input, parameterise queries, encode output
- Survivor 6.3 now: Validate all external input at the boundary, treat external API responses as untrusted too, parameterise queries and encode output.
- Why: 6.3 already says validate external input at the boundary; 2.11 only added that external API responses are untrusted, which is now in 6.3.
- Skill folder removed: `skills/2.11-validate-at-the-boundary` (now `skills/6.3-validate-parameterise-encode`)
- Folded in: dos (3), don'ts (2), steps (4), reviewer checks (2); repeats removed. The duplicate's source files (4) are all in the survivor's SOURCES.md (4 present; link-only ones appear under Further reading).

The duplicate's content, for the record:

- Do: Validate shape, type and range at the entry point with a schema; Validate third-party responses the same way; Reject early with the standard error shape
- Don't: Validate deep inside business logic only; Trust upstream services' payloads

## Partial overlaps (kept separate, wording to sharpen after testing)

- 2.14 and 3.5: flag parameters belong to 3.5; 2.14 is about layered defaults.
- 7.6 and 7.10: 7.6 is PR size, 7.10 is the pipeline and shift-left.
- 7.1 and 8.7: 7.1 owns review, 8.7 owns fact-finding.
- 4.9 and 7.12: 4.9 is the agent's own evidence, 7.12 is the reviewer-facing ship proof.
- 3.14 and 5.4: 3.14 is the build-time rule, 5.4 is what to do when the build goes red.
- 8.5 and 9.9: 8.5 is the eval before adopting a skill, 9.9 is the held-out test before accepting a learned change.
- 8.1 and 8.3: loading context vs layering skills.
- 2.5 and 3.1: structure vs code volume.
