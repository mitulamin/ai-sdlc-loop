# Sources for 7.12 before-and-after-proof

Principle: 7.12 Ship with before-and-after proof
Licence status: rebuilt from MIT sources; original sources link-only.

## Dedupe summary

pr-evidence (ArefMozafari), pr-visuals pr-screenshots (michalklejdysz), sideshot (victorsaly) and pr-screenshots (nullswan), all MIT, agree: a UI change is shown with before and after screenshots of the same screen, device and state, and the 'before' is captured first; other changes are shown by one short snippet. They differ in mechanism: pr-evidence hosts images on a non-merging branch with a fresh path per capture and a fixed PR body; pr-visuals gets the 'before' by putting the changed files back to the base branch while the dev server hot-reloads; sideshot pictures only the part that changed, on desktop and phone and in dark mode, and marks what changed; nullswan's scripts capture base and feature branches and write a comparison report. Partial overlap with 4.9, which is the evidence for the agent itself.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[ArefMozafari/pr-evidence](https://github.com/ArefMozafari/pr-evidence/blob/cb8c053d31ca064e87454419059301d9fcf3e2b7/skills/pr-evidence/SKILL.md) | ArefMozafari/pr-evidence | MIT |
| *[michalklejdysz/pr-screenshots](https://github.com/michalklejdysz/pr-visuals/blob/6cc2de319a83da8f0277ce0f483ab6185780d8e2/skills/pr-screenshots/SKILL.md) | michalklejdysz/pr-visuals | MIT |
| *[victorsaly/sideshot](https://github.com/victorsaly/sideshot/blob/48802c68e1fcc8718f34fa7cbcc2026a32e11c12/skills/sideshot/SKILL.md) | victorsaly/sideshot | MIT |
| *[nullswan/pr-screenshots (nullswan)](https://github.com/nullswan/pr-screenshots/blob/3c5592d6a0afcc27f85015d5593f1e8763dde9d3/SKILL.md) | nullswan/pr-screenshots | MIT |

## Further reading (link only)

Not copied or adapted. Linked for the reader only.

| Source | Repo | Licence | Why link only |
|---|---|---|---|
| [michaelshimeles/before-and-after](https://github.com/michaelshimeles/rstack/blob/8ad39442fd64cf2b407249024c5310dda90f6283/before-and-after/SKILL.md) | michaelshimeles/rstack | PolyForm-Shield-1.0.0 | rstack before-and-after folder is PolyForm Shield (non-compete) |
| [michaelshimeles/AGENTS.md workflow template](https://github.com/michaelshimeles/rstack/blob/8ad39442fd64cf2b407249024c5310dda90f6283/AGENTS.md) | michaelshimeles/rstack | No licence | rstack has no repo licence, so its other files are all rights reserved |
| [vercel-labs/before-and-after (Vercel Labs)](https://github.com/vercel-labs/before-and-after/blob/8306d34f459b6704e08e6adb5829fcddb0dc3557/skill/SKILL.md) | vercel-labs/before-and-after | PolyForm Shield 1.0.0 | PolyForm Shield 1.0.0 (non-compete), not compatible with CC BY-SA or GPLv3 |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE.md and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
