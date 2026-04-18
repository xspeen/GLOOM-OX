#!/usr/bin/env python3
"""
GLOOM-OX v5.2.0 - Universal Social Media Downloader
Setup script for PyPI distribution
"""

import os
from setuptools import setup
from setuptools.command.install import install

VERSION = "5.2.0"
AUTHOR = "xspeen"
EMAIL = "xspeen@proton.me"
REPO_URL = "https://github.com/xspeen/GLOOM-OX"

# Read README
try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except:
    long_description = "Universal Social Media Video Downloader with Gallery Injection"

# Read requirements
try:
    with open("requirements.txt", "r", encoding="utf-8") as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]
except:
    requirements = ["yt-dlp>=2024.12.13"]

class CustomInstall(install):
    """Custom install handler"""
    def run(self):
        install.run(self)
        print("""
╔══════════════════════════════════════════════════════════════════╗
║                    GLOOM-OX INSTALLED!                           ║
║                                                                  ║
║  Run: gloom-ox                                                   ║
║  Or:  python -m gloom-ox                                         ║
║                                                                  ║
║  For help: gloom-ox --help                                       ║
╚══════════════════════════════════════════════════════════════════╝
        """)

setup(
    name="gloom-ox",
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description="Universal Social Media Video Downloader with Gallery Injection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=REPO_URL,
    project_urls={
        "Bug Reports": f"{REPO_URL}/issues",
        "Source": REPO_URL,
        "Documentation": f"{REPO_URL}/blob/main/README.md",
        "Changelog": f"{REPO_URL}/releases",
    },
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Video",
        "Topic :: Internet :: WWW/HTTP",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "Operating System :: Android",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
    ],
    keywords=[
        "youtube-downloader",
        "instagram-downloader",
        "tiktok-downloader",
        "twitter-downloader",
        "facebook-downloader",
        "video-downloader",
        "social-media-downloader",
        "gallery-injector",
        "yt-dlp",
        "termux",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=8.0.0",
            "pytest-cov>=4.1.0",
            "black>=24.0.0",
            "ruff>=0.1.0",
            "mypy>=1.8.0",
            "build>=1.0.0",
            "twine>=5.0.0",
        ],
        "full": [
            "tqdm>=4.66.0",
            "requests>=2.31.0",
            "colorama>=0.4.6",
        ],
    },
    entry_points={
        "console_scripts": [
            "gloom-ox=gloom_ox:main",
            "gloomox=gloom_ox:main",
        ],
    },
    py_modules=["gloom_ox"],
    include_package_data=True,
    zip_safe=False,
    cmdclass={
        "install": CustomInstall,
    },
)
