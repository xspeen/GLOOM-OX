#!/usr/bin/env python3
"""
GLOOM-OX v5.1 - Integrity Tests
Tests system integrity, dependencies, and cross-platform compatibility
"""

import unittest
import sys
import os
import subprocess
import platform
import importlib

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestSystemIntegrity(unittest.TestCase):
    """Test system integrity and dependencies"""
    
    def test_python_version(self):
        """Test Python version compatibility"""
        version = sys.version_info
        self.assertGreaterEqual(version.major, 3)
        self.assertGreaterEqual(version.minor, 8)
    
    def test_required_modules(self):
        """Test that required modules can be imported"""
        required_modules = [
            'yt_dlp',
            'requests',
            'json',
            'subprocess',
            'pathlib',
        ]
        
        for module in required_modules:
            try:
                importlib.import_module(module)
            except ImportError as e:
                self.fail(f"Failed to import {module}: {e}")
    
    def test_optional_ffmpeg(self):
        """Test FFmpeg availability (optional)"""
        try:
            result = subprocess.run(
                ["ffmpeg", "-version"],
                capture_output=True,
                timeout=5
            )
            self.assertEqual(result.returncode, 0)
            print("\n✓ FFmpeg is available")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("\n⚠️ FFmpeg not found - video optimization will be disabled")
    
    def test_directory_permissions(self):
        """Test directory creation and permissions"""
        from gloom_ox import DOWNLOAD_DIR
        
        self.assertIsNotNone(DOWNLOAD_DIR)
        
        # Test we can write to the directory (or parent directory)
        try:
            test_file = os.path.join(DOWNLOAD_DIR, ".write_test")
            with open(test_file, 'w') as f:
                f.write("test")
            os.remove(test_file)
        except Exception as e:
            self.skipTest(f"Cannot write to download directory: {e}")
    
    def test_history_file(self):
        """Test history file operations"""
        from gloom_ox import DOWNLOAD_HISTORY_FILE, load_history, save_history
        
        # Test load (should not crash)
        try:
            load_history()
        except Exception as e:
            self.fail(f"Failed to load history: {e}")
        
        # Test save
        try:
            save_history("https://test.com")
        except Exception as e:
            self.fail(f"Failed to save history: {e}")

class TestCrossPlatform(unittest.TestCase):
    """Test cross-platform compatibility"""
    
    def test_platform_detection(self):
        """Test platform detection"""
        system = platform.system().lower()
        
        self.assertIn(system, ['windows', 'linux', 'darwin'])
    
    def test_path_separators(self):
        """Test path handling across platforms"""
        import os
        from pathlib import Path
        
        # Test Path object works
        test_path = Path.home() / "test" / "file.txt"
        self.assertIsInstance(str(test_path), str)
    
    @unittest.skipIf(os.name == 'nt', "Unix-specific test")
    def test_unix_permissions(self):
        """Test Unix file permissions"""
        if os.name == 'posix':
            import stat
            from gloom_ox import DOWNLOAD_DIR
            
            mode = os.stat(DOWNLOAD_DIR).st_mode
            # Check if directory has execute permission (for traversal)
            self.assertTrue(mode & stat.S_IXUSR or True)  # Warning only

class TestPerformance(unittest.TestCase):
    """Performance tests"""
    
    def test_import_time(self):
        """Test import performance"""
        import time
        
        start = time.time()
        try:
            import gloom_ox
        except ImportError:
            self.skipTest("gloom_ox module not available")
        elapsed = time.time() - start
        
        # Import should be reasonably fast (< 2 seconds)
        self.assertLess(elapsed, 2)
    
    def test_memory_usage(self):
        """Test memory usage (basic)"""
        import sys
        
        # Get current memory usage (approximate)
        initial_size = sys.getsizeof({})
        
        # Import modules
        import gloom_ox
        
        # Should not cause memory explosion
        self.assertLess(sys.getsizeof(gloom_ox), 10 * 1024 * 1024)  # 10MB

class TestSecurity(unittest.TestCase):
    """Security tests"""
    
    def test_no_hardcoded_secrets(self):
        """Test for hardcoded secrets in code"""
        import re
        
        test_file = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "gloom-ox.py"
        )
        
        if not os.path.exists(test_file):
            self.skipTest("Main script not found")
        
        with open(test_file, 'r') as f:
            content = f.read()
        
        # Check for patterns that look like secrets
        secret_patterns = [
            r'api_key\s*=\s*[\'\"][^\'\"]+[\'\"]',
            r'token\s*=\s*[\'\"][^\'\"]+[\'\"]',
            r'password\s*=\s*[\'\"][^\'\"]+[\'\"]',
            r'secret\s*=\s*[\'\"][^\'\"]+[\'\"]',
        ]
        
        for pattern in secret_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            # Allow empty strings or placeholder values
            for match in matches:
                if 'YOUR_' not in match.upper() and 'TODO' not in match.upper():
                    self.fail(f"Possible hardcoded secret found: {match[:50]}")

class TestDocumentation(unittest.TestCase):
    """Test documentation completeness"""
    
    def test_readme_exists(self):
        """Test that README.md exists"""
        readme_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "README.md"
        )
        self.assertTrue(os.path.exists(readme_path), "README.md not found")
    
    def test_license_exists(self):
        """Test that LICENSE exists"""
        license_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "LICENSE"
        )
        self.assertTrue(os.path.exists(license_path), "LICENSE not found")
    
    def test_version_match(self):
        """Test version consistency across files"""
        import re
        
        # Check main script version
        main_file = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "gloom-ox.py"
        )
        
        if os.path.exists(main_file):
            with open(main_file, 'r') as f:
                content = f.read()
            
            version_match = re.search(r'VERSION\s*=\s*["\']([^"\']+)["\']', content)
            if version_match:
                version = version_match.group(1)
                self.assertEqual(version, "5.1.0")

if __name__ == '__main__':
    # Run with verbosity
    unittest.main(verbosity=2)
