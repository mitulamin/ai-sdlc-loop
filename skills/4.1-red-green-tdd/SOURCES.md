# Sources for 4.1 red-green-tdd

Principle: 4.1 Write one failing test first and watch it fail, then write the minimal code to pass; one seam per cycle, never all tests up front. (aliases: 4.4)
Licence status: clean.

## Dedupe summary

Superpowers test-driven-development (iron law: no code without a failing test), Addy test-driven-development, Pocock tdd (one seam, one test, one minimal implementation per cycle) and the wshobson tdd-cycle, tdd-red, tdd-green and tdd-refactor commands agree on red-green-refactor. Pocock's vertical-slice rule, formerly principle 4.4, is merged in as the cycle rule: never write all the tests up front.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[obra/test-driven-development](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/test-driven-development/SKILL.md) | obra/superpowers | MIT |
| *[addyosmani/test-driven-development](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/test-driven-development/SKILL.md) | addyosmani/agent-skills | MIT |
| *[mattpocock/tdd](https://github.com/mattpocock/skills/blob/6f7f7831a625f040a8e06a0e7954826b87ce775a/skills/engineering/tdd/SKILL.md) | mattpocock/skills | MIT |
| *[addyosmani/test](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/.claude/commands/test.md) | addyosmani/agent-skills | MIT |
| *[wshobson/tdd-cycle](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/tdd-workflows/commands/tdd-cycle.md) | wshobson/agents | MIT |
| *[wshobson/tdd-red](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/tdd-workflows/commands/tdd-red.md) | wshobson/agents | MIT |
| *[wshobson/tdd-green](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/tdd-workflows/commands/tdd-green.md) | wshobson/agents | MIT |
| *[wshobson/tdd-refactor](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/tdd-workflows/commands/tdd-refactor.md) | wshobson/agents | MIT |
| [wshobson/tdd-workflows-tdd-orchestrator](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/tdd-workflows/agents/tdd-orchestrator.md) (identical copy in 2 plugins) | wshobson/agents | MIT |
| [wshobson/tdd-workflows-code-reviewer](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/tdd-workflows/agents/code-reviewer.md) | wshobson/agents | MIT |
| [wshobson/unit-testing-test-automator](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/unit-testing/agents/test-automator.md) (identical copy in 4 plugins) | wshobson/agents | MIT |
| [gotalab/kiro-impl](https://github.com/gotalab/cc-sdd/blob/e2a0c671aef37a482404905b409ab5c27092b25b/tools/cc-sdd/templates/agents/claude-code-skills/skills/kiro-impl/SKILL.md) | gotalab/cc-sdd | MIT |
| [obra/writing-skills](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/writing-skills/SKILL.md) | obra/superpowers | MIT |
| [obra/executing-plans](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/executing-plans/SKILL.md) | obra/superpowers | MIT |
| [wshobson/implement](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/conductor/commands/implement.md) | wshobson/agents | MIT |
| [wshobson/javascript-testing-patterns](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/javascript-typescript/skills/javascript-testing-patterns/SKILL.md) | wshobson/agents | MIT |
| [wshobson/backend-development-test-automator](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/backend-development/agents/test-automator.md) | wshobson/agents | MIT |
| [wshobson/python-testing-patterns](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/python-development/skills/python-testing-patterns/SKILL.md) | wshobson/agents | MIT |
| [wshobson/workflow-patterns](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/conductor/skills/workflow-patterns/SKILL.md) | wshobson/agents | MIT |
| [addyosmani/doubt-driven-development](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/doubt-driven-development/SKILL.md) | addyosmani/agent-skills | MIT |
| [obra/verification-before-completion](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/verification-before-completion/SKILL.md) | obra/superpowers | MIT |
| [wshobson/bats-testing-patterns](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/shell-scripting/skills/bats-testing-patterns/SKILL.md) | wshobson/agents | MIT |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE-CONTENT and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
