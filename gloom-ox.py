#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    GLOOM-OX v5.1 - UNIVERSAL EDITION                          ║
║                                                                               ║
║         [ WORKS ON: Termux | Linux | Windows | macOS | Ubuntu ]               ║
║         [ ONE LINK = ONE VIDEO - DUPLICATE PROTECTION ]                       ║
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
import shutil
import hashlib
from pathlib import Path
from urllib.parse import urlparse

# ==================== GLOBAL CONFIG ====================
VERSION = "5.1.0"
AUTHOR = "xspeen"
REPO_URL = "https://github.com/xspeen/GLOOM-OX"
HOME = str(Path.home())
SYSTEM = platform.system().lower()
IS_TERMUX = 'com.termux' in HOME or 'termux' in sys.executable
IS_WINDOWS = SYSTEM == 'windows'
IS_MAC = SYSTEM == 'darwin'
IS_LINUX = SYSTEM == 'linux'

# ==================== CROSS-PLATFORM PATHS ====================
if IS_WINDOWS:
    # Windows paths
    DOWNLOAD_DIR = os.path.join(HOME, "Videos", "GLOOM_OX")
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
elif IS_MAC:
    # macOS paths
    DOWNLOAD_DIR = os.path.join(HOME, "Movies", "GLOOM_OX")
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
elif IS_TERMUX:
    # Termux/Android paths
    DCIM_PATHS = [
        "/storage/emulated/0/DCIM",
        "/sdcard/DCIM",
        "/storage/emulated/0/Pictures",
    ]
    WORKING_DCIM = None
    for path in DCIM_PATHS:
        if os.path.exists(path) or os.access(os.path.dirname(path), os.W_OK):
            WORKING_DCIM = path
            break
    if not WORKING_DCIM:
        subprocess.run(["termux-setup-storage"], capture_output=True)
        time.sleep(2)
        WORKING_DCIM = "/storage/emulated/0/DCIM"
    DOWNLOAD_DIR = os.path.join(WORKING_DCIM, "GLOOM_OX")
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    os.chmod(DOWNLOAD_DIR, 0o777)
else:
    # Linux/Ubuntu
    DOWNLOAD_DIR = os.path.join(HOME, "Videos", "GLOOM_OX")
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# ==================== DUPLICATE TRACKING ====================
DOWNLOAD_HISTORY_FILE = os.path.join(HOME, ".gloom_ox_history.json")
DOWNLOADED_URLS = set()

def load_history():
    """Load download history"""
    global DOWNLOADED_URLS
    if os.path.exists(DOWNLOAD_HISTORY_FILE):
        try:
            with open(DOWNLOAD_HISTORY_FILE, 'r') as f:
                history = json.load(f)
                DOWNLOADED_URLS = set(history.get('urls', []))
        except:
            pass

def save_history(url):
    """Save URL to history"""
    DOWNLOADED_URLS.add(url)
    try:
        with open(DOWNLOAD_HISTORY_FILE, 'w') as f:
            json.dump({'urls': list(DOWNLOADED_URLS)}, f, indent=2)
    except:
        pass

def is_duplicate(url):
    """Check if URL was downloaded"""
    normalized = url.split('?')[0]
    for downloaded in DOWNLOADED_URLS:
        if downloaded.split('?')[0] == normalized:
            return True
    return False

# ==================== FULL BANNER ====================
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
║        [ UNIVERSAL SOCIAL MEDIA DOWNLOADER - v5.1.0 ]                         ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
\033[0m
"""

# ==================== USER AGENTS ====================
USER_AGENTS = [
    'Mozilla/5.0 (Linux; Android 14; SM-S901B) AppleWebKit/537.36 Chrome/122.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
]

# ==================== CROSS-PLATFORM GALLERY INJECTOR ====================
class GalleryInjector:
    """Cross-platform video injector"""
    
    @staticmethod
    def generate_unique_filename(title, url):
        """Generate unique filename"""
        url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
        clean_title = re.sub(r'[^\w\s-]', '', title)
        clean_title = re.sub(r'\s+', '_', clean_title)
        clean_title = clean_title[:50]
        timestamp = int(time.time())
        return f"GLOOM_{clean_title}_{url_hash}_{timestamp}.mp4"
    
    @staticmethod
    def save_to_gallery(filepath):
        """Save video to appropriate location based on OS"""
        if IS_WINDOWS:
            print(f"\033[1;32m📁 Saved to: {filepath}\033[0m")
            return True
        elif IS_MAC:
            print(f"\033[1;32m📁 Saved to: {filepath}\033[0m")
            # Trigger macOS Spotlight indexing
            subprocess.run(["mdimport", filepath], capture_output=True)
            return True
        elif IS_TERMUX:
            # Android gallery injection
            try:
                subprocess.run(["termux-media-scan", filepath], capture_output=True, timeout=10)
                print(f"\033[1;32m📱 Added to Android Gallery\033[0m")
                return True
            except:
                print(f"\033[1;32m📁 Saved to: {filepath}\033[0m")
                return True
        else:
            # Linux
            print(f"\033[1;32m📁 Saved to: {filepath}\033[0m")
            return True

# ==================== DOWNLOADER ENGINE ====================
class GloomOXDownloader:
    """Universal downloader for all platforms"""
    
    def __init__(self):
        self.download_dir = DOWNLOAD_DIR
        
    def get_headers(self):
        return {
            'User-Agent': random.choice(USER_AGENTS),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'DNT': '1',
        }
    
    def download(self, url):
        """Download video from any platform"""
        
        if is_duplicate(url):
            print(f"\033[1;33m⚠️ Video already downloaded! Skipping...\033[0m")
            return None, None
        
        try:
            import yt_dlp
            
            # Get video info first
            info_opts = {'quiet': True, 'no_warnings': True}
            with yt_dlp.YoutubeDL(info_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                title = info.get('title', 'Video')
            
            # Generate unique filename
            unique_filename = GalleryInjector.generate_unique_filename(title, url)
            output_template = os.path.join(self.download_dir, unique_filename)
            
            # Download options
            dl_opts = {
                'format': 'best[ext=mp4]/best',
                'outtmpl': output_template,
                'quiet': False,
                'no_warnings': False,
                'ignoreerrors': False,
                'retries': 5,
                'user_agent': random.choice(USER_AGENTS),
                'headers': self.get_headers(),
                'extractor_args': {
                    'youtube': {'player_client': ['android', 'ios']},
                    'instagram': {'user_agent': ['mobile']},
                    'tiktok': {'user_agent': ['mobile']},
                }
            }
            
            print(f"\033[1;33m⬇️ Downloading: {title[:50]}...\033[0m")
            
            with yt_dlp.YoutubeDL(dl_opts) as ydl:
                ydl.download([url])
                
                if os.path.exists(output_template):
                    save_history(url)
                    return output_template, title
                
                # Find any new file
                for file in os.listdir(self.download_dir):
                    if unique_filename[:30] in file or str(int(time.time())) in file:
                        filepath = os.path.join(self.download_dir, file)
                        save_history(url)
                        return filepath, title
                        
        except Exception as e:
            print(f"\033[1;31m❌ Error: {str(e)[:80]}\033[0m")
            
        return None, None
    
    def optimize_video(self, filename):
        """Optimize video for platform"""
        try:
            subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
            
            output = filename.replace('.mp4', '_opt.mp4')
            
            cmd = [
                "ffmpeg", "-i", filename,
                "-c:v", "libx264",
                "-preset", "fast",
                "-crf", "23",
                "-c:a", "aac",
                "-b:a", "128k",
                "-movflags", "+faststart",
                "-pix_fmt", "yuv420p",
                "-y", output
            ]
            
            subprocess.run(cmd, capture_output=True, timeout=180)
            
            if os.path.exists(output) and os.path.getsize(output) > 10240:
                os.remove(filename)
                os.rename(output, filename)
                print("\033[1;32m  ✓ Optimized\033[0m")
        except:
            pass
        
        return filename

# ==================== DEPENDENCY CHECK ====================
def check_dependencies():
    """Check and install dependencies for each OS"""
    print("\033[1;34m[+] Checking dependencies...\033[0m")
    
    # Check yt-dlp
    try:
        import yt_dlp
        print("\033[1;32m[✓] yt-dlp: Installed\033[0m")
    except ImportError:
        print("\033[1;33m[~] Installing yt-dlp...\033[0m")
        subprocess.run([sys.executable, "-m", "pip", "install", "yt-dlp", "--upgrade"])
    
    # Platform-specific dependencies
    if IS_TERMUX:
        try:
            subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
            print("\033[1;32m[✓] FFmpeg: Installed\033[0m")
        except:
            print("\033[1;33m[~] Installing FFmpeg...\033[0m")
            subprocess.run(["pkg", "install", "ffmpeg", "-y"])
    elif IS_WINDOWS:
        print("\033[1;33m[!] FFmpeg recommended for video optimization\033[0m")
    elif IS_MAC:
        try:
            subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
            print("\033[1;32m[✓] FFmpeg: Installed\033[0m")
        except:
            print("\033[1;33m[!] Install FFmpeg: brew install ffmpeg\033[0m")
    
    return True

# ==================== MAIN ====================
def main():
    """Main entry point"""
    os.system('cls' if IS_WINDOWS else 'clear')
    print(BANNER)
    
    # Load history
    load_history()
    
    # Display system info
    print(f"\033[1;33m[+] Author: {AUTHOR}\033[0m")
    print(f"\033[1;33m[+] Repository: {REPO_URL}\033[0m")
    print(f"\033[1;36m[+] Platform: {platform.system()} {platform.release()}\033[0m")
    print(f"\033[1;36m[+] Version: {VERSION}\033[0m")
    print(f"\033[1;36m[+] Duplicate Protection: ACTIVE\033[0m")
    print(f"\033[1;36m[+] Download History: {len(DOWNLOADED_URLS)} videos\033[0m")
    print(f"\033[1;36m[+] Save Location: {DOWNLOAD_DIR}\033[0m")
    print("\033[1;32m" + "="*70 + "\033[0m")
    
    print("\033[1;36m🎯 ONE LINK = ONE VIDEO - No duplicates!\033[0m")
    print("\033[1;36m📱 Supports: YouTube, Instagram, TikTok, Twitter, Facebook\033[0m\n")
    
    check_dependencies()
    
    downloader = GloomOXDownloader()
    
    while True:
        print("\n\033[1;35m" + "═"*70 + "\033[0m")
        print("\033[1;33m[+] Enter video URL:\033[0m")
        print("\033[1;36m   Commands: history | clear | exit\033[0m")
        
        try:
            url = input("\033[1;32m[GLOOM-OX] >> \033[0m").strip()
        except KeyboardInterrupt:
            print("\n\033[1;31m[!] Shutting down...\033[0m")
            break
        except EOFError:
            break
        
        if url.lower() in ['exit', 'quit', 'q']:
            print("\033[1;32m[+] Thanks for using GLOOM-OX!\033[0m")
            break
        elif url.lower() == 'clear':
            os.system('cls' if IS_WINDOWS else 'clear')
            print(BANNER)
            continue
        elif url.lower() == 'history':
            print(f"\n\033[1;36m📋 Downloaded videos ({len(DOWNLOADED_URLS)}):\033[0m")
            for i, old_url in enumerate(list(DOWNLOADED_URLS)[-10:], 1):
                print(f"   {i}. {old_url[:80]}...")
            continue
        elif not url:
            continue
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        if is_duplicate(url):
            print(f"\n\033[1;33m⚠️ SKIPPED: This video was already downloaded!\033[0m")
            continue
        
        print("\n")
        start_time = time.time()
        
        filename, title = downloader.download(url)
        
        if filename and os.path.exists(filename):
            filename = downloader.optimize_video(filename)
            GalleryInjector.save_to_gallery(filename)
            
            elapsed = time.time() - start_time
            
            print(f"\n\033[1;32m╔══════════════════════════════════════════════════════════╗")
            print(f"║              ✅ DOWNLOAD COMPLETE - 1 VIDEO                      ║")
            print(f"╚══════════════════════════════════════════════════════════╝\033[0m")
            print(f"\033[1;36m📹 Title: {title[:60]}\033[0m")
            print(f"\033[1;36m⏱️ Time: {elapsed:.1f} seconds\033[0m")
            print(f"\033[1;32m💾 Saved: {os.path.basename(filename)}\033[0m")
            print(f"\033[1;32m📁 Location: {filename}\033[0m")
        else:
            print(f"\n\033[1;31m❌ Download failed!\033[0m")
            print("\033[1;33m💡 Try: pip install --upgrade yt-dlp\033[0m")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\033[1;31m⚠️ Error: {e}\033[0m")
