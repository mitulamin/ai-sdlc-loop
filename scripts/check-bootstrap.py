#!/usr/bin/env python3
"""Check that scripts/bootstrap.sh sets up a new Cursor project where asked and touches nothing else.

Usage: scripts/check-bootstrap.py

Standard library only; needs bash and git. Each run goes into a temporary folder, with HOME and
XDG_CONFIG_HOME pointed at a fake home folder and a fake cursor command first on PATH, and fails if:
  - --help does not exit 0, or an option is accepted
  - a missing git or python3, a place inside the checkout, a bad or unknown place or name, a name
    that is already in use, or no answers at all is not refused with a plain message before
    anything is written
  - the questions do not show a numbered list of places with each full path, offer Documents when
    it does not exist, re-ask after a bad answer, an unusable name or a folder that is in use, take
    the suggested name on an empty answer, or put the project in the place chosen
  - the environment variables that skip the questions do not work
  - a project is made inside the checkout, or anything is written in the fake home folder other
    than the projects asked for
  - a copy of the checkout without .git (what downloading with curl gives) does not work
  - the Cursor harness files are not all there, or have the wrong licence, links or front matter
    (the same checks check-new-project.py runs on a Cursor project)
  - any editor, workspace, Cursor or model settings file is written (.vscode, .cursor/ files other than the
    agents, skills and one rule, settings or MCP files, .cursorrules and the like)
  - the project is not the solo template with the template's MIT LICENSE and no project notice, or
    holds the bootstrap sources or an unreplaced profile placeholder
  - START-HERE.md or the always-on rule is missing or differs from template/bootstrap/, the rule is
    not always on, the first-time note is not at the top of the rule and of AGENTS.md, or any of
    them names a path that does not exist in the project
  - the project is not a git repository on main with no commits, no remote and no git settings
    written, or has anything committed or staged
  - Cursor is not opened in the project when the cursor command works, or the next steps are not
    printed when it is missing or fails
"""
import importlib.util
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASH = shutil.which("bash") or "/bin/bash"
RULE = ".cursor/rules/ai-sdlc-bootstrap.mdc"


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def git(project, *args, env):
    return subprocess.run(["git", "-C", str(project), *args], capture_output=True, text=True, env=env)


def fake_cursor(folder, marker, exit_code=0):
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / "cursor"
    path.write_text(f'#!/bin/sh\necho "$1" > "{marker}"\nexit {exit_code}\n')
    path.chmod(path.stat().st_mode | stat.S_IXUSR)


def base_env(home):
    env = {k: v for k, v in os.environ.items() if not re.match(r"(GIT_(AUTHOR|COMMITTER|CONFIG|DIR|WORK_TREE)|AI_SDLC_)", k)}
    env.update(HOME=str(home), XDG_CONFIG_HOME=str(home / ".config"), GIT_CONFIG_NOSYSTEM="1")
    env.pop("PI_CODING_AGENT_DIR", None)
    return env


def run(checkout, env, answers="", extra=None, args=()):
    env = dict(env, **(extra or {}))
    return subprocess.run([BASH, str(checkout / "scripts" / "bootstrap.sh"), *args], cwd=checkout.parent,
                          input=answers, capture_output=True, text=True, env=env)


def listing(folder):
    return sorted(p.relative_to(folder).as_posix() for p in folder.rglob("*")) if folder.exists() else []


def check_refusals(tmp, checkout, env, home, errors):
    spot = tmp / "spot"
    spot.mkdir()
    ok_env = {"AI_SDLC_BOOTSTRAP_LOCATION": str(spot), "AI_SDLC_BOOTSTRAP_NAME": "fresh"}

    r = run(checkout, env, args=["--help"])
    if r.returncode != 0 or "new-project.sh" not in r.stdout or "AI_SDLC_BOOTSTRAP_LOCATION" not in r.stdout:
        errors.append("--help should exit 0, point teams at new-project.sh and name the environment variables")
    r = run(checkout, env, extra=ok_env, args=["--profile", "small-team"])
    if r.returncode == 0 or listing(spot):
        errors.append("an option was accepted, or something was written")

    limited = tmp / "limited"
    for label, tools, word in (("git", [], "Git"), ("python3", ["git"], "Python 3")):
        if limited.exists():
            shutil.rmtree(limited)
        limited.mkdir()
        for tool in tools:
            (limited / tool).symlink_to(shutil.which(tool))
        r = run(checkout, dict(env, PATH=str(limited)), extra=ok_env)
        if r.returncode == 0 or f"{word} is not installed" not in r.stderr or listing(spot):
            errors.append(f"missing {label} was not refused cleanly: {r.stderr.strip()!r}")

    cases = [
        ("a place inside the checkout", {"AI_SDLC_BOOTSTRAP_LOCATION": str(checkout / "scripts")}, "inside the ai-sdlc-loop"),
        ("an unknown place", {"AI_SDLC_BOOTSTRAP_LOCATION": "elsewhere"}, "must be home, documents, parent"),
        ("a missing Documents folder", {"AI_SDLC_BOOTSTRAP_LOCATION": "documents"}, "cannot find"),
        ("a folder that is not there", {"AI_SDLC_BOOTSTRAP_LOCATION": str(tmp / "nowhere")}, "cannot find"),
        ("a bad name", {"AI_SDLC_BOOTSTRAP_NAME": "my project"}, "not a good folder name"),
    ]
    for label, extra, message in cases:
        r = run(checkout, env, extra={**ok_env, **extra})
        if r.returncode == 0 or message not in r.stderr or listing(spot):
            errors.append(f"{label} was not refused cleanly: {r.stderr.strip()!r}")

    (spot / "taken").mkdir()
    (spot / "taken" / "mine.txt").write_text("mine\n")
    r = run(checkout, env, extra={**ok_env, "AI_SDLC_BOOTSTRAP_NAME": "taken"})
    if r.returncode == 0 or "not empty" not in r.stderr or listing(spot / "taken") != ["mine.txt"]:
        errors.append("a name that is in use was not refused cleanly")

    r = run(checkout, env)
    if r.returncode == 0 or "did not get an answer" not in r.stderr or listing(home):
        errors.append("no answers was not refused cleanly")
    if listing(checkout.parent / "my-project") or (ROOT / "my-project").exists():
        errors.append("a project was made after no answers")


def check_questions(tmp, checkout, env, home, marker, errors):
    docs = home / "Documents"
    parent = checkout.parent.resolve()
    home_r = home.resolve()

    r = run(checkout, env, answers="1\nmy-project\n")
    if r.returncode != 0 or not (home / "my-project" / "START-HERE.md").is_file():
        errors.append(f"home choice failed: {r.stderr.strip()}")
    if "no Documents folder" not in r.stdout or "3)" in r.stdout:
        errors.append("with no Documents folder, the list should say so and have two places")
    for path in (home_r, parent):
        if str(path) not in r.stdout:
            errors.append(f"the list does not show the full path {path}")
    if not re.search(r"1\) .*[Hh]ome", r.stdout) or not re.search(r"2\) .*(next to|one level up)", r.stdout):
        errors.append("the list does not number home and the folder next to the download")

    docs.mkdir()
    (docs / "existing").mkdir()
    (docs / "existing" / "x.txt").write_text("x\n")
    answers = "9\nx\n2\nmy project\nexisting\nmine\n"
    r = run(checkout, env, answers=answers)
    if r.returncode != 0 or not (docs / "mine" / "START-HERE.md").is_file():
        errors.append(f"Documents choice failed: {r.stderr.strip()}")
    for needle, why in (("3)", "three places"), (str(docs.resolve()), "the Documents path"), ("Please type one of the numbers", "a re-ask after a bad number"),
                        ("letters, numbers", "a re-ask after a bad name"), ("already exists", "a re-ask after a folder in use")):
        if needle not in r.stdout:
            errors.append(f"with Documents there, the output lacks {why}")
    if "no Documents folder" in r.stdout:
        errors.append("Documents exists but the list says it does not")
    if listing(docs / "existing") != ["x.txt"]:
        errors.append("a folder in use was changed")

    r = run(checkout, env, answers="3\n\n")
    if r.returncode != 0 or not (parent / "my-project-2" / "START-HERE.md").is_file() and not (parent / "my-project" / "START-HERE.md").is_file():
        errors.append(f"the folder next to the download, with the suggested name, failed: {r.stderr.strip()}")
    for made in (parent / "my-project", parent / "my-project-2"):
        shutil.rmtree(made, ignore_errors=True)
    if (ROOT / "my-project").exists() or any(p.name.startswith("my-project") for p in ROOT.iterdir()):
        errors.append("a project was made inside the checkout")
    return [home / "my-project", docs]


def check_project(check_new, inst_mod, project, errors):
    check_new.check_harness(inst_mod, "cursor", project, errors)
    template = ROOT / "template"
    if (project / "LICENSE").read_bytes() != (template / "LICENSE").read_bytes():
        errors.append("LICENSE differs from template/LICENSE")
    for rel in ("AGENTS.md", "PROCESS.md", "README.md", "CHANGELOG.md"):
        if not (project / rel).is_file():
            errors.append(f"{rel} is missing")
    for rel in ("ROLES.md", ".github/CODEOWNERS", ".github/PULL_REQUEST_TEMPLATE.md", "NOTICE.md", "bootstrap", "profiles"):
        if (project / rel).exists():
            errors.append(f"{rel} should not be in a solo bootstrap project")
    everything = "".join(p.read_text(encoding="utf-8", errors="ignore") for p in project.rglob("*") if p.is_file() and ".git" not in p.relative_to(project).parts)
    if "@PROFILE@" in everything:
        errors.append("an unreplaced @PROFILE@ placeholder")
    agents = (project / "AGENTS.md").read_text(encoding="utf-8")
    if "solo" not in agents:
        errors.append("AGENTS.md does not name the solo profile")

    cursor_dir = project / ".cursor"
    extra = sorted(p.name for p in cursor_dir.iterdir() if p.name not in ("agents", "skills", "rules"))
    if extra:
        errors.append("settings or other files in .cursor/ besides agents, skills and rules: " + ", ".join(extra))
    if sorted(p.name for p in (cursor_dir / "rules").iterdir()) != [Path(RULE).name]:
        errors.append("the rules folder holds more than the always-on rule")
    editor_files = sorted(p.relative_to(project).as_posix() for p in project.rglob("*")
                          if ".git" not in p.relative_to(project).parts
                          and (p.name in (".vscode", ".cursorrules", ".cursorignore", ".cursorindexingignore", ".idea", ".devcontainer")
                               or p.name.endswith(".code-workspace")
                               or (p.name in ("settings.json", "mcp.json", "cli.json", "hooks.json", "environment.json", "keybindings.json") and p.is_file())))
    if editor_files:
        errors.append("editor, Cursor or model settings were written: " + ", ".join(editor_files))
    brief, rule = project / "START-HERE.md", project / RULE
    for dest, src in ((brief, template / "bootstrap" / "START-HERE.md"), (rule, template / "bootstrap" / "ai-sdlc-bootstrap.mdc")):
        if not dest.is_file():
            errors.append(f"{dest.relative_to(project)} is missing")
        elif dest.read_bytes() != src.read_bytes():
            errors.append(f"{dest.relative_to(project)} differs from {src.relative_to(ROOT)}")
    note = (template / "bootstrap" / "first-time-note.md").read_text(encoding="utf-8").strip()
    if rule.is_file():
        front, body = rule.read_text(encoding="utf-8").split("---", 2)[1:]
        if not re.search(r"^alwaysApply:\s*true\s*$", front, re.M):
            errors.append("the rule is not always on (alwaysApply: true)")
        if not body.lstrip().startswith(note):
            errors.append("the first-time note is not at the top of the rule")
    quoted = "\n".join("> " + line if line else ">" for line in note.splitlines())
    lines = agents.split("\n")
    if not lines[0].startswith("# ") or "\n".join(lines[1:6]).strip().split("\n\n")[0] != quoted:
        errors.append("the first-time note is not at the top of AGENTS.md, right under its heading")
    for f in (brief, rule, project / "AGENTS.md"):
        if f.is_file():
            for ref in re.findall(r"`((?:\.cursor/|START-HERE|AGENTS|PROCESS)[^`\s]*\.(?:md|mdc))`", f.read_text(encoding="utf-8")):
                if not (project / ref).is_file():
                    errors.append(f"{f.name} names {ref}, which is not in the project")
    if not (project / ".cursor" / "agents").is_dir():
        errors.append("the note points at .cursor/agents, which is not in the project")


def check_git(project, env, errors):
    if git(project, "symbolic-ref", "--short", "HEAD", env=env).stdout.strip() != "main":
        errors.append("the branch is not main")
    if git(project, "rev-parse", "--verify", "-q", "HEAD", env=env).returncode == 0:
        errors.append("a commit was made; the first commit is left to the agent")
    if git(project, "diff", "--cached", "--name-only", env=env).stdout.strip():
        errors.append("files were staged; staging is left to the agent")
    if git(project, "remote", env=env).stdout.strip():
        errors.append("a git remote was added")
    for key in ("user.name", "user.email", "commit.gpgsign"):
        if git(project, "config", "--local", "--get", key, env=env).stdout.strip():
            errors.append(f"{key} was written to the project's git settings")


def main():
    inst_mod = load("install_harness", "install-harness.py")
    check_new = load("check_new_project", "check-new-project.py")
    errors = []
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp).resolve()
        home = tmp / "home"
        home.mkdir()
        env = base_env(home)
        marker = tmp / "opened"
        fake_cursor(tmp / "bin", marker)
        env_open = dict(env, PATH=f"{tmp / 'bin'}{os.pathsep}{env['PATH']}")

        # What downloading with curl gives: the repo's files with no .git folder.
        checkout = tmp / "checkouts" / "ai-sdlc-loop-main"
        shutil.copytree(ROOT, checkout, ignore=shutil.ignore_patterns(".git", "__pycache__"), symlinks=True)

        check_refusals(tmp, checkout, env, home, errors)
        expected_in_home = check_questions(tmp, checkout, env, home, marker, errors)

        out = tmp / "out"
        out.mkdir()
        r = run(checkout, env_open, extra={"AI_SDLC_BOOTSTRAP_LOCATION": str(out), "AI_SDLC_BOOTSTRAP_NAME": "app"})
        project = out / "app"
        if r.returncode != 0:
            errors.append(f"bootstrap.sh exited {r.returncode}: {r.stderr.strip()}")
        else:
            check_project(check_new, inst_mod, project, errors)
            check_git(project, env, errors)
            if not marker.is_file() or marker.read_text().strip() != str(project):
                errors.append("Cursor was not opened in the project")
            if "Next:" in r.stdout:
                errors.append("printed next steps although Cursor opened")

        again = run(checkout, env_open, extra={"AI_SDLC_BOOTSTRAP_LOCATION": str(out), "AI_SDLC_BOOTSTRAP_NAME": "app"})
        if again.returncode == 0:
            errors.append("running again into a project that exists did not fail")

        failing = tmp / "failing-bin"
        fake_cursor(failing, tmp / "opened2", exit_code=1)
        r = run(checkout, dict(env, PATH=f"{failing}{os.pathsep}{env['PATH']}"),
                extra={"AI_SDLC_BOOTSTRAP_LOCATION": str(out), "AI_SDLC_BOOTSTRAP_NAME": "app2"})
        if r.returncode != 0 or "Next: open the folder" not in r.stdout:
            errors.append(f"a failing cursor command did not lead to the next steps: {r.stderr.strip()}")

        if shutil.which("cursor", path=env["PATH"]) is None:
            r = run(checkout, env, extra={"AI_SDLC_BOOTSTRAP_LOCATION": str(out), "AI_SDLC_BOOTSTRAP_NAME": "app3"})
            if r.returncode != 0 or "Next: open the folder" not in r.stdout:
                errors.append("without the cursor command, the next steps were not printed")

        allowed = [p.resolve() for p in expected_in_home]
        leaked = sorted(p.relative_to(home).as_posix() for p in home.rglob("*")
                        if not any(p.resolve() == a or a in p.resolve().parents for a in allowed))
        if leaked:
            errors.append("files written in the home folder other than the projects asked for: " + ", ".join(leaked))
        if list(ROOT.glob("my-project*")) or list((ROOT / "scripts").glob(".bootstrap*")):
            errors.append("something was written inside the checkout")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("bootstrap.sh asks where to put the project, sets it up for Cursor with no commits, and writes nothing else")
    return 0


if __name__ == "__main__":
    sys.exit(main())
