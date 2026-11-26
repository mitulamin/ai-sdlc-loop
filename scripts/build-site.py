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
REPO_URL = "https://github.com/mitulamin/ai-sdlc-loop"
BLOB = REPO_URL + "/blob/main/"
SITE_NAME = "ai-sdlc-loop"

GENERATED_DIRS = ["categories", "principles", "guides"]
GENERATED_FILES = [
    "index.html",
    "principles.html",
    "sources.html",
    "data/principles.json",
    "data/sources.json",
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
    ("index.html", "Learning path"),
    ("principles.html", "All principles"),
    ("sources.html", "Sources"),
    ("guides/index.html", "Guides"),
]


def page(title, body, depth, active=None, description=""):
    """Wrap body in the site chrome. depth is the folder depth below docs/."""
    up = "../" * depth
    nav = "".join(
        '<a href="{}{}"{}>{}</a>'.format(
            up, href, ' aria-current="page"' if href == active else "", esc(label)
        )
        for href, label in NAV
    )
    desc = esc(description or "A learning path through 108 software principles for agentic loops.")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} | {SITE_NAME}</title>
<meta name="description" content="{desc}">
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
{body}
</main>
<footer class="site-footer">
<div class="wrap">
<p>Written content is CC BY-SA 4.0 and code is GPL-3.0; the project template is MIT.
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

    def source_chips(self, p, up):
        out = []
        for lab in p["sources"]:
            r = self.repo_by_label.get(lab)
            if r:
                out.append(f'<a class="chip" href="{esc(r["url"])}">{esc(lab)}</a>')
            else:
                out.append(f'<span class="chip">{esc(lab)}</span>')
        return " ".join(out)

    def home(self):
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
        body = f"""<section class="hero">
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
<a href="guides/index.html">Read the developer guide</a></p>
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
        return page("Learning path", body, 0, "index.html")

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
            else '<a class="prev" href="../index.html"><small>Back to</small>Learning path</a>'
        )
        pager += (
            f'<a class="next" href="{esc(nxt["slug"])}.html"><small>Next stage</small>{esc(nxt["name"])}</a>'
            if nxt
            else '<a class="next" href="../principles.html"><small>Finished</small>All principles</a>'
        )
        pager += "</nav>"
        body = f"""<nav class="crumbs" aria-label="Breadcrumb"><a href="../index.html">Learning path</a> / Stage {c["number"]}</nav>
<h1>Stage {c["number"]}: {esc(c["name"])}</h1>
<p class="lede">{esc(tag)}</p>
<p>{esc(why)}</p>
<h2>{len(ps)} principles</h2>
<ol class="plist">{rows}</ol>
{pager}"""
        return page(c["name"], body, 1, "index.html", tag)

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
        body = f"""<nav class="crumbs" aria-label="Breadcrumb"><a href="../index.html">Learning path</a> /
<a href="../categories/{esc(c["slug"])}.html">Stage {c["number"]}: {esc(c["name"])}</a> / {esc(p["id"])}</nav>
<p class="pid-big">Principle {esc(p["id"])}</p>
<h1>{esc(p["statement"])}</h1>
<dl class="facts">
<dt>Category</dt><dd><a href="../categories/{esc(c["slug"])}.html">{esc(c["name"])}</a></dd>
<dt>Status</dt><dd>{esc(p["status"])}</dd>
<dt>Origin</dt><dd>{esc(prov["origin"])}, research {esc(prov["research_run"])}. {merged}</dd>
</dl>
{notes}
<h2>Sources</h2>
<p>This principle was drawn from these repos. Licences are as checked on the <a href="../sources.html">sources page</a>.</p>
<ul class="sources">{"".join(srcs)}</ul>
<h2>Amalgamated skill</h2>
<p>Not written yet. When it exists it will be linked here.</p>
<p class="muted"><a href="{BLOB}principles/{esc(p["id"])}.md">View this principle as markdown on GitHub</a></p>
{pager}"""
        return page(f'{p["id"]} {p["statement"]}', body, 1, "principles.html", p["statement"])

    def table_page(self):
        rows = []
        for p in self.principles:
            c = self.cat_by_slug[p["category"]]
            rows.append(
                f'<tr data-cat="{esc(c["slug"])}" data-sources="{esc("|".join(p["sources"]))}">'
                f'<td data-sort="{pid_key(p["id"])[0] * 1000 + pid_key(p["id"])[1]}"><a href="principles/{esc(p["id"])}.html">{esc(p["id"])}</a></td>'
                f'<td>{esc(p["statement"])}</td>'
                f'<td data-sort="{c["number"]}">{cat_link(c)}</td>'
                f'<td data-sort="{len(p["sources"])}">{self.source_chips(p, "")}</td></tr>'
            )
        opts = "".join(f'<option value="{esc(c["slug"])}">{c["number"]}. {esc(c["name"])}</option>' for c in self.cats)
        labels = sorted({lab for p in self.principles for lab in p["sources"]}, key=str.lower)
        src_opts = "".join(f'<option value="{esc(lab)}">{esc(lab)}</option>' for lab in labels)
        body = f"""<h1>All principles</h1>
<p>Search, filter by category or source, and click a column heading to sort. Works without a server; with JavaScript off you still get the full table.</p>
<div class="filters" role="search">
<label>Search <input id="q" type="search" placeholder="Search statements" autocomplete="off"></label>
<label>Category <select id="cat"><option value="">All categories</option>{opts}</select></label>
<label>Source <select id="src"><option value="">All sources</option>{src_opts}</select></label>
<button type="button" id="reset">Reset</button>
</div>
<p id="result-count" class="muted" aria-live="polite">{len(self.principles)} principles</p>
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
        body = f"""<h1>Source repos</h1>
<p>The {len(self.sdoc["repos"])} public repos the principles were drawn from ({esc(run["id"])}, {esc(run["date"])}).
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
                title, f'<nav class="crumbs"><a href="../index.html">Guides</a> / {esc(title)}</nav>\n{banner}\n<article class="prose">{body_html}</article>',
                2, "guides/index.html",
            )
            entries.append((slug, title, stub))
        badge = ' <span class="badge">stub</span>'
        listing = "".join(
            f'<li><a href="developer/{slug}.html">{esc(title)}</a>{badge if stub else ""}</li>'
            for slug, title, stub in entries
        )
        body = f"""<h1>Guides</h1>
<p>Plain-language guides to the principles. They cover everything, including what experienced developers already know.</p>
<h2>Developer guides</h2>
<ul>{listing}</ul>
<p class="muted">Source: <a href="{BLOB}guides/developer/">guides/developer/</a>. A page marked stub holds placeholder text until the guide is written.</p>"""
        out["guides/index.html"] = page("Guides", body, 1, "guides/index.html")
        return out

    def build(self):
        files = {}
        files["index.html"] = self.home()
        files["principles.html"] = self.table_page()
        files["sources.html"] = self.sources_page()
        for i, c in enumerate(self.cats):
            files[f"categories/{c['slug']}.html"] = self.category_page(i)
        for i, p in enumerate(self.principles):
            files[f"principles/{p['id']}.html"] = self.principle_page(i)
        files.update(self.guide_pages())
        files["data/principles.json"] = canonical_json(self.pdoc)
        files["data/sources.json"] = canonical_json(self.sdoc)
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
