#!/usr/bin/env python3
"""
GLOOM-OX - Enterprise Grade Universal Media Extractor
Author: xspeen | CEH Certified
Version: 4.0.0
"""

__version__ = "4.0.0"
__author__ = "xspeen"
__credits__ = ["xspeen"]
__license__ = "MIT"
__maintainer__ = "xspeen"
__email__ = "xspeen@proton.me"
__status__ = "Production"
__repository__ = "https://github.com/xspeen/GLOOM-OX.git"

from gloom_ox.core.download_manager import DownloadManagerUnleashed
from gloom_ox.ui.robot_assistant import RobotAssistant
from gloom_ox.ui.banner import display_banner
from gloom_ox.config.settings import VERSION, AUTHOR

__all__ = [
    'DownloadManagerUnleashed',
    'RobotAssistant',
    'display_banner',
    'VERSION',
    'AUTHOR'
]
