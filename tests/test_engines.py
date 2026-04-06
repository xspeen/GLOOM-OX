#!/usr/bin/env python3
"""
Tests for GLOOM-OX Extraction Engines
"""

import unittest
from unittest.mock import patch, Mock, MagicMock

class TestYouTubeEngine(unittest.TestCase):
    """Test YouTube extraction engine"""
    
    @patch('yt_dlp.YoutubeDL')
    def test_aggressive_extraction(self, mock_ydl):
        """Test aggressive extraction method"""
        from gloom_ox.core.youtube_engine import YouTubeEngineUnleashed
        
        # Mock yt-dlp response
        mock_instance = Mock()
        mock_instance.__enter__ = Mock()
        mock_instance.__exit__ = Mock()
        mock_instance.extract_info.return_value = {'title': 'Test Video'}
        mock_ydl.return_value = mock_instance
        
        engine = YouTubeEngineUnleashed()
        
        # Test with a URL
        with patch('os.path.exists', return_value=True):
            with patch('gloom_ox.core.youtube_engine.verify_video_integrity', return_value=True):
                result = engine._aggressive_extraction(
                    "https://youtube.com/watch?v=test", 
                    "/tmp/test"
                )
                
                # Should return (file_path, title) or (None, None)
                self.assertIsInstance(result, tuple)
    
    def test_progress_hook(self):
        """Test progress hook functionality"""
        from gloom_ox.core.youtube_engine import YouTubeEngineUnleashed
        
        engine = YouTubeEngineUnleashed()
        
        # Test downloading status
        hook_data = {'status': 'downloading', '_percent_str': '50%', '_speed_str': '1.2MB/s', '_eta_str': '10s'}
        try:
            engine._progress_hook(hook_data)
        except Exception as e:
            self.fail(f"Progress hook failed: {e}")
        
        # Test finished status
        hook_data = {'status': 'finished'}
        try:
            engine._progress_hook(hook_data)
        except Exception as e:
            self.fail(f"Progress hook failed: {e}")


class TestSocialEngine(unittest.TestCase):
    """Test social media extraction engine"""
    
    def test_platform_routing(self):
        """Test platform routing logic"""
        from gloom_ox.core.social_engine import SocialMediaEngineUnleashed
        
        engine = SocialMediaEngineUnleashed()
        
        # Mock the individual methods
        engine._pinterest_unleashed = Mock(return_value=("path.mp4", "Pinterest"))
        engine._instagram_unleashed = Mock(return_value=("path.mp4", "Instagram"))
        engine._tiktok_unleashed = Mock(return_value=("path.mp4", "TikTok"))
        engine._universal_unleashed = Mock(return_value=("path.mp4", "Universal"))
        
        # Test Pinterest
        engine.extract("https://pinterest.com/pin/123")
        engine._pinterest_unleashed.assert_called_once()
        
        # Reset and test Instagram
        engine._pinterest_unleashed.reset_mock()
        engine.extract("https://instagram.com/p/123")
        engine._instagram_unleashed.assert_called_once()
        
        # Test TikTok
        engine._instagram_unleashed.reset_mock()
        engine.extract("https://tiktok.com/@user/video/123")
        engine._tiktok_unleashed.assert_called_once()
        
        # Test unknown (should use universal)
        engine._tiktok_unleashed.reset_mock()
        engine.extract("https://unknown.com/video")
        engine._universal_unleashed.assert_called_once()
    
    def test_youtube_shorts_conversion(self):
        """Test YouTube Shorts URL conversion"""
        from gloom_ox.core.social_engine import SocialMediaEngineUnleashed
        
        engine = SocialMediaEngineUnleashed()
        
        shorts_url = "https://youtube.com/shorts/abc123xyz"
        
        with patch('gloom_ox.core.social_engine.YouTubeEngineUnleashed') as mock_yt:
            mock_instance = Mock()
            mock_instance.extract.return_value = ("path.mp4", "Short Video")
            mock_yt.return_value = mock_instance
            
            engine._youtube_shorts_unleashed(shorts_url)
            
            # Verify the conversion happened
            mock_instance.extract.assert_called_once()
            call_args = mock_instance.extract.call_args[0][0]
            self.assertIn("watch?v=", call_args)
            self.assertIn("abc123xyz", call_args)


if __name__ == '__main__':
    unittest.main()
