# Sources for 7.10 shift-left-ci

Principle: 7.10 Shift left, and ship in small, frequent batches
Licence status: rewritten, link-only sources moved to Further reading.

## Dedupe summary

Addy ci-cd-and-automation and shipping-and-launch: run checks as early as possible in CI and ship in small frequent batches.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[addyosmani/ci-cd-and-automation](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/ci-cd-and-automation/SKILL.md) | addyosmani/agent-skills | MIT |
| *[addyosmani/shipping-and-launch](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/shipping-and-launch/SKILL.md) | addyosmani/agent-skills | MIT |
| [wshobson/ship](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/ship-mate/commands/ship.md) | wshobson/agents | MIT |
| [wshobson/setup](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/ship-mate/commands/setup.md) | wshobson/agents | MIT |
| [wshobson/workflow-automate](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/cicd-automation/commands/workflow-automate.md) | wshobson/agents | MIT |
| [wshobson/secrets-management](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/cicd-automation/skills/secrets-management/SKILL.md) | wshobson/agents | MIT |
| [wshobson/gitlab-ci-patterns](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/cicd-automation/skills/gitlab-ci-patterns/SKILL.md) | wshobson/agents | MIT |
| [wshobson/deployment-pipeline-design](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/cicd-automation/skills/deployment-pipeline-design/SKILL.md) | wshobson/agents | MIT |
| [trailofbits/rust-review-fp-judge](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/rust-review/agents/rust-review-fp-judge.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [wshobson/unity-developer](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/game-development/agents/unity-developer.md) | wshobson/agents | MIT |
| [wshobson/full-stack-orchestration-deployment-engineer](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/full-stack-orchestration/agents/deployment-engineer.md) (identical copy in 4 plugins) | wshobson/agents | MIT |
| [wshobson/full-review](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/comprehensive-review/commands/full-review.md) | wshobson/agents | MIT |
| [wshobson/tdd-workflows-code-reviewer](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/tdd-workflows/agents/code-reviewer.md) (identical copy in 6 plugins) | wshobson/agents | MIT |
| [wshobson/review](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/ship-mate/agents/review.md) | wshobson/agents | MIT |
| [dash0hq/otel-collector](https://github.com/dash0hq/agent-skills/blob/8acd4d2a2da4a725466ded8ae5e9b0fc37289b7a/skills/otel-collector/SKILL.md) | dash0hq/agent-skills | Apache-2.0 |
| [ollygarden/otel-collector](https://github.com/ollygarden/opentelemetry-agent-skills/blob/402ffc259169b799f5dcc1648a21957ff475dbb3/skills/otel-collector/SKILL.md) | ollygarden/opentelemetry-agent-skills | Apache-2.0 |
| [muratcankoylan/project-development](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/d9202c76d6dc8351e648badb576a6e9b5aae1e7f/skills/project-development/SKILL.md) | muratcankoylan/Agent-Skills-for-Context-Engineering | MIT |
| [wshobson/unit-testing-test-automator](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/unit-testing/agents/test-automator.md) (identical copy in 4 plugins) | wshobson/agents | MIT |
| [wshobson/kubernetes-operations-kubernetes-architect](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/kubernetes-operations/agents/kubernetes-architect.md) (identical copy in 3 plugins) | wshobson/agents | MIT |
| [wshobson/deployment-validation-cloud-architect](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/deployment-validation/agents/cloud-architect.md) (identical copy in 4 plugins) | wshobson/agents | MIT |
| [wshobson/deployment-strategies-terraform-specialist](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/deployment-strategies/agents/terraform-specialist.md) (identical copy in 3 plugins) | wshobson/agents | MIT |
| [wshobson/database-admin](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/database-migrations/agents/database-admin.md) | wshobson/agents | MIT |
| [wshobson/comprehensive-review-architect-review](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/comprehensive-review/agents/architect-review.md) | wshobson/agents | MIT |
| [wshobson/sast-configuration](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/security-scanning/skills/sast-configuration/SKILL.md) | wshobson/agents | MIT |
| [wshobson/turborepo-caching](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/developer-essentials/skills/turborepo-caching/SKILL.md) | wshobson/agents | MIT |
| [trailofbits/agentic-actions-auditor](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [wshobson/bash-pro](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/shell-scripting/agents/bash-pro.md) | wshobson/agents | MIT |
| [wshobson/security-scanning-security-auditor](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/security-scanning/agents/security-auditor.md) (identical copy in 4 plugins) | wshobson/agents | MIT |
| [wshobson/cicd-automation-devops-troubleshooter](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/cicd-automation/agents/devops-troubleshooter.md) | wshobson/agents | MIT |
| [wshobson/ai-review](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/performance-testing-review/commands/ai-review.md) | wshobson/agents | MIT |
| [wshobson/database-cloud-optimization-database-optimizer](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/database-cloud-optimization/agents/database-optimizer.md) | wshobson/agents | MIT |
| [wshobson/signed-audit-trails-recipe](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/signed-audit-trails/skills/signed-audit-trails-recipe/SKILL.md) | wshobson/agents | MIT |
| [wshobson/github-actions-templates](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/cicd-automation/skills/github-actions-templates/SKILL.md) | wshobson/agents | MIT |
| [trailofbits/rust-review](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/rust-review/skills/rust-review/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |

## Further reading (link only)

Not copied or adapted. Linked for the reader only.

| Source | Repo | Licence | Why link only |
|---|---|---|---|
| [NousResearch/evolve_skill pipeline](https://github.com/NousResearch/hermes-agent-self-evolution/blob/0a929e3aa20e15cf04dc7c28492a7d41a5139125/README.md) | NousResearch/hermes-agent-self-evolution | No LICENSE file (pyproject claims MIT) | no LICENSE file, only a pyproject claim of MIT |
| [anthropics/attack-surface-analysis](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/skills/attack-surface-analysis/SKILL.md) | anthropics/claude-plugins-official | Proprietary (Anthropic claude-security licence) | claude-security plugin has a proprietary licence that forbids redistribution |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE-CONTENT and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
