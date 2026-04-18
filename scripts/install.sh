#!/bin/bash
# ============================================================
# GLOOM-OX v5.1 - Universal Installer for Unix Systems
# Supports: Linux, macOS, Termux, Ubuntu, WSL
# ============================================================

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Banner
echo -e "${CYAN}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════════════╗
║                    GLOOM-OX v5.1 INSTALLER                        ║
║                                                                   ║
║         Universal Social Media Video Downloader                   ║
╚═══════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

# Detect OS
detect_os() {
    case "$(uname -s)" in
        Linux*)     
            if [ -d "/data/data/com.termux" ]; then
                OS="termux"
            else
                OS="linux"
            fi
            ;;
        Darwin*)    OS="macos" ;;
        MINGW*)     OS="windows" ;;
        CYGWIN*)    OS="windows" ;;
        MSYS*)      OS="windows" ;;
        *)          OS="unknown" ;;
    esac
    echo -e "${GREEN}✓ Detected OS: ${OS}${NC}"
}

# Check Python version
check_python() {
    echo -e "${BLUE}[1/6] Checking Python...${NC}"
    
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
        PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
        echo -e "${GREEN}✓ Python ${PYTHON_VERSION} found${NC}"
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
        PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
        echo -e "${GREEN}✓ Python ${PYTHON_VERSION} found${NC}"
    else
        echo -e "${RED}✗ Python not found!${NC}"
        echo -e "${YELLOW}Installing Python...${NC}"
        
        if [ "$OS" = "termux" ]; then
            pkg update && pkg install python -y
        elif [ "$OS" = "linux" ]; then
            if command -v apt &> /dev/null; then
                sudo apt update && sudo apt install python3 python3-pip -y
            elif command -v yum &> /dev/null; then
                sudo yum install python3 python3-pip -y
            fi
        elif [ "$OS" = "macos" ]; then
            brew install python3
        fi
    fi
}

# Install dependencies
install_dependencies() {
    echo -e "${BLUE}[2/6] Installing system dependencies...${NC}"
    
    if [ "$OS" = "termux" ]; then
        pkg update -y
        pkg install -y ffmpeg nodejs git
    elif [ "$OS" = "linux" ]; then
        if command -v apt &> /dev/null; then
            sudo apt update
            sudo apt install -y ffmpeg nodejs git
        elif command -v yum &> /dev/null; then
            sudo yum install -y ffmpeg nodejs git
        fi
    elif [ "$OS" = "macos" ]; then
        brew install ffmpeg nodejs git
    fi
    
    echo -e "${GREEN}✓ System dependencies installed${NC}"
}

# Install Python packages
install_python_packages() {
    echo -e "${BLUE}[3/6] Installing Python packages...${NC}"
    
    $PYTHON_CMD -m pip install --upgrade pip
    $PYTHON_CMD -m pip install yt-dlp requests beautifulsoup4
    
    echo -e "${GREEN}✓ Python packages installed${NC}"
}

# Clone or update repository
setup_repository() {
    echo -e "${BLUE}[4/6] Setting up GLOOM-OX...${NC}"
    
    if [ -d "$HOME/GLOOM-OX" ]; then
        echo -e "${YELLOW}Directory exists, updating...${NC}"
        cd "$HOME/GLOOM-OX"
        git pull origin main
    else
        echo -e "${YELLOW}Cloning repository...${NC}"
        git clone https://github.com/xspeen/GLOOM-OX.git "$HOME/GLOOM-OX"
        cd "$HOME/GLOOM-OX"
    fi
    
    # Make scripts executable
    chmod +x gloom-ox.py
    chmod +x scripts/*.sh 2>/dev/null || true
    
    echo -e "${GREEN}✓ Repository ready at $HOME/GLOOM-OX${NC}"
}

# Create desktop entry (Linux only)
create_desktop_entry() {
    if [ "$OS" = "linux" ] && [ ! "$TERMUX" ]; then
        echo -e "${BLUE}[5/6] Creating desktop entry...${NC}"
        
        cat > ~/.local/share/applications/gloom-ox.desktop << EOF
[Desktop Entry]
Name=GLOOM-OX
Comment=Universal Social Media Video Downloader
Exec=$HOME/GLOOM-OX/scripts/gloom_ox.sh
Icon=$HOME/GLOOM-OX/assets/icon.png
Terminal=true
Type=Application
Categories=Network;Video;
EOF
        
        chmod +x ~/.local/share/applications/gloom-ox.desktop
        echo -e "${GREEN}✓ Desktop entry created${NC}"
    fi
}

# Create alias
create_alias() {
    echo -e "${BLUE}[6/6] Creating alias...${NC}"
    
    SHELL_CONFIG="$HOME/.bashrc"
    if [ -f "$HOME/.zshrc" ]; then
        SHELL_CONFIG="$HOME/.zshrc"
    fi
    
    if ! grep -q "alias gloom-ox=" "$SHELL_CONFIG"; then
        echo "alias gloom-ox='cd $HOME/GLOOM-OX && python3 gloom-ox.py'" >> "$SHELL_CONFIG"
        echo -e "${GREEN}✓ Alias added to $SHELL_CONFIG${NC}"
    else
        echo -e "${YELLOW}Alias already exists${NC}"
    fi
}

# Show success message
show_success() {
    echo -e "\n${GREEN}╔════════════════════════════════════════════════════════════╗"
    echo -e "║              INSTALLATION COMPLETE!                            ║"
    echo -e "╚════════════════════════════════════════════════════════════╝${NC}\n"
    
    echo -e "${CYAN}🚀 To run GLOOM-OX:${NC}"
    echo -e "   ${YELLOW}cd $HOME/GLOOM-OX${NC}"
    echo -e "   ${YELLOW}python3 gloom-ox.py${NC}\n"
    
    echo -e "${CYAN}📝 Or use alias:${NC}"
    echo -e "   ${YELLOW}gloom-ox${NC}\n"
    
    echo -e "${CYAN}💡 Commands:${NC}"
    echo -e "   ${YELLOW}history${NC} - Show downloaded videos"
    echo -e "   ${YELLOW}clear${NC}   - Clear screen"
    echo -e "   ${YELLOW}exit${NC}    - Exit program\n"
    
    echo -e "${PURPLE}⭐ Support the project: https://github.com/xspeen/GLOOM-OX${NC}\n"
}

# Main installation
main() {
    detect_os
    check_python
    install_dependencies
    install_python_packages
    setup_repository
    create_desktop_entry
    create_alias
    show_success
    
    # Ask to run
    echo -e "${YELLOW}Do you want to run GLOOM-OX now? (y/n)${NC}"
    read -r run_now
    if [ "$run_now" = "y" ] || [ "$run_now" = "Y" ]; then
        cd "$HOME/GLOOM-OX"
        $PYTHON_CMD gloom-ox.py
    fi
}

# Run main function
main
