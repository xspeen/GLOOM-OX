@echo off
title GLOOM-OX v5.1 - Universal Social Media Downloader
color 0A

:: Get script directory
set SCRIPT_DIR=%~dp0
set GLOOM_DIR=%SCRIPT_DIR%..

:: Change to GLOOM directory
cd /d "%GLOOM_DIR%"

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    python3 --version >nul 2>&1
    if errorlevel 1 (
        echo [ERROR] Python not found!
        echo Please install Python 3.8+ from python.org
        pause
        exit /b 1
    ) else (
        set PYTHON_CMD=python3
    )
) else (
    set PYTHON_CMD=python
)

:: Run GLOOM-OX
echo Starting GLOOM-OX...
%PYTHON_CMD% gloom-ox.py

:: Pause on exit
echo.
pause
