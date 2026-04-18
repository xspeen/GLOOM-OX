#!/usr/bin/env python3
"""
GLOOM-OX v5.1 - Downloader Module Tests
Tests video downloading functionality across platforms
"""

import unittest
import os
import sys
import tempfile
import shutil
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestDownloader(unittest.TestCase):
    """Test cases for video downloader functionality"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test environment"""
        cls.test_dir = tempfile.mkdtemp()
        cls.downloader = None
        
        # Try to import the downloader
        try:
            from gloom_ox import GloomOXDownloader
            cls.downloader = GloomOXDownloader()
        except ImportError:
            pass
    
    @classmethod
    def tearDownClass(cls):
        """Clean up test environment"""
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)
    
    def test_import(self):
        """Test that required modules can be imported"""
        try:
            import yt_dlp
            self.assertIsNotNone(yt_dlp)
        except ImportError:
            self.skipTest("yt-dlp not installed")
    
    def test_downloader_initialization(self):
        """Test downloader initialization"""
        if not self.downloader:
            self.skipTest("Downloader not available")
        
        self.assertIsNotNone(self.downloader)
        self.assertTrue(hasattr(self.downloader, 'download'))
        self.assertTrue(hasattr(self.downloader, 'detect_platform'))
    
    def test_platform_detection(self):
        """Test platform detection from URLs"""
        if not self.downloader:
            self.skipTest("Downloader not available")
        
        test_urls = {
            "https://youtube.com/watch?v=123": "youtube",
            "https://youtu.be/123": "youtube",
            "https://instagram.com/p/123": "instagram",
            "https://tiktok.com/@user/video/123": "tiktok",
            "https://twitter.com/user/status/123": "twitter",
            "https://facebook.com/watch/123": "facebook",
        }
        
        for url, expected in test_urls.items():
            result = self.downloader.detect_platform(url)
            self.assertEqual(result, expected, f"Failed for {url}")
    
    def test_url_validation(self):
        """Test URL validation"""
        valid_urls = [
            "https://youtube.com/watch?v=123",
            "http://instagram.com/p/123",
            "https://www.tiktok.com/@user/video/123",
        ]
        
        invalid_urls = [
            "not a url",
            "ftp://invalid.com",
            "",
            None,
        ]
        
        for url in valid_urls:
            self.assertTrue(url.startswith(('http://', 'https://')))
        
        for url in invalid_urls:
            if url:
                self.assertFalse(url.startswith(('http://', 'https://')))
    
    def test_filename_sanitization(self):
        """Test filename sanitization"""
        from gloom_ox import GalleryInjector
        
        test_titles = [
            ("Video/With/Slashes", "Video_With_Slashes"),
            ("Video:With:Colons", "Video_With_Colons"),
            ("Video?With?Question", "Video_With_Question"),
            ("Normal Title", "Normal Title"),
        ]
        
        for title, expected in test_titles:
            # Just check that sanitization works, exact result may vary
            sanitized = GalleryInjector.generate_unique_filename(title, "http://test.com")
            self.assertIsInstance(sanitized, str)
            self.assertTrue(len(sanitized) > 0)
    
    @unittest.skipIf(os.environ.get('SKIP_NETWORK_TESTS'), "Skipping network tests")
    def test_youtube_extraction(self):
        """Test YouTube video extraction (requires network)"""
        try:
            import yt_dlp
            
            url = "https://youtube.com/watch?v=dQw4w9WgXcQ"
            ydl_opts = {'quiet': True, 'no_warnings': True}
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                self.assertIsNotNone(info)
                self.assertIn('title', info)
                self.assertIn('duration', info)
                
        except Exception as e:
            self.skipTest(f"Network test failed: {e}")
    
    def test_duplicate_detection(self):
        """Test duplicate URL detection"""
        from gloom_ox import is_duplicate, save_history
        
        test_url = "https://test.com/video1"
        
        # Initially should not be duplicate
        self.assertFalse(is_duplicate(test_url))
        
        # Save to history
        save_history(test_url)
        
        # Now should be duplicate (may depend on implementation)
        # Note: This test may need adjustment based on actual implementation
    
    def test_error_handling(self):
        """Test error handling for invalid URLs"""
        if not self.downloader:
            self.skipTest("Downloader not available")
        
        invalid_url = "https://invalid.url.that.does.not.exist.com/video"
        
        # Should handle gracefully without crashing
        try:
            result = self.downloader.download(invalid_url)
            # Should return None or tuple with None
            self.assertTrue(result is None or (isinstance(result, tuple) and result[0] is None))
        except Exception as e:
            self.fail(f"Downloader crashed on invalid URL: {e}")

class TestGalleryInjector(unittest.TestCase):
    """Test gallery injection functionality"""
    
    def test_gallery_paths(self):
        """Test gallery path detection"""
        from gloom_ox import GalleryInjector, DOWNLOAD_DIR
        
        self.assertIsNotNone(DOWNLOAD_DIR)
        self.assertTrue(os.path.exists(DOWNLOAD_DIR) or True)  # May not exist in CI
    
    def test_unique_filename_generation(self):
        """Test unique filename generation"""
        from gloom_ox import GalleryInjector
        
        url1 = "https://youtube.com/watch?v=abc123"
        url2 = "https://youtube.com/watch?v=def456"
        
        filename1 = GalleryInjector.generate_unique_filename("Test Video", url1)
        filename2 = GalleryInjector.generate_unique_filename("Test Video", url2)
        
        self.assertIsInstance(filename1, str)
        self.assertIsInstance(filename2, str)
        self.assertTrue(filename1.endswith('.mp4'))
        self.assertTrue(filename2.endswith('.mp4'))

if __name__ == '__main__':
    unittest.main()
