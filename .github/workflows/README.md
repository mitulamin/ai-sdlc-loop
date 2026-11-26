# workflows

| Workflow | What it does |
| --- | --- |
| `ci.yml` | On every pull request and push to `main`. Job `data-and-docs`: validates `data/*.json` against `data/schemas/`, runs `scripts/validate.py` (the output must be exactly `OK: 103 principles, 103 skills, 5 aliases, licences clean`), runs `scripts/check-kit-layout.py`, checks `principles/*.md` and `docs/` are not stale, and checks internal links in `docs/` and markdown. Job `skillspector`: scans every folder in `skills/` with NVIDIA SkillSpector. |

Run the same checks locally:

```
pip install jsonschema pyyaml
python scripts/validate-data.py
python3 scripts/validate.py
python3 scripts/check-kit-layout.py
scripts/build-principles.py --check
scripts/build-site.py --check
python scripts/check-links.py
```

SkillSpector scan (needs Python 3.12 or later):

```
pip install "skillspector==2.13.7"
python3 scripts/skillspector-scan.py
```

[SkillSpector](https://github.com/NVIDIA/SkillSpector) is NVIDIA's open-source scanner for agent skills (Apache-2.0, on PyPI). CI runs it static only (`--no-llm`), so no skill text leaves the runner and no API key is needed. It fails on any finding and on incomplete coverage. SkillSpector refuses a baseline for a recursive scan, so `scripts/skillspector-scan.py` runs it once per skill folder. The findings we reviewed and accepted as false positives are in `.github/skillspector-exceptions.yaml`, each with a reason; an exception that matches nothing fails the scan. SkillSpector is pinned to 2.13.7, so bump the pin and re-review the exceptions together.

## GitHub Pages

The site is the `docs/` folder, served as is. In the repo go to Settings, Pages, set Source to "Deploy from a branch", Branch `main`, folder `/docs`, and save. No workflow is needed. `docs/.nojekyll` stops GitHub running Jekyll over the generated files.
