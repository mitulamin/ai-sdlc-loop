# workflows

| Workflow | What it does |
| --- | --- |
| `ci.yml` | On every pull request and push to `main`. Job `data-and-docs`: validates `data/*.json` against `data/schemas/`, checks `skills/` against the principles and skill data, checks `principles/*.md`, `agents/`, `commands/` and `docs/` are not stale, checks internal links in `docs/` and markdown, and runs `scripts/new-project.sh` into temporary folders for every harness in `data/harnesses.json` and for none, failing if it writes outside the target or installs a wrong or incomplete layout. Job `skillspector`: scans every folder in `skills/`, `agents/`, `commands/`, `template/` and a throwaway install for each harness with NVIDIA SkillSpector, static only. The model-assisted scan is the separate workflows below. |
| `skillspector-llm.yml` | On pull requests and pushes to `main` that change something SkillSpector scans, and by hand. Runs `scripts/skillspector-llm-scan.py` with the repository secret `NVIDIA_INFERENCE_KEY`. Skips with a notice when the secret is not available (pull requests from forks), fails if the key is rejected or the LLM stage did not really run, reports unexplained findings as warnings, and uploads the scan record as an artifact. |
| `release-gate.yml` | When a `v*` tag is pushed. Verifies `release-scans/<tag>.md` against the tagged files and runs a fresh LLM-mode scan; fails without the key. |

Run the same checks locally:

```
pip install jsonschema
python scripts/validate-data.py
python scripts/check-skills.py
scripts/build-principles.py --check
scripts/build-agents.py --check
scripts/build-site.py --check
python scripts/check-links.py
python scripts/check-new-project.py
```

SkillSpector scan (needs Python 3.12 or later):

```
pip install "skillspector==2.13.7" pyyaml
python scripts/skillspector-scan.py
```

[SkillSpector](https://github.com/NVIDIA/SkillSpector) is NVIDIA's open-source scanner for agent skills (Apache-2.0, on PyPI). CI runs it static only (`--no-llm`), so no text leaves the runner and no API key is needed. It fails on any finding that is not an accepted exception, on incomplete coverage, and when SkillSpector did not inspect every file under a target. SkillSpector refuses a baseline for a recursive scan, and its baseline rules match only by rule, file and matched text (so a second hit with the same text in a file would be suppressed silently). `scripts/skillspector-scan.py` therefore runs it once per target and matches each finding itself against `.github/skillspector-exceptions.yaml`. The targets are each skill folder, `agents/`, `commands/`, `template/` (which includes `template/bootstrap/`), and, for each harness in `data/harnesses.json`, a throwaway install made by `scripts/install-harness.py` without the installed skill copies (those are scanned from `skills/`). The list is in `scripts/skillspector_targets.py`, so a new harness is scanned without a change here. An exception must match the rule, file, matched text and full source line (`line`), carries a non-empty reason, and explains at most `max_per_file` findings in a file (default 1); a further hit fails. An exception that explains nothing for one of its `target` globs fails the scan, and so does an unknown key. The script also checks the SkillSpector version, so bump `SCANNER_VERSION` in `scripts/skillspector_targets.py`, the pin in `ci.yml` and re-review the exceptions together. `--only GLOB` scans some targets while you work on exceptions.

The scan with the LLM analyzers on sends text to NVIDIA Build and varies from run to run, so it is its own workflow (`skillspector-llm.yml`) and its findings are triaged by a person instead of failing every pull request. Its entry point, the secret it needs, how to run it locally and how it gates a release are in [RELEASING.md](../../RELEASING.md). Run it locally with `export NVIDIA_INFERENCE_KEY=...` and `python scripts/skillspector-llm-scan.py --record record.md`.

## GitHub Pages

The site is the `docs/` folder, served as is. In the repo go to Settings, Pages, set Source to "Deploy from a branch", Branch `main`, folder `/docs`, and save. No workflow is needed. `docs/.nojekyll` stops GitHub running Jekyll over the generated files.
