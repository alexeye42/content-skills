# Creates .claude\skills and .claude\rules as directory junctions to .agents\skills
# and .agents\rules, so Claude and Cursor read the same files as Codex and Antigravity.
# Junctions need no admin rights. Run once after cloning: scripts\setup-claude.ps1
Set-Location (Join-Path $PSScriptRoot "..")
New-Item -ItemType Directory -Force -Path ".claude" | Out-Null
foreach ($d in @("skills", "rules")) {
    $link = ".claude\$d"
    if (Test-Path $link) {
        Write-Host "$link already exists - skipped"
    } else {
        New-Item -ItemType Junction -Path $link -Target (Resolve-Path ".agents\$d") | Out-Null
        Write-Host "created $link -> .agents\$d"
    }
}
