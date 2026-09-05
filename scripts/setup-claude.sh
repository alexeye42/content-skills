#!/bin/sh
# Creates .claude/skills and .claude/rules as symlinks to .agents/skills and
# .agents/rules, so Claude and Cursor read the same files as Codex and Antigravity.
# Run once after cloning: scripts/setup-claude.sh
set -e
cd "$(dirname "$0")/.."
mkdir -p .claude
for d in skills rules; do
  if [ -e ".claude/$d" ] || [ -L ".claude/$d" ]; then
    echo ".claude/$d already exists - skipped"
  else
    ln -s "../.agents/$d" ".claude/$d"
    echo "created .claude/$d -> ../.agents/$d"
  fi
done
