# Sources for 6.3 validate-parameterise-encode

Principle: 6.3 Validate all external input at the boundary, treat external API responses as untrusted too, parameterise queries and encode output. (aliases: 2.11)
Licence status: clean.

## Dedupe summary

Addy security-and-hardening, agamm owasp-security, wshobson security-coder agents and xss-scan, plus Addy api-and-interface-design and ciembor release-it agree: validate input at the boundary, parameterise queries, encode output. Treating external API responses as untrusted, formerly principle 2.11, is merged in.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[addyosmani/security-and-hardening](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/security-and-hardening/SKILL.md) | addyosmani/agent-skills | MIT |
| *[agamm/owasp-security](https://github.com/agamm/claude-code-owasp/blob/1ae29cb22518560e3625d77f2ae64f61647d9201/.claude/skills/owasp-security/SKILL.md) | agamm/claude-code-owasp | MIT |
| [wshobson/xss-scan](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/frontend-mobile-security/commands/xss-scan.md) | wshobson/agents | MIT |
| [wshobson/mobile-security-coder](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/frontend-mobile-security/agents/mobile-security-coder.md) | wshobson/agents | MIT |
| [wshobson/frontend-security-coder](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/frontend-mobile-security/agents/frontend-security-coder.md) | wshobson/agents | MIT |
| [wshobson/data-validation-suite-backend-security-coder](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/data-validation-suite/agents/backend-security-coder.md) (identical copy in 2 plugins) | wshobson/agents | MIT |
| [wshobson/security-sast](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/security-scanning/commands/security-sast.md) | wshobson/agents | MIT |
| [wshobson/security-hardening](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/security-scanning/commands/security-hardening.md) | wshobson/agents | MIT |
| [wshobson/security-scanning-security-auditor](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/security-scanning/agents/security-auditor.md) (identical copy in 4 plugins) | wshobson/agents | MIT |
| [wshobson/backend-development-security-auditor](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/backend-development/agents/security-auditor.md) | wshobson/agents | MIT |
| [trailofbits/cvss-scoring](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/cvss-scoring/skills/cvss-scoring/SKILL.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [trailofbits/data-flow-analyzer](https://github.com/trailofbits/skills/blob/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/fp-check/agents/data-flow-analyzer.md) | trailofbits/skills | CC-BY-SA-4.0 |
| [wshobson/codebase-cleanup-code-reviewer](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/codebase-cleanup/agents/code-reviewer.md) (identical copy in 2 plugins) | wshobson/agents | MIT |
| *[addyosmani/api-and-interface-design](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/api-and-interface-design/SKILL.md) | addyosmani/agent-skills | MIT |
| *[ciembor/release-it](https://github.com/ciembor/agent-rules-books/blob/893a88a6fce3a80c565bf39ac65021b43a8b2990/release-it/SKILL.md) | ciembor/agent-rules-books | MIT |
| [wshobson/multi-platform-apps-backend-architect](https://github.com/wshobson/agents/blob/c96b5f6552dba32e4492307493ee613581430715/plugins/multi-platform-apps/agents/backend-architect.md) (identical copy in 5 plugins) | wshobson/agents | MIT |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE-CONTENT and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
