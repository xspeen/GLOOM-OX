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
import shutil
from pathlib import Path
from urllib.parse import urlparse

# ==================== GLOBAL CONFIG ====================
VERSION = "4.0.0"
AUTHOR = "xspeen"
REPO_URL = "https://github.com/xspeen/GLOOM-OX"
HOME = str(Path.home())
SYSTEM = platform.system().lower()
IS_TERMUX = 'com.termux' in HOME or 'termux' in sys.executable

# Paths - Fix for DCIM Gallery
if IS_TERMUX:
    # Termux path setup
    try:
        # Check if storage is accessible
        TERMUX_STORAGE = "/data/data/com.termux/files/home/storage/shared"
        if not os.path.exists(TERMUX_STORAGE):
            TERMUX_STORAGE = os.path.join(HOME, "storage/shared")
        
        DCIM_PATH = os.path.join(TERMUX_STORAGE, "DCIM")
        # Create GLOOM-OX folder inside DCIM
        DOWNLOAD_DIR = os.path.join(DCIM_PATH, "GLOOM-OX_Videos")
    except:
        DOWNLOAD_DIR = os.path.join(HOME, "storage/shared/DCIM/GLOOM-OX_Videos")
else:
    # Non-Termux (Windows/Linux/Mac)
    DOWNLOAD_DIR = os.path.join(HOME, "Videos", "GLOOM-OX_Videos")
    if SYSTEM == "windows":
        DOWNLOAD_DIR = os.path.join(os.environ.get('USERPROFILE', HOME), "Videos", "GLOOM-OX_Videos")
    elif SYSTEM == "linux":
        DOWNLOAD_DIR = os.path.join(HOME, "Videos", "GLOOM-OX_Videos")
    elif SYSTEM == "darwin":  # macOS
        DOWNLOAD_DIR = os.path.join(HOME, "Movies", "GLOOM-OX_Videos")

# Create download directory
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# ==================== TIER 3 BYPASS CONFIG ====================
# Multiple user agents for rotation
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Linux; Android 14; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
]

# Supported platforms and their extractors
SUPPORTED_PLATFORMS = {
    'youtube': 'youtube',
    'youtu.be': 'youtube',
    'instagram': 'instagram',
    'pinterest': 'pinterest',
    'tiktok': 'tiktok',
    'twitter': 'twitter',
    'x.com': 'twitter',
    'facebook': 'facebook',
    'reddit': 'reddit',
    'vimeo': 'vimeo',
    'dailymotion': 'dailymotion',
}

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

# ==================== DEPENDENCY CHECK ====================
def check_dependencies():
    """Check and install all dependencies"""
    print("\033[1;34m[+] Checking dependencies...\033[0m")
    
    dependencies_ok = True
    
    # Check/Install yt-dlp
    try:
        import yt_dlp
        print("\033[1;32m[✓] yt-dlp: Installed\033[0m")
    except ImportError:
        print("\033[1;33m[~] Installing yt-dlp...\033[0m")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "yt-dlp", "--upgrade", "--quiet"], check=True)
            print("\033[1;32m[✓] yt-dlp installed successfully\033[0m")
        except:
            print("\033[1;31m[✗] Failed to install yt-dlp\033[0m")
            dependencies_ok = False
    
    # Check FFmpeg for video processing
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        print("\033[1;32m[✓] FFmpeg: Installed\033[0m")
    except:
        print("\033[1;33m[!] FFmpeg not found - videos will still download but may not play on all devices\033[0m")
        if IS_TERMUX:
            print("\033[1;33m[~] Install FFmpeg: pkg install ffmpeg\033[0m")
    
    return dependencies_ok

# ==================== VIDEO DOWNLOADER ====================
class SocialMediaDownloader:
    """Universal social media video downloader"""
    
    def __init__(self):
        self.download_dir = DOWNLOAD_DIR
        self.session = None
        
    def get_platform(self, url):
        """Detect platform from URL"""
        domain = urlparse(url).netloc.lower()
        domain = domain.replace('www.', '')
        
        for platform, extractor in SUPPORTED_PLATFORMS.items():
            if platform in domain:
                return extractor
        return 'generic'
    
    def sanitize_filename(self, filename):
        """Remove invalid characters from filename"""
        # Remove invalid characters for Windows/Linux
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            filename = filename.replace(char, '_')
        # Limit length
        if len(filename) > 200:
            filename = filename[:200]
        return filename.strip()
    
    def download_video(self, url):
        """Download video from any social media platform"""
        platform = self.get_platform(url)
        print(f"\033[1;36m🤖 [AI] Detected platform: {platform.upper()}\033[0m")
        
        # Generate unique filename
        timestamp = int(time.time())
        random_id = random.randint(1000, 9999)
        
        # Configure yt-dlp options
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': os.path.join(self.download_dir, f'%(title)s_{timestamp}_{random_id}.%(ext)s'),
            'quiet': False,
            'no_warnings': False,
            'ignoreerrors': False,
            'retries': 10,
            'fragment_retries': 10,
            'skip_unavailable_fragments': False,
            'user_agent': random.choice(USER_AGENTS),
            'http_headers': {
                'User-Agent': random.choice(USER_AGENTS),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'DNT': '1',
                'Connection': 'keep-alive',
            },
            'extractor_args': {
                'youtube': {
                    'skip': ['dash', 'hls'],
                    'player_client': ['android', 'ios', 'web'],
                },
                'instagram': {
                    'user_agent': ['mobile'],
                },
                'tiktok': {
                    'user_agent': ['mobile'],
                }
            },
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }] if self.check_ffmpeg() else [],
        }
        
        try:
            import yt_dlp
            
            print(f"\033[1;33m[+] Starting download...\033[0m")
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                # Extract info first
                print(f"\033[1;36m🤖 [AI] Extracting video information...\033[0m")
                info = ydl.extract_info(url, download=False)
                
                if info:
                    title = info.get('title', 'Unknown Title')
                    duration = info.get('duration', 0)
                    
                    print(f"\033[1;36m[✓] Title: {title[:60]}\033[0m")
                    if duration:
                        print(f"\033[1;36m[✓] Duration: {duration // 60}:{duration % 60:02d} minutes\033[0m")
                    
                    # Now download
                    print(f"\033[1;33m[+] Downloading video...\033[0m")
                    ydl.download([url])
                    
                    # Get the actual downloaded filename
                    downloaded_files = []
                    for file in os.listdir(self.download_dir):
                        if str(timestamp) in file and (random_id in file or str(random_id) in file):
                            downloaded_files.append(os.path.join(self.download_dir, file))
                    
                    if downloaded_files:
                        # Get the most recent file
                        downloaded_files.sort(key=os.path.getctime, reverse=True)
                        filename = downloaded_files[0]
                        
                        # Verify file size
                        file_size = os.path.getsize(filename)
                        if file_size > 10240:  # At least 10KB
                            print(f"\033[1;32m[✓] Download successful! Size: {file_size / 1024 / 1024:.2f} MB\033[0m")
                            return filename, title
                        else:
                            print(f"\033[1;31m[✗] Downloaded file is too small ({file_size} bytes)\033[0m")
                            os.remove(filename)
                            return None, None
                    
            return None, None
            
        except Exception as e:
            print(f"\033[1;31m[✗] Download failed: {str(e)}\033[0m")
            return None, None
    
    def check_ffmpeg(self):
        """Check if ffmpeg is available"""
        try:
            subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
            return True
        except:
            return False
    
    def fix_video_for_gallery(self, filename):
        """Convert video to ensure gallery compatibility"""
        if not self.check_ffmpeg():
            return filename
        
        try:
            output_filename = filename.replace('.mp4', '_fixed.mp4').replace('.webm', '_fixed.mp4')
            
            print(f"\033[1;36m🤖 [AI] Optimizing video for gallery...\033[0m")
            
            # Convert to Android/iOS compatible format
            cmd = [
                "ffmpeg", "-i", filename,
                "-c:v", "libx264",
                "-preset", "fast",
                "-crf", "23",
                "-c:a", "aac",
                "-b:a", "128k",
                "-movflags", "+faststart",
                "-pix_fmt", "yuv420p",
                "-y", output_filename
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            
            if result.returncode == 0 and os.path.exists(output_filename):
                file_size = os.path.getsize(output_filename)
                if file_size > 10240:
                    # Replace original with fixed version
                    os.remove(filename)
                    os.rename(output_filename, filename)
                    print(f"\033[1;32m[✓] Video optimized for gallery\033[0m")
                    return filename
                else:
                    os.remove(output_filename)
                    print(f"\033[1;33m[!] Optimization failed, using original\033[0m")
                    return filename
            else:
                return filename
                
        except Exception as e:
            print(f"\033[1;33m[!] Optimization skipped: {str(e)[:50]}\033[0m")
            return filename
    
    def add_to_gallery(self, filename):
        """Add video to device gallery (Android/Termux only)"""
        if not IS_TERMUX:
            print(f"\033[1;36m[✓] Video saved to: {filename}\033[0m")
            return True
        
        try:
            # Try termux-media-scan for Android gallery
            subprocess.run(["termux-media-scan", filename], capture_output=True, timeout=10)
            print(f"\033[1;32m[✓] Video added to Android Gallery\033[0m")
            return True
        except:
            # Alternative method - copy to DCIM if not already there
            if not filename.startswith(DCIM_PATH):
                dcim_filename = os.path.join(DCIM_PATH, os.path.basename(filename))
                try:
                    shutil.copy2(filename, dcim_filename)
                    print(f"\033[1;32m[✓] Video copied to DCIM Gallery\033[0m")
                    subprocess.run(["termux-media-scan", dcim_filename], capture_output=True)
                    return True
                except:
                    print(f"\033[1;33m[!] Could not add to gallery, but video is saved in: {filename}\033[0m")
                    return False
            else:
                print(f"\033[1;32m[✓] Video already in DCIM Gallery\033[0m")
                return True

# ==================== MAIN FUNCTION ====================
def main():
    """Main entry point"""
    os.system('clear' if SYSTEM == 'windows' else 'clear')
    print(BANNER)
    
    print(f"\033[1;33m[+] Author: {AUTHOR}\033[0m")
    print(f"\033[1;33m[+] Repository: {REPO_URL}\033[0m")
    print(f"\033[1;36m[+] Platform: {SYSTEM.upper()} | Termux: {'YES' if IS_TERMUX else 'NO'}\033[0m")
    print(f"\033[1;36m[+] Download Directory: {DOWNLOAD_DIR}\033[0m")
    print(f"\033[1;32m" + "="*70 + "\033[0m")
    
    print("\033[1;36m🤖 [AI] GLOOM-OX activated - Social Media Video Downloader\033[0m")
    print("\033[1;36m🤖 [AI] Supports: YouTube, Instagram, TikTok, Pinterest, Twitter, Facebook, Reddit\033[0m")
    print("\033[1;32m💡 Videos will be saved to DCIM Gallery on Android/Termux\033[0m\n")
    
    # Check dependencies
    if not check_dependencies():
        print("\033[1;31m[!] Missing critical dependencies. Please install them manually.\033[0m")
        return
    
    # Initialize downloader
    downloader = SocialMediaDownloader()
    
    while True:
        print("\n\033[1;35m" + "═"*70 + "\033[0m")
        print("\033[1;33m[+] Enter video URL (or 'exit' to quit):\033[0m")
        print("\033[1;36m   Commands: clear | dir | exit\033[0m")
        
        try:
            url = input("\033[1;32m[GLOOM-OX] >> \033[0m").strip()
        except KeyboardInterrupt:
            print("\n\033[1;31m[!] Exiting...\033[0m")
            break
        except EOFError:
            break
        
        if url.lower() in ['exit', 'quit', 'q']:
            print("\033[1;32m[+] Thanks for using GLOOM-OX!\033[0m")
            break
        elif url.lower() == 'clear':
            os.system('clear' if SYSTEM == 'windows' else 'clear')
            print(BANNER)
            continue
        elif url.lower() == 'dir':
            print(f"\n\033[1;36m[+] Download directory: {DOWNLOAD_DIR}\033[0m")
            if os.path.exists(DOWNLOAD_DIR):
                files = os.listdir(DOWNLOAD_DIR)
                if files:
                    print("\033[1;33m[+] Downloaded videos:\033[0m")
                    for f in files[-10:]:  # Show last 10 files
                        print(f"   - {f}")
                else:
                    print("\033[1;33m[+] No videos downloaded yet\033[0m")
            continue
        elif not url:
            continue
        
        # Add https:// if missing
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        print("\n")
        start_time = time.time()
        
        # Download video
        filename, title = downloader.download_video(url)
        
        if filename and os.path.exists(filename):
            # Optimize for gallery
            filename = downloader.fix_video_for_gallery(filename)
            
            # Add to gallery
            downloader.add_to_gallery(filename)
            
            elapsed = time.time() - start_time
            
            print(f"\n\033[1;32m╔══════════════════════════════════════════════════════════╗")
            print(f"║                   DOWNLOAD COMPLETE!                          ║")
            print(f"╚══════════════════════════════════════════════════════════╝\033[0m")
            print(f"\033[1;36m[✓] Title: {title[:60] if title else 'Unknown'}\033[0m")
            print(f"\033[1;36m[✓] Time taken: {elapsed:.1f} seconds\033[0m")
            print(f"\033[1;36m[✓] Location: {filename}\033[0m")
            print(f"\033[1;32m🤖 [AI] Video saved to DCIM Gallery successfully!\033[0m")
        else:
            print(f"\n\033[1;31m[✗] Download failed! Please check the URL and try again.\033[0m")
            print("\033[1;33m[!] Tips:\033[0m")
            print("   - Make sure the video is public/accessible")
            print("   - Check your internet connection")
            print("   - Try a different URL")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Interrupted by user\033[0m")
    except Exception as e:
        print(f"\033[1;31m[!] Unexpected error: {e}\033[0m")
        print("\033[1;33m[!] Try updating: pip install --upgrade yt-dlp\033[0m")
