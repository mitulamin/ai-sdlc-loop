# Releasing

Every release, and every tag, goes through these steps. Step 3 is required: nothing is tagged until a complete SkillSpector LLM-mode scan of the release commit is recorded in the repo and every finding in it has a disposition. This page is for whoever cuts the release, including the Cursor project that runs it for the maintainer.

## Two scans, two jobs

| Scan | When | Command | Needs a key | Sends text off the machine |
| --- | --- | --- | --- | --- |
| Static | Every pull request and push to `main`, in CI (job `skillspector`) | `python scripts/skillspector-scan.py` | No | No |
| LLM mode | Before every release or tag, by hand | `python scripts/skillspector-llm-scan.py --record release-scans/<tag>.md` | Yes, for a model provider | Yes, to that provider |

Both scan the same targets: each folder in `skills/`, `agents/`, `commands/`, `template/` (the project template, including `template/bootstrap/`), and a throwaway install for each harness in `data/harnesses.json` (without the installed skill copies, which are scanned from `skills/`). The shared list lives in `scripts/skillspector_targets.py`, so a new harness or top-level agent-facing folder is picked up by both. SkillSpector's LLM mode adds a semantic read of intent that the static rules cannot make, so it can find things the static scan does not, and can flag things that are fine. That is why its findings are triaged by a person, not suppressed by a list.

The LLM scan is not run in CI: it needs a secret, it costs money, and a model gives different answers on different runs, which would make a build flaky.

## The release steps

1. **Start from a green `main`.** CI passes on the commit you mean to release, including the static `skillspector` job.
2. **Prepare the release pull request.** Update `CHANGELOG.md` and `data/changelog.json` as usual. Do not tag yet.
3. **Run the LLM-mode scan and record it** (below), on a clean checkout of the commit the release pull request would merge as. A change to any scanned file after the scan means running it again.
4. **Triage every finding** in the record: fix it, or give it a disposition with a reason. Commit the fixes, then run the scan again if a fix touched a scanned file.
5. **Verify the record**: `python scripts/skillspector-llm-scan.py --verify release-scans/<tag>.md`. It must print `OK`.
6. **Commit `release-scans/<tag>.md` in the release pull request**, get it reviewed and merged, then tag and publish.

## Running the scan

Install the pinned scanner and PyYAML (Python 3.12 or later, as in CI):

```bash
python -m pip install "skillspector==2.13.7" pyyaml
```

Choose a provider and export its credential. SkillSpector reads these itself; `skillspector scan --help` lists every provider. The script refuses to run unless `SKILLSPECTOR_PROVIDER` is set, so a missing setting can never fall back to a provider you did not pick.

| `SKILLSPECTOR_PROVIDER` | Credential it needs |
| --- | --- |
| `anthropic` | `ANTHROPIC_API_KEY` |
| `openai` | `OPENAI_API_KEY` (and `OPENAI_BASE_URL` for a compatible gateway) |
| `openai_compatible` | `SKILLSPECTOR_COMPAT_API_KEY` and `SKILLSPECTOR_COMPAT_BASE_URL` |
| `azure_openai` | `AZURE_OPENAI_API_KEY` and `AZURE_OPENAI_ENDPOINT` |
| `bedrock` | AWS credentials (`AWS_PROFILE` optional) and `AWS_REGION` |
| `gemini` | `GOOGLE_CLOUD_PROJECT` and Application Default Credentials |

Optionally set `SKILLSPECTOR_MODEL` to pin the model. Use a current, capable model, and say which one in the release pull request. The record states the provider and model SkillSpector actually used for each analyzer. Keep the key in your shell or your secret store, never in the repo, a command line or a log.

Then run, from the repo root:

```bash
export SKILLSPECTOR_PROVIDER=anthropic   # or the provider you chose
export ANTHROPIC_API_KEY=...             # its credential, from your secret store
python scripts/skillspector-llm-scan.py --record release-scans/<tag>.md
```

`<tag>` is the tag you are about to create, for example `v0.0.3`. The scan sends the text of the scanned files to the provider you chose. Everything it scans is in this public repo, but do not run it from a fork or branch that holds private material you would not send there.

What the script does:

- Runs `skillspector scan` without `--no-llm` on every target, and counts a target only if the LLM was requested, every LLM call succeeded, no semantic analyzer failed, and every file under the target was inspected. SkillSpector itself reports a missing or rejected key as a warning and still exits 0 with static results, so the script treats that as a failure and exits 2 with the reason. A scan with no working key is never recorded as a pass.
- Writes the record: the commit, the scanner version, the provider and model, how many LLM calls succeeded, and a table of every finding with its rule, severity, file and line, the matched text, SkillSpector's explanation, and a disposition.
- Marks a finding `COVERED BY STATIC EXCEPTION` only when it has the same rule, file, matched text and source line as an entry in `.github/skillspector-exceptions.yaml`. Every other finding is written as `UNREVIEWED`, and the script exits 1 while any remain.

A full run reads every file with a model and takes a while; `--jobs N` runs targets in parallel. `--only GLOB` scans some targets for a trial run, and a record made with it fails `--verify`.

## How findings are recorded

The record is `release-scans/<tag>.md`, committed with the release. For every finding, replace `UNREVIEWED` in the last column with exactly one of these, followed by a colon and a reason:

| Disposition | Use it when | The reason names |
| --- | --- | --- |
| `FIXED:` | The finding was real and you changed the text | The commit or pull request |
| `FALSE POSITIVE:` | The model or rule misread the text | Why it is not an issue, after reading the finding in context |
| `ACCEPTED:` | The finding is real, the risk is understood, and it ships anyway | Who accepted it and why |

Read each finding in the file before you decide. Fix real problems in the source: `agents/` and `commands/` are generated, so change `data/` or `scripts/build-agents.py` and regenerate, never the generated file. If a LLM finding is a stable false positive that the static scan also raises, add a reviewed entry to `.github/skillspector-exceptions.yaml` (with a reason) so that it shows as covered next time. Do not add an exception to make a record pass, and do not turn a finding into `FALSE POSITIVE` without reading it.

`--verify` checks that the record names a commit, says the scan completed on a full run with no uncommitted changes, and that no finding is `UNREVIEWED` or has a disposition without a reason. It cannot judge whether a reason is good: that is what the review of the release pull request is for.

## When the scan cannot run

If no provider key is available, do not tag. Ask the maintainer for a key and a provider, or for an explicit, written decision to release without the LLM scan, and record that decision in the release pull request. Do not substitute a hand-written record.

## When the pinned scanner changes

Bump `SCANNER_VERSION` in `scripts/skillspector_targets.py`, the pin in `.github/workflows/ci.yml` and the install line above together, then re-review every entry in `.github/skillspector-exceptions.yaml` against the new version. See also [UPDATING.md](UPDATING.md).
