# Sources for 3.14 vertical-slices-green-build

Principle: 3.14 One thing at a time, in vertical slices, keeping the build green
Licence status: clean.

## Dedupe summary

Addy incremental-implementation and /build, Pocock to-tickets (tracer bullets) agree: one thin vertical slice at a time, build always green. PARTIAL overlap with 5.4 (stop the line) and 7.6 (small changes); kept as the build-time rule.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[addyosmani/incremental-implementation](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/incremental-implementation/SKILL.md) | addyosmani/agent-skills | MIT |
| *[addyosmani/build](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/.claude/commands/build.md) | addyosmani/agent-skills | MIT |
| *[mattpocock/to-tickets](https://github.com/mattpocock/skills/blob/6f7f7831a625f040a8e06a0e7954826b87ce775a/skills/engineering/to-tickets/SKILL.md) | mattpocock/skills | MIT |
| [wshobson/deps-upgrade](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/framework-migration/commands/deps-upgrade.md) | wshobson/agents | MIT |
| [addyosmani/deprecation-and-migration](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/deprecation-and-migration/SKILL.md) | addyosmani/agent-skills | MIT |
| [wshobson/tdd-refactor](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/tdd-workflows/commands/tdd-refactor.md) | wshobson/agents | MIT |
| [wshobson/legacy-modernize](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/framework-migration/commands/legacy-modernize.md) | wshobson/agents | MIT |
| [wshobson/angular-migration](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/framework-migration/skills/angular-migration/SKILL.md) | wshobson/agents | MIT |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE.md and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
