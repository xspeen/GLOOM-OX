#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║     ██████╗  ██╗      ██████╗  ██████╗ ███╗   ███╗     ██████╗ ██╗  ██╗      ║
║    ██╔════╝ ██║     ██╔═══██╗██╔═══██╗████╗ ████║    ██╔═══██╗██║  ██║      ║
║    ██║  ███╗██║     ██║   ██║██║   ██║██╔████╔██║    ██║   ██║███████║      ║
║    ██║   ██║██║     ██║   ██║██║   ██║██║╚██╔╝██║    ██║   ██║██╔══██║      ║
║    ╚██████╔╝███████╗╚██████╔╝╚██████╔╝██║ ╚═╝ ██║    ╚██████╔╝██║  ██║      ║
║     ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝     ╚═════╝ ╚═╝  ╚═╝      ║
║                                                                               ║
║         [ ULTIMATE AGGRESSIVE BYPASS ENGINE - UNDETECTABLE v5.2 ]             ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import platform
import time
import random
import subprocess
import json
import hashlib
import tempfile
import shutil
from pathlib import Path
from urllib.parse import urlparse

VERSION = "5.2.0"
AUTHOR = "xspeen"
REPO_URL = "https://github.com/xspeen/GLOOM-OX"
HOME = str(Path.home())
SYSTEM = platform.system().lower()
IS_TERMUX = 'com.termux' in HOME or 'termux' in sys.executable
IS_WINDOWS = SYSTEM == 'windows'
IS_MAC = SYSTEM == 'darwin'

# ==================== PATHS ====================
if IS_TERMUX:
    DOWNLOAD_DIR = "/storage/emulated/0/DCIM/GLOOM_OX"
elif IS_WINDOWS:
    DOWNLOAD_DIR = os.path.join(HOME, "Videos", "GLOOM_OX")
elif IS_MAC:
    DOWNLOAD_DIR = os.path.join(HOME, "Movies", "GLOOM_OX")
else:
    DOWNLOAD_DIR = os.path.join(HOME, "Videos", "GLOOM_OX")

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# ==================== DUPLICATE TRACKING ====================
HISTORY_FILE = os.path.join(HOME, ".gloom_ox_history.json")
DOWNLOADED_URLS = set()

def load_history():
    global DOWNLOADED_URLS
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r') as f:
                data = json.load(f)
                DOWNLOADED_URLS = set(data.get('urls', []))
        except:
            pass

def save_history(url):
    DOWNLOADED_URLS.add(url)
    try:
        with open(HISTORY_FILE, 'w') as f:
            json.dump({'urls': list(DOWNLOADED_URLS)}, f)
    except:
        pass

def is_duplicate(url):
    normalized = url.split('?')[0]
    for downloaded in DOWNLOADED_URLS:
        if downloaded.split('?')[0] == normalized:
            return True
    return False

# ==================== ULTIMATE BYPASS ENGINE ====================

class UltimateBypass:
    """Ultimate aggressive bypass with 10 methods"""
    
    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Linux; Android 14; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0',
    ]
    
    @staticmethod
    def get_cookies():
        """Extract cookies from multiple browsers"""
        browsers = ['chrome', 'firefox', 'brave', 'edge', 'chromium', 'opera', 'safari']
        
        for browser in browsers:
            try:
                temp_file = tempfile.NamedTemporaryFile(suffix='.txt', delete=False)
                temp_file.close()
                
                subprocess.run([
                    sys.executable, "-m", "yt_dlp",
                    f"--cookies-from-browser", browser,
                    "--cookies", temp_file.name,
                    "https://youtube.com", "--skip-download", "--quiet"
                ], capture_output=True, timeout=30)
                
                if os.path.exists(temp_file.name) and os.path.getsize(temp_file.name) > 100:
                    return temp_file.name
                else:
                    os.unlink(temp_file.name)
            except:
                continue
        
        return None

class AggressiveDownloader:
    """10 aggressive bypass methods"""
    
    def __init__(self):
        self.download_dir = DOWNLOAD_DIR
        
    def download(self, url):
        if is_duplicate(url):
            print("\033[1;33m[!] Already downloaded. Skipping...\033[0m")
            return None, None
        
        methods = [
            self.method_android,
            self.method_ios,
            self.method_tv,
            self.method_embed,
            self.method_cookies,
            self.method_web_client,
            self.method_music_client,
            self.method_vr_client,
            self.method_android_vr,
            self.method_legacy,
        ]
        
        for i, method in enumerate(methods, 1):
            print(f"\033[1;36m[{i}/10] {method.__name__.replace('_', ' ').upper()}\033[0m")
            time.sleep(random.uniform(0.5, 1.5))
            
            result = method(url)
            if result and result[0] and os.path.exists(result[0]) and os.path.getsize(result[0]) > 10240:
                save_history(url)
                return result
        
        return None, None
    
    def method_android(self, url):
        try:
            import yt_dlp
            timestamp = int(time.time())
            rid = random.randint(1000, 9999)
            output = os.path.join(self.download_dir, f"AND_{timestamp}_{rid}.mp4")
            
            opts = {
                'format': 'best[ext=mp4]/best',
                'outtmpl': output,
                'quiet': False,
                'no_warnings': False,
                'ignoreerrors': False,
                'retries': 30,
                'user_agent': 'Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 Chrome/122.0.0.0 Mobile Safari/537.36',
                'extractor_args': {'youtube': {'player_client': ['android']}},
                'http_headers': {'X-YouTube-Client-Name': '3', 'X-YouTube-Client-Version': '19.09.37'},
            }
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
                if os.path.exists(output):
                    return output, info.get('title', 'Video')
        except Exception as e:
            print(f"\033[1;30mFailed: {str(e)[:50]}\033[0m")
        return None, None
    
    def method_ios(self, url):
        try:
            import yt_dlp
            timestamp = int(time.time())
            rid = random.randint(1000, 9999)
            output = os.path.join(self.download_dir, f"IOS_{timestamp}_{rid}.mp4")
            
            opts = {
                'format': 'best[ext=mp4]/best',
                'outtmpl': output,
                'quiet': False,
                'no_warnings': False,
                'ignoreerrors': False,
                'retries': 30,
                'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148 Safari/604.1',
                'extractor_args': {'youtube': {'player_client': ['ios']}},
                'http_headers': {'X-YouTube-Client-Name': '5', 'X-YouTube-Client-Version': '19.09.37'},
            }
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
                if os.path.exists(output):
                    return output, info.get('title', 'Video')
        except Exception as e:
            print(f"\033[1;30mFailed: {str(e)[:50]}\033[0m")
        return None, None
    
    def method_tv(self, url):
        try:
            import yt_dlp
            timestamp = int(time.time())
            rid = random.randint(1000, 9999)
            output = os.path.join(self.download_dir, f"TV_{timestamp}_{rid}.mp4")
            
            opts = {
                'format': 'best[ext=mp4]/best',
                'outtmpl': output,
                'quiet': False,
                'no_warnings': False,
                'ignoreerrors': False,
                'retries': 25,
                'user_agent': 'Mozilla/5.0 (SMART-TV; Linux; Tizen 7.0) AppleWebKit/537.36 SamsungBrowser/2.1 Chrome/122.0.0.0 Safari/537.36',
                'extractor_args': {'youtube': {'player_client': ['tv_embedded']}},
            }
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
                if os.path.exists(output):
                    return output, info.get('title', 'Video')
        except Exception as e:
            print(f"\033[1;30mFailed: {str(e)[:50]}\033[0m")
        return None, None
    
    def method_embed(self, url):
        try:
            import yt_dlp
            timestamp = int(time.time())
            rid = random.randint(1000, 9999)
            output = os.path.join(self.download_dir, f"EMB_{timestamp}_{rid}.mp4")
            
            video_id = url.split('v=')[-1].split('&')[0].split('/')[-1]
            embed_url = f"https://www.youtube.com/embed/{video_id}"
            
            opts = {
                'format': 'best[ext=mp4]/best',
                'outtmpl': output,
                'quiet': False,
                'no_warnings': False,
                'ignoreerrors': False,
                'retries': 20,
                'user_agent': UltimateBypass.USER_AGENTS[0],
            }
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(embed_url, download=True)
                if os.path.exists(output):
                    return output, info.get('title', 'Video')
        except Exception as e:
            print(f"\033[1;30mFailed: {str(e)[:50]}\033[0m")
        return None, None
    
    def method_cookies(self, url):
        try:
            import yt_dlp
            timestamp = int(time.time())
            rid = random.randint(1000, 9999)
            output = os.path.join(self.download_dir, f"COOK_{timestamp}_{rid}.mp4")
            
            cookie_file = UltimateBypass.get_cookies()
            
            opts = {
                'format': 'best[ext=mp4]/best',
                'outtmpl': output,
                'quiet': False,
                'no_warnings': False,
                'ignoreerrors': False,
                'retries': 35,
                'user_agent': UltimateBypass.USER_AGENTS[0],
            }
            
            if cookie_file:
                opts['cookiefile'] = cookie_file
                print("\033[1;32m[+] Cookies loaded\033[0m")
            
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
                if os.path.exists(output):
                    return output, info.get('title', 'Video')
        except Exception as e:
            print(f"\033[1;30mFailed: {str(e)[:50]}\033[0m")
        return None, None
    
    def method_web_client(self, url):
        try:
            import yt_dlp
            timestamp = int(time.time())
            rid = random.randint(1000, 9999)
            output = os.path.join(self.download_dir, f"WEB_{timestamp}_{rid}.mp4")
            
            opts = {
                'format': 'best[ext=mp4]/best',
                'outtmpl': output,
                'quiet': False,
                'no_warnings': False,
                'ignoreerrors': False,
                'retries': 20,
                'user_agent': UltimateBypass.USER_AGENTS[2],
                'extractor_args': {'youtube': {'player_client': ['web']}},
            }
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
                if os.path.exists(output):
                    return output, info.get('title', 'Video')
        except Exception as e:
            print(f"\033[1;30mFailed: {str(e)[:50]}\033[0m")
        return None, None
    
    def method_music_client(self, url):
        try:
            import yt_dlp
            timestamp = int(time.time())
            rid = random.randint(1000, 9999)
            output = os.path.join(self.download_dir, f"MUSIC_{timestamp}_{rid}.mp4")
            
            opts = {
                'format': 'best[ext=mp4]/best',
                'outtmpl': output,
                'quiet': False,
                'no_warnings': False,
                'ignoreerrors': False,
                'retries': 20,
                'user_agent': UltimateBypass.USER_AGENTS[4],
                'extractor_args': {'youtube': {'player_client': ['web_music']}},
            }
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
                if os.path.exists(output):
                    return output, info.get('title', 'Video')
        except Exception as e:
            print(f"\033[1;30mFailed: {str(e)[:50]}\033[0m")
        return None, None
    
    def method_vr_client(self, url):
        try:
            import yt_dlp
            timestamp = int(time.time())
            rid = random.randint(1000, 9999)
            output = os.path.join(self.download_dir, f"VR_{timestamp}_{rid}.mp4")
            
            opts = {
                'format': 'best[ext=mp4]/best',
                'outtmpl': output,
                'quiet': False,
                'no_warnings': False,
                'ignoreerrors': False,
                'retries': 20,
                'user_agent': UltimateBypass.USER_AGENTS[3],
                'extractor_args': {'youtube': {'player_client': ['web_embedded']}},
            }
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
                if os.path.exists(output):
                    return output, info.get('title', 'Video')
        except Exception as e:
            print(f"\033[1;30mFailed: {str(e)[:50]}\033[0m")
        return None, None
    
    def method_android_vr(self, url):
        try:
            import yt_dlp
            timestamp = int(time.time())
            rid = random.randint(1000, 9999)
            output = os.path.join(self.download_dir, f"ANDVR_{timestamp}_{rid}.mp4")
            
            opts = {
                'format': 'best[ext=mp4]/best',
                'outtmpl': output,
                'quiet': False,
                'no_warnings': False,
                'ignoreerrors': False,
                'retries': 20,
                'user_agent': UltimateBypass.USER_AGENTS[4],
                'extractor_args': {'youtube': {'player_client': ['android_vr']}},
            }
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
                if os.path.exists(output):
                    return output, info.get('title', 'Video')
        except Exception as e:
            print(f"\033[1;30mFailed: {str(e)[:50]}\033[0m")
        return None, None
    
    def method_legacy(self, url):
        try:
            import yt_dlp
            timestamp = int(time.time())
            rid = random.randint(1000, 9999)
            output = os.path.join(self.download_dir, f"LEGACY_{timestamp}_{rid}.mp4")
            
            opts = {
                'format': 'worst[ext=mp4]/worst',
                'outtmpl': output,
                'quiet': False,
                'no_warnings': False,
                'ignoreerrors': False,
                'retries': 15,
                'user_agent': UltimateBypass.USER_AGENTS[6],
            }
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
                if os.path.exists(output):
                    return output, info.get('title', 'Video')
        except Exception as e:
            print(f"\033[1;30mFailed: {str(e)[:50]}\033[0m")
        return None, None

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
║         [ ULTIMATE AGGRESSIVE BYPASS ENGINE - UNDETECTABLE v5.2 ]             ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
\033[0m
"""

# ==================== MAIN ====================
def main():
    os.system('clear')
    print(BANNER)
    
    load_history()
    
    print(f"\033[1;33m[+] Author: {AUTHOR}\033[0m")
    print(f"\033[1;33m[+] Repository: {REPO_URL}\033[0m")
    print(f"\033[1;36m[+] Platform: {platform.system()} {platform.release()}\033[0m")
    print(f"\033[1;36m[+] Version: {VERSION}\033[0m")
    print(f"\033[1;36m[+] History: {len(DOWNLOADED_URLS)} videos\033[0m")
    print(f"\033[1;36m[+] Save Location: {DOWNLOAD_DIR}\033[0m")
    print("\033[1;32m" + "="*70 + "\033[0m")
    print("\033[1;36m[+] 10 Aggressive Bypass Methods Active\033[0m")
    print("\033[1;36m[+] YouTube Detection: FULLY BYPASSED\033[0m\n")
    
    downloader = AggressiveDownloader()
    
    while True:
        print("\n\033[1;35m" + "═"*70 + "\033[0m")
        print("\033[1;33m[+] Enter Video URL:\033[0m")
        print("\033[1;36m    Commands: history | clear | exit\033[0m")
        
        try:
            url = input("\033[1;32m[GLOOM-OX] >> \033[0m").strip()
        except KeyboardInterrupt:
            print("\n\033[1;31m[!] Shutting down...\033[0m")
            break
        
        if url.lower() in ['exit', 'quit']:
            break
        elif url.lower() == 'clear':
            os.system('clear')
            print(BANNER)
            continue
        elif url.lower() == 'history':
            print(f"\n\033[1;36m[+] Downloaded Videos ({len(DOWNLOADED_URLS)}):\033[0m")
            for i, u in enumerate(list(DOWNLOADED_URLS)[-10:], 1):
                print(f"    {i}. {u[:80]}...")
            continue
        elif not url:
            continue
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        print()
        start = time.time()
        filename, title = downloader.download(url)
        elapsed = time.time() - start
        
        if filename:
            print(f"\n\033[1;32m╔══════════════════════════════════════════════════════════╗")
            print(f"║                 ✅ DOWNLOAD SUCCESSFUL!                          ║")
            print(f"╚══════════════════════════════════════════════════════════╝\033[0m")
            print(f"\033[1;36m[+] Title: {title[:60]}\033[0m")
            print(f"\033[1;36m[+] Time: {elapsed:.1f}s\033[0m")
            print(f"\033[1;36m[+] File: {os.path.basename(filename)}\033[0m")
            print(f"\033[1;32m[+] Location: {filename}\033[0m")
            
            if IS_TERMUX:
                subprocess.run(["termux-media-scan", filename], capture_output=True)
                print("\033[1;32m[+] Added to Android Gallery\033[0m")
        else:
            print(f"\n\033[1;31m╔══════════════════════════════════════════════════════════╗")
            print(f"║                 ❌ DOWNLOAD FAILED!                              ║")
            print(f"╚══════════════════════════════════════════════════════════╝\033[0m")
            print("\033[1;33m[+] Solutions:\033[0m")
            print("    1. Run: pip install --upgrade yt-dlp")
            print("    2. Login to YouTube in browser")
            print("    3. Extract cookies: yt-dlp --cookies-from-browser chrome --cookies cookies.txt")
            print("    4. Try a VPN if rate limited")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\033[1;31m[!] Error: {e}\033[0m")
