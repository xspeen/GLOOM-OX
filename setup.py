#!/usr/bin/env python3
"""
GLOOM-OX Setup Script
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="gloom-ox",
    version="4.0.0",
    author="xspeen",
    author_email="xspeen@proton.me",
    description="Enterprise Grade Universal Media Extractor - NO LIMITS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xspeen/GLOOM-OX",
    project_urls={
        "Bug Reports": "https://github.com/xspeen/GLOOM-OX/issues",
        "Source": "https://github.com/xspeen/GLOOM-OX",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Video",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "gloom-ox=gloom_ox.__main__:run",
            "gloomox=gloom_ox.__main__:run",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
