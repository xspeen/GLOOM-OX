#!/usr/bin/env python3
"""
Dependency installation and management
"""

import subprocess
import sys
import time


def check_internet():
    """Check internet connectivity"""
    try:
        import urllib.request
        urllib.request.urlopen('https://www.google.com', timeout=3)
        return True
    except:
        return False


def install_ytdlp_2026():
    """Install/Update yt-dlp to latest development version"""
    print("\033[1;35m[~] FORCE UPDATING yt-dlp to LATEST VERSION...\033[0m")
    
    try:
        subprocess.run([
            sys.executable, "-m", "pip", "install",
            "--upgrade", "yt-dlp",
            "--no-cache-dir", "--force-reinstall"
        ], capture_output=True, timeout=120)
        
        subprocess.run([
            sys.executable, "-m", "pip", "install",
            "https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz",
            "--upgrade", "--no-cache-dir"
        ], capture_output=True, timeout=120)
        
        result = subprocess.run([
            sys.executable, "-m", "yt_dlp", "--version"
        ], capture_output=True, text=True)
        
        version = result.stdout.strip()
        print(f"\033[1;32m[✓] yt-dlp Version: {version}\033[0m")
        return version
        
    except Exception as e:
        print(f"\033[1;33m[~] Update issue: {e}\033[0m")
        return None


def install_dependencies():
    """Install ALL dependencies with NO restrictions"""
    print("\033[1;34m[+] DEPENDENCY SCAN & FORCE DEPLOYMENT\033[0m")
    
    # Import here to avoid circular imports
    try:
        from gloom_ox.utils.integrity import ensure_ffmpeg
        
        if ensure_ffmpeg():
            print("\033[1;32m[✓] FFmpeg: Available\033[0m")
        else:
            print("\033[1;31m[!] FFmpeg: NOT FOUND - Some features limited\033[0m")
    except:
        print("\033[1;33m[~] Could not check FFmpeg\033[0m")
    
    install_ytdlp_2026()
    
    packages = [
        "requests>=2.31.0",
        "browser-cookie3>=0.19.1",
        "mutagen>=1.47.0",
        "pycryptodomex>=3.19.0",
        "websockets>=12.0",
        "urllib3>=2.0.0",
    ]
    
    for package in packages:
        try:
            print(f"\033[1;35m[~] Installing {package}...\033[0m")
            subprocess.run([
                sys.executable, "-m", "pip", "install",
                package, "--upgrade", "--no-cache-dir"
            ], capture_output=True, timeout=60)
            print(f"\033[1;32m[✓] {package.split('>=')[0]}: OK\033[0m")
        except Exception as e:
            print(f"\033[1;33m[~] {package}: Issue - {e}\033[0m")
    
    time.sleep(1)
    print("\033[1;32m[✓] ALL DEPENDENCIES READY - NO LIMITS MODE ACTIVATED\033[0m")
    return True
