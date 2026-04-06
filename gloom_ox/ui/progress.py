#!/usr/bin/env python3
"""
Download progress UI components
"""

import sys
import threading


class ProgressBar:
    """Thread-safe progress bar"""
    
    def __init__(self, total=100, prefix='Download', suffix='Complete', length=50):
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.length = length
        self.current = 0
        self.lock = threading.Lock()
        
    def update(self, percent, speed='N/A'):
        """Update progress bar"""
        with self.lock:
            self.current = percent
            filled = int(self.length * percent // 100)
            bar = '█' * filled + '░' * (self.length - filled)
            sys.stdout.write(f'\r{self.prefix}: |{bar}| {percent:.1f}% {speed}')
            sys.stdout.flush()
            
            if percent >= 100:
                sys.stdout.write(f' {self.suffix}\n')
                sys.stdout.flush()
    
    def complete(self):
        """Mark as complete"""
        self.update(100)
    
    def reset(self):
        """Reset progress bar"""
        with self.lock:
            self.current = 0
