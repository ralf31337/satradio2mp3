FROM python:3.11-slim

RUN apt-get update && apt-get install -y ffmpeg && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY radio_server.py .

ENV PORT=8000

CMD ["python3", "radio_server.py"]
