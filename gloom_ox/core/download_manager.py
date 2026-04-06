#!/usr/bin/env python3
"""
GLOOM-OX Core Download Manager - Enterprise Grade
"""

import os
import time
import shutil
from datetime import datetime
from pathlib import Path

from gloom_ox.core.youtube_engine import YouTubeEngineUnleashed
from gloom_ox.core.social_engine import SocialMediaEngineUnleashed
from gloom_ox.utils.integrity import verify_video_integrity, ensure_ffmpeg
from gloom_ox.utils.paths import EXP_LINK_DIR, DCIM_PATH, IS_TERMUX
from gloom_ox.config.settings import VERSION, AUTHOR


class DownloadManagerUnleashed:
    """NO LIMITS download manager - Enterprise Grade"""
    
    def __init__(self):
        self.youtube_engine = YouTubeEngineUnleashed()
        self.social_engine = SocialMediaEngineUnleashed()
        self.history = []
        self.bypass_attempts = 0
        
    def download(self, url):
        """Main download entry - NO ERRORS, NO LIMITS"""
        print(f"\033[1;33m[+] PROCESSING: {url[:80]}...\033[0m")
        
        # URL validation FIXED - accept any URL format
        if not url.startswith(('http://', 'https://')):
            if 'youtu.be' in url or 'youtube.com' in url:
                url = 'https://' + url.lstrip('/')
            else:
                url = 'https://' + url
        
        # Detect platform
        url_lower = url.lower()
        
        if any(domain in url_lower for domain in ['youtube.com', 'youtu.be']):
            file_path, title = self.youtube_engine.extract(url)
        else:
            file_path, title = self.social_engine.extract(url)
        
        if file_path and os.path.exists(file_path):
            # Verify integrity
            if not verify_video_integrity(file_path):
                print(f"\033[1;33m[~] File integrity check - attempting auto-repair\033[0m")
                if ensure_ffmpeg():
                    try:
                        from gloom_ox.utils.integrity import repair_video
                        file_path = repair_video(file_path)
                    except:
                        pass
            
            # Final processing
            final_path = self._finalize_file(file_path, title)
            
            if final_path:
                self.history.append({
                    'url': url,
                    'file': final_path,
                    'title': title,
                    'time': time.time(),
                })
                
                return final_path, title
        
        print(f"\033[1;31m[!] EXTRACTION FAILED - Trying alternative methods...\033[0m")
        return self._last_resort_download(url)
    
    def download_with_bypass(self, url):
        """Download with enhanced bypass protocols"""
        self.bypass_attempts += 1
        print(f"\033[1;35m[+] BYPASS ATTEMPT #{self.bypass_attempts}\033[0m")
        
        # Aggressive bypass mode
        from gloom_ox.core.universal_engine import UniversalEngineUnleashed
        engine = UniversalEngineUnleashed()
        return engine.aggressive_extract(url)
    
    def _finalize_file(self, file_path, title):
        """Finalize downloaded file"""
        if not os.path.exists(file_path):
            return None
        
        # Clean title
        clean_title = re.sub(r'[^\w\s-]', '', str(title))
        clean_title = clean_title.replace(' ', '_')[:50]
        
        # Get extension
        ext = os.path.splitext(file_path)[1]
        if not ext:
            ext = '.mp4'
        
        # Final filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        final_name = f"GLOOMOX_{clean_title}_{timestamp}{ext}"
        final_path = os.path.join(EXP_LINK_DIR, final_name)
        
        # Move file
        try:
            shutil.move(file_path, final_path)
        except:
            shutil.copy2(file_path, final_path)
            os.remove(file_path)
        
        # Save to gallery if Termux
        if IS_TERMUX:
            try:
                gallery_path = os.path.join(DCIM_PATH, final_name)
                shutil.copy2(final_path, gallery_path)
                import subprocess
                subprocess.run(["termux-media-scan", gallery_path], capture_output=True)
                print(f"\033[1;32m[✓] Saved to Gallery: {final_name}\033[0m")
            except:
                pass
        
        print(f"\033[1;32m[✓] File saved: {final_name}\033[0m")
        print(f"\033[1;32m[✓] Size: {os.path.getsize(final_path) // 1024}KB\033[0m")
        
        return final_path
    
    def _last_resort_download(self, url):
        """Last resort download method"""
        try:
            import requests
            from gloom_ox.utils.headers import get_random_headers
            
            print(f"\033[1;31m[!] LAST RESORT: Direct download attempt\033[0m")
            
            headers = get_random_headers()
            response = requests.get(url, headers=headers, stream=True, timeout=30)
            
            timestamp = int(time.time())
            file_path = os.path.join(EXP_LINK_DIR, f"direct_{timestamp}.mp4")
            
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            
            if os.path.exists(file_path) and os.path.getsize(file_path) > 1024:
                final_path = self._finalize_file(file_path, "Direct_Download")
                return final_path, "Direct_Download"
                
        except Exception as e:
            print(f"\033[1;31m[!] Last resort failed: {e}\033[0m")
        
        return None, None


# Add missing import
import re
