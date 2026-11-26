# Sources for 7.1 separate-reviewer-early-and-often

Principle: 7.1 Review early and often, using a separate reviewer subagent
Licence status: clean.

## Dedupe summary

Superpowers requesting-code-review (with code-reviewer.md) and subagent-driven-development, Pocock code-review and many wshobson code-reviewer copies (six identical files) agree: a separate reviewer subagent after each task. PARTIAL overlap with 8.7; proposed sharpening: 7.1 owns review, 8.7 owns fact-finding.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[obra/requesting-code-review](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/requesting-code-review/SKILL.md) | obra/superpowers | MIT |
| *[obra/requesting-code-review/code-reviewer.md](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/requesting-code-review/code-reviewer.md) | obra/superpowers | MIT |
| *[obra/subagent-driven-development](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/subagent-driven-development/SKILL.md) | obra/superpowers | MIT |
| *[mattpocock/code-review](https://github.com/mattpocock/skills/blob/6f7f7831a625f040a8e06a0e7954826b87ce775a/skills/engineering/code-review/SKILL.md) | mattpocock/skills | MIT |
| [wshobson/git-workflow](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/git-pr-workflows/commands/git-workflow.md) | wshobson/agents | MIT |
| [wshobson/tdd-workflows-code-reviewer](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/tdd-workflows/agents/code-reviewer.md) (identical copy in 6 plugins) | wshobson/agents | MIT |
| [wshobson/ai-review](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/performance-testing-review/commands/ai-review.md) | wshobson/agents | MIT |
| [wshobson/code-review-excellence](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/developer-essentials/skills/code-review-excellence/SKILL.md) | wshobson/agents | MIT |
| [addyosmani/code-reviewer](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/agents/code-reviewer.md) | addyosmani/agent-skills | MIT |
| [wshobson/multi-reviewer-patterns](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/agent-teams/skills/multi-reviewer-patterns/SKILL.md) | wshobson/agents | MIT |
| [addyosmani/code-review-and-quality](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/code-review-and-quality/SKILL.md) | addyosmani/agent-skills | MIT |
| [obra/receiving-code-review](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/receiving-code-review/SKILL.md) | obra/superpowers | MIT |
| [anthropics/code-review](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/code-review/commands/code-review.md) | anthropics/claude-plugins-official | Apache-2.0 (plugin LICENSE) |
| [sanyuan0704/code-review-expert](https://github.com/sanyuan0704/sanyuan-skills/blob/08b6572ef108f22d4e8a3ecf9182a4bbef097744/skills/code-review-expert/SKILL.md) | sanyuan0704/sanyuan-skills | MIT |
| [wshobson/review](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/ship-mate/agents/review.md) | wshobson/agents | MIT |
| [wshobson/team-reviewer](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/agent-teams/agents/team-reviewer.md) | wshobson/agents | MIT |
| [wshobson/team-review](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/agent-teams/commands/team-review.md) | wshobson/agents | MIT |
| [wshobson/incident-response-code-reviewer](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/incident-response/agents/code-reviewer.md) | wshobson/agents | MIT |
| [steipete/pr-review](https://github.com/steipete/agent-rules/blob/42993e48c165d8dfe44baacef7daee1edb38f0c6/project-rules/pr-review.mdc) | steipete/agent-rules | MIT |
| [JuliusBrussee/caveman-review](https://github.com/JuliusBrussee/caveman/blob/e74a11ccdb38b98d15c9f9545787c907dd15f0ab/skills/caveman-review/SKILL.md) | JuliusBrussee/caveman | Apache-2.0 |
| [wshobson/code-review-preshipment](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/operating-kit/agents/code-review-preshipment.md) | wshobson/agents | MIT |
| [addyosmani/review](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/.claude/commands/review.md) | addyosmani/agent-skills | MIT |
| [anthropics/code-reviewer](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/pr-review-toolkit/agents/code-reviewer.md) | anthropics/claude-plugins-official | Apache-2.0 (plugin LICENSE) |
| [anthropics/code-reviewer](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/feature-dev/agents/code-reviewer.md) | anthropics/claude-plugins-official | Apache-2.0 (plugin LICENSE) |
| [hyhmrright/brooks-review](https://github.com/hyhmrright/brooks-lint/blob/7c1a6f3ce50de016ea0dc2f73db14b061bd11200/commands/brooks-review.md) | hyhmrright/brooks-lint | MIT |
| [hyhmrright/brooks-review](https://github.com/hyhmrright/brooks-lint/blob/7c1a6f3ce50de016ea0dc2f73db14b061bd11200/skills/brooks-review/SKILL.md) | hyhmrright/brooks-lint | MIT |
| [trailofbits/second-opinion](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/second-opinion/skills/second-opinion/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [wshobson/standup-notes](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/team-collaboration/commands/standup-notes.md) | wshobson/agents | MIT |
| [wshobson/smart-fix](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/incident-response/commands/smart-fix.md) | wshobson/agents | MIT |
| [addyosmani/ship](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/.claude/commands/ship.md) | addyosmani/agent-skills | MIT |
| [wshobson/full-review](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/comprehensive-review/commands/full-review.md) | wshobson/agents | MIT |
| [wshobson/multi-agent-review](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/performance-testing-review/commands/multi-agent-review.md) (identical copy in 2 plugins) | wshobson/agents | MIT |
| [wshobson/pr-enhance](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/git-pr-workflows/commands/pr-enhance.md) (identical copy in 2 plugins) | wshobson/agents | MIT |
| [anthropics/review-pr](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/pr-review-toolkit/commands/review-pr.md) | anthropics/claude-plugins-official | Apache-2.0 (plugin LICENSE) |
| [anthropics/skill-reviewer](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/plugin-dev/agents/skill-reviewer.md) | anthropics/claude-plugins-official | Apache-2.0 (plugin LICENSE) |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE.md and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
