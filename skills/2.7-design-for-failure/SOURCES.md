# Sources for 2.7 design-for-failure

Principle: 2.7 Design for failure: explicit timeouts, bounded retries with backoff, circuit breakers, bulkheads
Licence status: clean.

## Dedupe summary

ciembor release-it (Nygard) is the main source: timeouts, bounded retries with backoff, circuit breakers, bulkheads; wshobson error-handling-patterns and backend-architect agents repeat parts. Amalgam: every outbound call gets a timeout and a retry policy, decided at design time.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[ciembor/release-it](https://github.com/ciembor/agent-rules-books/blob/893a88a6fce3a80c565bf39ac65021b43a8b2990/release-it/SKILL.md) | ciembor/agent-rules-books | MIT |
| *[wshobson/error-handling-patterns](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/developer-essentials/skills/error-handling-patterns/SKILL.md) | wshobson/agents | MIT |
| [wshobson/multi-platform-apps-backend-architect](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/multi-platform-apps/agents/backend-architect.md) (identical copy in 5 plugins) | wshobson/agents | MIT |
| [wshobson/microservices-patterns](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/backend-development/skills/microservices-patterns/SKILL.md) | wshobson/agents | MIT |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE.md and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
