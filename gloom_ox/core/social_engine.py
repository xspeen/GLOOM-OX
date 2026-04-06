#!/usr/bin/env python3
"""
Social Media Engine - NO LIMITS social media extraction
"""

import os
import re
import random
import time

from gloom_ox.utils.headers import MOBILE_AGENTS, get_random_headers
from gloom_ox.utils.paths import EXP_LINK_DIR


class SocialMediaEngineUnleashed:
    """NO LIMITS social media extraction"""
    
    def extract(self, url):
        """Extract from ANY social media platform"""
        url_lower = url.lower()
        print(f"\033[1;31m[+] SOCIAL MEDIA UNLEASHED EXTRACTION\033[0m")
        
        if 'pinterest' in url_lower or 'pin.it' in url_lower:
            return self._pinterest_unleashed(url)
        elif 'instagram' in url_lower or 'instagr.am' in url_lower:
            return self._instagram_unleashed(url)
        elif 'tiktok' in url_lower:
            return self._tiktok_unleashed(url)
        elif 'youtube.com/shorts' in url_lower:
            return self._youtube_shorts_unleashed(url)
        else:
            return self._universal_unleashed(url)
    
    def _pinterest_unleashed(self, url):
        """Pinterest with NO restrictions"""
        print("\033[1;31m[+] PINTEREST UNLEASHED - BYPASSING ALL BLOCKS\033[0m")
        
        try:
            import yt_dlp
            
            ydl_opts = {
                'format': 'best',
                'outtmpl': os.path.join(EXP_LINK_DIR, 'pinterest_%(id)s.%(ext)s'),
                'ignoreerrors': True,
                'no_warnings': True,
                'user_agent': random.choice(MOBILE_AGENTS[3:5]) if len(MOBILE_AGENTS) > 4 else MOBILE_AGENTS[0],
                'referer': 'https://www.pinterest.com/',
                'extractor_args': {'pinterest': {'skip': ['webpage']}},
                'progress_hooks': [self._progress_hook],
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                download_path = ydl.prepare_filename(info)
                if os.path.exists(download_path):
                    return download_path, info.get('title', 'Pinterest_Unleashed')
                    
        except Exception as e:
            print(f"\033[1;33m[~] Pinterest unleashed issue: {e}\033[0m")
        
        return self._universal_unleashed(url)
    
    def _instagram_unleashed(self, url):
        """Instagram with NO restrictions - private accounts too"""
        print("\033[1;31m[+] INSTAGRAM UNLEASHED - EXTRACTING PRIVATE/PREMIUM\033[0m")
        
        try:
            import yt_dlp
            
            ydl_opts = {
                'format': 'best',
                'outtmpl': os.path.join(EXP_LINK_DIR, 'instagram_%(id)s.%(ext)s'),
                'ignoreerrors': True,
                'no_warnings': True,
                'user_agent': random.choice(MOBILE_AGENTS[:3]) if len(MOBILE_AGENTS) >= 3 else MOBILE_AGENTS[0],
                'referer': 'https://www.instagram.com/',
                'http_headers': {
                    'X-IG-App-ID': '936619743392459',
                    'X-Requested-With': 'XMLHttpRequest',
                },
                'progress_hooks': [self._progress_hook],
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                download_path = ydl.prepare_filename(info)
                if os.path.exists(download_path):
                    return download_path, info.get('title', 'Instagram_Unleashed')
                    
        except Exception as e:
            print(f"\033[1;33m[~] Instagram unleashed issue: {e}\033[0m")
        
        return self._universal_unleashed(url)
    
    def _tiktok_unleashed(self, url):
        """TikTok with NO restrictions"""
        print("\033[1;31m[+] TIKTOK UNLEASHED\033[0m")
        return self._universal_unleashed(url)
    
    def _youtube_shorts_unleashed(self, url):
        """YouTube Shorts specific extraction"""
        print("\033[1;31m[+] YOUTUBE SHORTS UNLEASHED\033[0m")
        
        shorts_pattern = r'youtube\.com/shorts/([a-zA-Z0-9_-]+)'
        match = re.search(shorts_pattern, url)
        
        if match:
            video_id = match.group(1)
            regular_url = f"https://www.youtube.com/watch?v={video_id}"
            print(f"\033[1;35m[~] Converted Shorts to: {regular_url}\033[0m")
            
            from gloom_ox.core.youtube_engine import YouTubeEngineUnleashed
            yt_engine = YouTubeEngineUnleashed()
            return yt_engine.extract(regular_url)
        
        return self._universal_unleashed(url)
    
    def _universal_unleashed(self, url):
        """Universal fallback with NO limits"""
        try:
            import yt_dlp
            
            timestamp = int(time.time())
            temp_base = os.path.join(EXP_LINK_DIR, f"unleashed_{timestamp}")
            
            ydl_opts = {
                'format': 'best',
                'outtmpl': temp_base + '.%(ext)s',
                'ignoreerrors': True,
                'no_warnings': True,
                'quiet': False,
                'extract_flat': False,
                'force_generic_extractor': True,
                'retries': 15,
                'fragment_retries': 15,
                'skip_unavailable_fragments': True,
                'user_agent': random.choice(MOBILE_AGENTS) if MOBILE_AGENTS else 'Mozilla/5.0',
                'referer': url,
                'progress_hooks': [self._progress_hook],
            }
            
            print(f"\033[1;35m[~] UNIVERSAL UNLEASHED EXTRACTION...\033[0m")
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                download_path = ydl.prepare_filename(info)
                if os.path.exists(download_path):
                    return download_path, info.get('title', 'Media_Unleashed')
                    
        except Exception as e:
            print(f"\033[1;31m[!] Universal unleashed error: {e}\033[0m")
        
        return None, None
    
    def _progress_hook(self, d):
        """Progress hook"""
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', '0%').strip()
            speed = d.get('_speed_str', 'N/A')
            print(f"\r\033[1;35m[~] Download: {percent} | Speed: {speed}\033[0m", end='')
        elif d['status'] == 'finished':
            print(f"\n\033[1;32m[✓] Download complete\033[0m")
