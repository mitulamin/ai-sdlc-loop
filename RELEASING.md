# Releasing

Every release goes through these steps. The gate is the SkillSpector LLM-mode scan: a release is not tagged or published until every group of that scan has passed in CI on the exact commit being released, and its findings have been triaged. This page is for whoever cuts the release, including the Cursor project that runs it for the maintainer.

## Why the LLM scan runs on release candidates

The static scan is fast and deterministic, so it runs on every pull request. The LLM-mode scan sends every agent-facing file to a model provider, takes a long time (an hour or more is normal), is limited by the provider's request rates, and gives somewhat different answers from run to run. So it does not run on pull requests. It runs once per release candidate, on the commit that will be released, in groups that run one after another so that request rates stay low and a group that fails, for example on a rate limit, can be run again on its own.

## Tags

- **`vX.Y.Z-rcN`** (for example `v0.0.3-rc1`) is a release-candidate tag. Pushing it starts the LLM scan (workflow `skillspector-llm.yml`) on the tagged commit. The commit must be on `main`; the scan refuses any other. A new candidate for the same version, after a fix, is the next `N`.
- **`vX.Y.Z`** (for example `v0.0.3`) is the release. Create it, and the GitHub release, only after every scan group for a `vX.Y.Z-rcN` tag has passed, and on the same commit as that candidate, however long that takes (a day is fine). The `Release gate` workflow (`release-gate.yml`) runs when `vX.Y.Z` is pushed and fails unless such a passed scan exists for that commit.

## Two scans, three workflows

| Scan | Where and when | Entry point | Needs a key | Sends text off the machine |
| --- | --- | --- | --- | --- |
| Static | CI, every pull request and push to `main` (workflow `ci.yml`, job `skillspector`) | `python scripts/skillspector-scan.py` | No | No |
| LLM mode | CI, when a `vX.Y.Z-rcN` tag is pushed on a `main` commit, and by hand (workflow `skillspector-llm.yml`) | `python scripts/skillspector-llm-scan.py --group NAME --record PATH`, one job per group | Yes: `XAI_API_KEY` or `NVIDIA_INFERENCE_KEY` | Yes, to xAI or NVIDIA Build |
| Release gate | CI, when a `vX.Y.Z` tag is pushed (workflow `release-gate.yml`) | Checks for a passed LLM scan of a candidate on the same commit | No | No |

`scripts/skillspector-llm-scan.py` is the only entry point for the LLM scan. CI calls it and does not repeat its logic, so a local run behaves the same as CI when the same key is set.

Both scans cover the same targets: each folder in `skills/`, `agents/`, `commands/`, `template/` (the project template, including `template/bootstrap/`), and a throwaway install for each harness in `data/harnesses.json` (without the installed skill copies, which are scanned from `skills/`). The shared list lives in `scripts/skillspector_targets.py`, so a new harness or top-level agent-facing folder is picked up by both. SkillSpector's LLM mode adds a semantic read of intent that the static rules cannot make, so it can find things the static scan does not, and can flag things that are fine. That is why its findings are triaged by a person and recorded, not suppressed by a list.

## What the LLM scan workflow does

The workflow passes two repository secrets to the script as environment variables and nothing else, and the script never prints either:

- `XAI_API_KEY`, an xAI API key (endpoint `https://api.x.ai/v1`). Used when it is set.
- `NVIDIA_INFERENCE_KEY`, an NVIDIA Build key (`nvapi-...`, endpoint `https://integrate.api.nvidia.com/v1`). Used when `XAI_API_KEY` is not set.

The jobs:

1. **plan** checks that a release-candidate tag points at a commit on `main`, then lists the scan groups with `python scripts/skillspector-llm-scan.py --list-groups`. The groups come from the repo, not from a list in the workflow: one per skill family (`skills-1` holds every `1.x` skill, `skills-2` every `2.x` skill, and so on), then `agents`, `commands`, `template` (which includes the Bootstrap files) and `harness-installs`. A new skill family or harness is picked up without editing the workflow.
2. **scan (group)** runs once per group, one group at a time, in that order. Each job checks the key and model with one small request, scans its group, and uploads its record as the artifact `skillspector-llm-group-<group>`. A failed group does not stop the later groups. A rejected key, a model that is gone or not answering, a key that stays rate-limited, or a target whose LLM calls did not all succeed fails that group's job with the reason. Findings that no static exception explains are listed as warnings in that job; they do not fail it.
3. **summary** combines the group records into one record of the whole scan (`--merge`), uploads it as the artifact `skillspector-llm-record-<sha>`, and passes only if every group passed.

If a group fails, open the run and use **Re-run failed jobs**. GitHub runs the failed groups and the summary again, and keeps the groups that passed and their records. Repeat until the summary passes. Each group job allows several hours, and the script itself retries a target whose calls failed after an exponential backoff, so slow or rate-limited runs are expected and fine.

## The release steps

1. **Start from a green `main`.** CI passes on the commit you mean to release, including the static `skillspector` job. Update `CHANGELOG.md` and `data/changelog.json` for the release in a pull request and merge it first.
2. **Tag a release candidate** on that `main` commit: `git tag v0.0.3-rc1 <commit>` and `git push origin v0.0.3-rc1`. The `SkillSpector LLM scan` workflow starts.
3. **Wait for every group to pass.** Re-run only the failed jobs until the `summary` job passes. This can take hours; that is expected.
4. **Download the combined record** (artifact `skillspector-llm-record-<sha>` from the summary job) into `release-scans/vX.Y.Z.md` in a checkout of the candidate commit.
5. **Triage every finding** in the record: give it a disposition with a reason (below). If a finding is real and needs a change to a scanned file, fix it in a pull request and start again from step 1 with the next candidate (`-rc2`).
6. **Check the record** with the candidate commit checked out: `python scripts/skillspector-llm-scan.py --verify release-scans/vX.Y.Z.md`. It must print `OK`. It fails if the record is not of every group, was made on other content, or has a finding without a disposition.
7. **Tag the release** `vX.Y.Z` on the same commit as the candidate, push the tag, and create the GitHub release from it with the triaged record attached. The `Release gate` workflow must pass on the tag; if it does not, delete the release and the tag and find out why.
8. **Keep the record in the repo:** commit `release-scans/vX.Y.Z.md` to `main` in a pull request after the release.

## Running the scan locally

Install the pinned scanner and PyYAML (Python 3.12 or later, as in CI):

```bash
python -m pip install "skillspector==2.13.7" pyyaml
```

Then, from the repo root, with a key in the environment (from your secret store, never typed into a command line or the repo):

```bash
export XAI_API_KEY=xai-...      # or NVIDIA_INFERENCE_KEY=nvapi-...
python scripts/skillspector-llm-scan.py --list-groups                                   # the groups, in order
python scripts/skillspector-llm-scan.py --group skills-1 --record scan/skills-1.md       # one group, as CI does
python scripts/skillspector-llm-scan.py --record scan/all.md                            # every group in one run
```

A group run also writes `scan/skills-1.md.json`. After running every group into one folder, `python scripts/skillspector-llm-scan.py --merge scan/all.md --from scan` combines them into one record, the same way the summary job does. `--only GLOB` scans the targets whose names match, for a trial; a record made with it, or with `--group` alone, fails `--verify`.

The script picks the provider by the key it finds, `XAI_API_KEY` first:

- **xAI** (`XAI_API_KEY`): SkillSpector's `openai_compatible` provider pointed at `https://api.x.ai/v1`. The script sets `SKILLSPECTOR_COMPAT_BASE_URL` and `SKILLSPECTOR_COMPAT_API_KEY` for SkillSpector itself, and picks the model by asking xAI which models the key can use, taking the first of `XAI_MODELS` at the top of the script (a fast non-reasoning Grok model first). xAI's fastest tier is not offered on its public API, so it is not in that list.
- **NVIDIA Build** (`NVIDIA_INFERENCE_KEY`): SkillSpector's `nv_build` provider with the model named by `NV_BUILD_MODEL` at the top of the script, rather than SkillSpector's own default for that provider, which NVIDIA Build still lists but does not answer.

`SKILLSPECTOR_PROVIDER` overrides the choice (`xai` or `nv_build` to pick one when both keys are set, or another SkillSpector provider, below), and `SKILLSPECTOR_MODEL` overrides the model. Providers retire models without notice (NVIDIA Build answers HTTP 410 for a retired one), so if the check before the scan says the model is gone or not answering, pick a current chat model from the provider's `/v1/models`, try it with `--only`, and update `NV_BUILD_MODEL` or `XAI_MODELS` in a pull request. The record states the provider and model SkillSpector actually used for each analyzer. The scan sends the text of the scanned files to the provider. Everything it scans is in this public repo, but do not run it from a fork or branch that holds private material you would not send there.

To use another provider, set `SKILLSPECTOR_PROVIDER` and that provider's own variables. `skillspector scan --help` lists them all.

| `SKILLSPECTOR_PROVIDER` | Credential it needs | Notes |
| --- | --- | --- |
| `xai` (chosen when `XAI_API_KEY` is set) | `XAI_API_KEY` | xAI, `https://api.x.ai/v1`, through SkillSpector's `openai_compatible` provider. Paid per token; rate limits per team. CI uses it when the secret is set. |
| `nv_build` (chosen when only `NVIDIA_INFERENCE_KEY` is set) | `NVIDIA_INFERENCE_KEY` | NVIDIA Build, `https://integrate.api.nvidia.com/v1`. Free tier, about 40 requests a minute, and a cap over longer periods. CI falls back to it. |
| `ollama` | None; a local Ollama service | Nothing leaves your machine. Set `SKILLSPECTOR_MODEL` to a model you have pulled. Use it when the key is unavailable or the text must stay local. |
| `openai_compatible` | `SKILLSPECTOR_COMPAT_API_KEY` and `SKILLSPECTOR_COMPAT_BASE_URL` | Any OpenAI-compatible gateway you run or trust. |

Other SkillSpector providers work the same way through their own variables, but nothing in this repo relies on them. A record made with a provider other than `xai` or `nv_build` must say so in the GitHub release. Keep every key in your shell or your secret store, never in the repo, a command line or a log.

What the script does:

- With `xai` or `nv_build`, checks the key and the model with one small request first. No key stops it with exit code 2 (or exit code 0 and a notice with `--skip-without-key`). A rejected key, a retired or unknown model, a model that does not answer that request within a short limit, or a key still rate-limited after a few tries (NVIDIA Build's free tier also caps use over longer periods, and answers HTTP 429 for a while once that is used up) always exits 2, with the reason.
- Runs `skillspector scan` without `--no-llm` on every target of the run, and counts a target only if the LLM was requested, every LLM call succeeded, no semantic analyzer failed, and every file under the target was inspected. A target where SkillSpector's semantic analyzers find no file they apply to (most harness installs, which hold agents, commands and config but no skill package) makes no LLM calls; it counts, and the record names it as scanned with static rules only. SkillSpector itself reports a missing or rejected key as a warning and still exits 0 with static results, so the script treats that as a failure and exits 2 with the reason. A scan with no working key is never recorded as a pass.
- Scans a few targets at a time (`SKILLSPECTOR_JOBS` or `--jobs`; the default stays well under each provider's rate limit), retries a target whose calls failed after an exponential backoff (`--retries`), and collects every result into one record and one exit code.
- Writes the record: the commit, a content id of the scanned files, the scanner version, the provider, model and endpoint, the wall-clock time, how many LLM calls succeeded, and a table of every finding with its rule, severity, file and line, the matched text, SkillSpector's explanation, and a disposition. A combined record also lists each group with its time and date.
- Marks a finding `COVERED BY STATIC EXCEPTION` only when it has the same rule, file, matched text and source line as an entry in `.github/skillspector-exceptions.yaml`. Every other finding is written as `UNREVIEWED`, and the script exits 1 while any remain (exit 0 with `--allow-unreviewed`, which CI uses so that findings are reported without failing the group).

## How findings are recorded

The record is `release-scans/vX.Y.Z.md`: the combined record from the summary job, attached to the GitHub release and then committed to `main`. For every finding, replace `UNREVIEWED` in the last column with exactly one of these, followed by a colon and a reason:

| Disposition | Use it when | The reason names |
| --- | --- | --- |
| `FIXED:` | The finding was real and you changed the text | The commit or pull request |
| `FALSE POSITIVE:` | The model or rule misread the text | Why it is not an issue, after reading the finding in context |
| `ACCEPTED:` | The finding is real, the risk is understood, and it ships anyway | Who accepted it and why |

Read each finding in the file before you decide. Fix real problems in the source: `agents/` and `commands/` are generated, so change `data/` or `scripts/build-agents.py` and regenerate, never the generated file. A fix changes the scanned files, so it needs a new candidate and a new scan. If a LLM finding is a stable false positive that the static scan also raises, add a reviewed entry to `.github/skillspector-exceptions.yaml` (with a reason) so that it shows as covered next time. Do not add an exception to make a record pass, and do not turn a finding into `FALSE POSITIVE` without reading it.

`--verify` checks that the record names a commit, says the scan completed on a full run (every group) with no uncommitted changes, was made on exactly the files now in `HEAD` (it compares a content id that leaves out `release-scans/`), and that no finding is `UNREVIEWED` or has a disposition without a reason. Run it with the candidate commit checked out. It cannot judge whether a reason is good: that is for whoever approves the release.

## When the scan cannot run

If neither `XAI_API_KEY` nor `NVIDIA_INFERENCE_KEY` works (missing, expired or rejected), every group fails with the reason: do not tag the release. Ask the maintainer to add or replace a repository secret and re-run the failed jobs, or run the scan locally with `SKILLSPECTOR_PROVIDER=ollama`, or ask for an explicit, written decision to release without the LLM scan and record that decision in the GitHub release. Do not substitute a hand-written record.

## When the pinned scanner changes

Bump `SCANNER_VERSION` in `scripts/skillspector_targets.py`, the pin in each workflow under `.github/workflows/` that installs it, and the install line above together, then re-review every entry in `.github/skillspector-exceptions.yaml` against the new version. See also [UPDATING.md](UPDATING.md).
