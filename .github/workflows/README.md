# workflows

| Workflow | What it does |
| --- | --- |
| `ci.yml` | On every pull request and push to `main`. Job `data-and-docs`: validates `data/*.json` against `data/schemas/`, checks `skills/` against the principles and skill data, checks `principles/*.md`, `agents/`, `commands/` and `docs/` are not stale, checks internal links in `docs/` and markdown, and runs `scripts/new-project.sh` into temporary folders for every harness in `data/harnesses.json` and for none, failing if it writes outside the target or installs a wrong or incomplete layout. Job `skillspector`: scans every folder in `skills/`, `agents/`, `commands/`, `template/` and a throwaway install for each harness with NVIDIA SkillSpector, static only. The model-assisted scan is a required release step, not a CI job: [RELEASING.md](../../RELEASING.md). |

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

The scan with the LLM analyzers on needs a model provider key, sends text to that provider and varies from run to run, so it is not in CI. It is a required step before every release: see [RELEASING.md](../../RELEASING.md).

## GitHub Pages

The site is the `docs/` folder, served as is. In the repo go to Settings, Pages, set Source to "Deploy from a branch", Branch `main`, folder `/docs`, and save. No workflow is needed. `docs/.nojekyll` stops GitHub running Jekyll over the generated files.
