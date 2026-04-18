#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    GLOOM-OX v5.1 - Setup Script                               ║
║                                                                               ║
║         Universal Social Media Video Downloader with Gallery Injection        ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop

# Get version from environment or use default
VERSION = os.environ.get('GLOOM_OX_VERSION', '5.1.0')

# Read README
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "GLOOM-OX - Universal Social Media Video Downloader with Gallery Injection"

# Read requirements
requirements = [
    "yt-dlp>=2024.12.13",
    "requests>=2.31.0",
    "beautifulsoup4>=4.12.0",
    "certifi>=2023.0.0",
]

# Optional dependencies
extras_require = {
    'dev': [
        'pytest>=7.0.0',
        'black>=23.0.0',
        'ruff>=0.1.0',
        'mypy>=1.0.0',
        'build>=0.10.0',
        'twine>=4.0.0',
    ],
    'test': [
        'pytest>=7.0.0',
        'pytest-cov>=4.0.0',
        'pytest-mock>=3.10.0',
    ],
    'docker': [
        'docker>=6.0.0',
    ],
    'all': [
        'pytest>=7.0.0',
        'black>=23.0.0',
        'ruff>=0.1.0',
        'mypy>=1.0.0',
        'docker>=6.0.0',
    ]
}

# Custom install class for platform-specific setup
class CustomInstall(install):
    """Custom install handler for platform-specific dependencies"""
    
    def run(self):
        """Run installation with platform-specific checks"""
        install.run(self)
        
        # Check for FFmpeg after installation
        self.announce("Checking for FFmpeg...", level=3)
        import subprocess
        try:
            subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
            self.announce("✓ FFmpeg found", level=3)
        except (subprocess.CalledProcessError, FileNotFoundError):
            self.announce("⚠️ FFmpeg not found. Video optimization disabled.", level=3)
            self.announce("  Install FFmpeg:", level=3)
            self.announce("    - Ubuntu/Debian: sudo apt install ffmpeg", level=3)
            self.announce("    - macOS: brew install ffmpeg", level=3)
            self.announce("    - Windows: choco install ffmpeg", level=3)
            self.announce("    - Termux: pkg install ffmpeg", level=3)

# Custom develop class
class CustomDevelop(develop):
    """Custom develop handler"""
    
    def run(self):
        """Run develop installation"""
        develop.run(self)
        self.announce("GLOOM-OX installed in development mode", level=3)
        self.announce("Run 'gloom-ox' to start", level=3)

setup(
    # Basic metadata
    name="gloom-ox",
    version=VERSION,
    author="xspeen",
    author_email="xspeen@proton.me",
    maintainer="xspeen",
    maintainer_email="xspeen@proton.me",
    description="Universal Social Media Video Downloader with Gallery Injection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    # URLs
    url="https://github.com/xspeen/GLOOM-OX",
    project_urls={
        "Bug Reports": "https://github.com/xspeen/GLOOM-OX/issues",
        "Source": "https://github.com/xspeen/GLOOM-OX",
        "Documentation": "https://github.com/xspeen/GLOOM-OX/blob/main/README.md",
        "Changelog": "https://github.com/xspeen/GLOOM-OX/releases",
        "Docker Hub": "https://hub.docker.com/r/xspeen/gloom-ox",
        "PyPI": "https://pypi.org/project/gloom-ox/",
    },
    
    # Package configuration
    packages=find_packages(
        where=".",
        exclude=["tests", "tests.*", "docs", "docs.*", "assets", "scripts"]
    ),
    package_dir={"": "."},
    include_package_data=True,
    zip_safe=False,
    
    # Dependencies
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require=extras_require,
    
    # Entry points
    entry_points={
        "console_scripts": [
            "gloom-ox=gloom_ox.__main__:main",
            "gloomox=gloom_ox.__main__:main",
            "gloom=gloom_ox.__main__:main",
        ],
        "gui_scripts": [
            "gloom-ox-gui=gloom_ox.gui:main",
        ],
        "distutils.commands": [
            "install = setup:CustomInstall",
            "develop = setup:CustomDevelop",
        ],
    },
    
    # Classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Other Audience",
        "Topic :: Multimedia :: Video",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Utilities",
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
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows 11",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Environment :: Console",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Natural Language :: English",
    ],
    
    # Keywords for PyPI search
    keywords=[
        "youtube-downloader",
        "instagram-downloader", 
        "tiktok-downloader",
        "twitter-downloader",
        "facebook-downloader",
        "reddit-downloader",
        "social-media-downloader",
        "video-downloader",
        "gallery-injector",
        "yt-dlp",
        "termux",
        "android-gallery",
        "media-downloader",
        "video-saver",
    ],
    
    # Data files
    package_data={
        "gloom_ox": [
            "py.typed",
            "*.txt",
            "*.md",
            "assets/*.png",
            "assets/*.ico",
            "assets/*.svg",
        ],
    },
    
    # Exclude files from package
    exclude_package_data={
        "": ["tests/*", "docs/*", "assets/*.psd"],
    },
    
    # Custom commands
    cmdclass={
        "install": CustomInstall,
        "develop": CustomDevelop,
    },
    
    # Additional metadata
    license="MIT",
    license_files=["LICENSE"],
    platforms=["any"],
    
    # Scripts to include
    scripts=[
        "scripts/gloom_ox.sh",
        "scripts/install.sh",
        "scripts/uninstall.sh",
    ] if os.path.exists("scripts") else [],
    
    # Options
    options={
        "bdist_wheel": {
            "universal": True,
        },
        "build_scripts": {
            "executable": "/usr/bin/env python3",
        },
    },
)

# Post-installation message
if __name__ == "__main__":
    # This runs when setup.py is executed directly
    print("""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    GLOOM-OX v5.1 - Installation Complete                       ║
║                                                                               ║
║  🚀 To start using GLOOM-OX:                                                  ║
║     $ gloom-ox                                                                ║
║                                                                               ║
║  📝 For more information:                                                     ║
║     https://github.com/xspeen/GLOOM-OX                                        ║
║                                                                               ║
║  ⭐ If you find this tool useful, consider giving it a star on GitHub!        ║
╚═══════════════════════════════════════════════════════════════════════════════╝
    """)
