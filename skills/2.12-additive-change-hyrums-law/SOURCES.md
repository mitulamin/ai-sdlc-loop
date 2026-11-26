# Sources for 2.12 additive-change-hyrums-law

Principle: 2.12 Prefer adding over changing; assume every observable behaviour is depended on (Hyrum's law)
Licence status: clean.

## Dedupe summary

Addy api-and-interface-design and deprecation-and-migration lead; wshobson ADRs and Anthropic version-delta-analyst touch compatibility. Amalgam: assume every observable behaviour is depended on; add, deprecate, then remove.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[addyosmani/api-and-interface-design](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/api-and-interface-design/SKILL.md) | addyosmani/agent-skills | MIT |
| *[addyosmani/deprecation-and-migration](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/deprecation-and-migration/SKILL.md) | addyosmani/agent-skills | MIT |
| [wshobson/architecture-decision-records](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/documentation-generation/skills/architecture-decision-records/SKILL.md) | wshobson/agents | MIT |
| [anthropics/version-delta-analyst](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/code-modernization/agents/version-delta-analyst.md) | anthropics/claude-plugins-official | Apache-2.0 (plugin LICENSE) |
| [anthropics/claude-api](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/claude-api/SKILL.md) | anthropics/skills | Apache-2.0 (folder LICENSE.txt) |
| [ollygarden/otel-go](https://github.com/ollygarden/opentelemetry-agent-skills/blob/402ffc259169b799f5dcc1648a21957ff475dbb3/skills/otel-go/SKILL.md) | ollygarden/opentelemetry-agent-skills | Apache-2.0 |
| [ollygarden/otel-span-events-to-logs-migration](https://github.com/ollygarden/opentelemetry-agent-skills/blob/402ffc259169b799f5dcc1648a21957ff475dbb3/skills/otel-span-events-to-logs-migration/SKILL.md) | ollygarden/opentelemetry-agent-skills | Apache-2.0 |
| [wshobson/git-workflow](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/git-pr-workflows/commands/git-workflow.md) | wshobson/agents | MIT |
| [wshobson/deps-upgrade](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/framework-migration/commands/deps-upgrade.md) | wshobson/agents | MIT |
| [addyosmani/git-workflow-and-versioning](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/git-workflow-and-versioning/SKILL.md) | addyosmani/agent-skills | MIT |
| [ollygarden/otel-collector](https://github.com/ollygarden/opentelemetry-agent-skills/blob/402ffc259169b799f5dcc1648a21957ff475dbb3/skills/otel-collector/SKILL.md) | ollygarden/opentelemetry-agent-skills | Apache-2.0 |
| [wshobson/reference-builder](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/documentation-generation/agents/reference-builder.md) | wshobson/agents | MIT |
| [wshobson/api-design-principles](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/backend-development/skills/api-design-principles/SKILL.md) | wshobson/agents | MIT |
| [addyosmani/source-driven-development](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/source-driven-development/SKILL.md) | addyosmani/agent-skills | MIT |
| [wshobson/documentation-generation-api-documenter](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/documentation-generation/agents/api-documenter.md) (identical copy in 2 plugins) | wshobson/agents | MIT |
| [wshobson/backend-development-graphql-architect](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/backend-development/agents/graphql-architect.md) (identical copy in 2 plugins) | wshobson/agents | MIT |
| [wshobson/design-system-architect](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/ui-design/agents/design-system-architect.md) | wshobson/agents | MIT |
| [wshobson/multi-platform-apps-backend-architect](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/multi-platform-apps/agents/backend-architect.md) (identical copy in 5 plugins) | wshobson/agents | MIT |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE.md and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
