# Sources for 8.7 fresh-context-subagents

Principle: 8.7 Use fresh-context subagents for fact-finding and review
Licence status: clean.

## Dedupe summary

Pocock chief-of-staff, Superpowers subagent-driven-development and dispatching-parallel-agents, EGM review (goldfish) and Cloudflare security-audit: fresh-context subagents for fact-finding and review. The core of the coordinator model; PARTIAL overlap with 7.1.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[mattpocock/chief-of-staff](https://github.com/mattpocock/skills/blob/6f7f7831a625f040a8e06a0e7954826b87ce775a/skills/in-progress/chief-of-staff/SKILL.md) | mattpocock/skills | MIT |
| *[obra/subagent-driven-development](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/subagent-driven-development/SKILL.md) | obra/superpowers | MIT |
| *[google/egm-review](https://github.com/google/elephant-goldfish-model/blob/46933754e63c0424daa9c270d7e0734245d79560/skills/egm-review/SKILL.md) | google/elephant-goldfish-model | Apache-2.0 |
| *[cloudflare/security-audit](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit/SKILL.md) | cloudflare/security-audit-skill | MIT |
| *[obra/dispatching-parallel-agents](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/dispatching-parallel-agents/SKILL.md) | obra/superpowers | MIT |
| [anthropics/claude-automation-recommender](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-code-setup/skills/claude-automation-recommender/SKILL.md) | anthropics/claude-plugins-official | Apache-2.0 (plugin LICENSE) |
| [google/egm-synthesizer](https://github.com/google/elephant-goldfish-model/blob/46933754e63c0424daa9c270d7e0734245d79560/agents/synthesizer.md) | google/elephant-goldfish-model | Apache-2.0 |
| [google/egm-review-loop](https://github.com/google/elephant-goldfish-model/blob/46933754e63c0424daa9c270d7e0734245d79560/skills/egm-review-loop/SKILL.md) | google/elephant-goldfish-model | Apache-2.0 |
| [google/egm-lite](https://github.com/google/elephant-goldfish-model/blob/46933754e63c0424daa9c270d7e0734245d79560/skills/egm-lite/SKILL.md) | google/elephant-goldfish-model | Apache-2.0 |
| [google/egm-brainstorm](https://github.com/google/elephant-goldfish-model/blob/46933754e63c0424daa9c270d7e0734245d79560/skills/egm-brainstorm/SKILL.md) | google/elephant-goldfish-model | Apache-2.0 |
| [gotalab/kiro-impl](https://github.com/gotalab/cc-sdd/blob/e2a0c671aef37a482404905b409ab5c27092b25b/tools/cc-sdd/templates/agents/claude-code-skills/skills/kiro-impl/SKILL.md) | gotalab/cc-sdd | MIT |
| [addyosmani/doubt-driven-development](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/doubt-driven-development/SKILL.md) | addyosmani/agent-skills | MIT |
| [google/egm-inventive-catalyst](https://github.com/google/elephant-goldfish-model/blob/46933754e63c0424daa9c270d7e0734245d79560/agents/inventive_catalyst.md) | google/elephant-goldfish-model | Apache-2.0 |
| [google/egm-bootstrap](https://github.com/google/elephant-goldfish-model/blob/46933754e63c0424daa9c270d7e0734245d79560/skills/egm-bootstrap/SKILL.md) | google/elephant-goldfish-model | Apache-2.0 |
| [peterfriese/chief-of-staff](https://github.com/peterfriese/Stratos/blob/64879724d53a6ca2c925fd614e2c2c15c1d49120/.opencode/agents/chief-of-staff.md) | peterfriese/Stratos | Apache-2.0 |
| [JuliusBrussee/cavecrew](https://github.com/JuliusBrussee/caveman/blob/e74a11ccdb38b98d15c9f9545787c907dd15f0ab/skills/cavecrew/SKILL.md) | JuliusBrussee/caveman | Apache-2.0 |
| [anthropics/skill-creator](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/skill-creator/skills/skill-creator/SKILL.md) (identical copy in 2 plugins) | anthropics/claude-plugins-official | Apache-2.0 (plugin LICENSE) |
| [anthropics/hook-development](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/plugin-dev/skills/hook-development/SKILL.md) | anthropics/claude-plugins-official | Apache-2.0 (plugin LICENSE) |
| [muratcankoylan/long-horizon-prompting](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/d9202c76d6dc8351e648badb576a6e9b5aae1e7f/skills/long-horizon-prompting/SKILL.md) | muratcankoylan/Agent-Skills-for-Context-Engineering | MIT |
| [google/egm-bootstrap-orchestrator](https://github.com/google/elephant-goldfish-model/blob/46933754e63c0424daa9c270d7e0734245d79560/agents/bootstrap_orchestrator.md) | google/elephant-goldfish-model | Apache-2.0 |
| [gotalab/kiro-spec-batch](https://github.com/gotalab/cc-sdd/blob/e2a0c671aef37a482404905b409ab5c27092b25b/tools/cc-sdd/templates/agents/claude-code-skills/skills/kiro-spec-batch/SKILL.md) | gotalab/cc-sdd | MIT |
| [wshobson/tdd-cycle](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/tdd-workflows/commands/tdd-cycle.md) | wshobson/agents | MIT |
| [wshobson/security-hardening](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/security-scanning/commands/security-hardening.md) | wshobson/agents | MIT |
| [wshobson/multi-platform](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/multi-platform-apps/commands/multi-platform.md) | wshobson/agents | MIT |
| [wshobson/smart-fix](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/incident-response/commands/smart-fix.md) | wshobson/agents | MIT |
| [wshobson/incident-response](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/incident-response/commands/incident-response.md) | wshobson/agents | MIT |
| [wshobson/full-stack-feature](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/full-stack-orchestration/commands/full-stack-feature.md) | wshobson/agents | MIT |
| [wshobson/legacy-modernize](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/framework-migration/commands/legacy-modernize.md) | wshobson/agents | MIT |
| [wshobson/performance-optimization](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/application-performance/commands/performance-optimization.md) | wshobson/agents | MIT |
| [obra/writing-skills](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/writing-skills/SKILL.md) | obra/superpowers | MIT |
| [obra/executing-plans](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/executing-plans/SKILL.md) | obra/superpowers | MIT |
| [mattpocock/implement-spec](https://github.com/mattpocock/skills/blob/6f7f7831a625f040a8e06a0e7954826b87ce775a/skills/engineering/implement-spec/SKILL.md) | mattpocock/skills | MIT |
| [google/egm-codebase-details](https://github.com/google/elephant-goldfish-model/blob/46933754e63c0424daa9c270d7e0734245d79560/agents/codebase_details.md) | google/elephant-goldfish-model | Apache-2.0 |
| [google/egm-resolve](https://github.com/google/elephant-goldfish-model/blob/46933754e63c0424daa9c270d7e0734245d79560/skills/egm-resolve/SKILL.md) | google/elephant-goldfish-model | Apache-2.0 |
| [trailofbits/github-triage](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/github-triage/skills/github-triage/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [gotalab/kiro-discovery](https://github.com/gotalab/cc-sdd/blob/e2a0c671aef37a482404905b409ab5c27092b25b/tools/cc-sdd/templates/agents/claude-code-skills/skills/kiro-discovery/SKILL.md) | gotalab/cc-sdd | MIT |
| [wshobson/git-workflow](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/git-pr-workflows/commands/git-workflow.md) | wshobson/agents | MIT |
| [wshobson/full-review](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/comprehensive-review/commands/full-review.md) | wshobson/agents | MIT |
| [wshobson/feature-development](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/backend-development/commands/feature-development.md) | wshobson/agents | MIT |
| [anthropics/code-review](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/code-review/commands/code-review.md) | anthropics/claude-plugins-official | Apache-2.0 (plugin LICENSE) |
| [Kulaxyz/self-learning](https://github.com/Kulaxyz/self-learning-skills/blob/1304fce375b5d4c4508cab9eea05bbb8b95c38f6/skills/self-learning/SKILL.md) | Kulaxyz/self-learning-skills | MIT |
| [trailofbits/rust-review](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/rust-review/skills/rust-review/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [obra/diagnosing-superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/diagnosing-superpowers/SKILL.md) | obra/superpowers | MIT |
| [anthropics/session-report](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/session-report/skills/session-report/SKILL.md) | anthropics/claude-plugins-official | Apache-2.0 (plugin LICENSE) |
| [muratcankoylan/multi-agent-patterns](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/d9202c76d6dc8351e648badb576a6e9b5aae1e7f/skills/multi-agent-patterns/SKILL.md) | muratcankoylan/Agent-Skills-for-Context-Engineering | MIT |
| [microsoft/skillopt-sleep-handoff](https://github.com/microsoft/SkillOpt/blob/dc0b5e654cafa1073a2819086151c1e0d13012f0/plugins/claude-code/commands/skillopt-sleep-handoff.md) | microsoft/SkillOpt | MIT |
| [wshobson/team-composition-patterns](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/agent-teams/skills/team-composition-patterns/SKILL.md) | wshobson/agents | MIT |
| [anthropics/claude-api](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/claude-api/SKILL.md) | anthropics/skills | Apache-2.0 (folder LICENSE.txt) |
| [JuliusBrussee/caveman-learn](https://github.com/JuliusBrussee/caveman/blob/e74a11ccdb38b98d15c9f9545787c907dd15f0ab/skills/caveman-learn/SKILL.md) | JuliusBrussee/caveman | Apache-2.0 |
| [muratcankoylan/self-managed-context](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/d9202c76d6dc8351e648badb576a6e9b5aae1e7f/skills/self-managed-context/SKILL.md) | muratcankoylan/Agent-Skills-for-Context-Engineering | MIT |
| [obra/using-superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/using-superpowers/SKILL.md) | obra/superpowers | MIT |
| [mattpocock/ask-matt](https://github.com/mattpocock/skills/blob/6f7f7831a625f040a8e06a0e7954826b87ce775a/skills/engineering/ask-matt/SKILL.md) | mattpocock/skills | MIT |
| [anthropics/new-sdk-app](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/agent-sdk-dev/commands/new-sdk-app.md) | anthropics/claude-plugins-official | Apache-2.0 (plugin LICENSE) |
| [anthropics/plugin-structure](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/plugin-dev/skills/plugin-structure/SKILL.md) | anthropics/claude-plugins-official | Apache-2.0 (plugin LICENSE) |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE.md and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
