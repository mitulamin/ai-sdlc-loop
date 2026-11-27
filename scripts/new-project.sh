#!/usr/bin/env bash
# Create a new project from template/ with a profile applied, and optionally a harness layout.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
profiles_dir="$root/template/profiles"
installer="$root/scripts/install-harness.py"
default_profile="solo"
default_harness="none"
use_page="https://mitulamin.github.io/ai-sdlc-loop/use.html"

usage() {
  cat <<EOF
Usage: scripts/new-project.sh [--harness <name>] <target-dir> [profile]

Copies the shared base from template/ into <target-dir>, applies the profile,
installs the skills, agents and commands for the harness (if any) into the
project's own folders, and runs git init. <target-dir> must not exist or must
be empty. Nothing is written outside <target-dir>.

Profiles (default: $default_profile):
EOF
  for p in "$profiles_dir"/*/; do
    name="$(basename "$p")"
    printf '  %-16s %s\n' "$name" "$(head -n 1 "$p/profile.txt" 2>/dev/null)"
  done
  cat <<EOF

Harnesses (default: $default_harness; layouts in data/harnesses.json):
EOF
  printf '  %-16s %s\n' "none" "No harness files: the template and profile only."
  if command -v python3 >/dev/null 2>&1; then
    python3 "$installer" --list | while IFS=$'\t' read -r id name; do
      printf '  %-16s %s\n' "$id" "$name"
    done
  else
    echo "  (install python3 to list and use the harnesses)"
  fi
  cat <<EOF

Guide: $use_page
EOF
}

harness="$default_harness"
args=()
while [ $# -gt 0 ]; do
  case "$1" in
    -h|--help) usage; exit 0 ;;
    --harness)
      if [ $# -lt 2 ]; then echo "--harness needs a name" >&2; echo >&2; usage >&2; exit 1; fi
      harness="$2"; shift 2 ;;
    --harness=*) harness="${1#--harness=}"; shift ;;
    --) shift; args+=("$@"); break ;;
    -*) echo "Unknown option: $1" >&2; echo >&2; usage >&2; exit 1 ;;
    *) args+=("$1"); shift ;;
  esac
done
set -- ${args[@]+"${args[@]}"}

if [ $# -lt 1 ] || [ $# -gt 2 ]; then
  usage >&2
  exit 1
fi

target="$1"
profile="${2:-$default_profile}"

if ! [[ "$profile" =~ ^[a-z0-9-]+$ ]] || [ ! -f "$profiles_dir/$profile/profile.txt" ]; then
  echo "Unknown profile: $profile" >&2
  echo >&2
  usage >&2
  exit 1
fi

if [ "$harness" != "none" ]; then
  if ! command -v python3 >/dev/null 2>&1; then
    echo "The $harness harness needs python3." >&2
    exit 1
  fi
  if ! [[ "$harness" =~ ^[a-z0-9-]+$ ]] || ! python3 "$installer" --validate "$harness"; then
    echo "Unknown harness: $harness" >&2
    echo >&2
    usage >&2
    exit 1
  fi
fi

if [ -e "$target" ] && [ -n "$(ls -A "$target" 2>/dev/null)" ]; then
  echo "$target exists and is not empty" >&2
  exit 1
fi

mkdir -p "$target"

# Base: everything in template/ except the profiles folder.
find "$root/template" -mindepth 1 -maxdepth 1 ! -name profiles -exec cp -a {} "$target/" \;

# Profile: omit listed paths from the base, then add or replace files from the overlay.
omit="$profiles_dir/$profile/omit"
if [ -f "$omit" ]; then
  while IFS= read -r path || [ -n "$path" ]; do
    case "$path" in
      ""|\#*) continue ;;
      /*|*..*) echo "Bad omit path in $profile profile: $path" >&2; exit 1 ;;
    esac
    rm -rf "${target:?}/$path"
  done < "$omit"
fi

overlay="$profiles_dir/$profile/overlay"
if [ -d "$overlay" ]; then
  cp -a "$overlay/." "$target/"
fi

# Record the profile name in the files that mention it.
grep -rlF '@PROFILE@' "$target" 2>/dev/null | while IFS= read -r f; do
  sed -i.bak "s/@PROFILE@/$profile/g" "$f" && rm -f "$f.bak"
done

# Harness: skills, agents and commands in the project's own harness folders (MIT, except files adapted from share-alike sources, which carry their own notice).
if [ "$harness" != "none" ]; then
  python3 "$installer" "$target" "$harness"
fi

git -C "$target" init -q
if [ "$harness" = "none" ]; then
  echo "Created $target from template/ with the $profile profile."
else
  echo "Created $target from template/ with the $profile profile and the $harness harness."
fi
echo "Next: edit AGENTS.md, read PROCESS.md, then start your first loop. Guide: $use_page"
