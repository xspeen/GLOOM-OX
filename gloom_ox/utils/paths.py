#!/usr/bin/env python3
"""
Cross-platform path management
"""

import os
import tempfile
from pathlib import Path

HOME = str(Path.home())
SYSTEM = os.name

# Detect Termux
IS_TERMUX = 'com.termux' in HOME or 'termux' in sys.executable if 'sys' in dir() else False

# Set paths
if IS_TERMUX:
    TERMUX_STORAGE = "/data/data/com.termux/files/home/storage/shared"
    if not os.path.exists(TERMUX_STORAGE):
        TERMUX_STORAGE = HOME + "/storage/shared"
    DCIM_PATH = os.path.join(TERMUX_STORAGE, "DCIM")
    DEFAULT_DOWNLOAD_DIR = os.path.join(TERMUX_STORAGE, "Download")
else:
    DCIM_PATH = os.path.join(HOME, "Pictures")
    DEFAULT_DOWNLOAD_DIR = os.path.join(HOME, "Downloads")

EXP_LINK_DIR = os.path.join(DEFAULT_DOWNLOAD_DIR, "GLOOM-OX_Videos")
os.makedirs(EXP_LINK_DIR, exist_ok=True)

def cleanup_temp_files():
    """Clean up temporary files"""
    temp_patterns = ['temp_', 'frag_', 'tmp_', '_temp', 'aggressive_', 'direct_']
    for root, dirs, files in os.walk(EXP_LINK_DIR):
        for file in files:
            if any(pattern in file for pattern in temp_patterns):
                try:
                    os.remove(os.path.join(root, file))
                except:
                    pass


import sys
