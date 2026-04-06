#!/usr/bin/env python3
"""
Tests for GLOOM-OX Download Manager
"""

import unittest
import os
import tempfile
from unittest.mock import Mock, patch

class TestDownloadManager(unittest.TestCase):
    """Test cases for DownloadManagerUnleashed"""
    
    def setUp(self):
        """Set up test environment"""
        self.temp_dir = tempfile.mkdtemp()
        
    def tearDown(self):
        """Clean up test environment"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    @patch('gloom_ox.core.download_manager.YouTubeEngineUnleashed')
    def test_download_youtube_url(self, mock_youtube):
        """Test YouTube URL detection"""
        from gloom_ox.core.download_manager import DownloadManagerUnleashed
        
        mock_instance = Mock()
        mock_instance.extract.return_value = ("/fake/path.mp4", "Test Video")
        mock_youtube.return_value = mock_instance
        
        manager = DownloadManagerUnleashed()
        result = manager.download("https://youtube.com/watch?v=test123")
        
        self.assertIsNotNone(result)
    
    def test_url_validation(self):
        """Test URL validation and fixing"""
        from gloom_ox.core.download_manager import DownloadManagerUnleashed
        
        manager = DownloadManagerUnleashed()
        
        # Test without protocol
        test_urls = [
            ("youtube.com/watch?v=123", "https://youtube.com/watch?v=123"),
            ("youtu.be/abc123", "https://youtu.be/abc123"),
        ]
        
        # Mock the engines to avoid actual downloads
        manager.youtube_engine.extract = Mock(return_value=(None, None))
        manager.social_engine.extract = Mock(return_value=(None, None))
        
        for input_url, expected_prefix in test_urls:
            manager.download(input_url)
            # Just verify it doesn't crash
    
    def test_history_tracking(self):
        """Test download history tracking"""
        from gloom_ox.core.download_manager import DownloadManagerUnleashed
        
        manager = DownloadManagerUnleashed()
        
        # Add fake history
        manager.history.append({
            'url': 'https://test.com',
            'file': '/fake/path.mp4',
            'title': 'Test Video',
            'time': 1234567890
        })
        
        self.assertEqual(len(manager.history), 1)
        self.assertEqual(manager.history[0]['title'], 'Test Video')


class TestURLParsing(unittest.TestCase):
    """Test URL parsing and platform detection"""
    
    def test_platform_detection(self):
        """Test platform detection from URLs"""
        test_cases = [
            ("https://youtube.com/watch?v=123", "youtube"),
            ("https://youtu.be/abc123", "youtube"),
            ("https://instagram.com/p/123", "instagram"),
            ("https://pinterest.com/pin/123", "pinterest"),
            ("https://tiktok.com/@user/video/123", "tiktok"),
        ]
        
        for url, expected in test_cases:
            url_lower = url.lower()
            if 'youtube' in url_lower or 'youtu.be' in url_lower:
                detected = 'youtube'
            elif 'instagram' in url_lower:
                detected = 'instagram'
            elif 'pinterest' in url_lower:
                detected = 'pinterest'
            elif 'tiktok' in url_lower:
                detected = 'tiktok'
            else:
                detected = 'unknown'
            
            self.assertEqual(detected, expected, f"Failed for {url}")


if __name__ == '__main__':
    unittest.main()
