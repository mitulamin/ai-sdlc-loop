# Sources for 5.13 sample-in-the-collector

Principle: 5.13 Sample in the collector pipeline, not the SDK
Licence status: clean.

## Dedupe summary

dash0 otel-instrumentation ('defer all sampling to the Collector') and otel-collector, ollygarden otel-collector. Amalgam: SDK exports everything; sampling policy lives centrally.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[dash0hq/otel-collector](https://github.com/dash0hq/agent-skills/blob/8acd4d2a2da4a725466ded8ae5e9b0fc37289b7a/skills/otel-collector/SKILL.md) | dash0hq/agent-skills | Apache-2.0 |
| *[dash0hq/otel-instrumentation](https://github.com/dash0hq/agent-skills/blob/8acd4d2a2da4a725466ded8ae5e9b0fc37289b7a/skills/otel-instrumentation/SKILL.md) | dash0hq/agent-skills | Apache-2.0 |
| *[ollygarden/otel-collector](https://github.com/ollygarden/opentelemetry-agent-skills/blob/402ffc259169b799f5dcc1648a21957ff475dbb3/skills/otel-collector/SKILL.md) | ollygarden/opentelemetry-agent-skills | Apache-2.0 |
| [wshobson/debug-trace](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/distributed-debugging/commands/debug-trace.md) | wshobson/agents | MIT |
| [ollygarden/otel-ottl](https://github.com/ollygarden/opentelemetry-agent-skills/blob/402ffc259169b799f5dcc1648a21957ff475dbb3/skills/otel-ottl/SKILL.md) | ollygarden/opentelemetry-agent-skills | Apache-2.0 |
| [ollygarden/otel-browser](https://github.com/ollygarden/opentelemetry-agent-skills/blob/402ffc259169b799f5dcc1648a21957ff475dbb3/skills/otel-browser/SKILL.md) | ollygarden/opentelemetry-agent-skills | Apache-2.0 |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE.md and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
