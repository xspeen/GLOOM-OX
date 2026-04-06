#!/usr/bin/env python3
"""
Global configuration settings
"""

import platform
import os
import sys
from pathlib import Path

VERSION = "4.0.0"
AUTHOR = "xspeen"
REPO_URL = "https://github.com/xspeen/GLOOM-OX.git"

SYSTEM = platform.system().lower()
IS_TERMUX = 'com.termux' in str(Path.home()) or 'termux' in sys.executable
