#!/bin/bash
# ============================================================
# GLOOM-OX v5.1 - Uninstaller for Unix Systems
# ============================================================

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${RED}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════════════╗
║                    GLOOM-OX UNINSTALLER                           ║
╚═══════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

echo -e "${YELLOW}This will remove GLOOM-OX and all downloaded videos!${NC}"
read -p "Are you sure? (y/n): " -n 1 -r
echo

if [[ $REPLY =~ ^[Yy]$ ]]; then
    # Remove directory
    if [ -d "$HOME/GLOOM-OX" ]; then
        rm -rf "$HOME/GLOOM-OX"
        echo -e "${GREEN}✓ Removed GLOOM-OX directory${NC}"
    fi
    
    # Remove alias
    if [ -f "$HOME/.bashrc" ]; then
        sed -i '/alias gloom-ox=/d' "$HOME/.bashrc"
        echo -e "${GREEN}✓ Removed alias from .bashrc${NC}"
    fi
    
    if [ -f "$HOME/.zshrc" ]; then
        sed -i '/alias gloom-ox=/d' "$HOME/.zshrc"
        echo -e "${GREEN}✓ Removed alias from .zshrc${NC}"
    fi
    
    # Remove desktop entry
    if [ -f "$HOME/.local/share/applications/gloom-ox.desktop" ]; then
        rm "$HOME/.local/share/applications/gloom-ox.desktop"
        echo -e "${GREEN}✓ Removed desktop entry${NC}"
    fi
    
    # Remove history
    if [ -f "$HOME/.gloom_ox_history.json" ]; then
        rm "$HOME/.gloom_ox_history.json"
        echo -e "${GREEN}✓ Removed download history${NC}"
    fi
    
    echo -e "\n${GREEN}GLOOM-OX has been uninstalled!${NC}"
else
    echo -e "${YELLOW}Uninstall cancelled${NC}"
fi
