# Sources for 5.3 reproduce-localise-reduce-fix-guard

Principle: 5.3 Reproduce the bug with a failing test first, then localise, reduce, fix, keep the test as a guard, and verify end to end. (aliases: 4.5)
Licence status: rewritten, link-only sources moved to Further reading.

## Dedupe summary

Addy debugging-and-error-recovery gives the full sequence; Pocock diagnosing-bugs, Superpowers systematic-debugging and Trail of Bits reproduce-bug cover parts; Addy test-driven-development has a 'prove it' pattern for bug fixes; wshobson smart-fix and issue repeat the flow. The reproducing test first, formerly principle 4.5, is merged in as step one.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[addyosmani/debugging-and-error-recovery](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/debugging-and-error-recovery/SKILL.md) | addyosmani/agent-skills | MIT |
| *[mattpocock/diagnosing-bugs](https://github.com/mattpocock/skills/blob/6f7f7831a625f040a8e06a0e7954826b87ce775a/skills/engineering/diagnosing-bugs/SKILL.md) | mattpocock/skills | MIT |
| *[obra/systematic-debugging](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/systematic-debugging/SKILL.md) | obra/superpowers | MIT |
| [wshobson/git-advanced-workflows](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/developer-essentials/skills/git-advanced-workflows/SKILL.md) | wshobson/agents | MIT |
| [wshobson/issue](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/team-collaboration/commands/issue.md) | wshobson/agents | MIT |
| [wshobson/smart-fix](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/incident-response/commands/smart-fix.md) | wshobson/agents | MIT |
| [wshobson/incident-response-debugger](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/incident-response/agents/debugger.md) | wshobson/agents | MIT |
| [wshobson/debugging-strategies](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/developer-essentials/skills/debugging-strategies/SKILL.md) | wshobson/agents | MIT |
| *[addyosmani/test-driven-development](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/test-driven-development/SKILL.md) | addyosmani/agent-skills | MIT |
| *[JuliusBrussee/surgical-patch](https://github.com/JuliusBrussee/caveman/blob/e74a11ccdb38b98d15c9f9545787c907dd15f0ab/skills/surgical-patch/SKILL.md) | JuliusBrussee/caveman | Apache-2.0 |
| [trailofbits/reproduce-bug](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/patching-bugs/skills/reproduce-bug/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [wshobson/ui-visual-validator](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/accessibility-compliance/agents/ui-visual-validator.md) | wshobson/agents | MIT |
| [obra/verification-before-completion](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/verification-before-completion/SKILL.md) | obra/superpowers | MIT |

## Further reading (link only)

Not copied or adapted. Linked for the reader only.

| Source | Repo | Licence | Why link only |
|---|---|---|---|
| [multica-ai/CLAUDE.md (Karpathy guidelines)](https://github.com/multica-ai/andrej-karpathy-skills/blob/2c606141936f1eeef17fa3043a72095b4765b9c2/CLAUDE.md) | multica-ai/andrej-karpathy-skills | No LICENSE file (README claims MIT) | no LICENSE file, only a README claim of MIT |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE.md and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
