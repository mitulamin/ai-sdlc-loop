# Sources for 5.14 instrument-boundaries-and-failure-points

Principle: 5.14 Instrument boundaries and failure points: latency, errors, saturation, retries, breaker state
Licence status: clean.

## Dedupe summary

ciembor release-it, Addy observability and dash0 otel-instrumentation: instrument latency, errors, saturation, retries and breaker state at boundaries.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[ciembor/release-it](https://github.com/ciembor/agent-rules-books/blob/893a88a6fce3a80c565bf39ac65021b43a8b2990/release-it/SKILL.md) | ciembor/agent-rules-books | MIT |
| *[addyosmani/observability-and-instrumentation](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/observability-and-instrumentation/SKILL.md) | addyosmani/agent-skills | MIT |
| *[dash0hq/otel-instrumentation](https://github.com/dash0hq/agent-skills/blob/8acd4d2a2da4a725466ded8ae5e9b0fc37289b7a/skills/otel-instrumentation/SKILL.md) | dash0hq/agent-skills | Apache-2.0 |
| [ollygarden/otel-java](https://github.com/ollygarden/opentelemetry-agent-skills/blob/402ffc259169b799f5dcc1648a21957ff475dbb3/skills/otel-java/SKILL.md) | ollygarden/opentelemetry-agent-skills | Apache-2.0 |
| [ollygarden/otel-python](https://github.com/ollygarden/opentelemetry-agent-skills/blob/402ffc259169b799f5dcc1648a21957ff475dbb3/skills/otel-python/SKILL.md) | ollygarden/opentelemetry-agent-skills | Apache-2.0 |
| [ollygarden/otel-go](https://github.com/ollygarden/opentelemetry-agent-skills/blob/402ffc259169b799f5dcc1648a21957ff475dbb3/skills/otel-go/SKILL.md) | ollygarden/opentelemetry-agent-skills | Apache-2.0 |
| [ollygarden/otel-dotnet](https://github.com/ollygarden/opentelemetry-agent-skills/blob/402ffc259169b799f5dcc1648a21957ff475dbb3/skills/otel-dotnet/SKILL.md) | ollygarden/opentelemetry-agent-skills | Apache-2.0 |
| [ollygarden/otel-browser](https://github.com/ollygarden/opentelemetry-agent-skills/blob/402ffc259169b799f5dcc1648a21957ff475dbb3/skills/otel-browser/SKILL.md) | ollygarden/opentelemetry-agent-skills | Apache-2.0 |
| [wshobson/slo-implement](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/observability-monitoring/commands/slo-implement.md) | wshobson/agents | MIT |
| [ollygarden/otel-ruby](https://github.com/ollygarden/opentelemetry-agent-skills/blob/402ffc259169b799f5dcc1648a21957ff475dbb3/skills/otel-ruby/SKILL.md) | ollygarden/opentelemetry-agent-skills | Apache-2.0 |
| [trailofbits/coverage-analysis](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/testing-handbook-skills/skills/coverage-analysis/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/atheris](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/testing-handbook-skills/skills/atheris/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [wshobson/monitor-setup](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/observability-monitoring/commands/monitor-setup.md) | wshobson/agents | MIT |
| [wshobson/debug-trace](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/distributed-debugging/commands/debug-trace.md) | wshobson/agents | MIT |
| [wshobson/api-mock](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/api-testing-observability/commands/api-mock.md) | wshobson/agents | MIT |
| [wshobson/vector-database-engineer](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/llm-application-dev/agents/vector-database-engineer.md) | wshobson/agents | MIT |
| [wshobson/slo-implementation](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/observability-monitoring/skills/slo-implementation/SKILL.md) | wshobson/agents | MIT |
| [wshobson/service-mesh-observability](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/cloud-infrastructure/skills/service-mesh-observability/SKILL.md) | wshobson/agents | MIT |
| [wshobson/error-analysis](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/error-diagnostics/commands/error-analysis.md) (identical copy in 2 plugins) | wshobson/agents | MIT |
| [dash0hq/otel-collector](https://github.com/dash0hq/agent-skills/blob/8acd4d2a2da4a725466ded8ae5e9b0fc37289b7a/skills/otel-collector/SKILL.md) | dash0hq/agent-skills | Apache-2.0 |
| [muratcankoylan/context-optimization](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/d9202c76d6dc8351e648badb576a6e9b5aae1e7f/skills/context-optimization/SKILL.md) | muratcankoylan/Agent-Skills-for-Context-Engineering | MIT |
| [trailofbits/address-sanitizer](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/testing-handbook-skills/skills/address-sanitizer/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [wshobson/performance-optimization](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/application-performance/commands/performance-optimization.md) | wshobson/agents | MIT |
| [wshobson/python-observability](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/python-development/skills/python-observability/SKILL.md) | wshobson/agents | MIT |
| [wshobson/grafana-dashboards](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/observability-monitoring/skills/grafana-dashboards/SKILL.md) | wshobson/agents | MIT |
| [wshobson/distributed-tracing](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/observability-monitoring/skills/distributed-tracing/SKILL.md) | wshobson/agents | MIT |
| [addyosmani/shipping-and-launch](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/shipping-and-launch/SKILL.md) | addyosmani/agent-skills | MIT |
| [dash0hq/otel-semantic-conventions](https://github.com/dash0hq/agent-skills/blob/8acd4d2a2da4a725466ded8ae5e9b0fc37289b7a/skills/otel-semantic-conventions/SKILL.md) | dash0hq/agent-skills | Apache-2.0 |
| [ollygarden/otel-js](https://github.com/ollygarden/opentelemetry-agent-skills/blob/402ffc259169b799f5dcc1648a21957ff475dbb3/skills/otel-js/SKILL.md) | ollygarden/opentelemetry-agent-skills | Apache-2.0 |
| [wshobson/smart-debug](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/error-diagnostics/commands/smart-debug.md) | wshobson/agents | MIT |
| [wshobson/smart-debug](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/debugging-toolkit/commands/smart-debug.md) | wshobson/agents | MIT |
| [mattpocock/diagnosing-bugs](https://github.com/mattpocock/skills/blob/6f7f7831a625f040a8e06a0e7954826b87ce775a/skills/engineering/diagnosing-bugs/SKILL.md) | mattpocock/skills | MIT |
| [ollygarden/otel-weaver](https://github.com/ollygarden/opentelemetry-agent-skills/blob/402ffc259169b799f5dcc1648a21957ff475dbb3/skills/otel-weaver/SKILL.md) | ollygarden/opentelemetry-agent-skills | Apache-2.0 |
| [ollygarden/otel-telemetry-emissions](https://github.com/ollygarden/opentelemetry-agent-skills/blob/402ffc259169b799f5dcc1648a21957ff475dbb3/skills/otel-telemetry-emissions/SKILL.md) | ollygarden/opentelemetry-agent-skills | Apache-2.0 |
| [wshobson/observability-monitoring-observability-engineer](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/observability-monitoring/agents/observability-engineer.md) (identical copy in 2 plugins) | wshobson/agents | MIT |
| [addyosmani/debugging-and-error-recovery](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/debugging-and-error-recovery/SKILL.md) | addyosmani/agent-skills | MIT |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE.md and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
