# Merges

Every principle merged into another. The old ID stays as an `aliases` entry on the surviving principle in [data/principles.json](data/principles.json), so old references still resolve, and the old principle and site URLs redirect to the survivor. No other principle was renumbered. The machine-readable log is [data/changelog.json](data/changelog.json). Process: [UPDATING.md](UPDATING.md).

The dedupe pass was run by Rex, the research bot, and took the list from 108 principles to 103.

| Old ID | New ID | Reason | Date |
| --- | --- | --- | --- |
| 4.4 | [4.1](principles/4.1.md) | One test per cycle is a rule within red-green TDD. | 2026-11-26 |
| 4.5 | [5.3](principles/5.3.md) | The reproducing test is the first step of 5.3. | 2026-11-26 |
| 9.4 | [5.1](principles/5.1.md) | Same technique, same source (the Superpowers debugging skill). | 2026-11-26 |
| 5.6 | [5.10](principles/5.10.md) | Same rule. | 2026-11-26 |
| 2.11 | [6.3](principles/6.3.md) | Same rule. | 2026-11-26 |

## What each merge changed

- **4.4 into 4.1.** Old 4.4: "One seam, one test, one minimal implementation per cycle; never write all tests first". New 4.1: "Write one failing test first and watch it fail, then write the minimal code to pass; one seam per cycle, never all tests up front." Sources: Superpowers, Addy, Pocock (Pocock was on both).
- **4.5 into 5.3.** Old 4.5: "Start every bug fix with a test that reproduces it". New 5.3: "Reproduce the bug with a failing test first, then localise, reduce, fix, keep the test as a guard, and verify end to end." Sources: Addy, Karpathy, caveman, Pocock.
- **9.4 into 5.1.** Old 9.4: "Trace back to the original trigger, not the place the symptom showed up". New 5.1: "No fixes without root-cause investigation first: trace back to the original trigger, not where the symptom showed up." Sources: Superpowers, Addy.
- **5.6 into 5.10.** Old 5.6: "Redact secrets in any debug output you show". New 5.10: "Never log or display secrets, tokens or full personal data, including in debug output." Sources: Addy, ciembor (Release It!), Pocock.
- **2.11 into 6.3.** Old 2.11: "Validate input at the boundary; treat external responses as untrusted too". New 6.3: "Validate all external input at the boundary, treat external API responses as untrusted too, parameterise queries and encode output." Sources: Addy, ciembor.

No amalgamated skills exist yet (they are the next phase), so there were no skills, agents, commands or test-order slots to update. When skills are written, the survivor's skill should carry the merged principle's dos, don'ts, steps and reviewer checks, with no repeated rules.

## Overlapping pairs kept separate

These pairs overlap in part. Both principles stay. Their wording was sharpened and each now has a `distinct_from` note, shown on its principle file and page, saying when to use it and how it differs from its partner.

2.14 and 3.5, 7.6 and 7.10, 7.1 and 8.7, 4.9 and 7.12, 3.14 and 5.4, 8.5 and 9.9, 8.1 and 8.3, 2.5 and 3.1.
