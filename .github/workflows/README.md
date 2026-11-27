# workflows

| Workflow | What it does |
| --- | --- |
| `ci.yml` | On every pull request and push to `main`. Job `data-and-docs`: validates `data/*.json` against `data/schemas/`, checks `skills/` against the principles and skill data, checks `principles/*.md`, `agents/`, `commands/` and `docs/` are not stale, checks internal links in `docs/` and markdown, and runs `scripts/new-project.sh` into temporary folders for every harness in `data/harnesses.json` and for none, failing if it writes outside the target or installs a wrong or incomplete layout. Job `skillspector`: scans every folder in `skills/` with NVIDIA SkillSpector. |

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

[SkillSpector](https://github.com/NVIDIA/SkillSpector) is NVIDIA's open-source scanner for agent skills (Apache-2.0, on PyPI). CI runs it static only (`--no-llm`), so no skill text leaves the runner and no API key is needed. It fails on any finding that is not an accepted exception and on incomplete coverage. SkillSpector refuses a baseline for a recursive scan, and its baseline rules match only by rule, file and matched text (so a second hit with the same text in a file would be suppressed silently). `scripts/skillspector-scan.py` therefore runs it once per skill folder and matches each finding itself against `.github/skillspector-exceptions.yaml`. An exception must match the rule, file, matched text and full source line (`line`), carries a non-empty reason, and explains at most `max_per_file` findings in a file (default 1); a further hit fails. An exception that explains nothing for one of its skill globs fails the scan, and so does an unknown key. The script also checks the SkillSpector version, so bump `SCANNER_VERSION` in the script, the pin in `ci.yml` and re-review the exceptions together.

## GitHub Pages

The site is the `docs/` folder, served as is. In the repo go to Settings, Pages, set Source to "Deploy from a branch", Branch `main`, folder `/docs`, and save. No workflow is needed. `docs/.nojekyll` stops GitHub running Jekyll over the generated files.
