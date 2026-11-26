#!/usr/bin/env bash
# Create a new project from template/ with a profile applied.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
profiles_dir="$root/template/profiles"
default_profile="solo"

usage() {
  cat <<EOF
Usage: scripts/new-project.sh <target-dir> [profile]

Copies the shared base from template/ into <target-dir>, applies the profile,
and runs git init. <target-dir> must not exist or must be empty.

Profiles (default: $default_profile):
EOF
  for p in "$profiles_dir"/*/; do
    name="$(basename "$p")"
    printf '  %-12s %s\n' "$name" "$(head -n 1 "$p/profile.txt" 2>/dev/null)"
  done
}

case "${1:-}" in
  -h|--help) usage; exit 0 ;;
esac

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

git -C "$target" init -q
echo "Created $target from template/ with the $profile profile."
echo "Next: edit AGENTS.md, read PROCESS.md, then start your first loop."
