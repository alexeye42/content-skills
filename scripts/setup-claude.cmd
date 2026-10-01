@echo off
rem Creates .claude\skills as a directory junction to .agents\skills, so Claude and
rem Cursor read the same skills as Codex and Antigravity. The rules get no link: Claude
rem Code would load everything in .claude\rules into every session, while the skills
rem name the rules they need. Junctions need no admin rights. Run once after cloning: scripts\setup-claude.cmd
cd /d "%~dp0.."
if not exist ".claude" mkdir ".claude"
for %%d in (skills) do (
  if exist ".claude\%%d" (
    echo .claude\%%d already exists - skipped
  ) else (
    mklink /J ".claude\%%d" ".agents\%%d"
  )
)
