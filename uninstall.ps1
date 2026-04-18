# ============================================================
# GLOOM-OX v5.1 - Windows Uninstaller
# ============================================================

Write-Host @"
╔═══════════════════════════════════════════════════════════════════╗
║                    GLOOM-OX UNINSTALLER                           ║
╚═══════════════════════════════════════════════════════════════════╝
"@ -ForegroundColor Red

$gloomPath = "$env:USERPROFILE\GLOOM-OX"
$historyFile = "$env:USERPROFILE\.gloom_ox_history.json"

Write-Host "This will remove GLOOM-OX and all downloaded videos!" -ForegroundColor Yellow
$confirm = Read-Host "Are you sure? (y/n)"

if ($confirm -eq 'y') {
    # Remove directory
    if (Test-Path $gloomPath) {
        Remove-Item -Path $gloomPath -Recurse -Force
        Write-Host "✓ Removed GLOOM-OX directory" -ForegroundColor Green
    }
    
    # Remove history
    if (Test-Path $historyFile) {
        Remove-Item -Path $historyFile -Force
        Write-Host "✓ Removed download history" -ForegroundColor Green
    }
    
    # Remove desktop shortcut
    $shortcut = "$env:USERPROFILE\Desktop\GLOOM-OX.lnk"
    if (Test-Path $shortcut) {
        Remove-Item -Path $shortcut -Force
        Write-Host "✓ Removed desktop shortcut" -ForegroundColor Green
    }
    
    Write-Host "`nGLOOM-OX has been uninstalled!" -ForegroundColor Green
} else {
    Write-Host "Uninstall cancelled" -ForegroundColor Yellow
}
