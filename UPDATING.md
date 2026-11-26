# Updating: how to re-run the research

This repo is meant to be refreshed about every six months, and sooner if a source repo disappears or changes licence. This page is the playbook. The tooling it mentions is marked as built or not built yet.

## The rules

1. **Pin everything.** Every source repo has a commit SHA in `data/sources.json`. Every link in a skill's `SOURCES.md` is pinned to a commit. Nothing points at a moving branch.
2. **Keep generated and hand-written content apart.** A refresh may rewrite generated files. It must never touch hand-written ones.
3. **IDs are permanent.** A principle ID is never renumbered or reused. Merged and dropped principles stay in `data/principles.json` with a status.
4. **Log every change.** Merges, drops, additions, edits and re-pins go in `data/changelog.json` and `CHANGELOG.md`.
5. **Version the data.** Every data file has a `schema_version`, and every schema lives in `data/schemas/`.
6. **A human approves the result.** A refresh is a pull request. It is never pushed straight to main.

## What is generated and what is hand-written

| Path | Kind | Who changes it |
| --- | --- | --- |
| `data/principles.json` | Hand-written source of truth | People, through a PR, with a changelog entry |
| `data/sources.json` | Hand-written, except pins | People; pins by `scripts/refresh-sources.py --pin` or `--repin` |
| `data/changelog.json`, `CHANGELOG.md` | Hand-written log | People |
| `data/notes/` | Hand-written overlays (for example `data/notes/principles/1.1.md`) | People |
| `data/schemas/` | Hand-written, versioned | People |
| `principles/*.md` | Generated | `scripts/build-principles.py`. First line is a `GENERATED` marker. |
| `data/refresh/<run-id>/` | Generated reports and proposals from a refresh | Refresh tooling; reviewed, then kept as the audit trail |
| `skills/<id>-<slug>/SKILL.md` | Drafted from sources, then hand-edited | People. A refresh only produces a proposal for it, never an overwrite. |
| `skills/<id>-<slug>/SOURCES.md` | Pinned links and dedupe summary | Refresh proposes; a person accepts |
| `README.md`, `UPDATING.md`, `guides/`, `agents/`, `commands/` | Hand-written | People |

Rules of thumb:

- If a file starts with the `GENERATED` marker, do not edit it. Change the input and regenerate.
- If you want to add a human note to a generated page, put it in `data/notes/` and rebuild.
- A refresh writes only to `data/refresh/<run-id>/`, to the pins in `data/sources.json`, and to generated files. Anything else it wants to change is written as a proposal in `data/refresh/<run-id>/` for a person to apply.
- `scripts/build-principles.py --check` fails if a generated file is out of date. Run it before every commit. CI will run it later.

## The playbook

### 0. Start

1. Create a branch named `refresh/<run-id>`, for example `refresh/run-2`.
2. In `data/sources.json`, set a new `research_run` (id, date, description).

### 1. Check what moved (built)

```bash
scripts/refresh-sources.py --json data/refresh/run-2/sources-report.json
```

This reads each repo's upstream head and compares it with the pin. Each repo comes back as:

- `unchanged`: nothing to do.
- `changed`: upstream moved. The report includes a compare link.
- `missing`: git could not reach it. It was renamed, deleted or made private. Find out which, and decide whether to replace or drop the source.
- `unpinned`: never pinned. First run only: `scripts/refresh-sources.py --pin`.

### 2. Find new, changed and removed items (not built yet)

For each `changed` repo, compare the pinned commit with upstream head and list the skill, agent and command files that were added, modified, renamed or removed:

```bash
git diff --name-status <pinned_sha> <upstream_sha>
```

Also check whether the licence changed. Update `licence` in `data/sources.json` (an SPDX identifier where GitHub reports one, otherwise a description naming the licence file).

New sources found through the curation lists are added to `data/sources.json` only as `skill-source` entries pointing at the real repo. Never add a curation list's contents wholesale.

### 3. Scan anything new (not built yet)

Run NVIDIA SkillSpector over every new or changed file that could be borrowed. Do not carry forward anything that fails.

### 4. Re-collect and re-dedupe (not built yet)

For each principle whose sources changed, update that skill's source list and dedupe summary, then draft a proposed new `SKILL.md`. These land in `data/refresh/<run-id>/proposals/`. A person diffs each proposal against the current skill and accepts, edits or rejects it.

### 5. Change the principles

- **Add:** append a new number in the category. Set `provenance.origin` to `refresh` and `provenance.research_run` to the new run.
- **Merge:** only if truly duplicate. Keep the clearer one, set `provenance.merged_from` on it, set the other's `status` to `merged`, and log both IDs.
- **Drop:** set `status` to `dropped` and give the reason in `provenance.notes`.
- **Edit wording:** allowed. Log it as an `edit`.

Never delete an entry or reuse a number.

### 6. Re-score (not built yet)

Re-run the test-app workflow for skills that changed, and update `data/scorecard.json` with keep, revise or drop. A changed skill is not accepted until it has been re-scored.

### 7. Re-pin

After you have reviewed a repo's changes, move its pin:

```bash
scripts/refresh-sources.py --repin owner/repo
```

Only re-pin a repo whose changes you have actually handled.

### 8. Regenerate and check

```bash
scripts/build-principles.py
scripts/build-principles.py --check
```

### 9. Log and open the PR

1. Add entries to `data/changelog.json` (types: `add`, `edit`, `merge`, `drop`, `pin`, `repin`, `schema`).
2. Add a dated section to `CHANGELOG.md`.
3. Open a pull request. Say what moved, what was merged or dropped, and what needs a decision.

## Provenance

- Every principle has a `provenance` block: where it came from, which research run, what it was merged from.
- Every skill's `SOURCES.md` lists the source files it came from, linked at the pinned commit, with licence and attribution.
- Hand edits that change the meaning of a principle or skill get a changelog entry.

## Schema versions

Each data file has a `schema_version` (semantic versioning). The matching schema is in `data/schemas/`, and `scripts/build-principles.py` refuses to run on a version it does not know.

To change a schema:

1. Edit the schema in `data/schemas/`.
2. Bump `schema_version` in the schema, in every data file that uses it, and in the scripts that read it.
3. Add a `schema` entry to `data/changelog.json` and a note in `CHANGELOG.md` saying how to migrate.
4. A breaking change bumps the major version.

## Cadence

- About every six months: a full re-run of the playbook.
- Sooner: a source repo is deleted or made private, a licence changes, or a skill in use is found to be unsafe.
- Between runs: small additions and fixes through normal pull requests, each with a changelog entry.
