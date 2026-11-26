# Sources for 6.6 independent-finding-verification

Principle: 6.6 Have a separate agent verify each finding before it is reported
Licence status: rewritten, link-only sources moved to Further reading.

## Dedupe summary

Cloudflare security-audit runs separate hunter and verifier agents, each with its own working folders, and asks for an independent verifier when a finding is replaced; Trail of Bits fp-check does a structured false-positive check. Amalgam: a fresh verifier tries to refute each finding before it is reported. Giving the verifier only the claim, the code and the reproduction steps, not the finder's reasoning, is our own hardening of that idea, not something the sources prescribe.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[cloudflare/security-audit](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/SKILL.md) | cloudflare/security-audit-skill | MIT |
| [trailofbits/fp-check](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/fp-check/skills/fp-check/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/replay-regression](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/regression-hunt/skills/replay-regression/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/genotoxic](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/trailmark/skills/genotoxic/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/fuzzing-obstacles](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/testing-handbook-skills/skills/fuzzing-obstacles/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/semgrep-rule-creator](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/vector-forge](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/trailmark/skills/vector-forge/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/yara-rule-authoring](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/yara-authoring/skills/yara-rule-authoring/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/constant-time-analysis](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/constant-time-analysis/skills/constant-time-analysis/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [wshobson/sast-configuration](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/security-scanning/skills/sast-configuration/SKILL.md) | wshobson/agents | MIT |
| [trailofbits/data-flow-analyzer](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/fp-check/agents/data-flow-analyzer.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/burpsuite-project-parser](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/burpsuite-project-parser/skills/burpsuite-project-parser/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [anthropics/modernize-harden](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/code-modernization/commands/modernize-harden.md) | anthropics/claude-plugins-official | Apache-2.0 (plugin LICENSE) |

## Further reading (link only)

Not copied or adapted. Linked for the reader only.

| Source | Repo | Licence | Why link only |
|---|---|---|---|
| [anthropics/attack-surface-verifier](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/agents/attack-surface-verifier.md) | anthropics/claude-plugins-official | Proprietary (Anthropic claude-security licence) | claude-security plugin has a proprietary licence that forbids redistribution |
| [anthropics/scan-verifier](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/agents/scan-verifier.md) | anthropics/claude-plugins-official | Proprietary (Anthropic claude-security licence) | claude-security plugin has a proprietary licence that forbids redistribution |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE-CONTENT and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
