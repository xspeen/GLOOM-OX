#!/usr/bin/env python3
"""
Tests for file integrity verification
"""

import unittest
import os
import tempfile
import shutil

class TestIntegrity(unittest.TestCase):
    """Test file integrity functions"""
    
    def setUp(self):
        """Create test files"""
        self.temp_dir = tempfile.mkdtemp()
        self.valid_mp4 = os.path.join(self.temp_dir, "test.mp4")
        self.invalid_file = os.path.join(self.temp_dir, "test.txt")
        self.empty_file = os.path.join(self.temp_dir, "empty.mp4")
        
        # Create valid MP4 header (ftyp box)
        with open(self.valid_mp4, 'wb') as f:
            f.write(b'ftypmp42')  # MP4 header
            f.write(b'\x00' * 1000)  # Fill with zeros
        
        # Create invalid text file
        with open(self.invalid_file, 'w') as f:
            f.write("This is not a video file")
        
        # Create empty file
        open(self.empty_file, 'w').close()
    
    def tearDown(self):
        """Clean up test files"""
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_verify_video_integrity_valid(self):
        """Test valid video file detection"""
        from gloom_ox.utils.integrity import verify_video_integrity
        
        result = verify_video_integrity(self.valid_mp4)
        self.assertTrue(result)
    
    def test_verify_video_integrity_invalid(self):
        """Test invalid file detection"""
        from gloom_ox.utils.integrity import verify_video_integrity
        
        result = verify_video_integrity(self.invalid_file)
        self.assertFalse(result)
    
    def test_verify_video_integrity_empty(self):
        """Test empty file detection"""
        from gloom_ox.utils.integrity import verify_video_integrity
        
        result = verify_video_integrity(self.empty_file)
        self.assertFalse(result)
    
    def test_verify_video_integrity_nonexistent(self):
        """Test nonexistent file detection"""
        from gloom_ox.utils.integrity import verify_video_integrity
        
        result = verify_video_integrity("/nonexistent/path/file.mp4")
        self.assertFalse(result)
    
    def test_ensure_ffmpeg(self):
        """Test FFmpeg detection"""
        from gloom_ox.utils.integrity import ensure_ffmpeg
        
        # This should return True or False based on system
        result = ensure_ffmpeg()
        self.assertIsInstance(result, bool)


class TestRepair(unittest.TestCase):
    """Test video repair functionality"""
    
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.corrupted_file = os.path.join(self.temp_dir, "corrupted.mp4")
        
        # Create a file that looks like it might be repairable
        with open(self.corrupted_file, 'wb') as f:
            f.write(b'\x00' * 1024)  # All zeros
    
    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_repair_video_no_ffmpeg(self):
        """Test repair when FFmpeg is not available"""
        from gloom_ox.utils.integrity import repair_video
        
        with patch('gloom_ox.utils.integrity.ensure_ffmpeg', return_value=False):
            result = repair_video(self.corrupted_file)
            self.assertEqual(result, self.corrupted_file)
    
    @patch('subprocess.run')
    def test_repair_video_with_ffmpeg(self, mock_run):
        """Test repair with FFmpeg available"""
        from gloom_ox.utils.integrity import repair_video
        
        with patch('gloom_ox.utils.integrity.ensure_ffmpeg', return_value=True):
            with patch('os.path.exists', return_value=True):
                with patch('os.path.getsize', return_value=2048):
                    result = repair_video(self.corrupted_file)
                    # Should return the original or fixed path
                    self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
