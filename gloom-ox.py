#!/usr/bin/env python3
"""
GLOOM-OX v4.0 - ENTERPRISE GRADE UNIVERSAL MEDIA EXTRACTOR
STANDALONE VERSION - FULLY WORKING
Author: xspeen | CEH Certified 2026
"""

import os
import sys
import platform    # ← IMPORT FIXED
import time
import re
import random
import subprocess
from pathlib import Path

# Global settings
VERSION = "4.0.0"
AUTHOR = "xspeen"
HOME = str(Path.home())
SYSTEM = platform.system().lower()
IS_TERMUX = 'com.termux' in HOME or 'termux' in sys.executable

# Paths
if IS_TERMUX:
    TERMUX_STORAGE = "/data/data/com.termux/files/home/storage/shared"
    if not os.path.exists(TERMUX_STORAGE):
        TERMUX_STORAGE = HOME + "/storage/shared"
    DOWNLOAD_DIR = os.path.join(TERMUX_STORAGE, "DCIM", "GLOOM-OX_Videos")
else:
    DOWNLOAD_DIR = os.path.join(HOME, "Downloads", "GLOOM-OX_Videos")

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Banner
BANNER = """
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
║        [ ENTERPRISE GRADE v4.0.0 - CERTIFIED ETHICAL PENTESTER ]              ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
\033[0m
"""

def check_dependencies():
    """Check and install yt-dlp"""
    try:
        import yt_dlp
        print("\033[1;32m[✓] yt-dlp found\033[0m")
        return True
    except ImportError:
        print("\033[1;33m[~] Installing yt-dlp...\033[0m")
        subprocess.run([sys.executable, "-m", "pip", "install", "yt-dlp", "--upgrade"])
        return True

def download_media(url):
    """Download media using yt-dlp"""
    try:
        import yt_dlp
        
        timestamp = int(time.time())
        output_template = os.path.join(DOWNLOAD_DIR, f"GLOOMOX_%(title)s_{timestamp}.%(ext)s")
        
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': output_template,
            'quiet': False,
            'no_warnings': False,
            'ignoreerrors': True,
            'retries': 10,
            'fragment_retries': 10,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        }
        
        print(f"\033[1;33m[+] Downloading: {url}\033[0m")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            
            # Fix extension
            if not os.path.exists(filename):
                for ext in ['.mp4', '.mkv', '.webm']:
                    test_file = filename.rsplit('.', 1)[0] + ext
                    if os.path.exists(test_file):
                        filename = test_file
                        break
            
            if os.path.exists(filename):
                print(f"\033[1;32m[✓] Downloaded: {os.path.basename(filename)}\033[0m")
                print(f"\033[1;32m[✓] Saved to: {DOWNLOAD_DIR}\033[0m")
                
                # Termux gallery notification
                if IS_TERMUX:
                    try:
                        subprocess.run(["termux-media-scan", filename], capture_output=True)
                        print("\033[1;32m[✓] Saved to Gallery (Termux)\033[0m")
                    except:
                        pass
                
                return filename
        
        return None
        
    except Exception as e:
        print(f"\033[1;31m[!] Error: {e}\033[0m")
        return None

def main():
    """Main function"""
    os.system('clear' if SYSTEM != 'windows' else 'cls')
    print(BANNER)
    print(f"\033[1;33m[+] Author: {AUTHOR} | CEH Certified 2026\033[0m")
    print(f"\033[1;33m[+] Repository: https://github.com/xspeen/GLOOM-OX\033[0m")
    print(f"\033[1;36m[+] Platform: {SYSTEM.upper()} | Termux: {'YES' if IS_TERMUX else 'NO'}\033[0m")
    print(f"\033[1;36m[+] Download Directory: {DOWNLOAD_DIR}\033[0m")
    print("\033[1;32m" + "="*70 + "\033[0m")
    
    # Check dependencies
    check_dependencies()
    
    # Main loop
    while True:
        print("\n\033[1;35m" + "═"*70 + "\033[0m")
        print("\033[1;33m[+] Enter URL (commands: clear, exit):\033[0m")
        print("\033[1;31m[!] Supports: YouTube, Instagram, Pinterest, TikTok\033[0m")
        
        try:
            url = input("\033[1;32m[GLOOM-OX] >> \033[0m").strip()
        except KeyboardInterrupt:
            print("\n\033[1;31m[!] Exiting...\033[0m")
            break
        
        if url.lower() in ['exit', 'quit', 'q']:
            print("\033[1;32m[+] Thanks for using GLOOM-OX!\033[0m")
            break
        elif url.lower() == 'clear':
            os.system('clear' if SYSTEM != 'windows' else 'cls')
            print(BANNER)
            continue
        elif not url:
            continue
        
        # Add https if missing
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        # Download
        print("\n")
        start = time.time()
        result = download_media(url)
        elapsed = time.time() - start
        
        if result:
            print(f"\n\033[1;32m[✓] Download complete in {elapsed:.1f} seconds\033[0m")
        else:
            print("\n\033[1;31m[!] Download failed. Check URL and try again.\033[0m")

if __name__ == "__main__":
    main()
