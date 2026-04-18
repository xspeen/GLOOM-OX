#!/bin/bash
# ============================================================
# GLOOM-OX v5.1 - Shell Launcher
# Works on: Linux, macOS, Termux, Ubuntu
# ============================================================

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GLOOM_DIR="$(dirname "$SCRIPT_DIR")"

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

# Check if Python is available
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo -e "${RED}Error: Python not found!${NC}"
    echo "Please install Python 3.8+"
    exit 1
fi

# Check if main script exists
if [ ! -f "$GLOOM_DIR/gloom-ox.py" ]; then
    echo -e "${RED}Error: gloom-ox.py not found!${NC}"
    exit 1
fi

# Change to GLOOM directory
cd "$GLOOM_DIR"

# Run the main script
$PYTHON_CMD gloom-ox.py

# If script exits, wait for user input on Windows
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "win32" ]]; then
    echo ""
    read -p "Press Enter to exit..."
fi
