# Sources for 1.2 spec-before-code

Principle: 1.2 Write a spec before code for non-trivial work, and gate each phase on human review
Licence status: clean.

## Dedupe summary

Several source files (Addy spec-driven-development, spec-kit specify, OpenSpec propose, cc-sdd requirements, Pocock to-spec, agent-os shape-spec) agree on a written spec as the source of truth; they differ on artefacts (spec.md vs proposal+tasks vs requirements/design/tasks). Amalgam: one short spec.md with goal, non-goals, acceptance criteria and open questions; the human gate moves to the coordinator's end-of-run review, per the independent-loop principle.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[addyosmani/spec-driven-development](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/spec-driven-development/SKILL.md) | addyosmani/agent-skills | MIT |
| *[addyosmani/spec](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/.claude/commands/spec.md) | addyosmani/agent-skills | MIT |
| *[github/specify](https://github.com/github/spec-kit/blob/f2010547121b3351e4923fe467205079e4593a32/templates/commands/specify.md) | github/spec-kit | MIT |
| *[Fission-AI/openspec-propose](https://github.com/Fission-AI/OpenSpec/blob/f1cd852f4edce22b8df9548a4df889172ca8ff25/skills/openspec-propose/SKILL.md) | Fission-AI/OpenSpec | MIT |
| *[gotalab/kiro-spec-requirements](https://github.com/gotalab/cc-sdd/blob/e2a0c671aef37a482404905b409ab5c27092b25b/tools/cc-sdd/templates/agents/claude-code-skills/skills/kiro-spec-requirements/SKILL.md) | gotalab/cc-sdd | MIT |
| *[mattpocock/to-spec](https://github.com/mattpocock/skills/blob/6f7f7831a625f040a8e06a0e7954826b87ce775a/skills/engineering/to-spec/SKILL.md) | mattpocock/skills | MIT |
| *[buildermethods/shape-spec](https://github.com/buildermethods/agent-os/blob/e892e61d322759165e7d9173e92c1010406c9f4d/commands/agent-os/shape-spec.md) | buildermethods/agent-os | MIT |
| *[gotalab/kiro-spec-init](https://github.com/gotalab/cc-sdd/blob/e2a0c671aef37a482404905b409ab5c27092b25b/tools/cc-sdd/templates/agents/claude-code-skills/skills/kiro-spec-init/SKILL.md) | gotalab/cc-sdd | MIT |
| *[mattpocock/implement-spec](https://github.com/mattpocock/skills/blob/6f7f7831a625f040a8e06a0e7954826b87ce775a/skills/engineering/implement-spec/SKILL.md) | mattpocock/skills | MIT |
| [ForceInjection/ddd-openspec-bridge](https://github.com/ForceInjection/domain-driven-design-skills/blob/8923ce99f228da64ef1ae2fe7f94b578e3046acb/skills/ddd-openspec-bridge/SKILL.md) | ForceInjection/domain-driven-design-skills | Apache-2.0 |
| [wshobson/feature-development](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/backend-development/commands/feature-development.md) | wshobson/agents | MIT |
| [gotalab/kiro-spec-tasks](https://github.com/gotalab/cc-sdd/blob/e2a0c671aef37a482404905b409ab5c27092b25b/tools/cc-sdd/templates/agents/claude-code-skills/skills/kiro-spec-tasks/SKILL.md) | gotalab/cc-sdd | MIT |
| [gotalab/kiro-spec-design](https://github.com/gotalab/cc-sdd/blob/e2a0c671aef37a482404905b409ab5c27092b25b/tools/cc-sdd/templates/agents/claude-code-skills/skills/kiro-spec-design/SKILL.md) | gotalab/cc-sdd | MIT |
| [wshobson/tdd-cycle](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/tdd-workflows/commands/tdd-cycle.md) | wshobson/agents | MIT |
| [wshobson/full-stack-feature](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/full-stack-orchestration/commands/full-stack-feature.md) | wshobson/agents | MIT |
| [wshobson/new-track](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/conductor/commands/new-track.md) | wshobson/agents | MIT |
| [Fission-AI/openspec-sync-specs](https://github.com/Fission-AI/OpenSpec/blob/f1cd852f4edce22b8df9548a4df889172ca8ff25/skills/openspec-sync-specs/SKILL.md) | Fission-AI/OpenSpec | MIT |
| [Fission-AI/openspec-verify-change](https://github.com/Fission-AI/OpenSpec/blob/f1cd852f4edce22b8df9548a4df889172ca8ff25/skills/openspec-verify-change/SKILL.md) | Fission-AI/OpenSpec | MIT |
| [github/tasks](https://github.com/github/spec-kit/blob/f2010547121b3351e4923fe467205079e4593a32/templates/commands/tasks.md) | github/spec-kit | MIT |
| [github/converge](https://github.com/github/spec-kit/blob/f2010547121b3351e4923fe467205079e4593a32/templates/commands/converge.md) | github/spec-kit | MIT |
| [github/analyze](https://github.com/github/spec-kit/blob/f2010547121b3351e4923fe467205079e4593a32/templates/commands/analyze.md) | github/spec-kit | MIT |
| [gotalab/kiro-spec-batch](https://github.com/gotalab/cc-sdd/blob/e2a0c671aef37a482404905b409ab5c27092b25b/tools/cc-sdd/templates/agents/claude-code-skills/skills/kiro-spec-batch/SKILL.md) | gotalab/cc-sdd | MIT |
| [addyosmani/interview-me](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/interview-me/SKILL.md) | addyosmani/agent-skills | MIT |
| [Fission-AI/openspec-explore](https://github.com/Fission-AI/OpenSpec/blob/f1cd852f4edce22b8df9548a4df889172ca8ff25/skills/openspec-explore/SKILL.md) | Fission-AI/OpenSpec | MIT |
| [Fission-AI/openspec-continue-change](https://github.com/Fission-AI/OpenSpec/blob/f1cd852f4edce22b8df9548a4df889172ca8ff25/skills/openspec-continue-change/SKILL.md) | Fission-AI/OpenSpec | MIT |
| [Fission-AI/openspec-bulk-archive-change](https://github.com/Fission-AI/OpenSpec/blob/f1cd852f4edce22b8df9548a4df889172ca8ff25/skills/openspec-bulk-archive-change/SKILL.md) | Fission-AI/OpenSpec | MIT |
| [Fission-AI/openspec-apply-change](https://github.com/Fission-AI/OpenSpec/blob/f1cd852f4edce22b8df9548a4df889172ca8ff25/skills/openspec-apply-change/SKILL.md) | Fission-AI/OpenSpec | MIT |
| [github/clarify](https://github.com/github/spec-kit/blob/f2010547121b3351e4923fe467205079e4593a32/templates/commands/clarify.md) | github/spec-kit | MIT |
| [gotalab/kiro-spec-quick](https://github.com/gotalab/cc-sdd/blob/e2a0c671aef37a482404905b409ab5c27092b25b/tools/cc-sdd/templates/agents/claude-code-skills/skills/kiro-spec-quick/SKILL.md) | gotalab/cc-sdd | MIT |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE-CONTENT and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
