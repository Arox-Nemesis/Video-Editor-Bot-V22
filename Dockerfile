# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (for Pyrogram & TgCrypto)
RUN apt-get update && apt-get install -y \
    curl \
    ffmpeg \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency file
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot files into container
COPY . .

# Default command to run bot
CMD ["python", "bot/main.py"]
