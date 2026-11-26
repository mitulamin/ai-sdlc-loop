# Sources for 5.1 root-cause-before-fix

Principle: 5.1 No fixes without root-cause investigation first: trace back to the original trigger, not where the symptom showed up. (aliases: 9.4)
Licence status: clean.

## Dedupe summary

Superpowers systematic-debugging (with root-cause-tracing.md), Addy debugging-and-error-recovery, cc-sdd kiro-debug, steipete five and the wshobson debugger agents agree: no fix without a root cause. Tracing back to the original trigger, formerly principle 9.4, is the same technique and is merged in. The Learn step reuses it when analysing why an agent failed.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[obra/systematic-debugging](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/systematic-debugging/SKILL.md) | obra/superpowers | MIT |
| *[addyosmani/debugging-and-error-recovery](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/debugging-and-error-recovery/SKILL.md) | addyosmani/agent-skills | MIT |
| *[obra/systematic-debugging/root-cause-tracing.md](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/systematic-debugging/root-cause-tracing.md) | obra/superpowers | MIT |
| *[steipete/five](https://github.com/steipete/agent-rules/blob/42993e48c165d8dfe44baacef7daee1edb38f0c6/project-rules/five.mdc) | steipete/agent-rules | MIT |
| [gotalab/kiro-debug](https://github.com/gotalab/cc-sdd/blob/e2a0c671aef37a482404905b409ab5c27092b25b/tools/cc-sdd/templates/agents/claude-code-skills/skills/kiro-debug/SKILL.md) | gotalab/cc-sdd | MIT |
| [wshobson/incident-response-debugger](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/incident-response/agents/debugger.md) | wshobson/agents | MIT |
| [trailofbits/variant-analysis](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/variant-analysis/skills/variant-analysis/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [wshobson/smart-fix](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/incident-response/commands/smart-fix.md) | wshobson/agents | MIT |
| [wshobson/error-analysis](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/error-diagnostics/commands/error-analysis.md) (identical copy in 2 plugins) | wshobson/agents | MIT |
| [wshobson/incident-response](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/incident-response/commands/incident-response.md) | wshobson/agents | MIT |
| [wshobson/parallel-debugging](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/agent-teams/skills/parallel-debugging/SKILL.md) | wshobson/agents | MIT |
| [wshobson/team-debugger](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/agent-teams/agents/team-debugger.md) | wshobson/agents | MIT |
| [wshobson/smart-debug](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/error-diagnostics/commands/smart-debug.md) | wshobson/agents | MIT |
| [wshobson/smart-debug](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/debugging-toolkit/commands/smart-debug.md) | wshobson/agents | MIT |
| [wshobson/team-debug](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/agent-teams/commands/team-debug.md) | wshobson/agents | MIT |
| [wshobson/observability-monitoring-observability-engineer](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/observability-monitoring/agents/observability-engineer.md) (identical copy in 2 plugins) | wshobson/agents | MIT |
| [wshobson/incident-responder](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/incident-response/agents/incident-responder.md) | wshobson/agents | MIT |
| [wshobson/incident-response-devops-troubleshooter](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/incident-response/agents/devops-troubleshooter.md) (identical copy in 3 plugins) | wshobson/agents | MIT |
| [wshobson/debugging-strategies](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/developer-essentials/skills/debugging-strategies/SKILL.md) | wshobson/agents | MIT |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE.md and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
