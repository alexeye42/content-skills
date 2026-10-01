# Creates .claude\skills as a directory junction to .agents\skills, so Claude and
# Cursor read the same skills as Codex and Antigravity. The rules get no link: Claude
# Code would load everything in .claude\rules into every session, while the skills
# name the rules they need. Junctions need no admin rights. Run once after cloning: scripts\setup-claude.ps1
Set-Location (Join-Path $PSScriptRoot "..")
New-Item -ItemType Directory -Force -Path ".claude" | Out-Null
foreach ($d in @("skills")) {
    $link = ".claude\$d"
    if (Test-Path $link) {
        Write-Host "$link already exists - skipped"
    } else {
        New-Item -ItemType Junction -Path $link -Target (Resolve-Path ".agents\$d") | Out-Null
        Write-Host "created $link -> .agents\$d"
    }
}
