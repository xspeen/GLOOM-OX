#!/usr/bin/env python3
"""
Universal Engine - Last resort extraction
"""

import os
import time
import random

from gloom_ox.utils.headers import get_random_headers
from gloom_ox.utils.integrity import verify_video_integrity
from gloom_ox.utils.paths import EXP_LINK_DIR


class UniversalEngineUnleashed:
    """Universal extraction engine for difficult content"""
    
    def aggressive_extract(self, url):
        """Aggressive extraction with multiple methods"""
        
        # Method 1: Try with different user agents
        for _ in range(5):
            result = self._try_extract(url, method='ua_rotation')
            if result and result[0]:
                return result
        
        # Method 2: Try with different referers
        result = self._try_extract(url, method='referer_spoof')
        if result and result[0]:
            return result
        
        # Method 3: Direct download attempt
        return self._direct_download(url)
    
    def _try_extract(self, url, method='default'):
        """Try extraction with specific method"""
        try:
            import yt_dlp
            
            timestamp = int(time.time())
            random_id = random.randint(1000, 9999)
            output_template = os.path.join(EXP_LINK_DIR, f"aggressive_{timestamp}_{random_id}.%(ext)s")
            
            opts = {
                'format': 'best',
                'outtmpl': output_template,
                'ignoreerrors': True,
                'no_warnings': True,
                'quiet': True,
                'retries': 20,
                'socket_timeout': 30,
            }
            
            if method == 'ua_rotation':
                opts['user_agent'] = get_random_headers()['User-Agent']
            elif method == 'referer_spoof':
                opts['referer'] = 'https://www.google.com/'
            
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
                
                # Find downloaded file
                for ext in ['.mp4', '.mkv', '.webm', '.mp3', '.jpg']:
                    possible = output_template.replace('%(ext)s', ext.lstrip('.'))
                    if os.path.exists(possible) and verify_video_integrity(possible):
                        return possible, info.get('title', 'Extracted_Content')
                        
        except Exception:
            pass
        
        return None, None
    
    def _direct_download(self, url):
        """Direct download as last resort"""
        try:
            import requests
            
            timestamp = int(time.time())
            file_path = os.path.join(EXP_LINK_DIR, f"direct_{timestamp}.mp4")
            
            headers = get_random_headers()
            response = requests.get(url, headers=headers, stream=True, timeout=30)
            
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            
            if os.path.exists(file_path) and os.path.getsize(file_path) > 1024:
                return file_path, "Direct_Download"
                
        except Exception:
            pass
        
        return None, None
