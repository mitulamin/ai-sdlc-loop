# Sources for 3.10 small-behaviour-preserving-refactors

Principle: 3.10 Refactor in small behaviour-preserving steps, kept separate from feature changes
Licence status: clean.

## Dedupe summary

Fowler's Refactoring and refactoring-guru (ciembor), Addy code-simplification, Pocock improve-codebase-architecture, caveman safe-refactor and wshobson tdd-refactor/refactor-clean agree: small steps, tests green each step, separate from features.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[ciembor/refactoring](https://github.com/ciembor/agent-rules-books/blob/893a88a6fce3a80c565bf39ac65021b43a8b2990/refactoring/SKILL.md) | ciembor/agent-rules-books | MIT |
| *[ciembor/refactoring-guru](https://github.com/ciembor/agent-rules-books/blob/893a88a6fce3a80c565bf39ac65021b43a8b2990/refactoring-guru/SKILL.md) | ciembor/agent-rules-books | MIT |
| *[addyosmani/code-simplification](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/code-simplification/SKILL.md) | addyosmani/agent-skills | MIT |
| *[mattpocock/improve-codebase-architecture](https://github.com/mattpocock/skills/blob/6f7f7831a625f040a8e06a0e7954826b87ce775a/skills/engineering/improve-codebase-architecture/SKILL.md) | mattpocock/skills | MIT |
| *[JuliusBrussee/safe-refactor](https://github.com/JuliusBrussee/caveman/blob/e74a11ccdb38b98d15c9f9545787c907dd15f0ab/skills/safe-refactor/SKILL.md) | JuliusBrussee/caveman | Apache-2.0 |
| *[wshobson/refactor-clean](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/code-refactoring/commands/refactor-clean.md) (identical copy in 2 plugins) | wshobson/agents | MIT |
| [wshobson/tdd-refactor](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/tdd-workflows/commands/tdd-refactor.md) | wshobson/agents | MIT |
| [wshobson/code-refactoring-legacy-modernizer](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/code-refactoring/agents/legacy-modernizer.md) (identical copy in 3 plugins) | wshobson/agents | MIT |
| [addyosmani/test-driven-development](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/test-driven-development/SKILL.md) | addyosmani/agent-skills | MIT |
| [wshobson/code-refactoring-code-reviewer](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/code-refactoring/agents/code-reviewer.md) | wshobson/agents | MIT |
| [wshobson/tech-debt](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/codebase-cleanup/commands/tech-debt.md) (identical copy in 2 plugins) | wshobson/agents | MIT |
| [wshobson/tdd-cycle](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/tdd-workflows/commands/tdd-cycle.md) | wshobson/agents | MIT |
| [wshobson/tdd-workflows-tdd-orchestrator](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/tdd-workflows/agents/tdd-orchestrator.md) (identical copy in 2 plugins) | wshobson/agents | MIT |
| [addyosmani/code-review-and-quality](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/code-review-and-quality/SKILL.md) | addyosmani/agent-skills | MIT |
| [obra/test-driven-development](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/test-driven-development/SKILL.md) | obra/superpowers | MIT |
| [wshobson/unit-testing-test-automator](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/unit-testing/agents/test-automator.md) (identical copy in 4 plugins) | wshobson/agents | MIT |
| [addyosmani/git-workflow-and-versioning](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/git-workflow-and-versioning/SKILL.md) | addyosmani/agent-skills | MIT |
| [addyosmani/incremental-implementation](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/incremental-implementation/SKILL.md) | addyosmani/agent-skills | MIT |
| [obra/writing-skills](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/writing-skills/SKILL.md) | obra/superpowers | MIT |
| [hyhmrright/brooks-debt](https://github.com/hyhmrright/brooks-lint/blob/7c1a6f3ce50de016ea0dc2f73db14b061bd11200/skills/brooks-debt/SKILL.md) | hyhmrright/brooks-lint | MIT |
| [gotalab/kiro-impl](https://github.com/gotalab/cc-sdd/blob/e2a0c671aef37a482404905b409ab5c27092b25b/tools/cc-sdd/templates/agents/claude-code-skills/skills/kiro-impl/SKILL.md) | gotalab/cc-sdd | MIT |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE.md and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
