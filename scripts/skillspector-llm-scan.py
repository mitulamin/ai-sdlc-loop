#!/usr/bin/env python3
"""SkillSpector scan with the LLM analyzers on, and the record that goes with it.

Usage:
  scripts/skillspector-llm-scan.py --record PATH [--only GLOB] [--jobs N] [--retries N]
                                   [--skip-without-key] [--allow-unreviewed]
  scripts/skillspector-llm-scan.py --verify release-scans/<tag>.md

This is the one entry point for the LLM-mode scan: CI calls it (workflows skillspector-llm and
release-gate) and so does a person running it locally. It scans the same targets as
scripts/skillspector-scan.py (every skill, agents/, commands/, template/ and a throwaway install
for each harness) but without --no-llm, so SkillSpector sends the text of those files to the model
provider. Do not run it if that is not acceptable for the files being scanned. The steps and the
record are in RELEASING.md.

Provider and key. The script picks the provider from the key it finds:
  XAI_API_KEY           xAI (https://api.x.ai/v1), through SkillSpector's openai_compatible
                        provider. The model is the first of XAI_MODELS that xAI lists for the key.
  NVIDIA_INFERENCE_KEY  NVIDIA Build (https://integrate.api.nvidia.com/v1), SkillSpector's nv_build
                        provider, with the model NV_BUILD_MODEL. SkillSpector's own default for
                        nv_build (z-ai/glm-5.3-flash in 2.13.7) is listed but does not answer.
XAI_API_KEY wins when both are set. SKILLSPECTOR_PROVIDER overrides the choice: nv_build or xai
use the keys above, and any other SkillSpector provider (for example ollama, which needs a local
Ollama service and no key, or openai_compatible with SKILLSPECTOR_COMPAT_API_KEY and
SKILLSPECTOR_COMPAT_BASE_URL) uses that provider's own variables. SKILLSPECTOR_MODEL overrides the
model. Keys are never printed: anything the script echoes is scrubbed of them.

Before scanning, with xAI or NVIDIA Build, one tiny request checks the key and the model. No key
stops the script with exit code 2, or with exit code 0 and a notice under --skip-without-key (CI
uses that for runs that get no secrets, such as pull requests from forks). A key that is rejected,
a model that is retired or not served, or a model that does not answer the check in time always
stops it with exit code 2.

Speed and rate limits. A target takes most of a minute whatever the model, because SkillSpector
makes a few long LLM calls for it, so targets are scanned in parallel: --jobs, or SKILLSPECTOR_JOBS,
defaults to DEFAULT_JOBS for the provider. NVIDIA Build's free tier allows roughly 40 requests a
minute, which its default stays under; xAI's limits are per team and much higher. SkillSpector
retries a rate-limited call itself; a target whose LLM calls still failed is scanned again after
an exponential backoff with jitter, up to --retries times. Results from every target are
collected into one record and one exit code.

SkillSpector reports a degraded LLM stage (no key, a rejected key, a failed request) as a warning
and still exits 0 with static results only. This script treats that as a failure: a target counts
only if the LLM was requested, every LLM call succeeded, no semantic analyzer failed, every file
was inspected and the run succeeded. The exit code is 2 for a target that does not meet that.

--record writes a Markdown record with the commit, a content id of the scanned files, the scanner
version, provider and model, the coverage of each target and every finding. A finding that an
entry in .github/skillspector-exceptions.yaml explains (same rule, file, matched text and source
line) is marked as covered by it. Every other finding is written as UNREVIEWED. Exit code 0 means
no unreviewed findings (or --allow-unreviewed was given, which CI uses so that findings show up as
warnings and in the record without failing every run), 1 means there are some; a person then fixes
the issue or replaces UNREVIEWED in the record with one of the dispositions below, and --verify
checks the record is complete.

Dispositions (replace UNREVIEWED with exactly one, followed by a reason):
  FIXED: <commit or PR that fixed it>
  FALSE POSITIVE: <why it is not an issue>
  ACCEPTED: <who accepted the risk, and why it ships anyway>

--verify exits 0 only when the record names a commit, says the scan completed on a full run, was
made on exactly the files now in HEAD (apart from release-scans/), and no finding is left
UNREVIEWED or has a disposition without a reason.
"""
import argparse
import datetime
import fnmatch
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import hashlib
import random
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from skillspector_targets import (  # noqa: E402
    ROOT, apply_exceptions, as_list, coverage_problem, dir_targets, find_scanner, harness_targets, load_exceptions, skill_targets,
)

TIMEOUT_SECONDS = 1800
NV_BUILD_MODEL = "nvidia/nemotron-3.5-super-vl-120b-a12b"
XAI_BASE_URL = "https://api.x.ai/v1"
XAI_MODELS = ("grok-4.20-0309-non-reasoning", "grok-4.7")
KEY_ENVS = {"xai": "XAI_API_KEY", "nv_build": "NVIDIA_INFERENCE_KEY"}
DEFAULT_JOBS = {"xai": 16, "nv_build": 8}
FALLBACK_JOBS = 4
PREFLIGHT_TIMEOUT_SECONDS = 90
RETRY_PAUSE_SECONDS = 30
RECORDS_DIR = "release-scans"
UNREVIEWED = "UNREVIEWED"
DISPOSITION = re.compile(r"^(FIXED|FALSE POSITIVE|ACCEPTED|COVERED BY STATIC EXCEPTION): \S")
SEMANTIC_PREFIX = "semantic_"


def no_llm_work(data):
    """True when every semantic analyzer found no file it applies to, so a run with no LLM calls is complete.

    A harness install holds agent, command and config files but no skill package, so SkillSpector's
    semantic analyzers have nothing to read there; the same text is read with the LLM as agents/,
    commands/ and skills/.
    """
    statuses = (data.get("analysis_completeness") or {}).get("analyzer_statuses", [])
    semantic = [a for a in statuses if a.get("analyzer_id", "").startswith(SEMANTIC_PREFIX)]
    return bool(semantic) and all(a.get("status") == "not_applicable" for a in semantic)


def llm_problem(data, proc):
    """Return why this report cannot count as a successful LLM-mode scan, or None."""
    meta = data.get("metadata", {})
    comp = data.get("analysis_completeness") or {}
    if not data.get("execution_successful"):
        return "SkillSpector reported execution_successful=false"
    if not meta.get("llm_requested"):
        return "the LLM was not requested"
    if not meta.get("llm_available"):
        return "no LLM provider was available (check SKILLSPECTOR_PROVIDER and its credential)"
    attempted, succeeded = meta.get("llm_calls_attempted") or 0, meta.get("llm_calls_succeeded") or 0
    if meta.get("llm_degraded") or (not attempted and not no_llm_work(data)) or succeeded != attempted:
        return f"LLM stage degraded: {succeeded} of {attempted} calls succeeded ({meta.get('llm_error', 'no detail')})"
    for a in comp.get("analyzer_statuses", []):
        if a.get("analyzer_id", "").startswith(SEMANTIC_PREFIX) and a.get("status") not in ("completed", "not_applicable"):
            return f"semantic analyzer {a['analyzer_id']} finished with status {a.get('status')}"
    if not comp.get("is_complete"):
        return f"incomplete coverage ({comp.get('coverage_percent')}%)"
    if "LLM stage degraded" in (proc.stderr or ""):
        return "SkillSpector warned that the LLM stage degraded"
    return None


def scrub(text):
    for name in (*KEY_ENVS.values(), "SKILLSPECTOR_COMPAT_API_KEY"):
        key = os.environ.get(name, "").strip()
        if key:
            text = text.replace(key, "***")
    return text


def scan_once(target, tmp):
    report = tmp / f"{target.name}.json"
    report.unlink(missing_ok=True)
    try:
        proc = subprocess.run(
            ["skillspector", "scan", str(target.path), "--fail-on-incomplete", "--format", "json", "--output", str(report)],
            capture_output=True, text=True, timeout=TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        return None, f"timed out after {TIMEOUT_SECONDS}s", True
    if not report.exists():
        return None, scrub(proc.stderr.strip() or proc.stdout.strip())[:300], True
    data = json.loads(report.read_text(encoding="utf-8"))
    problem = llm_problem(data, proc)
    if problem:
        return data, scrub(problem), True
    return data, coverage_problem(target, data.get("analysis_completeness")), False


def scan(target, tmp, retries):
    """Return (target, report data or None, problem or None)."""
    started = time.monotonic()
    for attempt in range(retries + 1):
        data, problem, retryable = scan_once(target, tmp)
        if not problem or not retryable or attempt == retries:
            break
        # Jitter spreads parallel targets that hit the same rate limit at the same moment.
        pause = RETRY_PAUSE_SECONDS * 2 ** attempt * random.uniform(1, 1.5)
        print(f"retry {attempt + 1}/{retries} for {target.name} in {pause:.0f}s: {problem}", flush=True)
        time.sleep(pause)
    calls = (data or {}).get("metadata", {}).get("llm_calls_succeeded", 0)
    print(f"{'FAIL' if problem else 'ok  '} {target.name}: {calls} LLM calls, {time.monotonic() - started:.0f}s", flush=True)
    return target, data, problem


def choose_provider():
    """Return (provider, key env or None): SKILLSPECTOR_PROVIDER if set, else xai or nv_build by the key present."""
    explicit = os.environ.get("SKILLSPECTOR_PROVIDER", "").strip()
    if explicit:
        return explicit, KEY_ENVS.get(explicit)
    for provider, env in KEY_ENVS.items():
        if os.environ.get(env, "").strip():
            return provider, env
    return None, None


def endpoint(provider):
    if provider == "xai":
        return XAI_BASE_URL
    from skillspector.providers.nv_build.provider import BUILD_BASE_URL
    return BUILD_BASE_URL


def call(url, key, body=None):
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None, method="POST" if body else "GET",
                                 headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=PREFLIGHT_TIMEOUT_SECONDS) as r:
        return json.loads(r.read() or b"{}")


def pick_xai_model(key):
    """Return (model, None) for the first of XAI_MODELS the key can use, or (None, reason)."""
    try:
        listed = {m.get("id") for m in call(f"{XAI_BASE_URL}/models", key).get("data", [])}
    except urllib.error.HTTPError as e:
        detail = scrub(e.read().decode(errors="replace"))[:200]
        if e.code in (400, 401, 403):
            # xAI answers a malformed or unknown key with 400, not 401.
            return None, (f"XAI_API_KEY was rejected by {XAI_BASE_URL} (HTTP {e.code}: {detail}); "
                          "check the key is valid and its team has credits")
        return None, f"could not list models on {XAI_BASE_URL} (HTTP {e.code}: {detail})"
    except (TimeoutError, urllib.error.URLError) as e:
        return None, f"could not reach {XAI_BASE_URL} ({scrub(str(e))})"
    for model in XAI_MODELS:
        if model in listed:
            return model, None
    return None, (f"none of {', '.join(XAI_MODELS)} is listed for this key on {XAI_BASE_URL}/models; "
                  "set SKILLSPECTOR_MODEL to one that is")


def preflight(provider, key_env, model):
    """Check the key and model with one tiny request. Return None, or the reason the scan cannot run."""
    base = endpoint(provider)
    body = {"model": model, "messages": [{"role": "user", "content": "ping"}], "max_tokens": 16}
    last = None
    for attempt in range(3):
        try:
            call(f"{base}/chat/completions", os.environ[key_env].strip(), body)
            return None
        except urllib.error.HTTPError as e:
            if e.code in (401, 403):
                return f"{key_env} was rejected by {base} (HTTP {e.code}); check the key is valid and unexpired"
            if e.code in (400, 404, 410):
                detail = scrub(e.read().decode(errors="replace"))[:200]
                return f"model {model} is not available on {base} (HTTP {e.code}: {detail}); set SKILLSPECTOR_MODEL to one that is"
            if e.code == 429:
                return None
            last = f"HTTP {e.code}"
        except (TimeoutError, urllib.error.URLError) as e:
            if isinstance(e, TimeoutError) or isinstance(getattr(e, "reason", None), TimeoutError):
                # Both endpoints reject a bad key at once, so a timeout means the model is not answering.
                return (f"model {model} did not answer a tiny request on {base} within "
                        f"{PREFLIGHT_TIMEOUT_SECONDS}s; set SKILLSPECTOR_MODEL to a model that responds")
            last = scrub(str(e))
        time.sleep(10 * (attempt + 1))
    return f"could not reach {base} to check the key ({last})"


def configure(provider, key_env):
    """Set the SkillSpector variables for xai or nv_build. Return (model, None) or (None, reason)."""
    model = os.environ.get("SKILLSPECTOR_MODEL", "").strip()
    if provider == "xai":
        key = os.environ[key_env].strip()
        if not model:
            model, why = pick_xai_model(key)
            if why:
                return None, why
        os.environ.update(SKILLSPECTOR_PROVIDER="openai_compatible", SKILLSPECTOR_COMPAT_BASE_URL=XAI_BASE_URL,
                          SKILLSPECTOR_COMPAT_API_KEY=key)
    else:
        model = model or NV_BUILD_MODEL
        os.environ["SKILLSPECTOR_PROVIDER"] = provider
    os.environ["SKILLSPECTOR_MODEL"] = model
    return model, preflight(provider, key_env, model)


def content_id():
    """A hash of every tracked file in HEAD except the scan records, so a record survives a squash merge."""
    listing = git("ls-tree", "-r", "HEAD")
    kept = [x for x in listing.split("\n") if x and not x.split("\t", 1)[1].startswith(RECORDS_DIR + "/")]
    return hashlib.sha256("\n".join(kept).encode()).hexdigest()


def provider_summary(reports):
    seen = {}
    for data in reports:
        prov = data.get("metadata", {}).get("llm_provenance", {})
        adapter = prov.get("provider", {}).get("resolved_adapter", "unknown")
        for a in prov.get("analyzers", []):
            seen.setdefault((adapter, a.get("model", "unknown")), set()).add(a.get("analyzer_id"))
    return sorted(seen)


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True).stdout.strip()


def summary(lines):
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        with open(path, "a", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")


def cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def record(args):
    started = time.monotonic()
    provider, key_env = choose_provider()
    _, version, err = find_scanner()
    if err:
        print(err, file=sys.stderr)
        return 2
    wanted = [key_env] if key_env else list(KEY_ENVS.values())
    if provider in KEY_ENVS or provider is None:
        if not any(os.environ.get(e, "").strip() for e in wanted):
            names = " or ".join(wanted)
            msg = (f"{names} is not set, so the LLM-mode scan did not run. Export an xAI key as XAI_API_KEY or an "
                   "NVIDIA Build key as NVIDIA_INFERENCE_KEY, or set SKILLSPECTOR_PROVIDER to another provider (see RELEASING.md).")
            if args.skip_without_key:
                print(f"::notice title=LLM scan skipped::{msg}" if os.environ.get("GITHUB_ACTIONS") else f"SKIPPED: {msg}")
                summary(["## SkillSpector LLM-mode scan", "", f"Skipped: {names} is not available to this run (for example a pull request from a fork)."])
                return 0
            print(msg, file=sys.stderr)
            return 2
        model, why = configure(provider, key_env)
        if why:
            print(f"::error title=LLM scan could not run::{why}" if os.environ.get("GITHUB_ACTIONS") else f"ERROR: {why}", file=sys.stderr)
            return 2
        print(f"provider {provider} ({endpoint(provider)}), model {model}", flush=True)
    jobs = args.jobs or DEFAULT_JOBS.get(provider, FALLBACK_JOBS)
    exceptions, problems = load_exceptions()
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 2
    skills, err = skill_targets()
    dirs, err2 = dir_targets()
    if err or err2:
        print(err or err2, file=sys.stderr)
        return 2
    dirty = git("status", "--porcelain")
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        harnesses, err = harness_targets(tmp / "installs")
        if err:
            print(err, file=sys.stderr)
            return 2
        targets = skills + dirs + harnesses
        if args.only:
            targets = [x for x in targets if fnmatch.fnmatchcase(x.name, args.only)]
            if not targets:
                print(f"--only {args.only!r} matches no target", file=sys.stderr)
                return 2
        print(f"scanning {len(targets)} targets, {jobs} at a time", flush=True)
        with ThreadPoolExecutor(max_workers=jobs) as pool:
            results = list(pool.map(lambda x: scan(x, tmp, args.retries), targets))
        broken = [(x, p) for x, d, p in results if p]
        for x, p in broken:
            print(f"ERROR {x.name}: not a successful LLM-mode scan: {p}", file=sys.stderr)
        if broken:
            return 2
        rows = []
        for x, data, _ in results:
            own = [(i, e) for i, e in enumerate(exceptions) if any(fnmatch.fnmatchcase(x.name, g) for g in as_list(e["target"]))]
            unexplained, _hits = apply_exceptions(x.path, data.get("issues", []), own)
            ids = {id(f) for f in unexplained}
            for f in data.get("issues", []):
                loc = f.get("location", {})
                disp = UNREVIEWED if id(f) in ids else "COVERED BY STATIC EXCEPTION: same rule, file, text and line as an entry in .github/skillspector-exceptions.yaml"
                rows.append((x.name, f.get("id"), f.get("severity"), f"{loc.get('file')}:{loc.get('start_line')}",
                             f.get("finding"), f.get("explanation"), disp))
        reports = [d for _, d, _ in results]

    open_rows = [r for r in rows if r[6] == UNREVIEWED]
    models = provider_summary(reports)
    calls = sum(d["metadata"].get("llm_calls_succeeded", 0) for d in reports)
    minutes = f"{(time.monotonic() - started) / 60:.1f} minutes, {jobs} targets at a time"
    static_only = [x.name for x, d, _ in results if not d["metadata"].get("llm_calls_attempted")]
    lines = [
        "# SkillSpector LLM-mode scan record", "",
        f"- Commit: {git('rev-parse', 'HEAD')}" + (" (working tree has uncommitted changes)" if dirty else ""),
        f"- Date (UTC): {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M')}",
        f"- Content id (every tracked file except {RECORDS_DIR}/): {content_id()}",
        f"- Scanner: {version}",
        f"- Provider and model: " + ("; ".join(f"{p} / {m}" for p, m in models) or "unknown")
        + (f" (endpoint {endpoint(provider)})" if provider in KEY_ENVS else ""),
        f"- Wall-clock time: {minutes}",
        f"- Targets scanned: {len(targets)} ({'all' if not args.only else 'only ' + args.only}); every file inspected: yes",
        f"- LLM calls succeeded: {calls}, failed: 0",
        "- Targets with no file the LLM analyzers apply to (static rules only): " + (", ".join(static_only) or "none"),
        "- Scan completed: yes",
        f"- Findings: {len(rows)} in total, {len(open_rows)} {UNREVIEWED}", "",
        "## Findings", "",
    ]
    if rows:
        lines += ["| Target | Rule | Severity | Where | Matched | Why SkillSpector flagged it | Disposition |", "| --- | --- | --- | --- | --- | --- | --- |"]
        lines += ["| " + " | ".join(cell(c) for c in r) + " |" for r in rows]
    else:
        lines.append("None.")
    out = Path(args.record)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {out}: {len(targets)} targets in {minutes}, {len(rows)} findings, {len(open_rows)} {UNREVIEWED}")
    in_ci = bool(os.environ.get("GITHUB_ACTIONS"))
    for r in open_rows:
        text = cell(f"{r[0]} {r[1]} ({r[2]}) at {r[3]}: {r[4]}")[:400]
        print(f"::warning title=LLM scan finding::{text}" if in_ci else f"UNREVIEWED {text}")
    summary(["## SkillSpector LLM-mode scan", "",
             f"- Provider and model: " + ("; ".join(f"{p} / {m}" for p, m in models) or "unknown"),
             f"- Targets scanned: {len(targets)} in {minutes}; LLM calls succeeded: {calls}",
             f"- Findings: {len(rows)} in total, {len(open_rows)} not covered by a static exception", ""]
            + ([f"- {cell(r[0])}: {cell(r[1])} ({cell(r[2])}) at {cell(r[3])}: {cell(r[4])[:200]}" for r in open_rows] or []))
    return 1 if open_rows and not args.allow_unreviewed else 0


def verify(path):
    p = Path(path)
    if not p.is_file():
        print(f"{path}: no such record", file=sys.stderr)
        return 1
    text = p.read_text(encoding="utf-8")
    problems = []
    if not re.search(r"^- Commit: [0-9a-f]{7,40}", text, re.M):
        problems.append("no commit named")
    if "- Scan completed: yes" not in text:
        problems.append("the record does not say the scan completed")
    if "(all); every file inspected: yes" not in text:
        problems.append("the record is not of a full scan (it was made with --only, or a file was not inspected)")
    m = re.search(r"^- Content id \(.*?\): ([0-9a-f]{64})", text, re.M)
    if not m:
        problems.append("the record has no content id")
    elif m.group(1) != content_id():
        problems.append("files changed after the scan: the record was made on different content than HEAD (apart from "
                        f"{RECORDS_DIR}/); run the scan again")
    if "uncommitted changes" in text:
        problems.append("the scan ran on a working tree with uncommitted changes")
    in_table = False
    for n, line in enumerate(text.split("\n"), 1):
        if line.startswith("| Target |"):
            in_table = True
            continue
        if in_table and line.startswith("| ") and not line.startswith("| ---"):
            cells = re.split(r"(?<!\\)\|", line.strip().strip("|"))
            disposition = cells[-1].strip()
            if disposition == UNREVIEWED or not DISPOSITION.match(disposition):
                problems.append(f"line {n}: finding has no valid disposition ({disposition[:40]!r})")
    if problems:
        print("\n".join(f"{path}: {x}" for x in problems), file=sys.stderr)
        return 1
    print(f"OK: {path} names a commit, says the scan completed and has a disposition with a reason for every finding")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--record", metavar="PATH", help="run the scan and write the record here")
    mode.add_argument("--verify", metavar="PATH", help="check a record is complete")
    ap.add_argument("--jobs", type=int, default=int(os.environ.get("SKILLSPECTOR_JOBS", "0")),
                    help="targets scanned in parallel (default SKILLSPECTOR_JOBS, else DEFAULT_JOBS for the provider)")
    ap.add_argument("--retries", type=int, default=2, help="times to retry a target whose LLM calls failed")
    ap.add_argument("--skip-without-key", action="store_true",
                    help="exit 0 with a notice if neither XAI_API_KEY nor NVIDIA_INFERENCE_KEY is set (for CI runs without secrets)")
    ap.add_argument("--allow-unreviewed", action="store_true",
                    help="exit 0 even if findings are UNREVIEWED; they are still listed (CI)")
    ap.add_argument("--only", metavar="GLOB", help="scan only targets whose name matches (not for a release record)")
    args = ap.parse_args()
    if args.verify:
        return verify(args.verify)
    return record(args)


if __name__ == "__main__":
    sys.exit(main())
