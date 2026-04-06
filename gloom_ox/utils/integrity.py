#!/usr/bin/env python3
"""
File integrity verification and repair
"""

import os
import subprocess


def verify_video_integrity(file_path):
    """Check if video file is valid"""
    if not os.path.exists(file_path):
        return False
    
    file_size = os.path.getsize(file_path)
    if file_size < 1024 * 50:  # Less than 50KB = likely corrupted
        return False
    
    try:
        with open(file_path, 'rb') as f:
            header = f.read(12)
            if header[:4] in [b'ftyp', b'\x00\x00\x00\x1c', b'\x1aE\xdf\xa3', b'RIFF']:
                return True
    except:
        pass
    
    valid_extensions = ['.mp4', '.mkv', '.webm', '.mov', '.avi', '.flv', '.3gp']
    ext = os.path.splitext(file_path)[1].lower()
    return ext in valid_extensions


def ensure_ffmpeg():
    """Ensure FFmpeg is available"""
    try:
        result = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True, timeout=5)
        return "ffmpeg version" in result.stdout
    except:
        return False


def repair_video(file_path):
    """Attempt to repair corrupted video file"""
    if not ensure_ffmpeg():
        return file_path
    
    try:
        fixed_path = file_path.replace('.mp4', '_fixed.mp4')
        subprocess.run([
            'ffmpeg', '-i', file_path,
            '-c', 'copy',
            '-y', fixed_path
        ], capture_output=True, timeout=30)
        
        if os.path.exists(fixed_path) and os.path.getsize(fixed_path) > 1024:
            os.remove(file_path)
            return fixed_path
    except:
        pass
    
    return file_path
