# Sources for 1.3 capability-map-and-dependency-order

Principle: 1.3 Break big asks into a capability map and build modules in dependency order
Licence status: clean.

## Dedupe summary

Addy planning-and-task-breakdown, Pocock to-tickets/wayfinder, spec-kit tasks and cc-sdd tasks all break work into ordered units; Pocock insists on tracer-bullet vertical slices, spec-kit on dependency-ordered tasks.md. Amalgam: a capability map, then tasks in dependency order where each task is a vertical slice with its own check.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[addyosmani/planning-and-task-breakdown](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/planning-and-task-breakdown/SKILL.md) | addyosmani/agent-skills | MIT |
| *[addyosmani/plan](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/.claude/commands/plan.md) | addyosmani/agent-skills | MIT |
| *[mattpocock/to-tickets](https://github.com/mattpocock/skills/blob/6f7f7831a625f040a8e06a0e7954826b87ce775a/skills/engineering/to-tickets/SKILL.md) | mattpocock/skills | MIT |
| *[github/tasks](https://github.com/github/spec-kit/blob/f2010547121b3351e4923fe467205079e4593a32/templates/commands/tasks.md) | github/spec-kit | MIT |
| *[gotalab/kiro-spec-tasks](https://github.com/gotalab/cc-sdd/blob/e2a0c671aef37a482404905b409ab5c27092b25b/tools/cc-sdd/templates/agents/claude-code-skills/skills/kiro-spec-tasks/SKILL.md) | gotalab/cc-sdd | MIT |
| *[mattpocock/wayfinder](https://github.com/mattpocock/skills/blob/6f7f7831a625f040a8e06a0e7954826b87ce775a/skills/engineering/wayfinder/SKILL.md) | mattpocock/skills | MIT |
| [mattpocock/implement-spec](https://github.com/mattpocock/skills/blob/6f7f7831a625f040a8e06a0e7954826b87ce775a/skills/engineering/implement-spec/SKILL.md) | mattpocock/skills | MIT |
| [github/converge](https://github.com/github/spec-kit/blob/f2010547121b3351e4923fe467205079e4593a32/templates/commands/converge.md) | github/spec-kit | MIT |
| [gotalab/kiro-spec-batch](https://github.com/gotalab/cc-sdd/blob/e2a0c671aef37a482404905b409ab5c27092b25b/tools/cc-sdd/templates/agents/claude-code-skills/skills/kiro-spec-batch/SKILL.md) | gotalab/cc-sdd | MIT |
| [gotalab/kiro-discovery](https://github.com/gotalab/cc-sdd/blob/e2a0c671aef37a482404905b409ab5c27092b25b/tools/cc-sdd/templates/agents/claude-code-skills/skills/kiro-discovery/SKILL.md) | gotalab/cc-sdd | MIT |
| [gotalab/kiro-impl](https://github.com/gotalab/cc-sdd/blob/e2a0c671aef37a482404905b409ab5c27092b25b/tools/cc-sdd/templates/agents/claude-code-skills/skills/kiro-impl/SKILL.md) | gotalab/cc-sdd | MIT |
| [addyosmani/spec-driven-development](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/spec-driven-development/SKILL.md) | addyosmani/agent-skills | MIT |
| [github/analyze](https://github.com/github/spec-kit/blob/f2010547121b3351e4923fe467205079e4593a32/templates/commands/analyze.md) | github/spec-kit | MIT |
| [ForceInjection/ddd-openspec-bridge](https://github.com/ForceInjection/domain-driven-design-skills/blob/8923ce99f228da64ef1ae2fe7f94b578e3046acb/skills/ddd-openspec-bridge/SKILL.md) | ForceInjection/domain-driven-design-skills | Apache-2.0 |
| [Fission-AI/openspec-propose](https://github.com/Fission-AI/OpenSpec/blob/f1cd852f4edce22b8df9548a4df889172ca8ff25/skills/openspec-propose/SKILL.md) | Fission-AI/OpenSpec | MIT |
| [Fission-AI/openspec-onboard](https://github.com/Fission-AI/OpenSpec/blob/f1cd852f4edce22b8df9548a4df889172ca8ff25/skills/openspec-onboard/SKILL.md) | Fission-AI/OpenSpec | MIT |
| [gotalab/kiro-spec-quick](https://github.com/gotalab/cc-sdd/blob/e2a0c671aef37a482404905b409ab5c27092b25b/tools/cc-sdd/templates/agents/claude-code-skills/skills/kiro-spec-quick/SKILL.md) | gotalab/cc-sdd | MIT |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE.md and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
