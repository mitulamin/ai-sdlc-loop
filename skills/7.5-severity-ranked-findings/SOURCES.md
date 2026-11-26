# Sources for 7.5 severity-ranked-findings

Principle: 7.5 Rank findings by severity (P0-P3)
Licence status: rewritten, link-only sources moved to Further reading.

## Dedupe summary

sanyuan code-review-expert (P0-P3 with merge-blocking rules); Trail of Bits review workers also rank. Amalgam: every finding carries P0-P3 and P0/P1 block.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[sanyuan0704/code-review-expert](https://github.com/sanyuan0704/sanyuan-skills/blob/08b6572ef108f22d4e8a3ecf9182a4bbef097744/skills/code-review-expert/SKILL.md) | sanyuan0704/sanyuan-skills | MIT |
| [trailofbits/rust-review-worker](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/rust-review/agents/rust-review-worker.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/rust-review-fp-judge](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/rust-review/agents/rust-review-fp-judge.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/rust-review](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/rust-review/skills/rust-review/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [wshobson/ai-review](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/performance-testing-review/commands/ai-review.md) | wshobson/agents | MIT |
| [wshobson/full-review](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/comprehensive-review/commands/full-review.md) | wshobson/agents | MIT |
| [wshobson/multi-reviewer-patterns](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/agent-teams/skills/multi-reviewer-patterns/SKILL.md) | wshobson/agents | MIT |
| [trailofbits/c-review](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/c-review/skills/c-review/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [google/egm-lite](https://github.com/google/elephant-goldfish-model/blob/46933754e63c0424daa9c270d7e0734245d79560/skills/egm-lite/SKILL.md) | google/elephant-goldfish-model | Apache-2.0 |
| [trailofbits/4-report-assembler](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/zeroize-audit/agents/4-report-assembler.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/audit-augmentation](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/trailmark/skills/audit-augmentation/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/sarif-parsing](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/static-analysis/skills/sarif-parsing/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/mutation-testing](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/mutation-testing/skills/mutation-testing/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/burpsuite-project-parser](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/burpsuite-project-parser/skills/burpsuite-project-parser/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/agentic-actions-auditor](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [wshobson/security-sast](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/security-scanning/commands/security-sast.md) | wshobson/agents | MIT |
| [wshobson/security-dependencies](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/security-scanning/commands/security-dependencies.md) | wshobson/agents | MIT |
| [wshobson/incident-response](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/incident-response/commands/incident-response.md) | wshobson/agents | MIT |
| [wshobson/xss-scan](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/frontend-mobile-security/commands/xss-scan.md) | wshobson/agents | MIT |
| [wshobson/error-trace](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/error-diagnostics/commands/error-trace.md) (identical copy in 2 plugins) | wshobson/agents | MIT |
| [wshobson/deps-audit](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/dependency-management/commands/deps-audit.md) (identical copy in 2 plugins) | wshobson/agents | MIT |
| [anthropics/conversation-analyzer](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/hookify/agents/conversation-analyzer.md) | anthropics/claude-plugins-official | Apache-2.0 (plugin LICENSE) |
| [trailofbits/dimension-validator](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/dimensional-analysis/agents/dimension-validator.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [wshobson/monitor-setup](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/observability-monitoring/commands/monitor-setup.md) | wshobson/agents | MIT |
| [wshobson/git-workflow](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/git-pr-workflows/commands/git-workflow.md) | wshobson/agents | MIT |
| [trailofbits/graph-evolution](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/trailmark/skills/graph-evolution/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [wshobson/code-migrate](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/framework-migration/commands/code-migrate.md) | wshobson/agents | MIT |
| [anthropics/modernize-review](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/code-modernization/commands/modernize-review.md) | anthropics/claude-plugins-official | Apache-2.0 (plugin LICENSE) |
| [trailofbits/rust-review-dedup-judge](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/rust-review/agents/rust-review-dedup-judge.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [wshobson/team-reviewer](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/agent-teams/agents/team-reviewer.md) | wshobson/agents | MIT |
| [wshobson/avoid-ai-writing](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/avoid-ai-writing/skills/avoid-ai-writing/SKILL.md) | wshobson/agents | MIT |
| [google/egm-synthesizer](https://github.com/google/elephant-goldfish-model/blob/46933754e63c0424daa9c270d7e0734245d79560/agents/synthesizer.md) | google/elephant-goldfish-model | Apache-2.0 |
| [google/egm-review-loop](https://github.com/google/elephant-goldfish-model/blob/46933754e63c0424daa9c270d7e0734245d79560/skills/egm-review-loop/SKILL.md) | google/elephant-goldfish-model | Apache-2.0 |
| [google/egm-resolve](https://github.com/google/elephant-goldfish-model/blob/46933754e63c0424daa9c270d7e0734245d79560/skills/egm-resolve/SKILL.md) | google/elephant-goldfish-model | Apache-2.0 |
| [JuliusBrussee/cavecrew-reviewer](https://github.com/JuliusBrussee/caveman/blob/e74a11ccdb38b98d15c9f9545787c907dd15f0ab/agents/cavecrew-reviewer.md) | JuliusBrussee/caveman | Apache-2.0 |
| [wshobson/team-review](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/agent-teams/commands/team-review.md) | wshobson/agents | MIT |

## Further reading (link only)

Not copied or adapted. Linked for the reader only.

| Source | Repo | Licence | Why link only |
|---|---|---|---|
| [anthropics/attack-surface-analysis](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/skills/attack-surface-analysis/SKILL.md) | anthropics/claude-plugins-official | Proprietary (Anthropic claude-security licence) | claude-security plugin has a proprietary licence that forbids redistribution |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE.md and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
