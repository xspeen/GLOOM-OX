# GLOOM-OX Windows PowerShell Installer
Write-Host ""
Write-Host "╔═══════════════════════════════════════════════════════════╗" -ForegroundColor Blue
Write-Host "║              GLOOM-OX ENTERPRISE INSTALLER               ║" -ForegroundColor Blue
Write-Host "║                  Author: xspeen | CEH                    ║" -ForegroundColor Blue
Write-Host "╚═══════════════════════════════════════════════════════════╝" -ForegroundColor Blue
Write-Host ""

# Check Python
try {
    $pythonVersion = python --version 2>&1
    Write-Host "[+] Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "[!] Python not found. Please install Python 3.8+" -ForegroundColor Red
    Write-Host "[!] Download from: https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

# Clone or update repository
if (Test-Path "GLOOM-OX") {
    Write-Host "[+] Updating GLOOM-OX..." -ForegroundColor Green
    Set-Location GLOOM-OX
    git pull
} else {
    Write-Host "[+] Cloning GLOOM-OX repository..." -ForegroundColor Green
    git clone https://github.com/xspeen/GLOOM-OX.git
    Set-Location GLOOM-OX
}

# Install Python dependencies
Write-Host "[+] Installing Python dependencies..." -ForegroundColor Green
pip install -r requirements.txt

# Create batch launcher
$batchContent = @'
@echo off
python "%~dp0gloom-ox.py" %*
'@
$batchContent | Out-File -FilePath "gloom-ox.bat" -Encoding ASCII

Write-Host ""
Write-Host "╔═══════════════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║              INSTALLATION COMPLETE!                       ║" -ForegroundColor Green
Write-Host "║                                                           ║" -ForegroundColor Green
Write-Host "║  Run: python gloom-ox.py or ./gloom-ox.bat               ║" -ForegroundColor Green
Write-Host "║                                                           ║" -ForegroundColor Green
Write-Host "║  Repository: https://github.com/xspeen/GLOOM-OX          ║" -ForegroundColor Green
Write-Host "╚═══════════════════════════════════════════════════════════╝" -ForegroundColor Green
Write-Host ""
