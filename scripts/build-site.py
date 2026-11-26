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
SITE_NAME = "AI SDLC Loop"

GENERATED_DIRS = ["categories", "principles", "guides"]
GENERATED_FILES = [
    "index.html",
    "path.html",
    "principles.html",
    "skills.html",
    "sources.html",
    "data/principles.json",
    "data/sources.json",
    "data/skill-principle-map.json",
    "data/taxonomy.json",
    "data/scorecard.json",
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
    ("sources.html", "Sources"),
    ("guides/index.html", "Guides"),
]

# The redirect pages for merged principle IDs keep the nav they had before skills.html existed,
# so they stay byte-for-byte unchanged.
REDIRECT_NAV = [item for item in NAV if item[0] != "skills.html"]

LICENCE_LABELS = {
    "clean": ("Clean", "Every source could be adapted"),
    "rewritten": ("Rewritten", "Rewritten: link-only sources moved to Further reading"),
    "rebuilt": ("Rebuilt", "Rebuilt from MIT sources; the original sources are link only"),
}


def licence_key(status):
    """Group the free-text licence_status in the skill map: clean, rewritten or rebuilt."""
    word = status.split(",")[0].split(" ")[0].strip().lower()
    return word if word in LICENCE_LABELS else "other"


BRAND = "assets/brand/"


def page(title, body, depth, active=None, description="", nav_items=None, brand=True):
    """Wrap body in the site chrome. depth is the folder depth below docs/.

    brand=False leaves out the icons, social tags and header logo; the merged-ID redirect pages use it so
    they stay byte-for-byte unchanged.
    """
    up = "../" * depth
    nav = "".join(
        '<a href="{}{}"{}>{}</a>'.format(
            up, href, ' aria-current="page"' if href == active else "", esc(label)
        )
        for href, label in (nav_items or NAV)
    )
    desc = esc(description or "Software engineering principles for building with agents, and a loop that learns from each project.")
    head_extra = logo = ""
    if brand:
        full_title = f"{title} | {SITE_NAME}"
        head_extra = f"""<link rel="icon" href="{up}{BRAND}ai-sdlc-loop.ico" sizes="any">
<link rel="icon" href="{up}{BRAND}ai-sdlc-loop.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{up}{BRAND}ai-sdlc-loop-512.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{up}{BRAND}ai-sdlc-loop-photographic.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(full_title)}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{up}{BRAND}ai-sdlc-loop-photographic.jpg">
"""
        logo = f'<img class="brand-logo" src="{up}{BRAND}ai-sdlc-loop.svg" alt="AI SDLC Loop logo" width="28" height="28">'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} | {SITE_NAME}</title>
<meta name="description" content="{desc}">
{head_extra}<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
<div class="wrap header-inner">
<a class="brand" href="{up}index.html">{logo}{SITE_NAME}</a>
<nav aria-label="Main">{nav}<a href="{REPO_URL}">GitHub</a></nav>
</div>
</header>
<main id="main" class="wrap">
{body}
</main>
<footer class="site-footer">
<div class="wrap">
<p>{SITE_NAME}. Written content is CC BY-SA 4.0 and code is GPL-3.0; the project template is MIT.
See <a href="{REPO_URL}#readme">the README</a> and <a href="{REPO_URL}/blob/main/LICENSE-CONTENT">LICENSE-CONTENT</a>.
No trackers, no external scripts. Generated from <a href="{BLOB}data/principles.json">data/principles.json</a>.</p>
</div>
</footer>
<script src="{up}assets/site.js" defer></script>
</body>
</html>
"""


def cat_link(cat, up=""):
    return f'<a href="{up}categories/{esc(cat["slug"])}.html">{esc(cat["name"])}</a>'


class Site:
    def __init__(self):
        self.pdoc = load(DATA / "principles.json")
        self.sdoc = load(DATA / "sources.json")
        self.cats = sorted(self.pdoc["categories"], key=lambda c: c["number"])
        self.cat_by_slug = {c["slug"]: c for c in self.cats}
        self.principles = sorted(self.pdoc["principles"], key=lambda p: pid_key(p["id"]))
        self.repo_by_label = {}
        for r in self.sdoc["repos"]:
            for lab in r["labels"]:
                self.repo_by_label[lab] = r
        self.by_cat = {c["slug"]: [p for p in self.principles if p["category"] == c["slug"]] for c in self.cats}
        self.n_sources = len(self.sdoc["repos"])
        # Repos added after the research run carry a note starting "Added for"; they are cited, not researched.
        self.n_researched = sum(1 for r in self.sdoc["repos"] if not r.get("notes", "").startswith("Added for"))
        self.map_doc = load(DATA / "skill-principle-map.json")
        self.tax = load(DATA / "taxonomy.json")
        self.score_doc = load(DATA / "scorecard.json")
        self.skills = sorted(self.map_doc["skills"], key=lambda s: s["slot"])
        self.skill_by_pid = {s["principle_id"]: s for s in self.skills}
        self.score_by_pid = {r["skill_id"]: r for r in self.score_doc["skills"]}
        self.phases = sorted(self.tax["phases"], key=lambda ph: ph["order"])
        self.phase_by_slug = {ph["slug"]: ph for ph in self.phases}
        self.apps = self.tax["test_apps"]
        self.app_by_id = {a["id"]: a for a in self.apps}
        self.n_scored = sum(1 for r in self.score_doc["skills"] if r["runs"])

    def licence_badge(self, sk):
        key = licence_key(sk["licence_status"])
        label, tip = LICENCE_LABELS.get(key, (sk["licence_status"], sk["licence_status"]))
        return f'<span class="lic lic-{esc(key)}" title="{esc(tip)}">{esc(label)}</span>'

    def score_cells(self, pid):
        """(score text, sort value, verdict text) for a skill, from the latest run on the scorecard."""
        row = self.score_by_pid.get(pid)
        runs = row["runs"] if row else []
        verdict = row["verdict"] if row and row["verdict"] else "none yet"
        if not runs:
            return "not run", -1, verdict
        last = runs[-1]
        text = f'{last["total"]}/10'
        if len(runs) > 1:
            text += f" ({len(runs)} runs)"
        if any(r["harm_flag"] for r in runs):
            text += " harm flag"
        return text, last["total"], verdict

    def app_label(self, app_id):
        a = self.app_by_id[app_id]
        return f'App {a["id"]}: {a["name"]}' if a["id"] != "All" else a["name"]

    def source_chips(self, p, up):
        out = []
        for lab in p["sources"]:
            r = self.repo_by_label.get(lab)
            if r:
                out.append(f'<a class="chip" href="{esc(r["url"])}">{esc(lab)}</a>')
            else:
                out.append(f'<span class="chip">{esc(lab)}</span>')
        return " ".join(out)

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
        n_sources = self.n_sources
        n_researched = self.n_researched
        n_added = n_sources - n_researched
        n_skills = len(self.skills)
        n_phases = len(self.phases)
        first_cat = self.cats[0]
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
<picture class="lp-logo">
<source media="(prefers-reduced-motion: reduce)" srcset="{BRAND}ai-sdlc-loop.svg">
<img src="{BRAND}ai-sdlc-loop-animated.svg" alt="AI SDLC Loop logo" width="96" height="96">
</picture>
<p class="lp-eyebrow">Open source starter for agentic software development</p>
<h1 id="lp-title">Software engineering principles for building with agents, and a loop that learns from each project</h1>
<p class="lede">I distilled what {n_researched} public repos teach about working with coding agents into {n_principles} principles
in {n_cats} categories. Use them to adopt agentic tools with less trial and error, then build a learning loop of your own.</p>
<p class="lp-cta">
<a class="btn btn-primary" href="path.html">Explore the learning path</a>
<a class="btn" href="skills.html">See the skills</a>
<a class="btn" href="#start">Start a project</a>
<a class="btn" href="principles.html">Browse all principles</a>
</p>
<dl class="lp-stats">
<div><dt>Principles</dt><dd>{n_principles}</dd></div>
<div><dt>Categories</dt><dd>{n_cats}</dd></div>
<div><dt>Skills</dt><dd>{n_skills}</dd></div>
<div><dt>Repos reviewed</dt><dd>{n_researched}</dd></div>
<div><dt>Sources cited</dt><dd>{n_sources}</dd></div>
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
<p>So I had a research bot read {n_researched} public repos and boil them down to {n_principles} numbered principles in {n_cats} categories. Each one is traceable to the repos it came from.</p>
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
<li class="lp-card"><h3><a href="principles.html">Explore the principles</a></h3><p>Search, filter and sort all {n_principles}. Each links to its sources.</p></li>
<li class="lp-card"><h3><a href="categories/{esc(first_cat["slug"])}.html">Read the categories</a></h3><p>One page per category, with the principles that belong to it.</p></li>
<li class="lp-card"><h3><a href="skills.html">See the skills</a></h3><p>One skill per principle, in test run order, with its phase, test app and licence status. Filter all {n_skills} across {n_phases} phases.</p></li>
<li class="lp-card"><h3><a href="sources.html">Check the sources</a></h3><p>The {n_sources} sources cited ({n_researched} researched, plus {n_added} added for a skill), with their licences.</p></li>
<li class="lp-card"><h3><a href="guides/index.html">Read the guides</a></h3><p>Plain-language guides to the principles.</p></li>
<li class="lp-card"><h3><a href="#start">Start a project</a></h3><p>Copy the template and run your first loop.</p></li>
</ul>
<h3 class="lp-sub">The {n_cats} categories</h3>
<ul class="lp-chips">{stage_chips}</ul>
</section>

<section class="lp-section" id="start" aria-labelledby="start-title">
<h2 id="start-title">Start a project from the template</h2>
<p>Clone the repo and run <a href="{BLOB}scripts/new-project.sh"><code>scripts/new-project.sh</code></a> with a profile. It copies the shared base from <a href="{BLOB}template/"><code>template/</code></a>, applies the profile, and runs <code>git init</code>. It refuses a target folder that is not empty.</p>
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
            f"{n_principles} software engineering principles distilled from {n_researched} public repos, and a template to start your own agentic loop.",
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
<p class="muted"><a href="skills.html?cat={esc(c["slug"])}">{len(ps)} skills in this stage</a>, in test run order.</p>
</div>
</li>"""
            )
        body = f"""<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Learning path</nav>
<section class="hero">
<h1>A learning path through {total} software principles</h1>
<p class="lede">These principles were distilled from {self.n_researched} public repos of agent skills, sub-agents and commands.
They are the base of a loop that builds software with agents and learns from each project.
Work through the nine stages in order, or jump straight to the one you need.</p>
<form class="search" action="principles.html" method="get" role="search">
<label for="home-q" class="sr">Search principles</label>
<input id="home-q" name="q" type="search" placeholder="Search principles, e.g. test, secret, review" autocomplete="off">
<button type="submit">Search</button>
</form>
<p class="quick"><a href="categories/{esc(self.cats[0]["slug"])}.html">Start at stage 1</a>
<a href="principles.html">Browse the table</a>
<a href="skills.html">See the skills in run order</a>
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
<li>Want to see how the principles become skills and in what order they are tested? Open the <a href="skills.html">skills page</a>.</li>
<li>Want to know where an idea came from? Every principle links to the source repos it was drawn from, and the <a href="sources.html">sources page</a> lists all of them with their licences.</li>
</ul>
</section>"""
        return page("Learning path", body, 0, "path.html")

    def category_page(self, i):
        c = self.cats[i]
        ps = self.by_cat[c["slug"]]
        tag, why = PATH_TEXT.get(c["slug"], (f"{len(ps)} principles.", ""))
        def item(p):
            sk = self.skill_by_pid[p["id"]]
            phase = self.phase_by_slug[sk["phase"]]
            return (
                f'<li><a class="pid" href="../principles/{esc(p["id"])}.html">{esc(p["id"])}</a>'
                f'<div><span>{esc(p["statement"])}</span>'
                f'<p class="skill-meta">Skill <a href="{BLOB}{esc(sk["folder"])}/SKILL.md">{esc(sk["skill_name"])}</a>'
                f' <span class="muted">&middot; <a href="../skills.html?phase={esc(phase["slug"])}">{esc(phase["name"])} phase</a>'
                f' &middot; <a href="../skills.html#s-{esc(p["id"])}">run slot {sk["slot"]}</a>'
                f' &middot; {esc(self.app_label(sk["test_app"]))}</span> {self.licence_badge(sk)}</p></div></li>'
            )

        groups = [g for g in self.tax["subgroups"] if g["category"] == c["slug"]]
        grouped = {pid for g in groups for pid in g["principles"]}
        by_id = {p["id"]: p for p in ps}
        sections = []
        for g in groups:
            members = [by_id[pid] for pid in sorted(g["principles"], key=pid_key) if pid in by_id]
            sections.append(
                f'<h2 id="{esc(g["slug"])}">{esc(g["name"])} <span class="count">{len(members)} principles</span></h2>\n'
                f'<ol class="plist">{"".join(item(p) for p in members)}</ol>'
            )
        rest = [p for p in ps if p["id"] not in grouped]
        if groups:
            if rest:
                sections.insert(
                    0,
                    f'<h2 id="general">General principles <span class="count">{len(rest)} principles</span></h2>\n'
                    f'<ol class="plist">{"".join(item(p) for p in rest)}</ol>',
                )
        else:
            sections.append(f'<h2>{len(ps)} principles</h2>\n<ol class="plist">{"".join(item(p) for p in rest)}</ol>')
        phase_counts = {}
        for p in ps:
            ph = self.skill_by_pid[p["id"]]["phase"]
            phase_counts[ph] = phase_counts.get(ph, 0) + 1
        phase_links = ", ".join(
            f'<a href="../skills.html?phase={esc(ph["slug"])}">{esc(ph["name"])}</a> ({phase_counts[ph["slug"]]})'
            for ph in self.phases
            if ph["slug"] in phase_counts
        )
        taxonomy = (
            f'<p class="muted">The {len(ps)} skills here run in these phases: {phase_links}. '
            f'<a href="../skills.html?cat={esc(c["slug"])}">See them in run order</a>.</p>'
        )
        sections_html = "\n".join(sections)
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
{taxonomy}
{sections_html}
{pager}"""
        return page(c["name"], body, 1, "path.html", tag)

    def principle_page(self, idx):
        p = self.principles[idx]
        c = self.cat_by_slug[p["category"]]
        srcs = []
        for lab in p["sources"]:
            r = self.repo_by_label.get(lab)
            if r:
                srcs.append(
                    f'<li><a href="{esc(r["url"])}">{esc(r["owner"])}/{esc(r["repo"])}</a> '
                    f'<span class="muted">(as "{esc(lab)}", {esc(r["licence"])})</span></li>'
                )
            else:
                srcs.append(f'<li>{esc(lab)} <span class="muted">(no repo recorded)</span></li>')
        prov = p["provenance"]
        merged = (
            "Merged from: " + ", ".join(f'<a href="{esc(m)}.html">{esc(m)}</a>' for m in prov["merged_from"]) + "."
            if prov["merged_from"]
            else "No merges."
        )
        notes = f"<p>{esc(prov['notes'])}</p>" if prov["notes"] else ""
        aliases = (
            "<dt>Also known as</dt><dd>"
            + ", ".join(f'<a href="{esc(a)}.html">{esc(a)}</a>' for a in p.get("aliases", []))
            + " (merged into this principle)</dd>"
            if p.get("aliases")
            else ""
        )
        differs = (
            "<h2>How it differs from related principles</h2>\n<ul>"
            + "".join(
                f'<li><a href="{esc(d["id"])}.html">{esc(d["id"])}</a>: {esc(d["difference"])}</li>'
                for d in p["distinct_from"]
            )
            + "</ul>"
            if p.get("distinct_from")
            else ""
        )
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
        sk = self.skill_by_pid[p["id"]]
        phase = self.phase_by_slug[sk["phase"]]
        score_text, _, verdict = self.score_cells(p["id"])
        skills_html = f"""<p><a href="{BLOB}{esc(sk["folder"])}/SKILL.md">{esc(sk["skill_name"])}</a>
(<a href="{BLOB}{esc(sk["folder"])}/SOURCES.md">sources</a>) &middot; <a href="../skills.html#s-{esc(p["id"])}">see it in the run order</a></p>
<dl class="facts">
<dt>Phase</dt><dd><a href="../skills.html?phase={esc(phase["slug"])}">{esc(phase["name"])}</a>, led by the {esc(phase["role"])}</dd>
<dt>Run slot</dt><dd>{sk["slot"]} of {len(self.skills)}</dd>
<dt>Test app</dt><dd>{esc(self.app_label(sk["test_app"]))}</dd>
<dt>Licence status</dt><dd>{self.licence_badge(sk)} <span class="muted">{esc(sk["licence_status"])}; {sk["clean_sources"]} adaptable and {sk["link_only_sources"]} link-only sources</span></dd>
<dt>Scorecard</dt><dd>{esc(score_text)}, verdict: {esc(verdict)} <span class="muted">({esc(sk["status"])})</span></dd>
</dl>"""
        body = f"""<nav class="crumbs" aria-label="Breadcrumb"><a href="../index.html">Home</a> / <a href="../path.html">Learning path</a> /
<a href="../categories/{esc(c["slug"])}.html">Stage {c["number"]}: {esc(c["name"])}</a> / {esc(p["id"])}</nav>
<p class="pid-big">Principle {esc(p["id"])}</p>
<h1>{esc(p["statement"])}</h1>
<dl class="facts">
<dt>Category</dt><dd><a href="../categories/{esc(c["slug"])}.html">{esc(c["name"])}</a></dd>
<dt>Status</dt><dd>{esc(p["status"])}</dd>
<dt>Origin</dt><dd>{esc(prov["origin"])}, research {esc(prov["research_run"])}. {merged}</dd>
{aliases}</dl>
{notes}
{differs}
<h2>Sources</h2>
<p>This principle was drawn from these repos. Licences are as checked on the <a href="../sources.html">sources page</a>.</p>
<ul class="sources">{"".join(srcs)}</ul>
<h2>Amalgamated skill</h2>
{skills_html}
<p class="muted"><a href="{BLOB}principles/{esc(p["id"])}.md">View this principle as markdown on GitHub</a></p>
{pager}"""
        return page(f'{p["id"]} {p["statement"]}', body, 1, "principles.html", p["statement"])

    def alias_page(self, alias, target):
        body = f"""<p class="pid-big">Principle {esc(alias)}</p>
<h1>Merged into {esc(target["id"])}</h1>
<p>Principle {esc(alias)} was merged into <a href="{esc(target["id"])}.html">principle {esc(target["id"])}</a>: {esc(target["statement"])}</p>
<p>{esc(target["provenance"]["notes"])} See <a href="{BLOB}MERGES.md">MERGES.md</a>.</p>"""
        refresh = f'<meta http-equiv="refresh" content="0; url={esc(target["id"])}.html">\n<link rel="canonical" href="{esc(target["id"])}.html">\n'
        return page(f"Principle {alias} (merged)", body, 1, "principles.html", nav_items=REDIRECT_NAV, brand=False).replace("</head>", refresh + "</head>", 1)

    def table_page(self):
        rows = []
        for p in self.principles:
            c = self.cat_by_slug[p["category"]]
            rows.append(
                f'<tr data-cat="{esc(c["slug"])}" data-src="{esc("|".join(p["sources"]))}">'
                f'<td data-sort="{pid_key(p["id"])[0] * 1000 + pid_key(p["id"])[1]}"><a href="principles/{esc(p["id"])}.html">{esc(p["id"])}</a></td>'
                f'<td>{esc(p["statement"])}</td>'
                f'<td data-sort="{c["number"]}">{cat_link(c)}</td>'
                f'<td data-sort="{len(p["sources"])}">{self.source_chips(p, "")}</td></tr>'
            )
        opts = "".join(f'<option value="{esc(c["slug"])}">{c["number"]}. {esc(c["name"])}</option>' for c in self.cats)
        labels = sorted({lab for p in self.principles for lab in p["sources"]}, key=str.lower)
        src_opts = "".join(f'<option value="{esc(lab)}">{esc(lab)}</option>' for lab in labels)
        body = f"""<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / All principles</nav>
<h1>All principles</h1>
<p>Search, filter by category or source, and click a column heading to sort. Works without a server; with JavaScript off you still get the full table.</p>
<div class="filters" role="search" data-table="ptable" data-noun="principles">
<label>Search <input data-q type="search" placeholder="Search statements" autocomplete="off"></label>
<label>Category <select data-attr="cat"><option value="">All categories</option>{opts}</select></label>
<label>Source <select data-attr="src"><option value="">All sources</option>{src_opts}</select></label>
<button type="button" data-reset>Reset</button>
</div>
<p data-count class="muted" aria-live="polite">{len(self.principles)} principles</p>
<div class="table-wrap">
<table id="ptable" class="sortable">
<thead><tr>
<th scope="col" data-type="num">ID</th>
<th scope="col" data-type="text">Principle</th>
<th scope="col" data-type="num">Category</th>
<th scope="col" data-type="num">Sources</th>
</tr></thead>
<tbody>
{chr(10).join(rows)}
</tbody>
</table>
</div>
<p class="muted">Machine-readable copy: <a href="data/principles.json">data/principles.json</a>.</p>"""
        return page("All principles", body, 0, "principles.html")

    def skills_page(self):
        n = len(self.skills)
        n_draft = sum(1 for sk in self.skills if sk["status"].startswith("draft"))
        rows = []
        for sk in self.skills:
            pid = sk["principle_id"]
            p = next(x for x in self.principles if x["id"] == pid)
            c = self.cat_by_slug[sk["category"]]
            phase = self.phase_by_slug[sk["phase"]]
            app = self.app_by_id[sk["test_app"]]
            score_text, score_sort, verdict = self.score_cells(pid)
            aliases = "".join(
                f'<span class="alias" title="Merged into {esc(pid)}">also {esc(a)}<span class="sr"> (merged into {esc(pid)})</span></span>' for a in sk["aliases"]
            )
            key = licence_key(sk["licence_status"])
            if key not in LICENCE_LABELS:
                raise SystemExit(f'skill {pid}: unrecognised licence_status {sk["licence_status"]!r}; teach licence_key() about it')
            rows.append(
                f'<tr id="s-{esc(pid)}" data-cat="{esc(c["slug"])}" data-phase="{esc(phase["slug"])}" '
                f'data-app="{esc(app["id"])}" data-licence="{esc(key)}">'
                f'<td data-label="Slot" data-sort="{sk["slot"]}">{sk["slot"]}</td>'
                f'<td data-label="Principle" data-sort="{pid_key(pid)[0] * 1000 + pid_key(pid)[1]}">'
                f'<div><a href="principles/{esc(pid)}.html">{esc(pid)}</a>{aliases}</div></td>'
                f'<td data-label="Skill"><div><a href="{BLOB}{esc(sk["folder"])}/SKILL.md">{esc(sk["skill_name"])}</a>'
                f'<span class="muted skill-stmt">{esc(p["statement"])}</span></div></td>'
                f'<td data-label="Category" data-sort="{c["number"]}">{cat_link(c)}</td>'
                f'<td data-label="Phase" data-sort="{phase["order"]}">{esc(phase["name"])}</td>'
                f'<td data-label="Test app" title="{esc(app["name"])}">{esc(app["id"])}</td>'
                f'<td data-label="Licence" data-sort="{esc(key)}"><div>{self.licence_badge(sk)}'
                f'<span class="muted lic-counts">{sk["clean_sources"]} adaptable, {sk["link_only_sources"]} link-only</span></div></td>'
                f'<td data-label="Score /10" data-sort="{score_sort}">{esc(score_text)}</td>'
                f'<td data-label="Verdict">{esc(verdict)}</td></tr>'
            )
        counts = {}
        for sk in self.skills:
            counts[sk["test_app"]] = counts.get(sk["test_app"], 0) + 1
        app_cards = ""
        for a in self.apps:
            title = f'Test app {esc(a["id"])}' if a["id"] != "All" else "All runs"
            run = f' <span class="count">run {a["run"]}</span>' if a["run"] else ""
            app_cards += (
                f'<li class="lp-card"><h3>{title}{run}</h3><p>{esc(a["name"])}</p>'
                f'<p class="muted">{esc(a["example"])}</p>'
                f'<p class="muted"><a href="skills.html?app={esc(a["id"])}">{counts.get(a["id"], 0)} skills</a></p></li>'
            )
        phase_counts = {}
        for sk in self.skills:
            phase_counts[sk["phase"]] = phase_counts.get(sk["phase"], 0) + 1
        phase_cards = ""
        for ph in self.phases:
            cats = ", ".join(cat_link(self.cat_by_slug[cs]) for cs in ph["categories"])
            cmds = ", ".join(f"<code>/{esc(cm)}</code>" for cm in ph["commands"]) or "none"
            phase_cards += (
                f'<li class="lp-card"><h3>{ph["order"]}. <a href="skills.html?phase={esc(ph["slug"])}">{esc(ph["name"])}</a>'
                f' <span class="count">{phase_counts.get(ph["slug"], 0)} skills</span></h3>'
                f'<p>Role: {esc(ph["role"])}</p>'
                f'<p class="muted">Producer <code>{esc(ph["producer_agent"])}</code>, reviewer <code>{esc(ph["reviewer_agent"])}</code>. Commands: {cmds}.</p>'
                f'<p class="muted">Categories: {cats}</p></li>'
            )
        cat_opts = "".join(f'<option value="{esc(c["slug"])}">{c["number"]}. {esc(c["name"])}</option>' for c in self.cats)
        phase_opts = "".join(f'<option value="{esc(ph["slug"])}">{ph["order"]}. {esc(ph["name"])}</option>' for ph in self.phases)
        app_opts = "".join(
            f'<option value="{esc(a["id"])}">{esc(self.app_label(a["id"]))}</option>' for a in self.apps
        )
        lic_opts = "".join(f'<option value="{k}">{esc(tip)}</option>' for k, (_, tip) in LICENCE_LABELS.items())
        body = f"""<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Skills</nav>
<h1>The {n} skills, in test run order</h1>
<p>There is one amalgamated skill per principle. Each has a phase, a test app and a slot. The slot is its place in the run order, and the test app is the project it is exercised on.
Skills are scored in <a href="{BLOB}data/scorecard.json">data/scorecard.json</a>; {self.n_scored} of {n} have been scored so far, and {n_draft} of {n} are still drafts.
Licence status says whether every source could be adapted (clean), or whether link-only sources were moved to Further reading (rewritten, rebuilt).</p>
<h2>Test apps</h2>
<ul class="lp-cards">{app_cards}</ul>
<p class="muted">&ldquo;All runs&rdquo; skills apply on every run: the harness skills and the Learn skills.</p>
<h2>Phases</h2>
<p>Each phase is a producer and an adversarial reviewer. A category can span more than one phase.</p>
<ol class="lp-cards">{phase_cards}</ol>
<h2 id="run-order">Run order</h2>
<p>Skills are tested in slot order, 1 to {n}, as set in <a href="{BLOB}data/skill-principle-map.json">data/skill-principle-map.json</a>. Click a column heading to sort, or filter below.</p>
<div class="filters" role="search" data-table="stable" data-noun="skills">
<label>Search <input data-q type="search" placeholder="Name, ID or words" autocomplete="off"></label>
<label>Category <select data-attr="cat"><option value="">All categories</option>{cat_opts}</select></label>
<label>Phase <select data-attr="phase"><option value="">All phases</option>{phase_opts}</select></label>
<label>Test app <select data-attr="app"><option value="">All apps</option>{app_opts}</select></label>
<label>Licence status <select data-attr="licence"><option value="">All</option>{lic_opts}</select></label>
<button type="button" data-reset>Reset</button>
</div>
<p data-count class="muted" aria-live="polite">{n} skills</p>
<div class="table-wrap">
<table id="stable" class="sortable cards">
<thead><tr>
<th scope="col" data-type="num">Slot</th>
<th scope="col" data-type="num">Principle</th>
<th scope="col" data-type="text">Skill</th>
<th scope="col" data-type="num">Category</th>
<th scope="col" data-type="num">Phase</th>
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
<p class="muted">Machine-readable copies: <a href="data/skill-principle-map.json">skill-principle-map.json</a>, <a href="data/taxonomy.json">taxonomy.json</a>, <a href="data/scorecard.json">scorecard.json</a>.</p>"""
        return page("Skills", body, 0, "skills.html", f"The {n} amalgamated skills with their phase, test app, slot and licence status.")

    def sources_page(self):
        rows = []
        for r in sorted(self.sdoc["repos"], key=lambda r: (r["owner"].lower(), r["repo"].lower())):
            used = sum(1 for p in self.principles if any(lab in r["labels"] for lab in p["sources"]))
            pin = r["pinned_sha"][:7] if r["pinned_sha"] else "not pinned yet"
            rows.append(
                f'<tr><td><a href="{esc(r["url"])}">{esc(r["owner"])}/{esc(r["repo"])}</a></td>'
                f'<td>{esc(r["role"])}</td><td>{esc(r["licence"])}</td>'
                f'<td data-sort="{used}">{used}</td><td>{esc(pin)}</td></tr>'
            )
        run = self.sdoc["research_run"]
        body = f"""<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Sources</nav>
<h1>Source repos</h1>
<p>{self.n_sources} sources cited: the {self.n_researched} public repos the principles were drawn from ({esc(run["id"])}, {esc(run["date"])}), plus {self.n_sources - self.n_researched} added later for skill 7.12.
Licences are as checked and may need your own review before you reuse anything; see
<a href="{BLOB}ATTRIBUTIONS.md">ATTRIBUTIONS.md</a>. Curation lists are pointers to other sources and are never installed wholesale.</p>
<div class="table-wrap">
<table class="sortable">
<thead><tr>
<th scope="col" data-type="text">Repo</th>
<th scope="col" data-type="text">Role</th>
<th scope="col" data-type="text">Licence</th>
<th scope="col" data-type="num">Principles</th>
<th scope="col" data-type="text">Pinned commit</th>
</tr></thead>
<tbody>
{chr(10).join(rows)}
</tbody>
</table>
</div>
<p class="muted">Machine-readable copy: <a href="data/sources.json">data/sources.json</a>.</p>"""
        return page("Sources", body, 0, "sources.html")

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
<p class="muted">Source: <a href="{BLOB}guides/developer/">guides/developer/</a>. A page marked stub holds placeholder text until the guide is written.</p>"""
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
            for alias in p.get("aliases", []):
                files[f"principles/{alias}.html"] = self.alias_page(alias, p)
        files.update(self.guide_pages())
        files["data/principles.json"] = canonical_json(self.pdoc)
        files["data/sources.json"] = canonical_json(self.sdoc)
        files["data/skill-principle-map.json"] = canonical_json(self.map_doc)
        files["data/taxonomy.json"] = canonical_json(self.tax)
        files["data/scorecard.json"] = canonical_json(self.score_doc)
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
    files = Site().build()
    stale = []
    for rel, content in files.items():
        path = DOCS / rel
        if check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(rel)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
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
