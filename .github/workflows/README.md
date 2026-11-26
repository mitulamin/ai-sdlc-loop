# workflows

| Workflow | What it does |
| --- | --- |
| `ci.yml` | On every pull request and push to `main`: validates `data/*.json` against `data/schemas/`, checks `skills/` against the principles and skill data, checks `principles/*.md`, `agents/`, `commands/` and `docs/` are not stale, and checks internal links in `docs/` and markdown. |

Run the same checks locally:

```
pip install jsonschema
python scripts/validate-data.py
python scripts/check-skills.py
scripts/build-principles.py --check
scripts/build-agents.py --check
scripts/build-site.py --check
python scripts/check-links.py
```

Still to come: SkillSpector scan of `skills/`.

## GitHub Pages

The site is the `docs/` folder, served as is. In the repo go to Settings, Pages, set Source to "Deploy from a branch", Branch `main`, folder `/docs`, and save. No workflow is needed. `docs/.nojekyll` stops GitHub running Jekyll over the generated files.
