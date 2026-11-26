# Sources for 9.9 held-out-acceptance

Principle: 9.9 Accept a rule change only if it measurably helps on held-out cases
Licence status: rewritten, link-only sources moved to Further reading.

## Dedupe summary

muratcankoylan self-improvement-loops (a held-in split checks the targeted weakness, a held-out split the proposer never sees checks for regressions) and SkillOpt sleep (a change is kept only if it improves a held-out replay score; nothing goes live until adopted) agree. Partial overlap with 8.5, which is the pre-adoption eval.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[muratcankoylan/self-improvement-loops](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/d9202c76d6dc8351e648badb576a6e9b5aae1e7f/skills/self-improvement-loops/SKILL.md) | muratcankoylan/Agent-Skills-for-Context-Engineering | MIT |
| *[microsoft/skillopt-sleep](https://github.com/microsoft/SkillOpt/blob/dc0b5e654cafa1073a2819086151c1e0d13012f0/plugins/claude-code/commands/skillopt-sleep.md) | microsoft/SkillOpt | MIT |
| [microsoft/skillopt-sleep](https://github.com/microsoft/SkillOpt/blob/dc0b5e654cafa1073a2819086151c1e0d13012f0/plugins/claude-code/skills/skillopt-sleep/SKILL.md) | microsoft/SkillOpt | MIT |
| [trailofbits/ossfuzz](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/testing-handbook-skills/skills/ossfuzz/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [JuliusBrussee/caveman-learn](https://github.com/JuliusBrussee/caveman/blob/e74a11ccdb38b98d15c9f9545787c907dd15f0ab/skills/caveman-learn/SKILL.md) | JuliusBrussee/caveman | Apache-2.0 |
| [microsoft/skillopt-sleep-handoff](https://github.com/microsoft/SkillOpt/blob/dc0b5e654cafa1073a2819086151c1e0d13012f0/plugins/claude-code/commands/skillopt-sleep-handoff.md) | microsoft/SkillOpt | MIT |

## Further reading (link only)

Not copied or adapted. Linked for the reader only.

| Source | Repo | Licence | Why link only |
|---|---|---|---|
| [NousResearch/evolve_skill pipeline](https://github.com/NousResearch/hermes-agent-self-evolution/blob/0a929e3aa20e15cf04dc7c28492a7d41a5139125/README.md) | NousResearch/hermes-agent-self-evolution | No LICENSE file (pyproject claims MIT) | no LICENSE file, only a pyproject claim of MIT |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE.md and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
