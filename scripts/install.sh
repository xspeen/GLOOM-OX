#!/bin/bash
# GLOOM-OX Universal Installer for Unix/Linux/Termux

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}"
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║              GLOOM-OX ENTERPRISE INSTALLER               ║"
echo "║                  Author: xspeen | CEH                    ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[!] Python3 not found. Installing...${NC}"
    if command -v apt &> /dev/null; then
        sudo apt update && sudo apt install python3 python3-pip -y
    elif command -v pkg &> /dev/null; then
        pkg install python python-pip -y
    else
        echo -e "${RED}[!] Please install Python 3.8+ manually${NC}"
        exit 1
    fi
fi

# Clone repository
echo -e "${GREEN}[+] Cloning GLOOM-OX repository...${NC}"
git clone https://github.com/xspeen/GLOOM-OX.git
cd GLOOM-OX

# Install Python dependencies
echo -e "${GREEN}[+] Installing Python dependencies...${NC}"
pip3 install -r requirements.txt

# Install FFmpeg if needed
echo -e "${GREEN}[+] Checking FFmpeg...${NC}"
if ! command -v ffmpeg &> /dev/null; then
    echo -e "${YELLOW}[~] Installing FFmpeg...${NC}"
    if command -v apt &> /dev/null; then
        sudo apt install ffmpeg -y
    elif command -v pkg &> /dev/null; then
        pkg install ffmpeg -y
    fi
fi

# Make executable
chmod +x gloom-ox.py
chmod +x scripts/gloom-ox.sh

# Create symlink
echo -e "${GREEN}[+] Creating global symlink...${NC}"
sudo ln -sf "$(pwd)/gloom-ox.py" /usr/local/bin/gloom-ox 2>/dev/null || true

echo -e "${GREEN}"
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║              INSTALLATION COMPLETE!                       ║"
echo "║                                                           ║"
echo "║  Run: ./gloom-ox.py or gloom-ox                          ║"
echo "║                                                           ║"
echo "║  Repository: https://github.com/xspeen/GLOOM-OX          ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo -e "${NC}"
