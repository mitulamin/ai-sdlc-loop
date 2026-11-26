# Sources for 3.2 surgical-changes

Principle: 3.2 Make surgical changes: every changed line traces to the request
Licence status: rewritten, link-only sources moved to Further reading.

## Dedupe summary

caveman surgical-patch (change the narrowest layer that owns the bug, preserve unrelated behaviour and user changes, no cleanup or renaming outside the fix), caveman cavecrew-builder, Addy incremental-implementation (thin, revertable increments) and Addy code-simplification agree: touch only what the task needs. Strongest in brownfield work.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[JuliusBrussee/surgical-patch](https://github.com/JuliusBrussee/caveman/blob/e74a11ccdb38b98d15c9f9545787c907dd15f0ab/skills/surgical-patch/SKILL.md) | JuliusBrussee/caveman | Apache-2.0 |
| *[addyosmani/incremental-implementation](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/incremental-implementation/SKILL.md) | addyosmani/agent-skills | MIT |
| [JuliusBrussee/cavecrew-builder](https://github.com/JuliusBrussee/caveman/blob/e74a11ccdb38b98d15c9f9545787c907dd15f0ab/agents/cavecrew-builder.md) | JuliusBrussee/caveman | Apache-2.0 |

## Further reading (link only)

Not copied or adapted. Linked for the reader only.

| Source | Repo | Licence | Why link only |
|---|---|---|---|
| [multica-ai/CLAUDE.md (Karpathy guidelines)](https://github.com/multica-ai/andrej-karpathy-skills/blob/2c606141936f1eeef17fa3043a72095b4765b9c2/CLAUDE.md) | multica-ai/andrej-karpathy-skills | No LICENSE file (README claims MIT) | no LICENSE file, only a README claim of MIT |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE.md and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
