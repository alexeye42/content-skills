@echo off
rem Creates .claude\skills and .claude\rules as directory junctions to .agents\skills
rem and .agents\rules, so Claude and Cursor read the same files as Codex and Antigravity.
rem Junctions need no admin rights. Run once after cloning: scripts\setup-claude.cmd
cd /d "%~dp0.."
if not exist ".claude" mkdir ".claude"
for %%d in (skills rules) do (
  if exist ".claude\%%d" (
    echo .claude\%%d already exists - skipped
  ) else (
    mklink /J ".claude\%%d" ".agents\%%d"
  )
)
