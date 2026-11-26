# Sources for 6.5 report-real-trust-boundary-issues

Principle: 6.5 Report only issues that cross a real trust boundary, with evidence, a safe reproduction and the smallest fix
Licence status: rewritten, link-only sources moved to Further reading.

## Dedupe summary

Cloudflare security-audit (real trust boundary, evidence, safe reproduction, smallest fix) and Trail of Bits exploitability-verifier/fp-check/poc generator. Amalgam: findings must cross a real boundary and carry evidence.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[cloudflare/security-audit](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/SKILL.md) | cloudflare/security-audit-skill | MIT |
| [trailofbits/exploitability-verifier](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/fp-check/agents/exploitability-verifier.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/5-poc-generator](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/zeroize-audit/agents/5-poc-generator.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/fp-check](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/fp-check/skills/fp-check/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/cvss-scoring](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/cvss-scoring/skills/cvss-scoring/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [agamm/owasp-security](https://github.com/agamm/claude-code-owasp/blob/1ae29cb22518560e3625d77f2ae64f61647d9201/.claude/skills/owasp-security/SKILL.md) | agamm/claude-code-owasp | MIT |
| [trailofbits/adversarial-modeler](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/differential-review/agents/adversarial-modeler.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/5c-poc-verifier](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/zeroize-audit/agents/5c-poc-verifier.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/4-report-assembler](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/zeroize-audit/agents/4-report-assembler.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/genotoxic](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/trailmark/skills/genotoxic/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/fuzzing-obstacles](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/testing-handbook-skills/skills/fuzzing-obstacles/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/semgrep-rule-creator](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [addyosmani/security-auditor](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/agents/security-auditor.md) | addyosmani/agent-skills | MIT |
| [trailofbits/data-flow-analyzer](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/fp-check/agents/data-flow-analyzer.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/vulnerability-triage-brocards](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/vulnerability-triage-brocards/skills/vulnerability-triage-brocards/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/vector-forge](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/trailmark/skills/vector-forge/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/constant-time-analysis](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/constant-time-analysis/skills/constant-time-analysis/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/zeroize-audit](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/zeroize-audit/skills/zeroize-audit/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/yara-rule-authoring](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/yara-authoring/skills/yara-rule-authoring/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [wshobson/sast-configuration](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/security-scanning/skills/sast-configuration/SKILL.md) | wshobson/agents | MIT |
| [trailofbits/burpsuite-project-parser](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/burpsuite-project-parser/skills/burpsuite-project-parser/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |

## Further reading (link only)

Not copied or adapted. Linked for the reader only.

| Source | Repo | Licence | Why link only |
|---|---|---|---|
| [anthropics/attack-surface-analysis](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/skills/attack-surface-analysis/SKILL.md) | anthropics/claude-plugins-official | Proprietary (Anthropic claude-security licence) | claude-security plugin has a proprietary licence that forbids redistribution |
| [anthropics/scan-verifier](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/agents/scan-verifier.md) | anthropics/claude-plugins-official | Proprietary (Anthropic claude-security licence) | claude-security plugin has a proprietary licence that forbids redistribution |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE-CONTENT and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
