#!/bin/sh
# Creates .claude/skills as a symlink to .agents/skills, so Claude and Cursor read
# the same skills as Codex and Antigravity. The rules get no link: Claude Code would
# load everything in .claude/rules into every session, while the skills name the
# rules they need. Run once after cloning: scripts/setup-claude.sh
set -e
cd "$(dirname "$0")/.."
mkdir -p .claude
for d in skills; do
  if [ -e ".claude/$d" ] || [ -L ".claude/$d" ]; then
    echo ".claude/$d already exists - skipped"
  else
    ln -s "../.agents/$d" ".claude/$d"
    echo "created .claude/$d -> ../.agents/$d"
  fi
done
