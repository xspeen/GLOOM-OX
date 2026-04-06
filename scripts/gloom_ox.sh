#!/bin/bash
# GLOOM-OX Shell Launcher

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"

# Check if running from correct directory
if [[ -f "$PARENT_DIR/gloom-ox.py" ]]; then
    cd "$PARENT_DIR"
    python3 gloom-ox.py "$@"
else
    echo "[!] GLOOM-OX not found in current directory"
    echo "[!] Please run from GLOOM-OX root directory"
    exit 1
fi
