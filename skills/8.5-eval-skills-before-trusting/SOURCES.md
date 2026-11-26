# Sources for 8.5 eval-skills-before-trusting

Principle: 8.5 Test skills with evals before trusting them
Licence status: clean.

## Dedupe summary

Anthropic skill-creator with its grader/comparator/analyzer agents (blind comparison) and wshobson eval-harness-first. PARTIAL overlap with 9.9; this is the pre-adoption eval. These test apps are its practical form.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[anthropics/skill-creator](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/skill-creator/SKILL.md) (identical copy in 2 plugins) | anthropics/skills | Apache-2.0 (folder LICENSE.txt) |
| *[anthropics/analyzer](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/skill-creator/agents/analyzer.md) | anthropics/skills | Apache-2.0 (folder LICENSE.txt) |
| *[anthropics/comparator](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/skill-creator/agents/comparator.md) | anthropics/skills | Apache-2.0 (folder LICENSE.txt) |
| *[anthropics/grader](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/skill-creator/agents/grader.md) | anthropics/skills | Apache-2.0 (folder LICENSE.txt) |
| [wshobson/eval](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/plugin-eval/commands/eval.md) | wshobson/agents | MIT |
| [wshobson/eval-orchestrator](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/plugin-eval/agents/eval-orchestrator.md) | wshobson/agents | MIT |
| [wshobson/eval-judge](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/plugin-eval/agents/eval-judge.md) | wshobson/agents | MIT |
| [wshobson/evaluation-methodology](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/plugin-eval/skills/evaluation-methodology/SKILL.md) | wshobson/agents | MIT |
| [anthropics/claude-api](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/claude-api/SKILL.md) | anthropics/skills | Apache-2.0 (folder LICENSE.txt) |
| [muratcankoylan/evaluation](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/d9202c76d6dc8351e648badb576a6e9b5aae1e7f/skills/evaluation/SKILL.md) | muratcankoylan/Agent-Skills-for-Context-Engineering | MIT |
| [trailofbits/semgrep-rule-creator](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [JuliusBrussee/caveman-discover](https://github.com/JuliusBrussee/caveman/blob/e74a11ccdb38b98d15c9f9545787c907dd15f0ab/skills/caveman-discover/SKILL.md) | JuliusBrussee/caveman | Apache-2.0 |
| [trailofbits/agentic-actions-auditor](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [JuliusBrussee/caveman-optimize](https://github.com/JuliusBrussee/caveman/blob/e74a11ccdb38b98d15c9f9545787c907dd15f0ab/skills/caveman-optimize/SKILL.md) | JuliusBrussee/caveman | Apache-2.0 |
| [anthropics/writing-hookify-rules](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/hookify/skills/writing-rules/SKILL.md) | anthropics/claude-plugins-official | Apache-2.0 (plugin LICENSE) |
| [muratcankoylan/advanced-evaluation](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/d9202c76d6dc8351e648badb576a6e9b5aae1e7f/skills/advanced-evaluation/SKILL.md) | muratcankoylan/Agent-Skills-for-Context-Engineering | MIT |
| [anthropics/conversation-analyzer](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/hookify/agents/conversation-analyzer.md) | anthropics/claude-plugins-official | Apache-2.0 (plugin LICENSE) |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE-CONTENT and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
