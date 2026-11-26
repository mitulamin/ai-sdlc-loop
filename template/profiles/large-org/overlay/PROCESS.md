# Process (large org)

Many people, so changes pass gates. This is a starter. Add to it, and delete gates you do not need.

## Gates

1. **Intent**: the change has a ticket or written intent and a named owner before work starts.
2. **Build**: the work happens on a branch. No direct commits to main.
3. **Checks**: automated tests, lint and security checks pass. Do not merge on red.
4. **Review**: at least two approvals, and one must come from a code owner for the paths touched (see `.github/CODEOWNERS`). The author cannot approve their own change, and an agent cannot approve.
5. **Release**: the release manager (see [ROLES.md](ROLES.md)) approves anything that ships to users.
6. **Learn**: after a release or an incident, record what failed and which rule should change. Update `AGENTS.md` or the checks.

## Branch protection

Turn on branch protection for main that requires the checks and the reviews above. A rule that is not enforced is only a suggestion.

## Exceptions

An urgent fix may skip gate 5 only. Say so in the pull request and review it afterwards.
