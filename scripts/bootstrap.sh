#!/usr/bin/env bash
# The goal is to hand you over to a Cursor agent that understands what's going on and can
# handhold you from there, so you never feel unassisted. Bootstrap only gives Cursor a leg up
# into a full SDLC that protects you.
#
# Bootstrap: set up a new project for Cursor, with the solo template, the loop's coordinator,
# agents, skills and /sdlc-* commands in .cursor/, an always-on Cursor rule, a START-HERE.md brief
# and a local git repository (on main, with no commits yet). Run it from inside your checkout of
# ai-sdlc-loop. It asks where to put the project and what to call it, and never puts it inside
# this checkout.
#
# Before you start, you need:
#   - Python 3 (this script checks for it and does not install it)
#   - Git (this script checks for it and does not install it)
#   - cURL, only if you download ai-sdlc-loop with curl instead of git clone
#   - Cursor, signed in. If its cursor command is missing, you are told how to open the folder
#
# To skip the questions, set AI_SDLC_BOOTSTRAP_LOCATION to home, documents, parent or the full
# path of an existing folder, and AI_SDLC_BOOTSTRAP_NAME to the project's folder name.
set -euo pipefail

script="${BASH_SOURCE[0]}"
case "$script" in
  */*) root="$(cd "${script%/*}/.." && pwd -P)" ;;
  *) root="$(cd .. && pwd -P)" ;;
esac
use_page="https://mitulamin.github.io/ai-sdlc-loop/use.html"
default_name="my-project"

stop() {
  printf '%s\n' "$@" >&2
  exit 1
}

if [ $# -gt 0 ]; then
  case "$1" in
    -h|--help)
      cat <<EOT
Usage: ./scripts/bootstrap.sh

Run it from inside your checkout of ai-sdlc-loop. It asks where you would like
the project to be put (your home folder, your Documents folder, or the folder
next to this one) and what to call it, then sets up a new project for Cursor:
the solo template, the coordinator, agents, skills and /sdlc-* commands in
.cursor/, an always-on Cursor rule, a START-HERE.md brief, and a local git
repository on main with no commits yet. It never puts the project inside this
checkout, does not create a GitHub repository, add a remote or sign you up for
anything, and opens Cursor if the cursor command is available.

You need Python 3 and Git. It does not install them.

To skip the questions, set AI_SDLC_BOOTSTRAP_LOCATION to home, documents,
parent or the full path of an existing folder, and AI_SDLC_BOOTSTRAP_NAME to
the project's folder name.

Teams and larger organisations: use scripts/new-project.sh instead.
Guide: $use_page
EOT
      exit 0 ;;
    *) stop "bootstrap.sh takes no options. Run ./scripts/bootstrap.sh and answer the questions." ;;
  esac
fi

command -v git >/dev/null 2>&1 || stop \
  "Git is not installed, and this setup needs it to keep a history of your project." \
  "Install git from https://git-scm.com/downloads, then run this again."
command -v python3 >/dev/null 2>&1 || stop \
  "Python 3 is not installed, and this setup needs it to copy the project files." \
  "Install it from https://www.python.org/downloads/, then run this again."

resolve_dir() { (cd "$1" 2>/dev/null && pwd -P); }

inside_checkout() {
  case "$1/" in
    "$root"/*) return 0 ;;
  esac
  return 1
}

ask() {
  printf '%s ' "$1"
  if ! IFS= read -r answer; then
    echo
    stop "I did not get an answer, so I have stopped without changing anything." \
      "Run it again in a terminal, or set AI_SDLC_BOOTSTRAP_LOCATION and AI_SDLC_BOOTSTRAP_NAME (see --help)."
  fi
}

in_use() {
  [ -e "$1" ] && { [ ! -d "$1" ] || [ -n "$(ls -A "$1")" ]; }
}

home_dir=""
if [ -n "${HOME:-}" ] && [ -d "$HOME" ]; then home_dir="$(resolve_dir "$HOME")"; fi
docs_dir=""
if [ -n "$home_dir" ] && [ -d "$home_dir/Documents" ]; then docs_dir="$(resolve_dir "$home_dir/Documents")"; fi
parent_dir="$(resolve_dir "$root/..")"

location=""
if [ -n "${AI_SDLC_BOOTSTRAP_LOCATION:-}" ]; then
  want="$AI_SDLC_BOOTSTRAP_LOCATION"
  case "$want" in
    home) location="$home_dir" ;;
    documents) location="$docs_dir" ;;
    parent) location="$parent_dir" ;;
    /*) location="$(resolve_dir "$want" || true)" ;;
    *) stop "AI_SDLC_BOOTSTRAP_LOCATION must be home, documents, parent or the full path of an existing folder." ;;
  esac
  [ -n "$location" ] || stop "I cannot find the folder for AI_SDLC_BOOTSTRAP_LOCATION=$want, so I have not changed anything."
  if inside_checkout "$location"; then
    stop "That place is inside the ai-sdlc-loop folder itself, so I have not changed anything." \
      "Choose a place outside it."
  fi
else
  labels=()
  places=()
  if [ -n "$home_dir" ]; then labels+=("Your home folder"); places+=("$home_dir"); fi
  if [ -n "$docs_dir" ]; then labels+=("Your Documents folder"); places+=("$docs_dir"); fi
  labels+=("The folder next to this download (one level up)")
  places+=("$parent_dir")
  while true; do
    echo
    echo "Where would you like the project to be put?"
    for i in "${!places[@]}"; do
      printf '  %d) %s\n     %s\n' "$((i + 1))" "${labels[$i]}" "${places[$i]}"
    done
    if [ -z "$docs_dir" ]; then echo "  (There is no Documents folder here, so it is not on the list.)"; fi
    ask "Type a number and press Enter:"
    if [[ "$answer" =~ ^[0-9]+$ ]] && [ "$answer" -ge 1 ] && [ "$answer" -le "${#places[@]}" ]; then
      location="${places[$((answer - 1))]}"
      if inside_checkout "$location"; then
        echo "That place is inside the ai-sdlc-loop folder itself, and a project cannot go there. Please pick another."
        continue
      fi
      break
    fi
    echo "Please type one of the numbers above."
  done
fi

valid_name='^[A-Za-z0-9][A-Za-z0-9._-]*$'
explain_name="Please use letters, numbers, dashes or underscores, with no spaces, starting with a letter or number."
name=""
if [ -n "${AI_SDLC_BOOTSTRAP_NAME:-}" ]; then
  name="$AI_SDLC_BOOTSTRAP_NAME"
  [[ "$name" =~ $valid_name ]] || stop "AI_SDLC_BOOTSTRAP_NAME is not a good folder name. $explain_name"
  if in_use "$location/$name"; then
    stop "$location/$name already exists and is not empty, so I have not changed anything." \
      "Choose a different AI_SDLC_BOOTSTRAP_NAME."
  fi
else
  suggestion="$default_name"
  n=2
  while in_use "$location/$suggestion"; do
    suggestion="$default_name-$n"
    n=$((n + 1))
  done
  while true; do
    echo
    ask "What would you like to call your project? It becomes the folder's name. [$suggestion]"
    name="${answer:-$suggestion}"
    if ! [[ "$name" =~ $valid_name ]]; then
      echo "$explain_name"
      continue
    fi
    if in_use "$location/$name"; then
      echo "A folder called $name already exists in $location and is not empty. I will not touch it, so please choose another name."
      continue
    fi
    break
  done
fi
target="$location/$name"

if ! out="$(bash "$root/scripts/new-project.sh" --harness cursor "$target" solo 2>&1)"; then
  printf '%s\n' "$out" >&2
  stop "" "Setup stopped before it finished. The messages above say why."
fi
cd "$target"

copy_new() {
  if [ -e "$2" ]; then stop "$2 already exists in $target, so I stopped rather than overwrite it."; fi
  mkdir -p "$(dirname "$2")"
  cp "$1" "$2"
}
copy_new "$root/template/bootstrap/START-HERE.md" "START-HERE.md"
copy_new "$root/template/bootstrap/ai-sdlc-bootstrap.mdc" ".cursor/rules/ai-sdlc-bootstrap.mdc"

python3 - "$root/template/bootstrap/first-time-note.md" AGENTS.md <<'PY'
import sys
note = open(sys.argv[1], encoding="utf-8").read().strip()
text = open(sys.argv[2], encoding="utf-8").read()
head, sep, rest = text.partition("\n")
quoted = "\n".join("> " + line if line else ">" for line in note.splitlines())
open(sys.argv[2], "w", encoding="utf-8").write(head + sep + "\n" + quoted + "\n" + rest)
PY

# new-project.sh has already run git init; put the empty history on main (works on older git too).
git symbolic-ref HEAD refs/heads/main

echo
echo "Your project is ready in $target."
echo "It is a local git repository with nothing committed yet, and nothing was sent anywhere. The agent will make the first commit with you."
if command -v cursor >/dev/null 2>&1 && cursor "$target" >/dev/null 2>&1; then
  echo "Opening Cursor. Open the agent chat and say what you want to build."
else
  echo "Next: open the folder $target in Cursor (File, then Open Folder), open the agent chat, and say what you want to build."
  echo "The agent will read START-HERE.md on its own."
fi
