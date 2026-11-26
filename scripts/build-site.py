#!/usr/bin/env python3
"""Regenerate the static site in docs/ from data/ and guides/developer/.

Usage:
  scripts/build-site.py          write the generated files
  scripts/build-site.py --check  exit 1 if any generated file is stale (for CI)

Standard library only. Hand-written files in docs/ are never touched:
docs/assets/style.css, docs/assets/site.js, docs/.nojekyll and docs/README.md.
Everything else under docs/ is generated; edits are overwritten and extra
files in generated folders are reported as stale.
"""
import csv
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"
GUIDES = ROOT / "guides" / "developer"
PROFILES = ROOT / "template" / "profiles"
REPO_URL = "https://github.com/mitulamin/ai-sdlc-loop"
BLOB = REPO_URL + "/blob/main/"
TREE = REPO_URL + "/tree/main/"
SITE_NAME = "AI SDLC Loop"

GENERATED_DIRS = ["categories", "principles", "guides", "data"]
GENERATED_FILES = [
    "index.html",
    "path.html",
    "principles.html",
    "skills.html",
    "sources.html",
    "data/principles.json",
    "data/sources.json",
    "data/skill-principle-map.json",
    "data/mapping.json",
    "data/licences.json",
    "data/scorecard.csv",
]

# Hand-written teaching text for the learning path, keyed by category slug.
# A category with no entry here still gets a page, with a plain fallback.
PATH_TEXT = {
    "plan-and-specify": (
        "Decide what you are building before any code exists.",
        "Everything later depends on this. A vague ask turns into confident, wrong code, so this stage is about "
        "surfacing assumptions, asking questions and agreeing a spec.",
    ),
    "design-and-architecture": (
        "Shape the code so it is easy to change and easy to test.",
        "Once you know what to build, decide where the boundaries go. Good seams and small interfaces make the "
        "next three stages cheaper.",
    ),
    "code-craft": (
        "Write the smallest change that does the job, in the style already there.",
        "This is the day-to-day work of building. The theme is restraint: no speculative code, no drive-by edits.",
    ),
    "verify": (
        "Prove the code does what you said it would.",
        "Tests are how an agent, or you, can tell working from broken without guessing. These principles cover "
        "what to test and how to keep tests honest.",
    ),
    "debug-and-observe": (
        "When something breaks, find the cause before you change anything.",
        "Debugging is a method, not a hunch. Build a fast feedback loop, reproduce, narrow down, fix, then guard "
        "against it coming back.",
    ),
    "secure": (
        "Treat security as part of building, not a final pass.",
        "Threat-model early, validate what comes in, keep secrets out of the repo, and be explicit about what is "
        "always, sometimes and never allowed.",
    ),
    "review-and-ship": (
        "Get a second pair of eyes on the work, then release it safely.",
        "Review is where mistakes are caught cheaply. Shipping is where they get expensive. These principles cover "
        "both.",
    ),
    "agent-operations": (
        "Run the agents themselves well.",
        "Context is limited and expensive. This stage is about what an agent sees, how skills are loaded, and how "
        "work is split between a coordinator and the agents it starts.",
    ),
    "learn": (
        "Turn what went wrong into a better loop.",
        "The loop gets better only if mistakes change the rules. This closes the cycle and feeds back into "
        "stage one of the next project.",
    ),
}


def esc(s):
    return html.escape(str(s), quote=True)


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def pid_key(pid):
    a, b = pid.split(".")
    return (int(a), int(b))


def canonical_json(obj):
    return json.dumps(obj, indent=2, ensure_ascii=False) + "\n"


NAV = [
    ("index.html", "Home"),
    ("path.html", "Learning path"),
    ("principles.html", "All principles"),
    ("skills.html", "Skills"),
    ("sources.html", "Sources and licences"),
    ("guides/index.html", "Guides"),
]


def label_cells(body):
    """Give each cell of a .sortable table its column heading as data-label, so the stylesheet can stack rows on narrow screens."""

    def table(m):
        t = m.group(0)
        heads = [html.unescape(re.sub(r"<[^>]+>", "", h)).strip() for h in re.findall(r"<th[ >].*?</th>", t, re.S)]
        if not heads:
            return t

        def row(r):
            cells = iter(heads)
            return re.sub(r"<td(?=[ >])", lambda c: f'<td data-label="{esc(next(cells, ""))}"', r.group(0))

        head, sep, rest = t.partition("<tbody>")
        return head + sep + re.sub(r"<tr[ >].*?</tr>", row, rest, flags=re.S)

    return re.sub(r'<table[^>]*class="sortable".*?</table>', table, body, flags=re.S)


def page(title, body, depth, active=None, description=""):
    """Wrap body in the site chrome. depth is the folder depth below docs/."""
    up = "../" * depth
    nav = "".join(
        '<a href="{}{}"{}>{}</a>'.format(
            up, href, ' aria-current="page"' if href == active else "", esc(label)
        )
        for href, label in NAV
    )
    desc = esc(description or "Software engineering principles for building with agents, and a loop that learns from each project.")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} | {SITE_NAME}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="data:,">
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
<div class="wrap header-inner">
<a class="brand" href="{up}index.html">{SITE_NAME}</a>
<nav aria-label="Main">{nav}<a href="{REPO_URL}">GitHub</a></nav>
</div>
</header>
<main id="main" class="wrap">
{label_cells(body)}
</main>
<footer class="site-footer">
<div class="wrap">
<p>{SITE_NAME}. Text and data, including the data copies in <code>docs/data/</code>, are CC BY-SA 4.0; code, including this site, is GPL-3.0; the project template is MIT.
See <a href="{BLOB}LICENSE.md">LICENSE.md</a> and <a href="{BLOB}CREDITS.md">CREDITS.md</a>.
No trackers, no external scripts. Generated from <a href="{TREE}data/">data/</a> by <a href="{BLOB}scripts/build-site.py">scripts/build-site.py</a>.</p>
</div>
</footer>
<script src="{up}assets/site.js" defer></script>
</body>
</html>
"""


def cat_link(cat, up=""):
    return f'<a href="{up}categories/{esc(cat["slug"])}.html">{esc(cat["name"])}</a>'


def slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


# Licence status of a skill, as worded in data/skill-principle-map.json, to a short key and label.
LICENCE_STATUS = [
    ("clean", "clean", "Clean: every source could be adapted"),
    ("rewritten", "rewritten", "Rewritten: link-only sources moved to Further reading"),
    ("rebuilt", "rebuilt", "Rebuilt from MIT sources; the original sources are link only"),
]

# Research repos that are not in data/licences.json (no skill was written from them) but must only ever be
# linked, never copied. Reasons follow CREDITS.md.
NOT_USED_LINK_ONLY = {
    "anthropics/claude-code": "Proprietary (all rights reserved).",
    "hesreallyhim/awesome-claude-code": "CC BY-NC-ND 4.0: no derivatives, not for commercial use.",
    "travisvn/awesome-claude-skills": "No licence file.",
    "sickn33/agentic-awesome-skills": "A curation list that bundles third-party skills; each keeps its upstream licence.",
}


class DataError(Exception):
    pass


def licence_status(raw):
    for prefix, key, label in LICENCE_STATUS:
        if raw.startswith(prefix):
            return key, label
    raise DataError(f"unknown licence status in data/skill-principle-map.json: {raw!r}")


def load_scorecard():
    with open(ROOT / "scorecard.csv", encoding="utf-8", newline="") as f:
        return {r["skill_id"]: r for r in csv.DictReader(f)}


def site_view(pdoc, smap, licences, scorecard):
    """Join the kit's data files into the one model the pages are built from.

    principles.json gives the 103 principles and their aliases; skill-principle-map.json the skill, test app,
    phase, slot and licence status of each; licences.json the adapted and link-only source files of each;
    scorecard.csv the score. Any disagreement between them stops the build.
    """
    cats = [{"number": c["id"], "slug": slugify(c["name"]), "name": c["name"]} for c in pdoc["categories"]]
    slug_by_id = {c["number"]: c["slug"] for c in cats}
    skill_by_pid = {s["principle_id"]: s for s in smap["skills"]}
    ids = [p["id"] for p in pdoc["principles"]]
    if len(ids) != len(set(ids)) or set(ids) != set(skill_by_pid) or set(ids) != set(licences["skills"]):
        raise DataError("principles.json, skill-principle-map.json and licences.json must list the same principle IDs")
    if set(ids) != set(scorecard):
        raise DataError("scorecard.csv must have one row per principle ID")
    if len(ids) != pdoc["count"] or len(smap["skills"]) != smap["count"]:
        raise DataError("a data file's count does not match its entries")
    alias_map = {a["id"]: p["id"] for p in pdoc["principles"] for a in p["aliases"]}
    if alias_map != pdoc["aliases"]:
        raise DataError("principles.json: per-principle aliases do not match the top-level aliases map")
    principles = []
    for p in pdoc["principles"]:
        sk = skill_by_pid[p["id"]]
        lic = licences["skills"][p["id"]]
        row = scorecard[p["id"]]
        if (int(row["slot"]), row["app"], row["phase"]) != (sk["slot"], sk["test_app"], sk["phase"]):
            raise DataError(f"scorecard.csv row {p['id']} disagrees with skill-principle-map.json on slot, app or phase")
        if (sk["clean_sources"], sk["link_only_sources"]) != (len(lic["sources"]), len(lic["link_only"])):
            raise DataError(f"{p['id']}: source counts in skill-principle-map.json and licences.json differ")
        if sk["folder"] != p["skill_folder"]:
            raise DataError(f"{p['id']}: skill folder differs between principles.json and skill-principle-map.json")
        key, label = licence_status(sk["licence_status"])
        if lic["status"] != sk["licence_status"]:
            raise DataError(f"{p['id']}: licence status differs between skill-principle-map.json and licences.json")
        principles.append({
            "id": p["id"],
            "category": slug_by_id[p["category"]],
            "number": pid_key(p["id"])[1],
            "statement": p["statement"],
            "previous_statement": p["previous_statement"],
            "merged": p["aliases"],
            "overlap": p["partial_overlap_with"],
            "skill_folder": sk["folder"],
            "skill_name": sk["skill_name"],
            "phase": sk["phase"],
            "app": sk["test_app"],
            "app_name": sk["test_app_name"],
            "slot": sk["slot"],
            "licence_key": key,
            "licence_label": label,
            "text_licence": sk["text_licence"],
            "build_status": sk["status"],
            "adapted": lic["sources"],
            "link_only": lic["link_only"],
            "score": row,
        })
    return cats, principles


def uniq(items):
    return list(dict.fromkeys(items))


def repo_groups(sdoc, licences, principles):
    """Split every source repo by what the kit may do with it.

    adapted: the licence allowed adapting at least one file. link_only: nothing was copied, only linked.
    unused: researched, but no skill was written from it. A repo adapted in some folders and link only in
    another is in both, and each table shows only the licences that apply to its own files.
    """
    research = {f'{r["owner"]}/{r["repo"]}'.lower(): r for r in sdoc["repos"]}
    for name in NOT_USED_LINK_ONLY:
        if name not in research:
            raise DataError(f"NOT_USED_LINK_ONLY names {name}, which is not in data/sources.json")
    adapted_files, link_files = {}, {}
    for p in principles:
        for f in p["adapted"]:
            adapted_files.setdefault(f["repo"], []).append({**f, "principle": p["id"]})
        for f in p["link_only"]:
            link_files.setdefault(f["repo"], []).append({**f, "principle": p["id"]})
    adapted, link_only = [], []
    for name, info in licences["repos"].items():
        entry = {
            "name": name,
            "url": info["url"],
            "pin": info["pinned_commit"],
            "licence_file": info["licence_file"],
            "adapted_in": sorted({f["principle"] for f in adapted_files.get(name, [])}, key=pid_key),
            "link_only_in": sorted({f["principle"] for f in link_files.get(name, [])}, key=pid_key),
            "link_files": link_files.get(name, []),
            "role": research.get(name.lower(), {}).get("role", "skill-source"),
        }
        if entry["adapted_in"] != sorted(info["adapted_in_skills"], key=pid_key) or entry["link_only_in"] != sorted(
            info["link_only_in_skills"], key=pid_key
        ):
            raise DataError(f"{name}: licences.json lists different skills per repo and per skill")
        if entry["adapted_in"]:
            adapted.append({**entry, "licences": uniq(f["licence"] for f in adapted_files[name])})
        if entry["link_only_in"]:
            reasons = uniq(f'{f["licence"]} ({f["why"]})' for f in link_files[name])
            link_only.append({**entry, "partial": bool(entry["adapted_in"]), "reason": "; ".join(reasons)})
    in_kit = {n.lower() for n in licences["repos"]}
    unused = []
    for key, r in research.items():
        if key in in_kit:
            continue
        name = f'{r["owner"]}/{r["repo"]}'
        entry = {
            "name": name, "url": r["url"], "licences": [r["licence"]], "pin": None, "licence_file": None,
            "adapted_in": [], "link_only_in": [], "link_files": [], "role": r["role"],
        }
        if key in NOT_USED_LINK_ONLY:
            link_only.append({**entry, "partial": False, "reason": NOT_USED_LINK_ONLY[key]})
        else:
            unused.append(entry)
    key = lambda e: e["name"].lower()
    return sorted(adapted, key=key), sorted(link_only, key=key), sorted(unused, key=key)


class Site:
    def __init__(self):
        self.pdoc = load(DATA / "principles.json")
        self.sdoc = load(DATA / "sources.json")
        self.smap = load(DATA / "skill-principle-map.json")
        self.licences = load(DATA / "licences.json")
        self.mapping = load(DATA / "mapping.json")
        self.scorecard_csv = (DATA.parent / "scorecard.csv").read_bytes().decode("utf-8")
        cats, principles = site_view(self.pdoc, self.smap, self.licences, load_scorecard())
        self.cats = sorted(cats, key=lambda c: c["number"])
        self.cat_by_slug = {c["slug"]: c for c in self.cats}
        self.principles = sorted(principles, key=lambda p: pid_key(p["id"]))
        self.by_id = {p["id"]: p for p in self.principles}
        self.by_cat = {c["slug"]: [p for p in self.principles if p["category"] == c["slug"]] for c in self.cats}
        self.aliases = dict(self.pdoc["aliases"])
        self.adapted, self.link_only, self.unused = repo_groups(self.sdoc, self.licences, self.principles)

    def profile_cards(self):
        """The template profiles, in the order the README lists them. Descriptions come from profile.txt."""
        order = [
            ("solo", "Individuals", "Working alone, on your own projects."),
            ("small-team", "Small teams", "A few people sharing one repo."),
            ("large-org", "Large organisations", "Many people, with owners, gates and audit needs."),
        ]
        cards = []
        for slug, who, line in order:
            f = PROFILES / slug / "profile.txt"
            detail = f.read_text(encoding="utf-8").strip() if f.exists() else ""
            cards.append(
                f"""<li class="lp-card">
<h3>{esc(who)}</h3>
<p>{esc(line)}</p>
<p class="lp-profile"><span class="muted">Template profile</span> <code>{esc(slug)}</code></p>
<p class="muted">{esc(detail)}</p>
</li>"""
            )
        return "".join(cards)

    def landing_page(self):
        n_principles = len(self.principles)
        n_cats = len(self.cats)
        n_sources = len(self.sdoc["repos"])
        n_repos = len({e["name"].lower() for e in self.adapted + self.link_only + self.unused})
        n_merged = len(self.aliases)
        first_cat = self.cats[0]
        merged_links = ", ".join(
            f'<a href="principles/{esc(a)}.html">{esc(a)} to {esc(t)}</a>'
            for a, t in sorted(self.aliases.items(), key=lambda kv: pid_key(kv[0]))
        )
        learn = self.cat_by_slug.get("learn")
        learn_ids = [p["id"] for p in self.by_cat.get("learn", [])]
        learn_range = f"{learn_ids[0]} to {learn_ids[-1]}" if learn_ids else ""
        learn_link = (
            f'<a href="categories/{esc(learn["slug"])}.html">the {esc(learn["name"])} category</a>'
            + (f" (principles {learn_range})" if learn_range else "")
            if learn
            else "the last category"
        )
        stage_chips = "".join(
            f'<li><a class="chip" href="categories/{esc(c["slug"])}.html">{c["number"]}. {esc(c["name"])}</a></li>'
            for c in self.cats
        )
        body = f"""<section class="lp-hero" aria-labelledby="lp-title">
<p class="lp-eyebrow">Open source starter for agentic software development</p>
<h1 id="lp-title">Software engineering principles for building with agents, and a loop that learns from each project</h1>
<p class="lede">I distilled what {n_sources} public repos teach about working with coding agents into {n_principles} principles
in {n_cats} categories. Use them to adopt agentic tools with less trial and error, then build a learning loop of your own.</p>
<p class="lp-cta">
<a class="btn btn-primary" href="path.html">Explore the learning path</a>
<a class="btn" href="#start">Start a project</a>
<a class="btn" href="principles.html">Browse all principles</a>
</p>
<dl class="lp-stats">
<div><dt>Principles</dt><dd>{n_principles}</dd></div>
<div><dt>Skills</dt><dd>{n_principles}</dd></div>
<div><dt>Categories</dt><dd>{n_cats}</dd></div>
<div><dt>Source repos</dt><dd>{n_repos}</dd></div>
<div><dt>Merged IDs</dt><dd>{n_merged}</dd></div>
</dl>
</section>

<section class="lp-section" aria-labelledby="why">
<h2 id="why">What this is and why it exists</h2>
<div class="lp-cols">
<div>
<p>At Shravi Limited we are building aidev, a software engineering team in a box. I wanted agents that do real software work end to end without me steering every step.</p>
<p>The ideas for that are scattered across dozens of public repos: skills, sub-agents, slash commands and rules files. Many say the same thing in different words. Some contradict each other. Some are risky to install. And if you load them all, their descriptions alone use up the context window before the agent does anything useful.</p>
</div>
<div>
<p>So I had a research bot read {n_sources} public repos and boil them down to {n_principles} numbered principles in {n_cats} categories, with one amalgamated skill for each. Each one is traceable to the repos it came from.</p>
<p>The research first found {n_principles + n_merged} principles. {n_merged} were duplicates and were merged into the principle that kept their content; IDs are never renumbered, so a merged ID still opens its survivor ({merged_links}). See <a href="{BLOB}MERGES.md">MERGES.md</a>.</p>
<p>The principles are not the point. The point is the loop that produced them and the loop that keeps improving them. This repo is a base, not a finished product. Fork it, swap in your own principles, and let your own projects change it.</p>
</div>
</div>
</section>

<section class="lp-section" aria-labelledby="who">
<h2 id="who">Who it is for</h2>
<p>An individual and a large company share the same principles. What changes is ceremony: gates, roles, review and ownership. So there is one shared template, and three profiles that switch that ceremony on or off.</p>
<ul class="lp-cards">{self.profile_cards()}</ul>
<p class="muted">If you are unsure, start with <code>solo</code> or <code>small-team</code>. It is easier to add ceremony later than to remove it.</p>
</section>

<section class="lp-section" aria-labelledby="how">
<h2 id="how">How it works</h2>
<ol class="lp-cards lp-steps">
<li class="lp-card">
<h3>One coordinator</h3>
<p>I talk to one agent, the coordinator. It does not do the work. It plans, then starts new agents with blank contexts and gives each exactly the context its job needs.</p>
<p class="muted">An agent that has not seen the whole conversation cannot be misled by it.</p>
</li>
<li class="lp-card">
<h3>Producer and adversarial reviewer</h3>
<p>Every phase is a pair. The producer gets the dos and don'ts for that phase. The reviewer checks only against the don'ts and known failure modes, and is there to find problems.</p>
<p class="muted">Loops run on their own and come back at the end of a cycle.</p>
</li>
<li class="lp-card">
<h3>Human review feeds Learn</h3>
<p>After the last phase there is a human acceptance review. My feedback goes to {learn_link}, which asks which phase failed, which rule was at fault, and how to harden the checklist.</p>
<p class="muted">A change goes live only if it helps on held-out cases and a human approves it.</p>
</li>
</ol>
</section>

<section class="lp-section" aria-labelledby="do">
<h2 id="do">What you can do here</h2>
<ul class="lp-cards lp-links">
<li class="lp-card"><h3><a href="path.html">Follow the learning path</a></h3><p>Walk the {n_cats} stages in order, from planning to retrospective.</p></li>
<li class="lp-card"><h3><a href="principles.html">Explore the principles</a></h3><p>Search, filter and sort all {n_principles}. Each links to its skill and sources.</p></li>
<li class="lp-card"><h3><a href="categories/{esc(first_cat["slug"])}.html">Read the categories</a></h3><p>One page per category, with the principles that belong to it.</p></li>
<li class="lp-card"><h3><a href="skills.html">See the skills</a></h3><p>One skill per principle, with its test app, phase and slot in the run order.</p></li>
<li class="lp-card"><h3><a href="sources.html">Check the sources and licences</a></h3><p>The licence of every source repo, with link-only sources listed separately.</p></li>
<li class="lp-card"><h3><a href="guides/index.html">Read the guides</a></h3><p>Plain-language guides to the principles.</p></li>
<li class="lp-card"><h3><a href="#start">Start a project</a></h3><p>Copy the template and run your first loop.</p></li>
</ul>
<h3 class="lp-sub">The {n_cats} categories</h3>
<ul class="lp-chips">{stage_chips}</ul>
</section>

<section class="lp-section" id="start" aria-labelledby="start-title">
<h2 id="start-title">Start a project from the template</h2>
<p>Clone the repo and run <a href="{BLOB}scripts/new-project.sh"><code>scripts/new-project.sh</code></a> with a profile. It copies the shared base from <a href="{TREE}template/"><code>template/</code></a>, applies the profile, and runs <code>git init</code>. It refuses a target folder that is not empty.</p>
<pre tabindex="0"><code>git clone {esc(REPO_URL)}
cd ai-sdlc-loop
scripts/new-project.sh ../my-new-project              # solo, the default
scripts/new-project.sh ../my-new-project small-team
scripts/new-project.sh ../my-new-project large-org</code></pre>
<p>Then edit the new project's <code>AGENTS.md</code>, read its <code>PROCESS.md</code>, and start your first loop. More in <a href="{REPO_URL}#start-a-new-project-from-the-template">the README</a>.</p>
</section>

<section class="lp-section lp-final" aria-labelledby="next">
<h2 id="next">Where to go next</h2>
<p class="lp-cta">
<a class="btn btn-primary" href="path.html">Start at the learning path</a>
<a class="btn" href="categories/{esc(first_cat["slug"])}.html">Jump to stage 1: {esc(first_cat["name"])}</a>
<a class="btn" href="{REPO_URL}">View on GitHub</a>
</p>
<p class="muted">Open source. Code is GPL-3.0, written content is CC BY-SA 4.0, and the project template is MIT.
Details in <a href="{REPO_URL}#why-gplv3-and-cc-by-sa-for-the-writing">the README</a>.</p>
</section>"""
        return page(
            "Principles for building with agents",
            body,
            0,
            "index.html",
            f"{n_principles} software engineering principles distilled from {n_sources} public repos, and a template to start your own agentic loop.",
        )

    def path_page(self):
        total = len(self.principles)
        steps = []
        for c in self.cats:
            ps = self.by_cat[c["slug"]]
            tag, why = PATH_TEXT.get(
                c["slug"], (f"{len(ps)} principles in this category.", "Read the principles in order.")
            )
            first = ps[0] if ps else None
            sample = (
                f'<p class="sample">Start with <a href="principles/{esc(first["id"])}.html">{esc(first["id"])}</a>: '
                f'{esc(first["statement"])}</p>'
                if first
                else ""
            )
            steps.append(
                f"""<li class="step">
<div class="step-num" aria-hidden="true">{c["number"]}</div>
<div class="step-body">
<h3><a href="categories/{esc(c["slug"])}.html">{esc(c["name"])}</a> <span class="count">{len(ps)} principles</span></h3>
<p class="tag">{esc(tag)}</p>
<p>{esc(why)}</p>
{sample}
</div>
</li>"""
            )
        body = f"""<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Learning path</nav>
<section class="hero">
<h1>A learning path through {total} software principles</h1>
<p class="lede">These principles were distilled from {len(self.sdoc["repos"])} public repos of agent skills, sub-agents and commands.
They are the base of a loop that builds software with agents and learns from each project.
Work through the nine stages in order, or jump straight to the one you need.</p>
<form class="search" action="principles.html" method="get" role="search">
<label for="home-q" class="sr">Search principles</label>
<input id="home-q" name="q" type="search" placeholder="Search principles, e.g. test, secret, review" autocomplete="off">
<button type="submit">Search</button>
</form>
<p class="quick"><a href="categories/{esc(self.cats[0]["slug"])}.html">Start at stage 1</a>
<a href="principles.html">Browse the table</a>
<a href="guides/index.html">Read the developer guide</a>
<a href="index.html">About this project</a></p>
</section>
<section>
<h2>The nine stages</h2>
<p>The order follows a project from idea to retrospective. Stage 9 feeds back into stage 1 of the next project.</p>
<ol class="steps">
{"".join(steps)}
</ol>
</section>
<section>
<h2>How to use this</h2>
<ul>
<li>New to this? Read the stages in order and open a few principles in each.</li>
<li>Looking for something specific? <a href="principles.html">Search and filter</a> all {total} principles, or sort the table.</li>
<li>Want to know where an idea came from? Every principle links to the source repos it was drawn from, and the <a href="sources.html">sources page</a> lists all of them with their licences.</li>
</ul>
</section>"""
        return page("Learning path", body, 0, "path.html")

    def category_page(self, i):
        c = self.cats[i]
        ps = self.by_cat[c["slug"]]
        tag, why = PATH_TEXT.get(c["slug"], (f"{len(ps)} principles.", ""))
        rows = "".join(
            f'<li><a class="pid" href="../principles/{esc(p["id"])}.html">{esc(p["id"])}</a> '
            f'<span>{esc(p["statement"])}</span></li>'
            for p in ps
        )
        prev = self.cats[i - 1] if i > 0 else None
        nxt = self.cats[i + 1] if i + 1 < len(self.cats) else None
        pager = '<nav class="pager" aria-label="Learning path">'
        pager += (
            f'<a class="prev" href="{esc(prev["slug"])}.html"><small>Previous stage</small>{esc(prev["name"])}</a>'
            if prev
            else '<a class="prev" href="../path.html"><small>Back to</small>Learning path</a>'
        )
        pager += (
            f'<a class="next" href="{esc(nxt["slug"])}.html"><small>Next stage</small>{esc(nxt["name"])}</a>'
            if nxt
            else '<a class="next" href="../principles.html"><small>Finished</small>All principles</a>'
        )
        pager += "</nav>"
        body = f"""<nav class="crumbs" aria-label="Breadcrumb"><a href="../index.html">Home</a> / <a href="../path.html">Learning path</a> / Stage {c["number"]}</nav>
<h1>Stage {c["number"]}: {esc(c["name"])}</h1>
<p class="lede">{esc(tag)}</p>
<p>{esc(why)}</p>
<h2>{len(ps)} principles</h2>
<ol class="plist">{rows}</ol>
{pager}"""
        return page(c["name"], body, 1, "path.html", tag)

    def licence_badge(self, p):
        short = {"clean": "Clean", "rewritten": "Rewritten", "rebuilt": "Rebuilt"}[p["licence_key"]]
        return f'<span class="lic lic-{p["licence_key"]}" title="{esc(p["licence_label"])}">{short}</span>'

    def source_list(self, files):
        """Source files grouped by repo, in the order the data gives them."""
        groups = {}
        for f in files:
            groups.setdefault(f["repo"], []).append(f)
        out = []
        for repo, fs in groups.items():
            licences = ", ".join(dict.fromkeys(f["licence"] for f in fs))
            items = "".join(
                f'<li><a href="{esc(f["url"])}"><code>{esc(f["path"])}</code></a>'
                + (f' <span class="muted">({esc(f["licence"])}; {esc(f["why"])})</span>' if f.get("why") else f' <span class="muted">({esc(f["licence"])})</span>')
                + "</li>"
                for f in fs
            )
            out.append(
                f'<li><a href="https://github.com/{esc(repo)}">{esc(repo)}</a> '
                f'<span class="muted">{esc(licences)}</span><ul>{items}</ul></li>'
            )
        return "".join(out)

    def principle_page(self, idx):
        p = self.principles[idx]
        c = self.cat_by_slug[p["category"]]
        merged = "".join(
            f'<li><a href="{esc(m["id"])}.html">{esc(m["id"])}</a>: {esc(m["statement"])}</li>' for m in p["merged"]
        )
        merged_html = (
            "<dt>Also known as</dt><dd>"
            + ", ".join(f'<a href="{esc(m["id"])}.html">{esc(m["id"])}</a>' for m in p["merged"])
            + " (merged duplicates; each ID opens this principle)</dd>"
            if p["merged"]
            else ""
        )
        history = ""
        if p["merged"] or p["previous_statement"] or p["overlap"]:
            parts = []
            if p["merged"]:
                parts.append(f'<p>Merged duplicates, kept as aliases (see <a href="{BLOB}MERGES.md">MERGES.md</a>):</p><ul>{merged}</ul>')
            if p["previous_statement"]:
                parts.append(f'<p>Wording before the merge: {esc(p["previous_statement"])}</p>')
            if p["overlap"]:
                o = self.by_id[p["overlap"]]
                parts.append(
                    f'<p>Partly overlaps <a href="{esc(o["id"])}.html">{esc(o["id"])}</a> '
                    f'({esc(o["statement"])}); kept as a separate principle.</p>'
                )
            history = "<h2>History</h2>" + "".join(parts)
        score = p["score"]
        scored = score["total_0_10"] or "not run yet"
        verdict = score["verdict_keep_merge_drop"] or "none yet"
        if p["link_only"]:
            link_html = (
                '<div class="link-only"><h2>Link only: not copied or adapted</h2>'
                "<p>These sources could not be adapted because of their licence. Nothing was copied from them; "
                "they are linked as further reading.</p>"
                f'<ul class="sources">{self.source_list(p["link_only"])}</ul></div>'
            )
        else:
            link_html = '<h2>Link only</h2><p>None. Every source for this skill could be adapted.</p>'
        prev = self.principles[idx - 1] if idx > 0 else None
        nxt = self.principles[idx + 1] if idx + 1 < len(self.principles) else None
        pager = '<nav class="pager" aria-label="Neighbouring principles">'
        pager += (
            f'<a class="prev" href="{esc(prev["id"])}.html"><small>Previous</small>{esc(prev["id"])}</a>'
            if prev
            else "<span></span>"
        )
        pager += (
            f'<a class="next" href="{esc(nxt["id"])}.html"><small>Next</small>{esc(nxt["id"])}</a>'
            if nxt
            else "<span></span>"
        )
        pager += "</nav>"
        body = f"""<nav class="crumbs" aria-label="Breadcrumb"><a href="../index.html">Home</a> / <a href="../path.html">Learning path</a> /
<a href="../categories/{esc(c["slug"])}.html">Stage {c["number"]}: {esc(c["name"])}</a> / {esc(p["id"])}</nav>
<p class="pid-big">Principle {esc(p["id"])}</p>
<h1>{esc(p["statement"])}</h1>
<dl class="facts">
<dt>Category</dt><dd><a href="../categories/{esc(c["slug"])}.html">{esc(c["name"])}</a></dd>
<dt>Skill</dt><dd><a href="{BLOB}{esc(p["skill_folder"])}/SKILL.md">{esc(p["skill_name"])}</a> <span class="muted">({esc(p["build_status"])})</span></dd>
<dt>Phase</dt><dd>{esc(p["phase"])}</dd>
<dt>Test app</dt><dd>{esc(p["app_name"])}</dd>
<dt>Test slot</dt><dd>{p["slot"]} of {len(self.principles)} (<a href="../skills.html">run order</a>)</dd>
<dt>Licence status</dt><dd>{self.licence_badge(p)} <span class="muted">{esc(p["licence_label"])}. The skill text is {esc(p["text_licence"])}.</span></dd>
<dt>Score</dt><dd>{esc(scored)} <span class="muted">(verdict: {esc(verdict)})</span></dd>
{merged_html}</dl>
{history}
<h2>Adapted sources</h2>
<p>{len(p["adapted"])} source files this skill was written from, each pinned to a commit with its licence. The skill text is our own wording; see <a href="../sources.html">all sources</a> and <a href="{BLOB}CREDITS.md">CREDITS.md</a>.</p>
<ul class="sources">{self.source_list(p["adapted"])}</ul>
{link_html}
<h2>In the repo</h2>
<p><a href="{BLOB}{esc(p["skill_folder"])}/SKILL.md">SKILL.md</a>, <a href="{BLOB}{esc(p["skill_folder"])}/SOURCES.md">SOURCES.md</a>, and
<a href="{BLOB}principles/{esc(p["id"])}.md">this principle as markdown</a>.</p>
{pager}"""
        return page(f'{p["id"]} {p["statement"]}', body, 1, "principles.html", p["statement"])

    def alias_page(self, alias, target):
        m = next(m for m in target["merged"] if m["id"] == alias)
        body = f"""<p class="pid-big">Principle {esc(alias)} <span class="badge">merged</span></p>
<h1>{esc(alias)} now opens {esc(target["id"])}</h1>
<p>Principle {esc(alias)} ({esc(m["statement"])}) was a duplicate and was merged into
<a href="{esc(target["id"])}.html">principle {esc(target["id"])}</a>: {esc(target["statement"])}</p>
<p>IDs are never renumbered, so {esc(alias)} stays valid as an alias. Nothing was lost in the merge. See <a href="{BLOB}MERGES.md">MERGES.md</a>.</p>
<p><a class="btn btn-primary" href="{esc(target["id"])}.html">Open principle {esc(target["id"])}</a></p>"""
        refresh = f'<meta http-equiv="refresh" content="0; url={esc(target["id"])}.html">\n<link rel="canonical" href="{esc(target["id"])}.html">\n'
        return page(f"Principle {alias} (merged into {target['id']})", body, 1, "principles.html").replace("</head>", refresh + "</head>", 1)

    def table_page(self):
        n = len(self.principles)
        rows = []
        for p in self.principles:
            c = self.cat_by_slug[p["category"]]
            also = "".join(
                f' <span class="alias">also <a href="principles/{esc(m["id"])}.html">{esc(m["id"])}</a></span>' for m in p["merged"]
            )
            repos = sorted({f["repo"] for f in p["adapted"]} | {f["repo"] for f in p["link_only"]}, key=str.lower)
            rows.append(
                f'<tr data-cat="{esc(c["slug"])}" data-phase="{esc(p["phase"])}" data-app="{esc(p["app"])}" '
                f'data-licence="{esc(p["licence_key"])}" data-source="{esc("|".join(repos))}">'
                f'<td data-sort="{pid_key(p["id"])[0] * 1000 + pid_key(p["id"])[1]}"><a href="principles/{esc(p["id"])}.html">{esc(p["id"])}</a>{also}</td>'
                f'<td>{esc(p["statement"])}</td>'
                f'<td data-sort="{c["number"]}">{cat_link(c)}</td>'
                f'<td>{esc(p["phase"])}</td>'
                f'<td>{esc(p["app"])}</td>'
                f'<td data-sort="{p["slot"]}">{p["slot"]}</td>'
                f'<td>{self.licence_badge(p)}</td></tr>'
            )
        cat_opts = "".join(f'<option value="{esc(c["slug"])}">{c["number"]}. {esc(c["name"])}</option>' for c in self.cats)
        repos = sorted({f["repo"] for p in self.principles for f in p["adapted"] + p["link_only"]}, key=str.lower)
        src_opts = "".join(f'<option value="{esc(r)}">{esc(r)}</option>' for r in repos)
        merged_rows = "".join(
            f'<li><a href="principles/{esc(a)}.html">{esc(a)}</a> opens <a href="principles/{esc(t)}.html">{esc(t)}</a>: '
            f'<span class="muted">{esc(next(m["statement"] for m in self.by_id[t]["merged"] if m["id"] == a))}</span></li>'
            for a, t in sorted(self.aliases.items(), key=lambda kv: pid_key(kv[0]))
        )
        body = f"""<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / All principles</nav>
<h1>All principles</h1>
<p>{n} principles: the original {n + len(self.aliases)} less {len(self.aliases)} merged duplicates (see <a href="{BLOB}MERGES.md">MERGES.md</a>).
IDs are never renumbered, so a merged ID is kept as an alias and opens the principle it was merged into.
Search and filter, and on a wide screen click a column heading to sort (on a phone each row is a card, so use the filters). With JavaScript off you still get the full table.</p>
<div class="filters" role="search" data-table="ptable">
<label>Search <input data-q type="search" placeholder="e.g. test or 4.4" autocomplete="off"></label>
<label>Category <select data-attr="cat"><option value="">All categories</option>{cat_opts}</select></label>
<label>Phase <select data-attr="phase"><option value="">All phases</option>{self.phase_options()}</select></label>
<label>Test app <select data-attr="app"><option value="">All apps</option>{self.app_options()}</select></label>
<label>Licence status <select data-attr="licence"><option value="">All</option>{self.licence_options()}</select></label>
<label>Source repo (adapted or linked) <select data-attr="source"><option value="">All sources</option>{src_opts}</select></label>
<button type="button" data-reset>Reset</button>
</div>
<p data-count class="muted" aria-live="polite">{n} principles</p>
<div class="table-wrap">
<table id="ptable" class="sortable">
<thead><tr>
<th scope="col" data-type="num">ID</th>
<th scope="col" data-type="text">Principle</th>
<th scope="col" data-type="num">Category</th>
<th scope="col" data-type="text">Phase</th>
<th scope="col" data-type="text">Test app</th>
<th scope="col" data-type="num">Slot</th>
<th scope="col" data-type="text">Licence</th>
</tr></thead>
<tbody>
{chr(10).join(rows)}
</tbody>
</table>
</div>
<h2 id="merged">Merged IDs</h2>
<p>These {len(self.aliases)} IDs were retired. Each one opens the principle that kept its content.</p>
<ul class="merged-list">{merged_rows}</ul>
<p class="muted">Machine-readable copies: <a href="data/principles.json">principles.json</a>,
<a href="data/skill-principle-map.json">skill-principle-map.json</a>, <a href="data/scorecard.csv">scorecard.csv</a>.</p>"""
        return page("All principles", body, 0, "principles.html")

    def phase_options(self):
        first = {}
        for p in self.principles:
            first[p["phase"]] = min(first.get(p["phase"], p["slot"]), p["slot"])
        return "".join(f'<option value="{esc(ph)}">{esc(ph)}</option>' for ph in sorted(first, key=first.get))

    def app_options(self):
        apps = {}
        for p in self.principles:
            apps[p["app"]] = p["app_name"]
        return "".join(f'<option value="{esc(k)}">{esc(v)}</option>' for k, v in sorted(apps.items()))

    def licence_options(self):
        return "".join(f'<option value="{k}">{esc(label)}</option>' for _, k, label in LICENCE_STATUS)

    def skills_page(self):
        n = len(self.principles)
        by_slot = sorted(self.principles, key=lambda p: p["slot"])
        scored = sum(1 for p in by_slot if p["score"]["total_0_10"])
        rows = []
        for p in by_slot:
            sc = p["score"]
            rows.append(
                f'<tr data-phase="{esc(p["phase"])}" data-app="{esc(p["app"])}" data-licence="{esc(p["licence_key"])}">'
                f'<td data-sort="{p["slot"]}">{p["slot"]}</td>'
                f'<td data-sort="{pid_key(p["id"])[0] * 1000 + pid_key(p["id"])[1]}"><a href="principles/{esc(p["id"])}.html">{esc(p["id"])}</a></td>'
                f'<td><a href="{BLOB}{esc(p["skill_folder"])}/SKILL.md">{esc(p["skill_name"])}</a></td>'
                f'<td>{esc(p["phase"])}</td>'
                f'<td>{esc(p["app"])}</td>'
                f'<td>{self.licence_badge(p)}</td>'
                f'<td data-sort="{esc(sc["total_0_10"] or -1)}">{esc(sc["total_0_10"]) if sc["total_0_10"] else "not run"}</td>'
                f'<td>{esc(sc["verdict_keep_merge_drop"]) if sc["verdict_keep_merge_drop"] else "none yet"}</td></tr>'
            )
        apps = {}
        for p in by_slot:
            apps.setdefault(p["app"], {"name": p["app_name"], "n": 0})["n"] += 1
        app_cards = "".join(
            f'<li class="lp-card"><h3>{esc(k)}</h3><p>{esc(v["name"])}</p><p class="muted">{v["n"]} skills</p></li>'
            for k, v in sorted(apps.items())
        )
        phases = {}
        for p in by_slot:
            phases.setdefault(p["phase"], []).append(p["slot"])
        phase_rows = "".join(
            f"<li><strong>{esc(ph)}</strong> <span class=\"muted\">slots {min(sl)} to {max(sl)}, {len(sl)} skills</span></li>"
            for ph, sl in phases.items()
        )
        body = f"""<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Skills</nav>
<h1>The {n} skills and their test slots</h1>
<p>There is exactly one amalgamated skill per principle. Each has a test app, a phase and a slot: the slot is the run order, and the test app is the project it is exercised on. Skills are scored in
<a href="{BLOB}scorecard.csv">scorecard.csv</a>; {scored} of {n} have been scored so far. The workflow is described in the <a href="{BLOB}README.md">README</a>.</p>
<h2>Test apps</h2>
<ul class="lp-cards">{app_cards}</ul>
<p class="muted">&ldquo;All&rdquo; skills are used on every run: the harness skills (stage 8) and the Learn skills (stage 9).</p>
<h2>Phases in run order</h2>
<ul class="phase-list">{phase_rows}</ul>
<h2>Run order</h2>
<div class="filters" role="search" data-table="stable">
<label>Search <input data-q type="search" placeholder="Skill name or principle ID" autocomplete="off"></label>
<label>Phase <select data-attr="phase"><option value="">All phases</option>{self.phase_options()}</select></label>
<label>Test app <select data-attr="app"><option value="">All apps</option>{self.app_options()}</select></label>
<label>Licence status <select data-attr="licence"><option value="">All</option>{self.licence_options()}</select></label>
<button type="button" data-reset>Reset</button>
</div>
<p data-count class="muted" aria-live="polite">{n} skills</p>
<div class="table-wrap">
<table id="stable" class="sortable">
<thead><tr>
<th scope="col" data-type="num">Slot</th>
<th scope="col" data-type="num">Principle</th>
<th scope="col" data-type="text">Skill</th>
<th scope="col" data-type="text">Phase</th>
<th scope="col" data-type="text">Test app</th>
<th scope="col" data-type="text">Licence</th>
<th scope="col" data-type="num">Score /10</th>
<th scope="col" data-type="text">Verdict</th>
</tr></thead>
<tbody>
{chr(10).join(rows)}
</tbody>
</table>
</div>
<p class="muted">Machine-readable copies: <a href="data/skill-principle-map.json">skill-principle-map.json</a>, <a href="data/scorecard.csv">scorecard.csv</a>.</p>"""
        return page("Skills", body, 0, "skills.html", f"The {n} amalgamated skills with their test app, phase and slot.")

    def id_links(self, ids, up=""):
        return ", ".join(f'<a href="{up}principles/{esc(i)}.html">{esc(i)}</a>' for i in ids)

    def skills_cell(self, ids):
        if not ids:
            return '<span class="muted">none, not used</span>'
        return f"<details><summary>{len(ids)} skill{'s' if len(ids) != 1 else ''}</summary>{self.id_links(ids)}</details>"

    def repo_cell(self, e):
        return f'<a href="{esc(e["url"])}">{esc(e["name"])}</a>'

    def sources_page(self):
        split = self.licences["split"]
        n_link_only_files = sum(len(p["link_only"]) for p in self.principles)
        def pin_cell(e):
            pin = esc(e["pin"][:10])
            return f'<a href="{esc(e["licence_file"])}">{pin}</a>' if e["licence_file"] else pin

        adapted_rows = "".join(
            f'<tr><td>{self.repo_cell(e)}'
            + (' <span class="badge">link-only folder</span>' if e["link_only_in"] else "")
            + f'</td><td>{esc("; ".join(e["licences"]))}</td>'
            f'<td data-sort="{len(e["adapted_in"])}">{self.skills_cell(e["adapted_in"])}</td>'
            f"<td>{pin_cell(e)}</td></tr>"
            for e in self.adapted
        )

        def files_cell(e):
            if not e["link_files"]:
                return '<span class="muted">repo link only</span>'
            items = "".join(
                f'<li><a href="{esc(f["url"])}"><code>{esc(f["path"])}</code></a> '
                f'<span class="muted">(skill {esc(f["principle"])}; {esc(f["why"])})</span></li>'
                for f in e["link_files"]
            )
            return f"<details><summary>{len(e['link_files'])} linked file{'s' if len(e['link_files']) != 1 else ''}</summary><ul>{items}</ul></details>"

        link_rows = "".join(
            f'<tr><td>{self.repo_cell(e)}'
            + (' <span class="badge">only this folder</span>' if e["partial"] else "")
            + f'</td><td>{esc(e["reason"])}</td>'
            f'<td data-sort="{len(e["link_only_in"])}">{self.skills_cell(e["link_only_in"])}</td>'
            f"<td>{files_cell(e)}</td></tr>"
            for e in self.link_only
        )
        unused_rows = "".join(
            f'<tr><td>{self.repo_cell(e)}</td><td>{esc(e["role"])}</td><td>{esc("; ".join(e["licences"]))}</td></tr>'
            for e in self.unused
        )
        run = self.sdoc["research_run"]
        n_repos = len({e["name"].lower() for e in self.adapted + self.link_only + self.unused})
        body = f"""<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Sources</nav>
<h1>Sources and licences</h1>
<p>Every skill was written from public repos whose licences allow adapting them. Sources that could not be adapted were never copied; they are only linked, and they are listed separately below.
Licences were checked on {esc(self.licences["checked"])}. {esc(self.licences["disclaimer"])}</p>
<div class="split">
<div><h2>Text</h2><p>Skills, principles, guides and data: <strong>{esc(split["text"])}</strong>.</p></div>
<div><h2>Code</h2><p>Scripts, this site and CI: <strong>{esc(split["code"])}</strong>.</p></div>
</div>
<p>See <a href="{BLOB}LICENSE.md">LICENSE.md</a>, <a href="{BLOB}CREDITS.md">CREDITS.md</a> (copyright notices and pinned commits) and <a href="{BLOB}ATTRIBUTIONS.md">ATTRIBUTIONS.md</a>.
Each skill's <code>SOURCES.md</code> lists its files, pinned to a commit.</p>
<p>{n_repos} repos in all: {len(self.sdoc["repos"])} from the initial research ({esc(run["id"])}, {esc(run["date"])}) and {n_repos - len(self.sdoc["repos"])} more added during the licence cleanup. A repo can be adapted for one folder and link only for another, so the three groups below add up to more than {n_repos}.</p>
<ul class="lp-cards">
<li class="lp-card"><h3>{len(self.adapted)}</h3><p>Adapted source repos</p></li>
<li class="lp-card"><h3>{len(self.link_only)}</h3><p>Link-only source repos, whole or in part</p><p class="muted">{n_link_only_files} linked files across {sum(1 for p in self.principles if p["link_only"])} skills</p></li>
<li class="lp-card"><h3>{len(self.unused)}</h3><p>Researched, not used</p></li>
</ul>

<h2 id="adapted">Adapted sources ({len(self.adapted)})</h2>
<p>The licence allows adapting. The skill text is our own wording; the pinned commit is the version that was read. Repos marked <span class="badge">link-only folder</span> are also in the link-only list below, for one folder.</p>
<div class="table-wrap">
<table class="sortable">
<thead><tr>
<th scope="col" data-type="text">Repo</th>
<th scope="col" data-type="text">Licence</th>
<th scope="col" data-type="num">Skills adapted</th>
<th scope="col" data-type="text">Pinned commit (opens its licence file)</th>
</tr></thead>
<tbody>
{adapted_rows}
</tbody>
</table>
</div>

<div class="link-only" id="link-only">
<h2>Link only: not copied or adapted ({len(self.link_only)})</h2>
<p>No licence we can rely on, a proprietary or non-commercial licence, or a curation list. Nothing was copied or adapted from these. Where a skill leaned on one, its text was rewritten from adaptable sources and the link moved to &ldquo;Further reading (link only)&rdquo; in that skill's <code>SOURCES.md</code>.</p>
<div class="table-wrap">
<table class="sortable">
<thead><tr>
<th scope="col" data-type="text">Repo</th>
<th scope="col" data-type="text">Licence situation</th>
<th scope="col" data-type="num">Linked from skills</th>
<th scope="col" data-type="text">What is linked</th>
</tr></thead>
<tbody>
{link_rows}
</tbody>
</table>
</div>
</div>

<h2 id="unused">Researched, not used ({len(self.unused)})</h2>
<p>Read during research but no skill was written from them. Nothing was copied.</p>
<div class="table-wrap">
<table class="sortable">
<thead><tr>
<th scope="col" data-type="text">Repo</th>
<th scope="col" data-type="text">Role</th>
<th scope="col" data-type="text">Licence</th>
</tr></thead>
<tbody>
{unused_rows}
</tbody>
</table>
</div>
<p class="muted">Machine-readable copies: <a href="data/licences.json">licences.json</a>, <a href="data/mapping.json">mapping.json</a>, <a href="data/sources.json">sources.json</a>.</p>"""
        return page("Sources and licences", body, 0, "sources.html", "The licence of every source repo, with link-only sources listed separately.")

    def guide_pages(self):
        out = {}
        files = sorted(GUIDES.glob("*.md"))
        entries = []
        for f in files:
            slug = "index" if f.name == "README.md" else f.stem
            text = f.read_text(encoding="utf-8")
            title_m = re.search(r"^#\s+(.+)$", text, re.M)
            title = title_m.group(1).strip() if title_m else f.stem
            stub = "coming later" in text.lower()
            rel = f.relative_to(ROOT).as_posix()
            banner = (
                '<div class="notice"><strong>This guide is still a stub.</strong> The page below is the placeholder text '
                f'from <a href="{BLOB}{rel}">{esc(rel)}</a>. The full guide is not written yet.</div>'
                if stub
                else ""
            )
            body_html = render_markdown(text, f.parent)
            out[f"guides/developer/{slug}.html"] = page(
                title, f'<nav class="crumbs" aria-label="Breadcrumb"><a href="../../index.html">Home</a> / <a href="../index.html">Guides</a> / {esc(title)}</nav>\n{banner}\n<article class="prose">{body_html}</article>',
                2, "guides/index.html",
            )
            entries.append((slug, title, stub))
        badge = ' <span class="badge">stub</span>'
        listing = "".join(
            f'<li><a href="developer/{slug}.html">{esc(title)}</a>{badge if stub else ""}</li>'
            for slug, title, stub in entries
        )
        body = f"""<nav class="crumbs" aria-label="Breadcrumb"><a href="../index.html">Home</a> / Guides</nav>
<h1>Guides</h1>
<p>Plain-language guides to the principles. They cover everything, including what experienced developers already know.</p>
<h2>Developer guides</h2>
<ul>{listing}</ul>
<p class="muted">Source: <a href="{TREE}guides/developer/">guides/developer/</a>. A page marked stub holds placeholder text until the guide is written.</p>"""
        out["guides/index.html"] = page("Guides", body, 1, "guides/index.html")
        return out

    def build(self):
        files = {}
        files["index.html"] = self.landing_page()
        files["path.html"] = self.path_page()
        files["principles.html"] = self.table_page()
        files["skills.html"] = self.skills_page()
        files["sources.html"] = self.sources_page()
        for i, c in enumerate(self.cats):
            files[f"categories/{c['slug']}.html"] = self.category_page(i)
        for i, p in enumerate(self.principles):
            files[f"principles/{p['id']}.html"] = self.principle_page(i)
            for m in p["merged"]:
                files[f"principles/{m['id']}.html"] = self.alias_page(m["id"], p)
        files.update(self.guide_pages())
        files["data/principles.json"] = canonical_json(self.pdoc)
        files["data/sources.json"] = canonical_json(self.sdoc)
        files["data/skill-principle-map.json"] = canonical_json(self.smap)
        files["data/mapping.json"] = canonical_json(self.mapping)
        files["data/licences.json"] = canonical_json(self.licences)
        files["data/scorecard.csv"] = self.scorecard_csv
        return files


def inline_md(text, base_dir):
    text = esc(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*([^*\s][^*]*)\*(?![\w*])", r"<em>\1</em>", text)

    def link(m):
        label, href = m.group(1), html.unescape(m.group(2))
        if re.match(r"^[a-z]+:", href) or href.startswith("#"):
            return f'<a href="{esc(href)}">{label}</a>'
        path, _, frag = href.partition("#")
        target = (base_dir / path).resolve()
        if target.parent == GUIDES.resolve() and target.suffix == ".md":
            slug = "index" if target.name == "README.md" else target.stem
            href = slug + ".html" + ("#" + frag if frag else "")
        else:
            try:
                href = BLOB + target.relative_to(ROOT).as_posix() + ("#" + frag if frag else "")
            except ValueError:
                pass
        return f'<a href="{esc(href)}">{label}</a>'

    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, text)


def render_markdown(text, base_dir):
    """Small markdown subset: headings, paragraphs, lists, tables, code fences."""
    out, para, items, kind = [], [], [], None
    lines = text.splitlines()

    def flush_para():
        if para:
            out.append("<p>" + inline_md(" ".join(para), base_dir) + "</p>")
            para.clear()

    def flush_list():
        nonlocal kind
        if items:
            tag = "ol" if kind == "ol" else "ul"
            out.append(f"<{tag}>" + "".join(f"<li>{inline_md(i, base_dir)}</li>" for i in items) + f"</{tag}>")
            items.clear()
        kind = None

    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            flush_para(); flush_list()
            i += 1
            code = []
            while i < len(lines) and not lines[i].startswith("```"):
                code.append(lines[i]); i += 1
            out.append("<pre><code>" + esc("\n".join(code)) + "</code></pre>")
        elif re.match(r"^#{1,6}\s", line):
            flush_para(); flush_list()
            level = len(line) - len(line.lstrip("#"))
            out.append(f"<h{level}>{inline_md(line[level:].strip(), base_dir)}</h{level}>")
        elif line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|$", lines[i + 1]):
            flush_para(); flush_list()
            head = [c.strip() for c in line.strip("|").split("|")]
            i += 2
            body_rows = []
            while i < len(lines) and lines[i].startswith("|"):
                body_rows.append([c.strip() for c in lines[i].strip("|").split("|")])
                i += 1
            i -= 1
            out.append(
                '<div class="table-wrap"><table><thead><tr>'
                + "".join(f"<th>{inline_md(h, base_dir)}</th>" for h in head)
                + "</tr></thead><tbody>"
                + "".join("<tr>" + "".join(f"<td>{inline_md(c, base_dir)}</td>" for c in r) + "</tr>" for r in body_rows)
                + "</tbody></table></div>"
            )
        elif re.match(r"^\s*[-*]\s+", line):
            flush_para()
            if kind != "ul":
                flush_list(); kind = "ul"
            items.append(re.sub(r"^\s*[-*]\s+", "", line))
        elif re.match(r"^\s*\d+\.\s+", line):
            flush_para()
            if kind != "ol":
                flush_list(); kind = "ol"
            items.append(re.sub(r"^\s*\d+\.\s+", "", line))
        elif not line.strip():
            flush_para(); flush_list()
        else:
            flush_list()
            para.append(line.strip())
        i += 1
    flush_para(); flush_list()
    return "\n".join(out)


def expected_paths(files):
    return set(files)


def existing_generated():
    found = set()
    for d in GENERATED_DIRS:
        base = DOCS / d
        if base.exists():
            found |= {p.relative_to(DOCS).as_posix() for p in base.rglob("*") if p.is_file()}
    for f in GENERATED_FILES:
        if (DOCS / f).exists():
            found.add(f)
    return found


def main():
    check = "--check" in sys.argv[1:]
    try:
        files = Site().build()
    except DataError as e:
        print(f"build-site: {e}", file=sys.stderr)
        return 1
    except (KeyError, ValueError, TypeError, IndexError) as e:
        print(f"build-site: a data file is malformed or missing a field ({type(e).__name__}: {e})", file=sys.stderr)
        return 1
    stale = []
    for rel, content in files.items():
        path = DOCS / rel
        if check:
            if not path.exists() or path.read_bytes() != content.encode("utf-8"):
                stale.append(rel)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content.encode("utf-8"))
    extra = sorted(existing_generated() - expected_paths(files))
    if check:
        if stale or extra:
            for rel in stale:
                print(f"stale or missing: docs/{rel}")
            for rel in extra:
                print(f"unexpected generated file: docs/{rel}")
            print("Run scripts/build-site.py and commit the result.")
            return 1
        print(f"docs/ is up to date ({len(files)} generated files).")
        return 0
    for rel in extra:
        (DOCS / rel).unlink()
        print(f"removed docs/{rel}")
    print(f"wrote {len(files)} files to docs/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
