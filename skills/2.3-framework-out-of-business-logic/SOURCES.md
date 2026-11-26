# Sources for 2.3 framework-out-of-business-logic

Principle: 2.3 Keep framework, persistence and vendor details out of business logic, behind adapters
Licence status: clean.

## Dedupe summary

ciembor clean-architecture, PoEAA and DDD rules agree: keep framework, persistence and vendor code at the edges behind adapters; wshobson architecture-patterns repeats hexagonal/ports-and-adapters. Amalgam keeps it pragmatic: adapters at real boundaries, not ceremonial layers (see 2.5).

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[ciembor/clean-architecture](https://github.com/ciembor/agent-rules-books/blob/893a88a6fce3a80c565bf39ac65021b43a8b2990/clean-architecture/SKILL.md) | ciembor/agent-rules-books | MIT |
| *[ciembor/patterns-of-enterprise-application-architecture](https://github.com/ciembor/agent-rules-books/blob/893a88a6fce3a80c565bf39ac65021b43a8b2990/patterns-of-enterprise-application-architecture/SKILL.md) | ciembor/agent-rules-books | MIT |
| *[ciembor/domain-driven-design](https://github.com/ciembor/agent-rules-books/blob/893a88a6fce3a80c565bf39ac65021b43a8b2990/domain-driven-design/SKILL.md) | ciembor/agent-rules-books | MIT |
| [wshobson/architecture-patterns](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/backend-development/skills/architecture-patterns/SKILL.md) | wshobson/agents | MIT |
| [wshobson/framework-migration-architect-review](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/framework-migration/agents/architect-review.md) (identical copy in 2 plugins) | wshobson/agents | MIT |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE.md and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
