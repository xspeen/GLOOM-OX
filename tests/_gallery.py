#!/usr/bin/env python3
"""
GLOOM-OX v5.1 - Gallery Injection Tests
Tests gallery injection functionality across platforms
"""

import unittest
import sys
import os
import tempfile
import shutil
from unittest.mock import Mock, patch, MagicMock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestGalleryInjection(unittest.TestCase):
    """Test gallery injection functionality"""
    
    def setUp(self):
        """Set up test environment"""
        self.temp_dir = tempfile.mkdtemp()
        
        try:
            from gloom_ox import GalleryInjector
            self.injector = GalleryInjector
        except ImportError:
            self.injector = None
    
    def tearDown(self):
        """Clean up test environment"""
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
    
    def test_injector_initialization(self):
        """Test gallery injector initialization"""
        if not self.injector:
            self.skipTest("GalleryInjector not available")
        
        self.assertIsNotNone(self.injector)
        self.assertTrue(hasattr(self.injector, 'inject_to_gallery'))
        self.assertTrue(hasattr(self.injector, 'generate_unique_filename'))
    
    def test_unique_filename(self):
        """Test unique filename generation"""
        if not self.injector:
            self.skipTest("GalleryInjector not available")
        
        url = "https://youtube.com/watch?v=abc123"
        title = "Test Video Title"
        
        filename = self.injector.generate_unique_filename(title, url)
        
        self.assertIsInstance(filename, str)
        self.assertTrue(filename.endswith('.mp4'))
        self.assertIn('GLOOM', filename.upper())
    
    def test_filename_uniqueness(self):
        """Test that different URLs generate different filenames"""
        if not self.injector:
            self.skipTest("GalleryInjector not available")
        
        url1 = "https://youtube.com/watch?v=abc123"
        url2 = "https://youtube.com/watch?v=def456"
        title = "Same Title"
        
        filename1 = self.injector.generate_unique_filename(title, url1)
        filename2 = self.injector.generate_unique_filename(title, url2)
        
        # Should be different due to URL hash
        self.assertNotEqual(filename1, filename2)
    
    def test_filename_sanitization(self):
        """Test filename sanitization removes invalid characters"""
        if not self.injector:
            self.skipTest("GalleryInjector not available")
        
        title = "Video/With:Invalid?Chars*<"
        url = "https://test.com"
        
        filename = self.injector.generate_unique_filename(title, url)
        
        # Should not contain invalid characters
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            self.assertNotIn(char, filename)
    
    @unittest.skipIf(os.name == 'nt', "Unix-specific test")
    def test_injection_methods(self):
        """Test that injection methods exist"""
        if not self.injector:
            self.skipTest("GalleryInjector not available")
        
        # Check for multiple injection methods
        methods = [
            'inject_to_gallery',
            'optimize_for_gallery',
            'copy_to_multiple_locations',
        ]
        
        for method in methods:
            self.assertTrue(hasattr(self.injector, method))

class TestVideoOptimization(unittest.TestCase):
    """Test video optimization"""
    
    def test_ffmpeg_check(self):
        """Test FFmpeg availability check"""
        import subprocess
        
        try:
            result = subprocess.run(
                ["ffmpeg", "-version"],
                capture_output=True,
                timeout=5
            )
            ffmpeg_available = result.returncode == 0
        except:
            ffmpeg_available = False
        
        # Just log, don't assert (FFmpeg is optional)
        if ffmpeg_available:
            print("\n✓ FFmpeg available for optimization")
        else:
            print("\n⚠️ FFmpeg not available")
    
    def test_optimization_command(self):
        """Test that optimization command is properly formed"""
        from gloom_ox import optimize_video
        
        # Test function exists
        self.assertTrue(callable(optimize_video))

if __name__ == '__main__':
    unittest.main()
