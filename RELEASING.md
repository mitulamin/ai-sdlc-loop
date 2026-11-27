# Releasing

Every release, and every tag, goes through these steps. The gate is the SkillSpector LLM-mode scan: nothing is tagged until the scan has passed in CI on the release commit and a complete scan record, with a disposition for every finding, is committed under `release-scans/`. This page is for whoever cuts the release, including the Cursor project that runs it for the maintainer.

## Two scans, three workflows

| Scan | Where and when | Entry point | Needs a key | Sends text off the machine |
| --- | --- | --- | --- | --- |
| Static | CI, every pull request and push to `main` (workflow `ci.yml`, job `skillspector`) | `python scripts/skillspector-scan.py` | No | No |
| LLM mode | CI, pull requests and pushes to `main` that change something scanned, and on demand (workflow `skillspector-llm.yml`) | `python scripts/skillspector-llm-scan.py --record PATH` | Yes: `NVIDIA_INFERENCE_KEY` | Yes, to NVIDIA Build |
| LLM mode, release gate | CI, when a `v*` tag is pushed (workflow `release-gate.yml`) | the same script, then `--verify release-scans/<tag>.md` | Yes: `NVIDIA_INFERENCE_KEY` | Yes, to NVIDIA Build |

`scripts/skillspector-llm-scan.py` is the only entry point for the LLM scan. CI calls it and does not repeat its logic, so a local run behaves the same as CI when `NVIDIA_INFERENCE_KEY` is set.

Both scans cover the same targets: each folder in `skills/`, `agents/`, `commands/`, `template/` (the project template, including `template/bootstrap/`), and a throwaway install for each harness in `data/harnesses.json` (without the installed skill copies, which are scanned from `skills/`). The shared list lives in `scripts/skillspector_targets.py`, so a new harness or top-level agent-facing folder is picked up by both. SkillSpector's LLM mode adds a semantic read of intent that the static rules cannot make, so it can find things the static scan does not, and can flag things that are fine. A model also gives different answers on different runs. That is why its findings are triaged by a person and recorded, not suppressed by a list, and why an unreviewed finding shows as a warning on a pull request instead of failing it.

## What CI does with the LLM scan

The key is the repository secret `NVIDIA_INFERENCE_KEY`, an NVIDIA Build key (`nvapi-...`, endpoint `https://integrate.api.nvidia.com/v1`). The workflow passes it to the script as an environment variable and nothing else. The script never prints it.

- **Key available** (pushes, and pull requests from this repository): the script checks the key with one small request, then scans every target. A key that is rejected fails the job with the reason. A scan whose LLM calls did not succeed fails the job. Findings that no static exception explains are listed as warnings and in the job summary, and the full record is uploaded as an artifact named `skillspector-llm-record-<sha>`.
- **Key not available** (pull requests from forks, which GitHub gives no secrets): the job skips cleanly with a notice that says so. It does not fail.
- **Request volume.** NVIDIA Build's free tier allows about 40 requests a minute. The workflow runs only when a scanned path changes, a newer push to the same pull request cancels the older run, and the script scans four targets at a time (each makes a few calls over most of a minute) and retries a target whose calls failed after a pause. Set `SKILLSPECTOR_LLM_JOBS` or `--jobs` to change the parallelism, `--retries` to change the retries.

## The release steps

1. **Start from a green `main`.** CI passes on the commit you mean to release, including the static `skillspector` job.
2. **Prepare the release pull request.** Update `CHANGELOG.md` and `data/changelog.json` as usual. Do not tag yet.
3. **Get a complete LLM-mode scan of the release pull request.** The `SkillSpector LLM scan` job must pass on it. If the pull request changed nothing that scan watches, run the workflow by hand (Actions, SkillSpector LLM scan, Run workflow), or run the script locally (below). Download its record: the artifact `skillspector-llm-record-<sha>`, or the file you wrote locally.
4. **Triage every finding** in the record: fix it, or give it a disposition with a reason (below). Commit the fixes, then scan again if a fix touched a scanned file.
5. **Commit the record** as `release-scans/<tag>.md` in the release pull request, then run `python scripts/skillspector-llm-scan.py --verify release-scans/<tag>.md`. It must print `OK`. It fails if any scanned file changed after the scan.
6. **Merge the release pull request, then tag** `<tag>` (for example `v0.0.3`) on the merge commit. The `Release gate` workflow runs on the tag: it verifies `release-scans/<tag>.md` again against the tagged files and runs a fresh LLM scan. If it fails, do not publish; delete the tag, fix the cause and tag again.

## Running the scan locally

Install the pinned scanner and PyYAML (Python 3.12 or later, as in CI):

```bash
python -m pip install "skillspector==2.13.7" pyyaml
```

Then, from the repo root:

```bash
export NVIDIA_INFERENCE_KEY=nvapi-...    # from your secret store, never typed into a command line or the repo
python scripts/skillspector-llm-scan.py --record release-scans/<tag>.md
```

The script defaults to `SKILLSPECTOR_PROVIDER=nv_build` (NVIDIA Build) and reads the key from `NVIDIA_INFERENCE_KEY`. With `nv_build` it uses the model named by `NV_BUILD_MODEL` at the top of the script rather than SkillSpector's own default for that provider, which NVIDIA Build still lists but does not answer; set `SKILLSPECTOR_MODEL` to use another. NVIDIA Build retires models without notice (a retired one answers HTTP 410), so if the check before the scan says the model is gone or not answering, pick a current chat model from `https://integrate.api.nvidia.com/v1/models`, try it with `--only`, and update `NV_BUILD_MODEL` in a pull request. The record states the provider and model SkillSpector actually used for each analyzer. The scan sends the text of the scanned files to the provider. Everything it scans is in this public repo, but do not run it from a fork or branch that holds private material you would not send there.

To use another provider, set `SKILLSPECTOR_PROVIDER` and that provider's own variables. `skillspector scan --help` lists them all.

| `SKILLSPECTOR_PROVIDER` | Credential it needs | Notes |
| --- | --- | --- |
| `nv_build` (default) | `NVIDIA_INFERENCE_KEY` | NVIDIA Build, `https://integrate.api.nvidia.com/v1`. Free tier, about 40 requests a minute. This is what CI uses. |
| `ollama` | None; a local Ollama service | Nothing leaves your machine. Set `SKILLSPECTOR_MODEL` to a model you have pulled. Use it when the key is unavailable or the text must stay local. |
| `openai_compatible` | `SKILLSPECTOR_COMPAT_API_KEY` and `SKILLSPECTOR_COMPAT_BASE_URL` | Any OpenAI-compatible gateway you run or trust. |

Other SkillSpector providers work the same way through their own variables, but nothing in this repo relies on them. A record made with a provider other than the default must say so in the release pull request. Keep every key in your shell or your secret store, never in the repo, a command line or a log.

What the script does:

- With `nv_build`, checks the key and the model with one small request first. No key stops it with exit code 2 (or exit code 0 and a notice with `--skip-without-key`, which CI uses for runs without secrets). A rejected key, a retired or unknown model, or a model that does not answer that request within a short limit always exits 2, with the reason.
- Runs `skillspector scan` without `--no-llm` on every target, and counts a target only if the LLM was requested, every LLM call succeeded, no semantic analyzer failed, and every file under the target was inspected. SkillSpector itself reports a missing or rejected key as a warning and still exits 0 with static results, so the script treats that as a failure and exits 2 with the reason. A scan with no working key is never recorded as a pass.
- Writes the record: the commit, a content id of the scanned files, the scanner version, the provider and model, how many LLM calls succeeded, and a table of every finding with its rule, severity, file and line, the matched text, SkillSpector's explanation, and a disposition.
- Marks a finding `COVERED BY STATIC EXCEPTION` only when it has the same rule, file, matched text and source line as an entry in `.github/skillspector-exceptions.yaml`. Every other finding is written as `UNREVIEWED`, and the script exits 1 while any remain (exit 0 with `--allow-unreviewed`, which CI uses so that findings are reported without failing every run).

A full run reads every file with a model and takes a while. `--only GLOB` scans some targets for a trial run, and a record made with it fails `--verify`.

## How findings are recorded

The record is `release-scans/<tag>.md`, committed with the release. For every finding, replace `UNREVIEWED` in the last column with exactly one of these, followed by a colon and a reason:

| Disposition | Use it when | The reason names |
| --- | --- | --- |
| `FIXED:` | The finding was real and you changed the text | The commit or pull request |
| `FALSE POSITIVE:` | The model or rule misread the text | Why it is not an issue, after reading the finding in context |
| `ACCEPTED:` | The finding is real, the risk is understood, and it ships anyway | Who accepted it and why |

Read each finding in the file before you decide. Fix real problems in the source: `agents/` and `commands/` are generated, so change `data/` or `scripts/build-agents.py` and regenerate, never the generated file. If a LLM finding is a stable false positive that the static scan also raises, add a reviewed entry to `.github/skillspector-exceptions.yaml` (with a reason) so that it shows as covered next time. Do not add an exception to make a record pass, and do not turn a finding into `FALSE POSITIVE` without reading it.

`--verify` checks that the record names a commit, says the scan completed on a full run with no uncommitted changes, was made on exactly the files now in `HEAD` (it compares a content id that leaves out `release-scans/`, so it survives a squash merge), and that no finding is `UNREVIEWED` or has a disposition without a reason. It cannot judge whether a reason is good: that is what the review of the release pull request is for.

## When the scan cannot run

If `NVIDIA_INFERENCE_KEY` is missing, expired or rejected, do not tag: the `Release gate` workflow fails on purpose without it. Ask the maintainer to add or replace the repository secret, or run the scan locally with `SKILLSPECTOR_PROVIDER=ollama`, or ask for an explicit, written decision to release without the LLM scan and record that decision in the release pull request. Do not substitute a hand-written record.

## When the pinned scanner changes

Bump `SCANNER_VERSION` in `scripts/skillspector_targets.py`, the pin in each workflow under `.github/workflows/` that installs it, and the install line above together, then re-review every entry in `.github/skillspector-exceptions.yaml` against the new version. See also [UPDATING.md](UPDATING.md).
