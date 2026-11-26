# Sources for 7.7 worktree-per-task

Principle: 7.7 One worktree and branch per task and per agent
Licence status: rewritten, link-only sources moved to Further reading.

## Dedupe summary

Superpowers using-git-worktrees (an isolated workspace per task, project setup and baseline tests, detect existing isolation and prefer native tools), finishing-a-development-branch (clean up when done) and dispatching-parallel-agents (parallel agents only for independent tasks) agree: one worktree and branch per task and per agent, so parallel agents never collide.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[obra/using-git-worktrees](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/using-git-worktrees/SKILL.md) | obra/superpowers | MIT |
| [trailofbits/git-cleanup](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/git-cleanup/commands/git-cleanup.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/graph-evolution](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/trailmark/skills/graph-evolution/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [wshobson/git-advanced-workflows](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/developer-essentials/skills/git-advanced-workflows/SKILL.md) | wshobson/agents | MIT |
| [obra/finishing-a-development-branch](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/finishing-a-development-branch/SKILL.md) | obra/superpowers | MIT |
| [anthropics/clean_gone](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/commit-commands/commands/clean_gone.md) | anthropics/claude-plugins-official | Apache-2.0 (plugin LICENSE) |
| [addyosmani/git-workflow-and-versioning](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/git-workflow-and-versioning/SKILL.md) | addyosmani/agent-skills | MIT |

## Further reading (link only)

Not copied or adapted. Linked for the reader only.

| Source | Repo | Licence | Why link only |
|---|---|---|---|
| [michaelshimeles/new-feature](https://github.com/michaelshimeles/rstack/blob/8ad39442fd64cf2b407249024c5310dda90f6283/new-feature/SKILL.md) | michaelshimeles/rstack | No licence | rstack has no repo licence, so its other files are all rights reserved |
| [michaelshimeles/AGENTS.md workflow template](https://github.com/michaelshimeles/rstack/blob/8ad39442fd64cf2b407249024c5310dda90f6283/AGENTS.md) | michaelshimeles/rstack | No licence | rstack has no repo licence, so its other files are all rights reserved |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE-CONTENT and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
