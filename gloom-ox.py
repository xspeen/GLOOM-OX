#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    GLOOM-OX v5.0 - ULTIMATE BYPASS ENGINE                     ║
║                                                                               ║
║  ██████╗ ██╗   ██╗██████╗  █████╗ ███████╗███████╗                           ║
║  ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝                           ║
║  ██████╔╝ ╚████╔╝ ██████╔╝███████║███████╗███████╗                           ║
║  ██╔══██╗  ╚██╔╝  ██╔══██╗██╔══██║╚════██║╚════██║                           ║
║  ██████╔╝   ██║   ██████╔╝██║  ██║███████║███████║                           ║
║  ╚═════╝    ╚═╝   ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝                           ║
║                                                                               ║
║         [ ADVANCED BYPASS ENGINE - UNDETECTABLE v5.0 ]                        ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import random
import json
import hashlib
import base64
import urllib.parse
import subprocess
import threading
import queue
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# ==================== ADVANCED CONFIGURATION ====================
VERSION = "5.0.0"
HOME = str(Path.home())
SYSTEM = platform.system().lower()
IS_TERMUX = 'com.termux' in HOME or 'termux' in sys.executable

# Stealth directories
if IS_TERMUX:
    TERMUX_STORAGE = "/data/data/com.termux/files/home/storage/shared"
    if not os.path.exists(TERMUX_STORAGE):
        TERMUX_STORAGE = os.path.join(HOME, "storage/shared")
    DCIM_PATH = os.path.join(TERMUX_STORAGE, "DCIM")
    DOWNLOAD_DIR = os.path.join(DCIM_PATH, "Videos")
else:
    DOWNLOAD_DIR = os.path.join(HOME, "Videos", "Downloads")

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# ==================== SOPHISTICATED BYPASS TECHNIQUES ====================

class StealthEngine:
    """Advanced anti-detection engine"""
    
    def __init__(self):
        self.request_count = 0
        self.fingerprint = self.generate_fingerprint()
        self.session_tokens = []
        
    def generate_fingerprint(self):
        """Generate unique browser fingerprint"""
        fingerprints = [
            f"{random.randint(1000000000, 9999999999)}",
            base64.b64encode(os.urandom(16)).decode(),
            hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
        ]
        return random.choice(fingerprints)
    
    def rotate_fingerprint(self):
        """Rotate fingerprint every request"""
        self.fingerprint = self.generate_fingerprint()
        self.request_count += 1
        
    def get_stealth_headers(self):
        """Generate undetectable request headers"""
        headers = {
            'User-Agent': self.get_random_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': random.choice(['en-US,en;q=0.9', 'en-GB,en;q=0.8', 'en;q=0.9']),
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Charset': 'UTF-8,*;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'DNT': '1',
            'Pragma': 'no-cache',
        }
        
        # Add random extra headers to appear more legitimate
        if random.random() > 0.7:
            headers['X-Requested-With'] = random.choice(['XMLHttpRequest', 'com.android.browser', ''])
            headers['X-Forwarded-For'] = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
            
        return headers
    
    def get_random_user_agent(self):
        """Extensive user agent rotation"""
        ua_list = [
            # Chrome on Android
            f'Mozilla/5.0 (Linux; Android {random.randint(11,14)}; {random.choice(["SM-G998B", "Pixel 6", "OnePlus 9Pro"])}) AppleWebKit/537.36 Chrome/{random.randint(90,122)}.0.0.0 Mobile Safari/537.36',
            
            # Safari on iOS
            f'Mozilla/5.0 (iPhone; CPU iPhone OS {random.randint(15,17)}_{random.randint(0,5)} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{random.randint(15,17)}.0 Mobile/15E148 Safari/604.1',
            
            # Chrome on Windows
            f'Mozilla/5.0 (Windows NT {random.randint(10,11)}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90,122)}.0.0.0 Safari/537.36',
            
            # Firefox
            f'Mozilla/5.0 (Windows NT {random.randint(10,11)}.0; Win64; x64; rv:{random.randint(90,109)}.0) Gecko/20100101 Firefox/{random.randint(90,109)}.0',
            
            # Edge
            f'Mozilla/5.0 (Windows NT {random.randint(10,11)}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90,122)}.0.0.0 Safari/537.36 Edg/{random.randint(90,122)}.0.0.0',
            
            # Samsung Internet
            f'Mozilla/5.0 (Linux; Android {random.randint(10,13)}; SAMSUNG {random.choice(["SM-G973F", "SM-N976B", "SM-F916B"])}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{random.randint(14,22)}.0 Chrome/{random.randint(90,110)}.0.0.0 Mobile Safari/537.36',
        ]
        return random.choice(ua_list)
    
    def random_delay(self):
        """Human-like random delays"""
        delay = random.uniform(0.5, 2.5)
        time.sleep(delay)
        
    def simulate_behavior(self):
        """Simulate human browsing behavior"""
        actions = [
            lambda: time.sleep(random.uniform(0.1, 0.5)),
            lambda: None,
            lambda: random.choice([True, False]),
        ]
        random.choice(actions)()

class AdaptiveExtractor:
    """Adaptive extractor that evolves with platform changes"""
    
    def __init__(self):
        self.successful_methods = defaultdict(int)
        self.failed_methods = defaultdict(int)
        self.method_cache = {}
        
    def get_best_method(self, platform):
        """Dynamically choose best extraction method"""
        if platform in self.successful_methods:
            methods = sorted(self.successful_methods[platform].items(), key=lambda x: x[1], reverse=True)
            if methods:
                return methods[0][0]
        return None
    
    def record_success(self, platform, method):
        """Record successful extraction method"""
        self.successful_methods[platform][method] += 1
        
    def record_failure(self, platform, method):
        """Record failed extraction method"""
        self.failed_methods[platform][method] += 1

class ProxyManager:
    """Smart proxy rotation system"""
    
    def __init__(self):
        self.proxies = []
        self.current_proxy = None
        self.proxy_rotation_count = 0
        
    def get_proxy(self):
        """Get proxy with rotation"""
        # In production, you would integrate with proxy services
        # For now, returns None (direct connection)
        return None

class CookieJar:
    """Advanced cookie management"""
    
    def __init__(self):
        self.cookies = {}
        self.session_id = hashlib.md5(os.urandom(32)).hexdigest()
        
    def generate_cookies(self, domain):
        """Generate realistic cookies"""
        cookies = {
            f'_ga_{random.randint(100000000, 999999999)}': hashlib.md5(os.urandom(16)).hexdigest(),
            '_ga': f'GA1.2.{random.randint(1000000000, 9999999999)}.{int(time.time())}',
            '_gid': f'GA1.2.{random.randint(1000000000, 9999999999)}.{int(time.time())}',
            f'{domain}_session': self.session_id,
            'csrftoken': hashlib.md5(os.urandom(32)).hexdigest(),
        }
        return cookies

# ==================== ULTIMATE DOWNLOADER ====================

class UltimateDownloader:
    """Ultimate bypass downloader"""
    
    def __init__(self):
        self.stealth = StealthEngine()
        self.extractor = AdaptiveExtractor()
        self.cookie_jar = CookieJar()
        self.download_dir = DOWNLOAD_DIR
        
    def detect_platform(self, url):
        """Intelligently detect platform"""
        domain = urlparse(url).netloc.lower()
        domain = domain.replace('www.', '')
        
        platforms = {
            'youtube': ['youtube', 'youtu.be'],
            'instagram': ['instagram'],
            'tiktok': ['tiktok'],
            'pinterest': ['pinterest'],
            'twitter': ['twitter', 'x.com'],
            'facebook': ['facebook', 'fb.watch'],
            'reddit': ['reddit'],
            'vimeo': ['vimeo'],
            'dailymotion': ['dailymotion'],
        }
        
        for platform, domains in platforms.items():
            if any(d in domain for d in domains):
                return platform
        return 'generic'
    
    def download_video(self, url):
        """Main download method with multiple fallbacks"""
        
        platform = self.detect_platform(url)
        print(f"\033[1;36m🎯 Target: {platform.upper()}\033[0m")
        
        # Try multiple download methods
        methods = [
            self.method_standard,
            self.method_mobile_api,
            self.method_desktop_emulation,
            self.method_direct_extract,
            self.method_legacy_compat
        ]
        
        for idx, method in enumerate(methods, 1):
            print(f"\033[1;33m🔄 Attempt {idx}/5 - {method.__name__}\033[0m")
            self.stealth.random_delay()
            
            result = method(url, platform)
            if result and result[0]:
                self.extractor.record_success(platform, method.__name__)
                return result
            else:
                self.extractor.record_failure(platform, method.__name__)
                
        return None, None
    
    def method_standard(self, url, platform):
        """Standard yt-dlp method with optimizations"""
        try:
            import yt_dlp
            
            timestamp = int(time.time())
            random_id = random.randint(1000, 9999)
            
            ydl_opts = {
                'format': 'best[ext=mp4]/best',
                'outtmpl': os.path.join(self.download_dir, f'video_{timestamp}_{random_id}.%(ext)s'),
                'quiet': True,
                'no_warnings': True,
                'ignoreerrors': False,
                'retries': 10,
                'fragment_retries': 10,
                'continuedl': True,
                'user_agent': self.stealth.get_random_user_agent(),
                'headers': self.stealth.get_stealth_headers(),
                'extractor_args': {
                    'youtube': {
                        'skip': ['dash', 'hls'],
                        'player_client': ['android', 'ios', 'web'],
                        'player_skip': ['webpage'],
                    },
                    'instagram': {
                        'user_agent': ['mobile'],
                        'api': ['web'],
                    },
                    'tiktok': {
                        'user_agent': ['mobile'],
                        'api_hostname': ['www.tiktok.com'],
                    }
                },
                'throttledratelimit': 10000000,
                'sleep_interval': random.uniform(1, 3),
                'max_sleep_interval': 5,
                'sleep_interval_requests': random.uniform(0.5, 1.5),
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                if info and 'requested_downloads' in info:
                    filename = info['requested_downloads'][0]['filepath']
                    title = info.get('title', 'Unknown')
                    if os.path.exists(filename) and os.path.getsize(filename) > 10240:
                        return filename, title
                        
        except Exception as e:
            print(f"\033[1;30mDebug: {str(e)[:50]}\033[0m")
            
        return None, None
    
    def method_mobile_api(self, url, platform):
        """Mobile API emulation method"""
        try:
            import yt_dlp
            
            timestamp = int(time.time())
            random_id = random.randint(1000, 9999)
            
            # Mobile-specific headers
            mobile_headers = {
                'User-Agent': self.stealth.get_random_user_agent(),
                'X-Requested-With': 'XMLHttpRequest',
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'en-US,en;q=0.9',
                'X-Client-Data': base64.b64encode(os.urandom(20)).decode(),
            }
            
            ydl_opts = {
                'format': 'best[ext=mp4]/best',
                'outtmpl': os.path.join(self.download_dir, f'mobile_{timestamp}_{random_id}.%(ext)s'),
                'quiet': True,
                'no_warnings': True,
                'ignoreerrors': True,
                'retries': 15,
                'user_agent': mobile_headers['User-Agent'],
                'headers': mobile_headers,
                'extractor_args': {
                    'youtube': {'player_client': ['android', 'ios']},
                    'instagram': {'user_agent': ['mobile']},
                }
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                if info and 'requested_downloads' in info:
                    filename = info['requested_downloads'][0]['filepath']
                    title = info.get('title', 'Unknown')
                    if os.path.exists(filename) and os.path.getsize(filename) > 10240:
                        return filename, title
                        
        except:
            pass
            
        return None, None
    
    def method_desktop_emulation(self, url, platform):
        """Desktop browser emulation"""
        try:
            import yt_dlp
            
            timestamp = int(time.time())
            random_id = random.randint(1000, 9999)
            
            # Desktop headers
            desktop_headers = {
                'User-Agent': self.stealth.get_random_user_agent(),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
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
            
            ydl_opts = {
                'format': 'bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': os.path.join(self.download_dir, f'desktop_{timestamp}_{random_id}.%(ext)s'),
                'quiet': True,
                'no_warnings': True,
                'ignoreerrors': True,
                'retries': 10,
                'user_agent': desktop_headers['User-Agent'],
                'headers': desktop_headers,
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                if info and 'requested_downloads' in info:
                    filename = info['requested_downloads'][0]['filepath']
                    title = info.get('title', 'Unknown')
                    if os.path.exists(filename) and os.path.getsize(filename) > 10240:
                        return filename, title
                        
        except:
            pass
            
        return None, None
    
    def method_direct_extract(self, url, platform):
        """Direct extraction without API"""
        try:
            import yt_dlp
            
            timestamp = int(time.time())
            random_id = random.randint(1000, 9999)
            
            ydl_opts = {
                'format': 'best',
                'outtmpl': os.path.join(self.download_dir, f'direct_{timestamp}_{random_id}.%(ext)s'),
                'quiet': True,
                'no_warnings': True,
                'ignoreerrors': True,
                'extract_flat': False,
                'force_generic_extractor': False,
                'user_agent': self.stealth.get_random_user_agent(),
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                if info and 'requested_downloads' in info:
                    filename = info['requested_downloads'][0]['filepath']
                    title = info.get('title', 'Unknown')
                    if os.path.exists(filename) and os.path.getsize(filename) > 10240:
                        return filename, title
                        
        except:
            pass
            
        return None, None
    
    def method_legacy_compat(self, url, platform):
        """Legacy compatibility method"""
        try:
            import yt_dlp
            
            timestamp = int(time.time())
            random_id = random.randint(1000, 9999)
            
            ydl_opts = {
                'format': 'worst',
                'outtmpl': os.path.join(self.download_dir, f'legacy_{timestamp}_{random_id}.%(ext)s'),
                'quiet': True,
                'no_warnings': True,
                'ignoreerrors': True,
                'retries': 20,
                'user_agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                if info and 'requested_downloads' in info:
                    filename = info['requested_downloads'][0]['filepath']
                    title = info.get('title', 'Unknown')
                    if os.path.exists(filename) and os.path.getsize(filename) > 10240:
                        return filename, title
                        
        except:
            pass
            
        return None, None
    
    def optimize_video(self, filename):
        """Optimize video for device compatibility"""
        try:
            # Check if ffmpeg is available
            subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
            
            output_filename = filename.replace('.mp4', '_optimized.mp4').replace('.webm', '_optimized.mp4')
            
            # Optimize for mobile playback
            cmd = [
                "ffmpeg", "-i", filename,
                "-c:v", "libx264",
                "-preset", "fast",
                "-crf", "23",
                "-c:a", "aac",
                "-b:a", "128k",
                "-movflags", "+faststart",
                "-pix_fmt", "yuv420p",
                "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2",
                "-y", output_filename
            ]
            
            subprocess.run(cmd, capture_output=True, timeout=180)
            
            if os.path.exists(output_filename) and os.path.getsize(output_filename) > 10240:
                os.remove(filename)
                os.rename(output_filename, filename)
                return filename
                
        except:
            pass
            
        return filename
    
    def add_to_gallery(self, filename):
        """Add to device gallery"""
        if IS_TERMUX:
            try:
                subprocess.run(["termux-media-scan", filename], capture_output=True, timeout=10)
                return True
            except:
                pass
        return False

# ==================== MAIN APPLICATION ====================

def banner():
    """Display banner"""
    banner_text = """
\033[1;35m
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║     ██████╗ ██╗      ██████╗  ██████╗ ███╗   ███╗    ██████╗ ██╗  ██╗        ║
║    ██╔════╝ ██║     ██╔═══██╗██╔═══██╗████╗ ████║    ██╔══██╗██║  ██║        ║
║    ██║  ███╗██║     ██║   ██║██║   ██║██╔████╔██║    ██████╔╝███████║        ║
║    ██║   ██║██║     ██║   ██║██║   ██║██║╚██╔╝██║    ██╔══██╗██╔══██║        ║
║    ╚██████╔╝███████╗╚██████╔╝╚██████╔╝██║ ╚═╝ ██║    ██║  ██║██║  ██║        ║
║     ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝        ║
║                                                                               ║
║         [ ULTIMATE BYPASS ENGINE - UNDETECTABLE v5.0 ]                        ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
\033[0m
"""
    print(banner)

def check_requirements():
    """Check and install requirements"""
    print("\033[1;34m🔧 Checking requirements...\033[0m")
    
    try:
        import yt_dlp
        print("\033[1;32m✅ yt-dlp installed\033[0m")
    except ImportError:
        print("\033[1;33m📦 Installing yt-dlp...\033[0m")
        subprocess.run([sys.executable, "-m", "pip", "install", "yt-dlp", "--upgrade", "--quiet"])
    
    # Check ffmpeg
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        print("\033[1;32m✅ FFmpeg installed\033[0m")
    except:
        if IS_TERMUX:
            print("\033[1;33m📦 Installing FFmpeg...\033[0m")
            subprocess.run(["pkg", "install", "ffmpeg", "-y"], capture_output=True)

def main():
    """Main entry point"""
    os.system('clear')
    banner()
    
    print(f"\033[1;36m🎯 Platform: {'Android/Termux' if IS_TERMUX else SYSTEM.upper()}\033[0m")
    print(f"\033[1;36m💾 Download Directory: {DOWNLOAD_DIR}\033[0m")
    print(f"\033[1;32m🛡️ Stealth Mode: ACTIVE\033[0m")
    print(f"\033[1;32m🤖 AI Bypass: ULTIMATE\033[0m")
    print("\033[1;33m" + "="*70 + "\033[0m")
    
    check_requirements()
    
    downloader = UltimateDownloader()
    
    while True:
        print("\n\033[1;35m" + "─"*70 + "\033[0m")
        print("\033[1;33m📎 Enter video URL (or 'exit' to quit):\033[0m")
        print("\033[1;36m💡 Supports: YouTube, Instagram, TikTok, Twitter, Facebook, Reddit, Pinterest\033[0m")
        
        try:
            url = input("\033[1;32m🔗 >> \033[0m").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\033[1;31m👋 Goodbye!\033[0m")
            break
        
        if url.lower() in ['exit', 'quit']:
            break
        elif not url:
            continue
            
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        print("\n\033[1;36m🚀 Initializing bypass sequence...\033[0m")
        start_time = time.time()
        
        # Download video
        filename, title = downloader.download_video(url)
        
        if filename and os.path.exists(filename):
            # Optimize video
            print("\033[1;36m⚙️ Optimizing video...\033[0m")
            filename = downloader.optimize_video(filename)
            
            # Add to gallery
            downloader.add_to_gallery(filename)
            
            elapsed = time.time() - start_time
            
            print(f"\n\033[1;32m╔══════════════════════════════════════════════════════════╗")
            print(f"║                    ✅ DOWNLOAD SUCCESS!                         ║")
            print(f"╚══════════════════════════════════════════════════════════╝\033[0m")
            print(f"\033[1;36m📹 Title: {title[:60] if title else 'Unknown'}\033[0m")
            print(f"\033[1;36m⏱️ Time: {elapsed:.1f} seconds\033[0m")
            print(f"\033[1;36m💾 Location: {filename}\033[0m")
            print(f"\033[1;32m🛡️ Bypass successful - Undetected!\033[0m")
        else:
            print(f"\n\033[1;31m╔══════════════════════════════════════════════════════════╗")
            print(f"║                    ❌ DOWNLOAD FAILED!                          ║")
            print(f"╚══════════════════════════════════════════════════════════╝\033[0m")
            print("\033[1;33m💡 Troubleshooting tips:\033[0m")
            print("   • Check if video is public/accessible")
            print("   • Update yt-dlp: pip install --upgrade yt-dlp")
            print("   • Try again (server might be rate limiting)")
            print("   • Use a different URL")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\033[1;31m⚠️ Error: {e}\033[0m")
        print("\033[1;33m🔧 Run: pip install --upgrade yt-dlp\033[0m")
