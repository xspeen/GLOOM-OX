#!/usr/bin/env python3
"""
GLOOM-OX v5.1 - Test Suite
Comprehensive testing for Universal Social Media Downloader
"""

__version__ = "5.1.0"
__author__ = "xspeen"
__all__ = [
    "test_downloader",
    "test_engines", 
    "test_integrity",
    "test_gallery",
    "test_platforms",
]

# Test configuration
TEST_CONFIG = {
    "timeout": 30,
    "retry_count": 3,
    "test_videos": {
        "youtube": "https://youtube.com/watch?v=dQw4w9WgXcQ",
        "short": "https://youtube.com/shorts/1n9W-E3a5Gg",
    },
    "skip_network_tests": False,  # Set to True for offline testing
}
