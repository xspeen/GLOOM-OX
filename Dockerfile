FROM python:3.11-slim

RUN apt-get update && apt-get install -y ffmpeg nodejs && rm -rf /var/lib/apt/lists/*

RUN pip install yt-dlp requests

COPY gloom-ox.py /app/gloom-ox.py
WORKDIR /app

ENTRYPOINT ["python", "gloom-ox.py"]
