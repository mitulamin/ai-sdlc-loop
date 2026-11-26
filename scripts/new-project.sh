#!/usr/bin/env bash
# Create a new project from template/.
# Usage: scripts/new-project.sh <target-dir>
set -euo pipefail

if [ $# -ne 1 ]; then
  echo "Usage: scripts/new-project.sh <target-dir>" >&2
  exit 1
fi

root="$(cd "$(dirname "$0")/.." && pwd)"
target="$1"

if [ -e "$target" ] && [ -n "$(ls -A "$target" 2>/dev/null)" ]; then
  echo "$target exists and is not empty" >&2
  exit 1
fi

mkdir -p "$target"
cp -a "$root/template/." "$target/"
git -C "$target" init -q
echo "Created $target from template/. Next: edit AGENTS.md, then start your first loop."
