# 📥 GLOOM-OX Installation Guide

## Quick Start

### Android (Termux)

```bash
# Update packages
pkg update && pkg upgrade

# Install dependencies
pkg install python ffmpeg git

# Clone and install
git clone https://github.com/xspeen/GLOOM-OX.git
cd GLOOM-OX
pip install -r requirements.txt

# Run
python gloom-ox.py
```

Linux (Ubuntu/Debian)

```bash
# Install Python and FFmpeg
sudo apt update
sudo apt install python3 python3-pip ffmpeg git

# Clone and install
git clone https://github.com/xspeen/GLOOM-OX.git
cd GLOOM-OX
pip3 install -r requirements.txt

# Run
python3 gloom-ox.py
```

Windows

```bash
# Install Python from python.org (3.8+)
# Install FFmpeg from ffmpeg.org

# Clone and install
git clone https://github.com/xspeen/GLOOM-OX.git
cd GLOOM-OX
pip install -r requirements.txt

# Run
python gloom-ox.py
```

Post-Installation

Verify installation:

```bash
python gloom-ox.py --version
```

Update tool:

```bash
python gloom-ox.py --update
```

Troubleshooting

"yt-dlp not found"

```bash
pip install --upgrade yt-dlp
```

"FFmpeg not found"

· Linux: sudo apt install ffmpeg
· Termux: pkg install ffmpeg
· Windows: Download from ffmpeg.org

Permission denied (Linux/Mac)

```bash
chmod +x gloom-ox.py
