---
name: simple-by-default-opt-in-complexity
description: "Use when designing a public API, config or CLI. Amalgamated skill for principle 2.14 (Design and architecture)."
principles: ["2.14"]
principle: "2.14 Design the API so the simple case is the default and advanced behaviour is opt-in, not switched on by boolean flags"
category: design-and-architecture
aliases: []
status: "draft, untested"
licence: CC-BY-SA-4.0
---

# 2.14 Simple by default opt in complexity

Principle 2.14 (Design and architecture / API design): Design the API so the simple case is the default and advanced behaviour is opt-in, not switched on by boolean flags

## When to use

Designing a public API, config or CLI.

## Producer: dos and don'ts

Do:
- Make the common case work with zero config and sensible defaults
- Put advanced options in a separate, opt-in layer
- Keep the primary constructor to 3-4 params

Don't:
- Force every caller to set options most never need
- Expose every knob at the top level

## Steps

1. List the common use case
2. Design the zero-config path
3. Layer advanced options
4. Reviewer writes the hello-world call

## Related practices

Established practices this skill applies alongside its principle. Each has a self-check item and a reviewer check below.

- **Convention over configuration** ([guide](../../guides/developer/quality-principles.md#convention-over-configuration)): agree sensible defaults once, following the platform's and the codebase's conventions, so callers declare only the exceptions. Be explicit where the domain is genuinely unusual, and say why. See also [3.3](../../principles/3.3.md).
- **Secure by default** ([guide](../../guides/developer/quality-principles.md#secure-by-default)): the safe option is the default and anything riskier is a deliberate opt-in: authentication on, debug endpoints and sample logins off, the narrowest permissions, and encryption in transit without a flag. Nobody should need a hardening guide to avoid being exposed. See also [6.2](../../principles/6.2.md), [6.4](../../principles/6.4.md).

## Self-check

Before you hand off, answer each item yes, no or N/A, with evidence. Fix every no, or record it as a `[BLOCKER: ...]`.

- [ ] Does the common case work with zero configuration and sensible defaults?
- [ ] Are advanced options in a separate opt-in layer, with no boolean flag switching behaviour and the primary constructor at three or four parameters?
- [ ] Convention over configuration: does the design follow the platform's and the codebase's conventions, so callers declare only the exceptions, with each departure explained?
- [ ] Secure by default: is the default configuration the safe one, with every riskier option an explicit opt-in?

## Adversarial reviewer (fresh context, tries to prove the work fails)

- Count steps for the common case
- Find an option every caller must set to the same value
- Convention over configuration: find a setting every caller must declare that a convention could have defaulted
- Secure by default: find a default that leaves something exposed, such as authentication off, debug on, a sample login or broad permissions
- Default verdict is FAIL until evidence shows otherwise; report findings to a file with P0-P3 severity.

## How the source skills compare

Stratos core (layered API: zero-config first layer, advanced layers opt-in), Ousterhout and Clean Code. PARTIAL overlap with 3.5 on flag parameters: proposed sharpening is to leave flag parameters to 3.5 and keep this about layered defaults.

## Sources

The licence-clean source files are listed with their licences and pinned links in SOURCES.md. Text here is written in our own words and released under CC BY-SA 4.0 (see ../../LICENSE-CONTENT and ../../CREDITS.md).

## Test plan

- Test app: App B (CRUD web app with auth)
- Phase: Design
- Test order: slot 56
- Record results in ../../data/scorecard.json (criteria in ../../README.md)
