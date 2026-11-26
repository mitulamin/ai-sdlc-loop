# Sources for 4.10 mark-untested-with-reason

Principle: 4.10 Mark anything you couldn't test as untested, with the reason; never skip silently
Licence status: rewritten, link-only sources moved to Further reading.

## Dedupe summary

Superpowers' cannot-verify reference (items the reviewer could not check from the diff must be resolved before a task is complete) and OpenSpec openspec-verify-change (mark a check as not verified with the specific reason, and carry on) both report what could not be verified instead of dropping it. Amalgam: an UNTESTED list with reasons in every report.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[obra/references/cannot-verify.md](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/subagent-driven-development/references/cannot-verify.md) | obra/superpowers | MIT |
| [Fission-AI/openspec-verify-change](https://github.com/Fission-AI/OpenSpec/blob/f1cd852f4edce22b8df9548a4df889172ca8ff25/skills/openspec-verify-change/SKILL.md) | Fission-AI/OpenSpec | MIT |

## Further reading (link only)

Not copied or adapted. Linked for the reader only.

| Source | Repo | Licence | Why link only |
|---|---|---|---|
| [michaelshimeles/evidence-driven-testing](https://github.com/michaelshimeles/rstack/blob/8ad39442fd64cf2b407249024c5310dda90f6283/evidence-driven-testing/SKILL.md) | michaelshimeles/rstack | No licence | rstack has no repo licence, so its other files are all rights reserved |
| [anthropics/patch-verifier](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/agents/patch-verifier.md) | anthropics/claude-plugins-official | Proprietary (Anthropic claude-security licence) | claude-security plugin has a proprietary licence that forbids redistribution |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE-CONTENT and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
