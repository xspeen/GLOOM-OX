#!/usr/bin/env python3
"""
GLOOM-OX v5.1 - Platform Tests
Tests platform-specific functionality
"""

import unittest
import sys
import os
import platform

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestPlatformDetection(unittest.TestCase):
    """Test platform detection across systems"""
    
    def test_platform_identification(self):
        """Test platform identification"""
        from gloom_ox import IS_TERMUX, IS_WINDOWS, IS_MAC, IS_LINUX
        
        system = platform.system().lower()
        
        if system == 'windows':
            self.assertTrue(IS_WINDOWS)
            self.assertFalse(IS_MAC)
            self.assertFalse(IS_LINUX)
        elif system == 'darwin':
            self.assertTrue(IS_MAC)
            self.assertFalse(IS_WINDOWS)
            self.assertFalse(IS_LINUX)
        elif system == 'linux':
            # Could be Linux or Termux
            self.assertTrue(IS_LINUX or IS_TERMUX)
    
    def test_path_separators(self):
        """Test path handling per platform"""
        import os
        
        if os.name == 'nt':
            # Windows paths
            self.assertEqual(os.path.sep, '\\')
        else:
            # Unix paths
            self.assertEqual(os.path.sep, '/')

class TestTermuxSpecific(unittest.TestCase):
    """Test Termux/Android specific features"""
    
    def test_termux_detection(self):
        """Test Termux environment detection"""
        from gloom_ox import IS_TERMUX
        
        # Just test that variable exists
        self.assertIsInstance(IS_TERMUX, bool)
    
    @unittest.skipIf(not os.path.exists('/data/data/com.termux'), "Not in Termux")
    def test_termux_paths(self):
        """Test Termux-specific paths"""
        from gloom_ox import DOWNLOAD_DIR
        
        # Should point to DCIM or shared storage
        self.assertIn('DCIM', DOWNLOAD_DIR or 'storage' in DOWNLOAD_DIR)

class TestWindowsSpecific(unittest.TestCase):
    """Test Windows specific features"""
    
    @unittest.skipIf(os.name != 'nt', "Windows-specific test")
    def test_windows_paths(self):
        """Test Windows paths"""
        from gloom_ox import DOWNLOAD_DIR
        
        # Should be in Videos folder
        self.assertIn('Videos', DOWNLOAD_DIR or 'GLOOM_OX' in DOWNLOAD_DIR)

class TestMacSpecific(unittest.TestCase):
    """Test macOS specific features"""
    
    @unittest.skipIf(platform.system() != 'Darwin', "macOS-specific test")
    def test_macos_paths(self):
        """Test macOS paths"""
        from gloom_ox import DOWNLOAD_DIR
        
        # Should be in Movies folder
        self.assertIn('Movies', DOWNLOAD_DIR or 'GLOOM_OX' in DOWNLOAD_DIR)

class TestLinuxSpecific(unittest.TestCase):
    """Test Linux specific features"""
    
    @unittest.skipIf(platform.system() != 'Linux', "Linux-specific test")
    @unittest.skipIf(os.path.exists('/data/data/com.termux'), "Not in Termux")
    def test_linux_paths(self):
        """Test Linux paths"""
        from gloom_ox import DOWNLOAD_DIR
        
        # Should be in Videos folder
        self.assertIn('Videos', DOWNLOAD_DIR or 'GLOOM_OX' in DOWNLOAD_DIR)

if __name__ == '__main__':
    unittest.main()
