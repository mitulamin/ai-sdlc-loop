# Sources for 2.4 orchestration-vs-services

Principle: 2.4 Separate orchestration (business rules) from reusable service operations
Licence status: rewritten, link-only sources moved to Further reading.

## Dedupe summary

Fowler's PoEAA and Vernon's Implementing DDD (both via the ciembor rule books) describe a service or application layer that coordinates use cases over the domain; Clean Architecture (ciembor) calls these use cases; wshobson python-design-patterns keeps the dependency pointing API to service to repository; wshobson full-stack-feature lists the service layer's responsibilities. Amalgam: one function per use case holds the flow, shared technical mechanics are extracted into services only when two use cases need them. Evidence from clean sources is thin here, so this is a good candidate to drop or merge after testing.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[ciembor/patterns-of-enterprise-application-architecture](https://github.com/ciembor/agent-rules-books/blob/893a88a6fce3a80c565bf39ac65021b43a8b2990/patterns-of-enterprise-application-architecture/SKILL.md) | ciembor/agent-rules-books | MIT |
| *[wshobson/python-design-patterns](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/python-development/skills/python-design-patterns/SKILL.md) | wshobson/agents | MIT |
| *[wshobson/full-stack-feature](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/full-stack-orchestration/commands/full-stack-feature.md) | wshobson/agents | MIT |
| *[ciembor/clean-architecture](https://github.com/ciembor/agent-rules-books/blob/893a88a6fce3a80c565bf39ac65021b43a8b2990/clean-architecture/SKILL.md) | ciembor/agent-rules-books | MIT |
| *[ciembor/implementing-domain-driven-design](https://github.com/ciembor/agent-rules-books/blob/893a88a6fce3a80c565bf39ac65021b43a8b2990/implementing-domain-driven-design/SKILL.md) | ciembor/agent-rules-books | MIT |

## Further reading (link only)

Not copied or adapted. Linked for the reader only.

| Source | Repo | Licence | Why link only |
|---|---|---|---|
| [michaelshimeles/code-structure](https://github.com/michaelshimeles/rstack/blob/8ad39442fd64cf2b407249024c5310dda90f6283/code-structure/SKILL.md) | michaelshimeles/rstack | No licence | rstack has no repo licence, so its other files are all rights reserved |
| [michaelshimeles/AGENTS.md workflow template](https://github.com/michaelshimeles/rstack/blob/8ad39442fd64cf2b407249024c5310dda90f6283/AGENTS.md) | michaelshimeles/rstack | No licence | rstack has no repo licence, so its other files are all rights reserved |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE-CONTENT and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
