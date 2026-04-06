#!/usr/bin/env python3
"""
GLOOM-OX Banner and Animations
"""

import os
import time
import sys
import threading

from gloom_ox.config.settings import VERSION, AUTHOR, REPO_URL, SYSTEM, IS_TERMUX

# Big Blue Header Banner
BLUE_BANNER = """
\033[1;34m
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║     ██████╗  ██╗      ██████╗  ██████╗ ███╗   ███╗     ██████╗ ██╗  ██╗      ║
║    ██╔════╝ ██║     ██╔═══██╗██╔═══██╗████╗ ████║    ██╔═══██╗██║  ██║      ║
║    ██║  ███╗██║     ██║   ██║██║   ██║██╔████╔██║    ██║   ██║███████║      ║
║    ██║   ██║██║     ██║   ██║██║   ██║██║╚██╔╝██║    ██║   ██║██╔══██║      ║
║    ╚██████╔╝███████╗╚██████╔╝╚██████╔╝██║ ╚═╝ ██║    ╚██████╔╝██║  ██║      ║
║     ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝     ╚═════╝ ╚═╝  ╚═╝      ║
║                                                                               ║
║                    ███████╗██╗  ██╗    ████████╗ ██████╗                     ║
║                    ██╔════╝╚██╗██╔╝    ╚══██╔══╝██╔═══██╗                    ║
║                    █████╗   ╚███╔╝        ██║   ██║   ██║                    ║
║                    ██╔══╝   ██╔██╗        ██║   ██║   ██║                    ║
║                    ███████╗██╔╝ ██╗       ██║   ╚██████╔╝                    ║
║                    ╚══════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝                     ║
║                                                                               ║
║        [ ENTERPRISE GRADE v{VERSION} - CERTIFIED ETHICAL PENTESTER ]          ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
\033[0m
"""

def animate_robot_detection():
    """Live robot detection animation"""
    frames = [
        """
        ╭─────────────────────────────────────╮
        │   🤖  SCANNING PLATFORM...          │
        │   ████░░░░░░░░░░░░░░░░  20%         │
        ╰─────────────────────────────────────╯
        """,
        """
        ╭─────────────────────────────────────╮
        │   🤖  ANALYZING RESTRICTIONS...     │
        │   ████████░░░░░░░░░░░░  40%         │
        ╰─────────────────────────────────────╯
        """,
        """
        ╭─────────────────────────────────────╮
        │   🤖  BYPASS PROTOCOL ACTIVE...     │
        │   ████████████░░░░░░░░  60%         │
        ╰─────────────────────────────────────╯
        """,
        """
        ╭─────────────────────────────────────╮
        │   🤖  EXTRACTING CONTENT...         │
        │   ████████████████░░░░  80%         │
        ╰─────────────────────────────────────╯
        """,
        """
        ╭─────────────────────────────────────╮
        │   🤖  DOWNLOAD READY! ✅            │
        │   ████████████████████  100%        │
        ╰─────────────────────────────────────╯
        """
    ]
    
    for frame in frames:
        sys.stdout.write('\r' + frame)
        sys.stdout.flush()
        time.sleep(0.3)
    
    print()  # New line after animation

def display_robot_animation():
    """Display the live robot detection animation"""
    print("\033[1;36m")
    animate_robot_detection()
    print("\033[0m")

def display_banner():
    """Display the main GLOOM-OX banner"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BLUE_BANNER.format(VERSION=VERSION))
    print(f"\033[1;33m[+] Made by: {AUTHOR} 🔓 | CEH Certified\033[0m")
    print(f"\033[1;33m[+] Repository: {REPO_URL}\033[0m")
    print(f"\033[1;36m[+] Platform: {SYSTEM.upper()} | Termux: {'YES' if IS_TERMUX else 'NO'}\033[0m")
    print(f"\033[1;31m[+] SUPPORTS ALL: YouTube, Shorts, Instagram, Pinterest, TikTok, Private/Premium\033[0m")
    print(f"\033[1;36m[+] Mode: ENTERPRISE - NO LIMITS\033[0m")
    print("\033[1;32m" + "="*70 + "\033[0m")
    print()
