#!/usr/bin/env python3
"""
User-Agent rotation and headers management
"""

import random

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Linux; Android 14; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36',
]

MOBILE_AGENTS = [
    'Instagram 319.0.0.12.107 Android',
    'Instagram 320.0.0.0.0 Android',
    'com.instagram.android 320.0.0.0.0',
    'TikTok 32.4.5',
    'com.pinterest/13.9.0',
    'com.facebook.katana/450.0.0.0.0',
]

HEADERS_TEMPLATE = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

def get_random_headers(platform='default'):
    """Generate random headers for specific platform"""
    headers = HEADERS_TEMPLATE.copy()
    headers['User-Agent'] = random.choice(USER_AGENTS)
    headers['Referer'] = random.choice([
        'https://www.google.com/',
        'https://www.youtube.com/',
        'https://www.instagram.com/',
    ])
    return headers
