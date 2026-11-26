# Sources for 5.10 never-log-secrets

Principle: 5.10 Never log or display secrets, tokens or full personal data, including in debug output. (aliases: 5.6)
Licence status: rewritten, link-only sources moved to Further reading.

## Dedupe summary

Addy observability-and-instrumentation and security-and-hardening, ciembor release-it, and the dash0 and ollygarden OpenTelemetry collector guidance on redaction agree; Pocock diagnosing-bugs and Superpowers diagnosing-superpowers add redaction of debug output and shared transcripts. Redacting secrets in debug output, formerly principle 5.6, is merged in.

## Adapted sources (licence-clean)

Links are pinned to the commit checked on 26 Nov 2026. * marks a primary source the principle cites.

| Source | Repo | Licence |
|---|---|---|
| *[addyosmani/observability-and-instrumentation](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/observability-and-instrumentation/SKILL.md) | addyosmani/agent-skills | MIT |
| *[ciembor/release-it](https://github.com/ciembor/agent-rules-books/blob/893a88a6fce3a80c565bf39ac65021b43a8b2990/release-it/SKILL.md) | ciembor/agent-rules-books | MIT |
| *[addyosmani/security-and-hardening](https://github.com/addyosmani/agent-skills/blob/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74/skills/security-and-hardening/SKILL.md) | addyosmani/agent-skills | MIT |
| *[mattpocock/diagnosing-bugs](https://github.com/mattpocock/skills/blob/6f7f7831a625f040a8e06a0e7954826b87ce775a/skills/engineering/diagnosing-bugs/SKILL.md) | mattpocock/skills | MIT |
| [obra/diagnosing-superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/diagnosing-superpowers/SKILL.md) | obra/superpowers | MIT |
| [dash0hq/otel-ottl](https://github.com/dash0hq/agent-skills/blob/8acd4d2a2da4a725466ded8ae5e9b0fc37289b7a/skills/otel-ottl/SKILL.md) | dash0hq/agent-skills | Apache-2.0 |
| [ollygarden/otel-collector](https://github.com/ollygarden/opentelemetry-agent-skills/blob/402ffc259169b799f5dcc1648a21957ff475dbb3/skills/otel-collector/SKILL.md) | ollygarden/opentelemetry-agent-skills | Apache-2.0 |
| [ollygarden/otel-java](https://github.com/ollygarden/opentelemetry-agent-skills/blob/402ffc259169b799f5dcc1648a21957ff475dbb3/skills/otel-java/SKILL.md) | ollygarden/opentelemetry-agent-skills | Apache-2.0 |

## Further reading (link only)

Not copied or adapted. Linked for the reader only.

| Source | Repo | Licence | Why link only |
|---|---|---|---|
| [anthropics/scan-redactor](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/agents/scan-redactor.md) | anthropics/claude-plugins-official | Proprietary (Anthropic claude-security licence) | claude-security plugin has a proprietary licence that forbids redistribution |
| [anthropics/attack-surface-redactor](https://github.com/anthropics/claude-plugins-official/blob/0fbfda5a91f4adc311daca25acc99132f40f0b6e/plugins/claude-security/agents/attack-surface-redactor.md) | anthropics/claude-plugins-official | Proprietary (Anthropic claude-security licence) | claude-security plugin has a proprietary licence that forbids redistribution |

## This skill's licence

Text: CC BY-SA 4.0 (Shravi Limited and contributors). See ../../LICENSE-CONTENT and ../../CREDITS.md. Keyword-matched sources are candidates: the comparison above is based on the primary sources' matching passages, not every line of every file.
