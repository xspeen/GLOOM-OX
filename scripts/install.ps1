# ============================================================
# GLOOM-OX v5.1 - Windows PowerShell Installer
# Supports: Windows 10/11, PowerShell 5.1+
# ============================================================

# Colors
$Green = "Green"
$Yellow = "Yellow"
$Cyan = "Cyan"
$Red = "Red"

Write-Host @"
╔═══════════════════════════════════════════════════════════════════╗
║                    GLOOM-OX v5.1 INSTALLER                        ║
║                                                                   ║
║         Universal Social Media Video Downloader                   ║
╚═══════════════════════════════════════════════════════════════════╝
"@ -ForegroundColor Cyan

# Check PowerShell version
$PSVersion = $PSVersionTable.PSVersion.Major
Write-Host "[1/5] Checking PowerShell version..." -ForegroundColor Blue
if ($PSVersion -ge 5) {
    Write-Host "✓ PowerShell $PSVersion detected" -ForegroundColor Green
} else {
    Write-Host "✗ PowerShell 5.0+ required" -ForegroundColor Red
    exit 1
}

# Check Python
Write-Host "[2/5] Checking Python..." -ForegroundColor Blue
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ $pythonVersion found" -ForegroundColor Green
    $pythonCmd = "python"
} catch {
    try {
        $pythonVersion = python3 --version 2>&1
        Write-Host "✓ $pythonVersion found" -ForegroundColor Green
        $pythonCmd = "python3"
    } catch {
        Write-Host "✗ Python not found! Installing..." -ForegroundColor Yellow
        
        # Download Python installer
        $pythonUrl = "https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe"
        $installer = "$env:TEMP\python-installer.exe"
        Invoke-WebRequest -Uri $pythonUrl -OutFile $installer
        
        # Install Python silently
        Start-Process -FilePath $installer -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait
        Remove-Item $installer
        
        # Refresh environment
        $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
        
        Write-Host "✓ Python installed" -ForegroundColor Green
        $pythonCmd = "python"
    }
}

# Install Python packages
Write-Host "[3/5] Installing Python packages..." -ForegroundColor Blue
& $pythonCmd -m pip install --upgrade pip
& $pythonCmd -m pip install yt-dlp requests beautifulsoup4
Write-Host "✓ Python packages installed" -ForegroundColor Green

# Clone repository
Write-Host "[4/5] Setting up GLOOM-OX..." -ForegroundColor Blue
$gloomPath = "$env:USERPROFILE\GLOOM-OX"

if (Test-Path $gloomPath) {
    Write-Host "Directory exists, updating..." -ForegroundColor Yellow
    Set-Location $gloomPath
    git pull origin main
} else {
    Write-Host "Cloning repository..." -ForegroundColor Yellow
    git clone https://github.com/xspeen/GLOOM-OX.git $gloomPath
    Set-Location $gloomPath
}

# Create shortcut on Desktop
Write-Host "[5/5] Creating shortcut..." -ForegroundColor Blue
$shortcutPath = "$env:USERPROFILE\Desktop\GLOOM-OX.lnk"
$WScriptShell = New-Object -ComObject WScript.Shell
$shortcut = $WScriptShell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = "$gloomPath\scripts\gloom_ox.bat"
$shortcut.WorkingDirectory = $gloomPath
$shortcut.IconLocation = "$gloomPath\assets\icon.ico"
$shortcut.Save()
Write-Host "✓ Shortcut created on Desktop" -ForegroundColor Green

# Create batch file
$batchContent = @"
@echo off
cd /d "$gloomPath"
$pythonCmd gloom-ox.py
pause
"@
$batchContent | Out-File -FilePath "$gloomPath\scripts\gloom_ox.bat" -Encoding ASCII

# Success message
Write-Host @"
╔════════════════════════════════════════════════════════════╗
║              INSTALLATION COMPLETE!                        ║
╚════════════════════════════════════════════════════════════╝
"@ -ForegroundColor Green

Write-Host "`n🚀 To run GLOOM-OX:" -ForegroundColor Cyan
Write-Host "   cd $gloomPath" -ForegroundColor Yellow
Write-Host "   $pythonCmd gloom-ox.py`n" -ForegroundColor Yellow

Write-Host "📝 Or double-click the shortcut on your Desktop!`n" -ForegroundColor Cyan

Write-Host "⭐ Support: https://github.com/xspeen/GLOOM-OX`n" -ForegroundColor Magenta

# Ask to run
$runNow = Read-Host "Do you want to run GLOOM-OX now? (y/n)"
if ($runNow -eq 'y') {
    Set-Location $gloomPath
    & $pythonCmd gloom-ox.py
}
