# ============================================================
# GLOOM-OX v5.1 - Universal Social Media Downloader
# Docker Image for Linux, Windows, macOS, Termux
# ============================================================

FROM python:3.11-slim

# Labels for Docker Hub
LABEL maintainer="xspeen"
LABEL version="5.1.0"
LABEL description="GLOOM-OX - Universal Social Media Video Downloader with Gallery Injection"
LABEL repository="https://github.com/xspeen/GLOOM-OX"

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive
ENV GLOOM_OX_VERSION=5.1.0

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    nodejs \
    npm \
    wget \
    curl \
    git \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js packages for better extraction
RUN npm install -g --quiet

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir \
    yt-dlp>=2024.12.13 \
    requests>=2.31.0 \
    beautifulsoup4>=4.12.0 \
    certifi>=2023.0.0

# Create app directory
WORKDIR /app

# Copy application files
COPY gloom-ox.py /app/gloom-ox.py
COPY requirements.txt /app/requirements.txt
COPY README.md /app/README.md

# Make script executable
RUN chmod +x /app/gloom-ox.py

# Create download directory
RUN mkdir -p /app/downloads && \
    chmod 777 /app/downloads

# Set volume for downloads
VOLUME ["/app/downloads"]

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import yt_dlp" || exit 1

# Entry point
ENTRYPOINT ["python", "/app/gloom-ox.py"]

# Default command (can be overridden)
CMD []
