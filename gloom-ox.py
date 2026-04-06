#!/usr/bin/env python3
"""
GLOOM-OX v4.0 - ENTERPRISE GRADE UNIVERSUAL MEDIA EXTRACTOR
Author: xspeen | Certified Ethical Pentester (CEH)
Launch: 2026
License: MIT
Repository: https://github.com/xspeen/GLOOM-OX.git

Description: Enterprise-grade media extraction tool with NO LIMITS.
Supports YouTube, Instagram, Pinterest, TikTok, and 50+ platforms.
Includes live robot assistant for platform bypass and automatic detection.
"""

import os
import sys
import subprocess
import platform

# Ensure we're in the right directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

def launch_new_terminal_session():
    """Launch GLOOM-OX in a new terminal session with the tool name"""
    system = platform.system().lower()
    
    if 'termux' in sys.executable or 'com.termux' in os.environ.get('PREFIX', ''):
        # Termux - just clear and run in current session
        os.system('clear')
        return False
    elif system == 'windows':
        # Windows: Open new PowerShell window
        script_path = os.path.abspath(__file__)
        subprocess.Popen(['start', 'powershell', '-NoExit', '-Command', 
                         f'Write-Host "GLOOM-OX" -ForegroundColor Blue; python "{script_path}" --no-new-term'],
                         shell=True)
        return True
    elif system == 'linux' or system == 'darwin':
        # Linux/Mac: Open new terminal
        script_path = os.path.abspath(__file__)
        terminals = ['gnome-terminal', 'xterm', 'konsole', 'terminal', 'xfce4-terminal']
        
        for term in terminals:
            try:
                subprocess.Popen([term, '--title', 'GLOOM-OX', '--', 'python3', script_path, '--no-new-term'],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                return True
            except FileNotFoundError:
                continue
    
    return False

def main():
    # Check if we should launch a new terminal
    if '--no-new-term' not in sys.argv and len(sys.argv) <= 2:
        launched = launch_new_terminal_session()
        if launched:
            print("[+] Launching GLOOM-OX in new terminal session...")
            sys.exit(0)
    
    # Import and run the main application
    try:
        from gloom_ox.__main__ import run
        sys.exit(run())
    except ImportError as e:
        print(f"[!] Import error: {e}")
        print("[!] Make sure you're in the GLOOM-OX directory")
        print("[!] Run: pip install -r requirements.txt")
        sys.exit(1)

if __name__ == "__main__":
    main()
