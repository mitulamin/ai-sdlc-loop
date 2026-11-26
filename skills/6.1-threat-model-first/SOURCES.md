# Sources for 6.1 threat-model-first

Principle: 6.1 Threat-model before hardening
Licence status: rewritten, link-only sources moved to Further reading.

## Dedupe summary

Addy security-and-hardening ('threat model first'), wshobson threat-modeling-expert, stride-analysis-patterns and security-requirement-extraction, and Trail of Bits adversarial-modeler agree: list assets, entry points and trust boundaries, and rank threats before hardening.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[addyosmani/security-and-hardening](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/security-and-hardening/SKILL.md) | addyosmani/agent-skills | MIT |
| [wshobson/threat-modeling-expert](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/security-scanning/agents/threat-modeling-expert.md) | wshobson/agents | MIT |
| [wshobson/stride-analysis-patterns](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/security-scanning/skills/stride-analysis-patterns/SKILL.md) | wshobson/agents | MIT |
| [wshobson/security-requirement-extraction](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/security-scanning/skills/security-requirement-extraction/SKILL.md) | wshobson/agents | MIT |
| [addyosmani/security-auditor](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/agents/security-auditor.md) | addyosmani/agent-skills | MIT |
| [wshobson/security-hardening](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/security-scanning/commands/security-hardening.md) | wshobson/agents | MIT |
| [trailofbits/rust-review-worker](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/rust-review/agents/rust-review-worker.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/rust-review-fp-judge](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/rust-review/agents/rust-review-fp-judge.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [wshobson/security-scanning-security-auditor](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/security-scanning/agents/security-auditor.md) (identical copy in 4 plugins) | wshobson/agents | MIT |
| [trailofbits/vulnerability-triage-brocards](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/vulnerability-triage-brocards/skills/vulnerability-triage-brocards/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/codeql](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/static-analysis/skills/codeql/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/adversarial-modeler](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/differential-review/agents/adversarial-modeler.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/cosmos-vulnerability-scanner](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/building-secure-contracts/skills/cosmos-vulnerability-scanner/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |

## Further reading (link only)

Not copied or adapted. Linked for the reader only.

| Source | Repo | Licence | Why link only |
|---|---|---|---|
| [anthropics/threat-model](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/skills/threat-model/SKILL.md) | anthropics/claude-plugins-official | Proprietary (Anthropic claude-security licence) | claude-security plugin has a proprietary licence that forbids redistribution |
| [anthropics/attack-surface-analysis](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/skills/attack-surface-analysis/SKILL.md) | anthropics/claude-plugins-official | Proprietary (Anthropic claude-security licence) | claude-security plugin has a proprietary licence that forbids redistribution |
| [anthropics/attack-surface-verifier](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/agents/attack-surface-verifier.md) | anthropics/claude-plugins-official | Proprietary (Anthropic claude-security licence) | claude-security plugin has a proprietary licence that forbids redistribution |
| [anthropics/attack-surface-stage](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/agents/attack-surface-stage.md) | anthropics/claude-plugins-official | Proprietary (Anthropic claude-security licence) | claude-security plugin has a proprietary licence that forbids redistribution |
| [anthropics/attack-surface-redactor](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/agents/attack-surface-redactor.md) | anthropics/claude-plugins-official | Proprietary (Anthropic claude-security licence) | claude-security plugin has a proprietary licence that forbids redistribution |
| [anthropics/claude-security](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/skills/claude-security/SKILL.md) | anthropics/claude-plugins-official | Proprietary (Anthropic claude-security licence) | claude-security plugin has a proprietary licence that forbids redistribution |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE-CONTENT and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
