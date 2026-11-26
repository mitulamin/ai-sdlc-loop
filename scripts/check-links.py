#!/usr/bin/env python3
"""Check internal links in docs/ HTML and in the repo's markdown files.

Usage: scripts/check-links.py

Offline and standard library only. It checks:
  - relative links and asset references resolve to a file in the repo
  - #fragments resolve to an id in an HTML target or a heading in a markdown target
  - absolute-path links (/foo) in docs/ are rejected, since the site may live under a sub-path
  - template/ is skipped: its files resolve in a generated project after a profile overlay is applied
  - links to https://github.com/mitulamin/ai-sdlc-loop/(blob|tree)/main/<path> point at a path that exists here
  - docs/ and the generated agents/ and commands/ are covered: each must hold at least one checked file
External links are not fetched, so CI does not flake on the network.
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/mitulamin/ai-sdlc-loop"
SKIP_DIRS = {".git", "node_modules"}
EXTERNAL = re.compile(r"^([a-z][a-z0-9+.-]*:|//)", re.I)
MUST_COVER = ("docs", "agents", "commands")


class Collector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a" and a.get("name"):
            self.ids.add(a["name"])
        for key in ("href", "src"):
            if a.get(key):
                self.links.append(a[key])


def md_slug(heading):
    s = re.sub(r"<[^>]+>", "", heading).strip().lower()
    s = re.sub(r"[`*_]", "", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


_anchor_cache = {}


def anchors(path):
    if path in _anchor_cache:
        return _anchor_cache[path]
    text = path.read_text(encoding="utf-8", errors="replace")
    if path.suffix in (".html", ".htm"):
        c = Collector()
        c.feed(text)
        found = c.ids
    else:
        found, seen = set(), {}
        in_code = False
        for line in text.splitlines():
            if line.startswith("```"):
                in_code = not in_code
            m = None if in_code else re.match(r"^#{1,6}\s+(.*?)\s*#*$", line)
            if m:
                slug = md_slug(m.group(1))
                n = seen.get(slug, 0)
                seen[slug] = n + 1
                found.add(slug if n == 0 else f"{slug}-{n}")
    _anchor_cache[path] = found
    return found


def md_links(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", "", text)
    out = [m.group(1) for m in re.finditer(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", text)]
    out += [m.group(1) for m in re.finditer(r"^\[[^\]]+\]:\s*(\S+)", text, re.M)]
    out += [m.group(1) for m in re.finditer(r"<(https?://[^>\s]+)>", text)]
    return out


def check_target(src, link, in_docs):
    link = link.strip()
    if not link:
        return None
    if link.startswith(REPO + "/"):
        m = re.match(re.escape(REPO) + r"/(?:blob|tree)/main/([^#?]*)", link)
        if m:
            rel = unquote(m.group(1)).rstrip("/")
            if rel and not (ROOT / rel).exists():
                return f"{link} points at {rel}, which does not exist in this repo"
        return None
    if EXTERNAL.match(link):
        return None
    if link.startswith("/"):
        return f"absolute path link {link} (use a relative link)" if in_docs else None
    path, _, frag = link.partition("#")
    path = unquote(path.partition("?")[0])
    target = src if not path else (src.parent / path).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        return f"{link} escapes the repo"
    if target.is_dir():
        index = target / "index.html"
        if in_docs and index.exists():
            target = index
        else:
            return None if not frag else f"{link}: fragment on a directory"
    if not target.exists():
        return f"{link} does not exist"
    if frag and target.suffix in (".html", ".htm", ".md"):
        if unquote(frag) not in anchors(target):
            return f"{link}: no #{frag} in {target.relative_to(ROOT)}"
    return None


def main():
    problems, files = [], 0
    covered = dict.fromkeys(MUST_COVER, 0)
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        rel = path.relative_to(ROOT)
        if rel.parts[0] == "template":
            continue
        in_docs = rel.parts[0] == "docs"
        if path.suffix in (".html", ".htm") and in_docs:
            c = Collector()
            c.feed(path.read_text(encoding="utf-8"))
            links = c.links
        elif path.suffix == ".md":
            links = md_links(path.read_text(encoding="utf-8", errors="replace"))
        else:
            continue
        files += 1
        if rel.parts[0] in covered:
            covered[rel.parts[0]] += 1
        for link in links:
            msg = check_target(path, link, in_docs)
            if msg:
                problems.append(f"{rel}: {msg}")
    for d, n in covered.items():
        if not n:
            problems.append(f"{d}/: no files checked")
    if problems:
        print("\n".join(problems))
        print(f"{len(problems)} broken link(s)")
        return 1
    detail = ", ".join(f"{n} in {d}/" for d, n in covered.items())
    print(f"checked links in {files} files ({detail}), none broken")
    return 0


if __name__ == "__main__":
    sys.exit(main())
