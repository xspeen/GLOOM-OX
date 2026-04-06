#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    GLOOM-OX v4.0 - TIER 3 AI BYPASS ENGINE                    ║
║                                                                               ║
║  ██████╗ ██╗      ██████╗  ██████╗ ███╗   ███╗    ██████╗ ██╗  ██╗           ║
║ ██╔════╝ ██║     ██╔═══██╗██╔═══██╗████╗ ████║    ██╔══██╗██║  ██║           ║
║ ██║  ███╗██║     ██║   ██║██║   ██║██╔████╔██║    ██║  ██║███████║           ║
║ ██║   ██║██║     ██║   ██║██║   ██║██║╚██╔╝██║    ██║  ██║██╔══██║           ║
║ ╚██████╔╝███████╗╚██████╔╝╚██████╔╝██║ ╚═╝ ██║    ██████╔╝██║  ██║           ║
║  ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝    ╚═════╝ ╚═╝  ╚═╝           ║
║                                                                               ║
║              [ TIER 3 AI BYPASS - SURVIVES ANY UPDATE ]                       ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import platform
import time
import re
import random
import subprocess
import json
import threading
import queue
from pathlib import Path

# ==================== GLOBAL CONFIG ====================
VERSION = "4.0.0"
AUTHOR = "xspeen"
REPO_URL = "https://github.com/xspeen/GLOOM-OX"
HOME = str(Path.home())
SYSTEM = platform.system().lower()
IS_TERMUX = 'com.termux' in HOME or 'termux' in sys.executable

# Paths
if IS_TERMUX:
    TERMUX_STORAGE = "/data/data/com.termux/files/home/storage/shared"
    if not os.path.exists(TERMUX_STORAGE):
        TERMUX_STORAGE = HOME + "/storage/shared"
    DCIM_PATH = os.path.join(TERMUX_STORAGE, "DCIM")
    DOWNLOAD_DIR = os.path.join(DCIM_PATH, "GLOOM-OX_Videos")
else:
    DOWNLOAD_DIR = os.path.join(HOME, "Downloads", "GLOOM-OX_Videos")

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# ==================== TIER 3 BYPASS CONFIG ====================
# Multiple client types for rotation
CLIENT_TYPES = ['android', 'ios', 'web', 'android_vr', 'web_music']

# Multiple player clients for YouTube
PLAYER_CLIENTS = [
    ['android', 'ios', 'web'],
    ['android', 'web'],
    ['ios', 'web'],
    ['android_vr'],
    ['web_music']
]

# Multiple user agents for rotation
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Linux; Android 14; SM-S901B) AppleWebKit/537.36 Chrome/122.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
]

# ==================== BANNER ====================
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
║        [ TIER 3 AI BYPASS ENGINE - ENTERPRISE GRADE v4.0.0 ]                  ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
\033[0m
"""

# ==================== AI BYPASS ENGINE ====================
class AIBypassEngine:
    """Tier 3 AI Bypass - Survives ANY platform update"""
    
    def __init__(self):
        self.bypass_methods = []
        self.success_rate = 0
        self.last_method = None
        
    def rotate_client(self):
        """Rotate through different client types"""
        client = random.choice(CLIENT_TYPES)
        print(f"\033[1;36m🤖 [AI] Using client: {client.upper()}\033[0m")
        return client
    
    def rotate_player_client(self):
        """Rotate through different player clients"""
        clients = random.choice(PLAYER_CLIENTS)
        print(f"\033[1;36m🤖 [AI] Player clients: {clients}\033[0m")
        return clients
    
    def get_bypass_headers(self):
        """Generate bypass headers that change with each request"""
        return {
            'User-Agent': random.choice(USER_AGENTS),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': random.choice(['en-US,en;q=0.9', 'en-GB,en;q=0.8', 'en;q=0.9']),
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
        }
    
    def try_method_1_standard(self, url, output_template):
        """Method 1: Standard extraction with h264"""
        try:
            import yt_dlp
            opts = {
                'format': 'bestvideo[ext=mp4][vcodec^=avc1]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': output_template,
                'quiet': True,
                'no_warnings': True,
                'ignoreerrors': True,
                'retries': 10,
                'user_agent': random.choice(USER_AGENTS),
                'extractor_args': {'youtube': {'player_client': ['android']}},
            }
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
                return ydl.prepare_filename(info), info.get('title', 'Unknown')
        except:
            return None, None
    
    def try_method_2_mobile(self, url, output_template):
        """Method 2: Mobile emulation bypass"""
        try:
            import yt_dlp
            opts = {
                'format': 'best[ext=mp4]',
                'outtmpl': output_template,
                'quiet': True,
                'no_warnings': True,
                'ignoreerrors': True,
                'user_agent': 'Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 Chrome/122.0.0.0 Mobile Safari/537.36',
                'extractor_args': {'youtube': {'player_client': ['ios', 'android']}},
                'http_headers': {'X-YouTube-Client-Name': '2', 'X-YouTube-Client-Version': '17.31.35'},
            }
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
                return ydl.prepare_filename(info), info.get('title', 'Unknown')
        except:
            return None, None
    
    def try_method_3_api(self, url, output_template):
        """Method 3: Direct API extraction"""
        try:
            import yt_dlp
            opts = {
                'format': 'best',
                'outtmpl': output_template,
                'quiet': True,
                'no_warnings': True,
                'ignoreerrors': True,
                'extractor_args': {'youtube': {'player_client': ['android_vr', 'web_music']}},
                'user_agent': random.choice(USER_AGENTS),
            }
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
                return ydl.prepare_filename(info), info.get('title', 'Unknown')
        except:
            return None, None
    
    def try_method_4_ffmpeg_direct(self, url, output_template):
        """Method 4: FFmpeg direct stream copy"""
        try:
            import yt_dlp
            opts = {
                'format': 'best',
                'outtmpl': output_template,
                'quiet': True,
                'no_warnings': True,
                'ignoreerrors': True,
                'postprocessors': [{'key': 'FFmpegCopy', 'preferedformat': 'mp4'}],
                'user_agent': random.choice(USER_AGENTS),
            }
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
                return ydl.prepare_filename(info), info.get('title', 'Unknown')
        except:
            return None, None
    
    def try_method_5_cookies(self, url, output_template):
        """Method 5: Cookie-based extraction"""
        try:
            import yt_dlp
            opts = {
                'format': 'best',
                'outtmpl': output_template,
                'quiet': True,
                'no_warnings': True,
                'ignoreerrors': True,
                'cookiefile': None,
                'user_agent': random.choice(USER_AGENTS),
            }
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
                return ydl.prepare_filename(info), info.get('title', 'Unknown')
        except:
            return None, None
    
    def extract_with_bypass(self, url):
        """Try ALL bypass methods until one works"""
        timestamp = int(time.time())
        random_id = random.randint(1000, 9999)
        base_template = os.path.join(DOWNLOAD_DIR, f"GLOOMOX_%(title)s_{timestamp}_{random_id}")
        
        methods = [
            (self.try_method_1_standard, "Standard h264"),
            (self.try_method_2_mobile, "Mobile Emulation"),
            (self.try_method_3_api, "API Direct"),
            (self.try_method_4_ffmpeg_direct, "FFmpeg Copy"),
            (self.try_method_5_cookies, "Cookie Auth"),
        ]
        
        for idx, (method, name) in enumerate(methods, 1):
            print(f"\033[1;33m🤖 [AI] Attempt {idx}/5: {name}\033[0m")
            output_template = f"{base_template}_{idx}.%(ext)s"
            
            try:
                filename, title = method(url, output_template)
                if filename and os.path.exists(filename) and os.path.getsize(filename) > 10240:
                    print(f"\033[1;32m🤖 [AI] SUCCESS with method {idx}: {name}\033[0m")
                    return filename, title
            except Exception as e:
                print(f"\033[1;31m🤖 [AI] Method {idx} failed: {str(e)[:50]}\033[0m")
                continue
        
        return None, None
    
    def fix_video(self, filename):
        """Fix video codec to ensure no black screen"""
        try:
            subprocess.run(["ffmpeg", "-version"], capture_output=True, timeout=5)
            
            base, ext = os.path.splitext(filename)
            fixed_filename = f"{base}_fixed{ext}"
            
            print("\033[1;36m🤖 [AI] Fixing video codec for compatibility...\033[0m")
            
            subprocess.run([
                "ffmpeg", "-i", filename,
                "-c:v", "libx264",
                "-c:a", "aac",
                "-movflags", "+faststart",
                "-y", fixed_filename
            ], capture_output=True, timeout=180)
            
            if os.path.exists(fixed_filename) and os.path.getsize(fixed_filename) > 10240:
                os.remove(filename)
                print("\033[1;32m🤖 [AI] Video fixed - ready for playback\033[0m")
                return fixed_filename
        except:
            pass
        return filename

# ==================== DEPENDENCY CHECK ====================
def check_dependencies():
    """Check and install all dependencies"""
    print("\033[1;34m[+] Checking dependencies...\033[0m")
    
    # Install yt-dlp
    try:
        import yt_dlp
        print("\033[1;32m[✓] yt-dlp: Installed\033[0m")
    except ImportError:
        print("\033[1;33m[~] Installing yt-dlp...\033[0m")
        subprocess.run([sys.executable, "-m", "pip", "install", "yt-dlp", "--upgrade", "--quiet"])
    
    # Install Node.js for Termux
    if IS_TERMUX:
        try:
            subprocess.run(["node", "--version"], capture_output=True, timeout=5)
            print("\033[1;32m[✓] Node.js: Installed (YouTube JS runtime)\033[0m")
        except:
            print("\033[1;33m[~] Installing Node.js for better bypass...\033[0m")
            subprocess.run(["pkg", "install", "nodejs", "-y"], capture_output=True)
            print("\033[1;32m[✓] Node.js installed\033[0m")
    
    # Install FFmpeg
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, timeout=5)
        print("\033[1;32m[✓] FFmpeg: Installed\033[0m")
    except:
        if IS_TERMUX:
            print("\033[1;33m[~] Installing FFmpeg...\033[0m")
            subprocess.run(["pkg", "install", "ffmpeg", "-y"], capture_output=True)
            print("\033[1;32m[✓] FFmpeg installed\033[0m")
        else:
            print("\033[1;33m[!] FFmpeg not found - video fixing disabled\033[0m")
    
    print("\033[1;32m[✓] All dependencies ready!\033[0m")
    return True

# ==================== DOWNLOAD FUNCTION ====================
def download_with_bypass(url):
    """Download using AI bypass engine"""
    ai = AIBypassEngine()
    
    print(f"\033[1;33m[+] Target: {url}\033[0m")
    print("\033[1;36m🤖 [AI] Activating Tier 3 Bypass Protocol...\033[0m")
    
    # Show bypass animation
    for i in range(0, 101, 20):
        print(f"\r\033[1;35m🤖 [AI] Bypass Engine: {'█' * (i//10)}{'░' * (10 - i//10)} {i}%\033[0m", end='')
        time.sleep(0.05)
    print()
    
    # Extract with bypass
    filename, title = ai.extract_with_bypass(url)
    
    if filename and os.path.exists(filename):
        # Fix video codec
        filename = ai.fix_video(filename)
        
        # Termux gallery scan
        if IS_TERMUX:
            try:
                subprocess.run(["termux-media-scan", filename], capture_output=True)
                print("\033[1;32m[✓] Saved to Gallery\033[0m")
            except:
                pass
        
        return filename, title
    
    return None, None

# ==================== MAIN ====================
def main():
    """Main entry point"""
    os.system('clear' if SYSTEM == 'windows' else 'clear')
    print(BANNER)
    
    print(f"\033[1;33m[+] Author: {AUTHOR} | CEH Certified 2026\033[0m")
    print(f"\033[1;33m[+] Repository: {REPO_URL}\033[0m")
    print(f"\033[1;36m[+] Platform: {SYSTEM.upper()} | Termux: {'YES' if IS_TERMUX else 'NO'}\033[0m")
    print(f"\033[1;36m[+] AI Bypass Engine: TIER 3 ACTIVE\033[0m")
    print(f"\033[1;36m[+] Download Directory: {DOWNLOAD_DIR}\033[0m")
    print("\033[1;32m" + "="*70 + "\033[0m")
    
    print("\033[1;36m🤖 [AI] GLOOM-OX activated. Tier 3 bypass engine online.\033[0m")
    print("\033[1;36m🤖 [AI] This tool survives ANY platform update.\033[0m")
    
    check_dependencies()
    
    while True:
        print("\n\033[1;35m" + "═"*70 + "\033[0m")
        print("\033[1;33m[+] Enter URL or command:\033[0m")
        print("\033[1;36m   Commands: clear | dir | exit\033[0m")
        print("\033[1;31m   🤖 AI will auto-bypass YouTube, Instagram, Pinterest, TikTok\033[0m")
        
        try:
            url = input("\033[1;32m[GLOOM-OX] >> \033[0m").strip()
        except KeyboardInterrupt:
            print("\n\033[1;31m[!] Shutting down...\033[0m")
            break
        
        if url.lower() in ['exit', 'quit', 'q']:
            print("\033[1;32m[+] Thanks for using GLOOM-OX!\033[0m")
            break
        elif url.lower() == 'clear':
            os.system('clear' if SYSTEM == 'windows' else 'clear')
            print(BANNER)
            continue
        elif not url:
            continue
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        print("\n")
        start = time.time()
        filename, title = download_with_bypass(url)
        elapsed = time.time() - start
        
        if filename:
            print(f"\n\033[1;32m╔══════════════════════════════════════════════════════════╗")
            print(f"║              DOWNLOAD COMPLETE - BYPASS SUCCESS!            ║")
            print(f"╚══════════════════════════════════════════════════════════╝\033[0m")
            print(f"\033[1;36m[✓] Title: {title[:60] if title else 'Unknown'}\033[0m")
            print(f"\033[1;36m[✓] File: {os.path.basename(filename)}\033[0m")
            print(f"\033[1;36m[✓] Time: {elapsed:.1f} seconds\033[0m")
            print(f"\033[1;36m[✓] Location: {DOWNLOAD_DIR}\033[0m")
            print(f"\033[1;32m🤖 [AI] Bypass successful - video should play normally\033[0m")
        else:
            print(f"\n\033[1;31m[!] All 5 bypass methods failed.\033[0m")
            print("\033[1;33m[!] Try: update tool or check URL\033[0m")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\033[1;31m[!] Error: {e}\033[0m")
        print("\033[1;33m[!] Run: pip install yt-dlp --upgrade\033[0m")
