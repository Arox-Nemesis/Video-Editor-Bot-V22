# Telegram Video Editor Bot - Deployment Guide

This guide provides comprehensive instructions for deploying the Telegram Video Editor Bot in various environments.

## 🚀 Quick Start

### Prerequisites

- **Telegram Bot Token**: Get from [@BotFather](https://t.me/BotFather)
- **API ID & API Hash**: Get from [my.telegram.org](https://my.telegram.org)
- **FFmpeg**: Required for video processing
- **Python 3.8+**: Runtime environment

### Option 1: Docker Deployment (Recommended)

```bash
# Clone the repository
git clone <repository-url>
cd Video-Editor-Bot-V22

# Copy environment template
cp .env.example .env

# Edit .env with your credentials
nano .env

# Deploy with Docker Compose
docker-compose up -d

# View logs
docker-compose logs -f video-editor-bot
```

### Option 2: Manual Deployment

```bash
# Clone the repository
git clone <repository-url>
cd Video-Editor-Bot-V22

# Run deployment script
chmod +x deploy.sh
./deploy.sh

# Configure .env file
nano .env

# Start the bot
./start_bot.sh
```

## 📋 System Requirements

### Minimum Requirements
- **CPU**: 1 core (2+ recommended)
- **RAM**: 2GB (4GB+ recommended for large files)
- **Storage**: 10GB free space
- **Network**: Stable internet connection
- **OS**: Linux (Ubuntu 18.04+, CentOS 7+, Debian 9+)

### Software Requirements
- **Python**: 3.8 or higher
- **FFmpeg**: 4.0 or higher
- **Docker**: 20.10+ (for Docker deployment)
- **Docker Compose**: 1.29+ (for Docker deployment)

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following configuration:

```bash
# Required: Telegram Bot Credentials
API_ID=your_api_id_here
API_HASH=your_api_hash_here
BOT_TOKEN=your_bot_token_here

# Optional: Database (for future features)
MONGO_URI=mongodb://localhost:27017/video_editor_bot

# Optional: Logging
LOG_CHANNEL=your_log_channel_id_here

# Processing Configuration
MAX_FILE_SIZE=2147483648  # 2GB in bytes
PROCESSING_TIMEOUT=300     # 5 minutes in seconds

# Development
DEBUG=false
LOG_LEVEL=INFO
```

### Getting Telegram Credentials

1. **API ID & API Hash**:
   - Visit [my.telegram.org](https://my.telegram.org)
   - Sign in with your phone number
   - Create a new application
   - Copy the `API ID` and `API Hash`

2. **Bot Token**:
   - Message [@BotFather](https://t.me/BotFather) on Telegram
   - Send `/newbot`
   - Follow the instructions to create your bot
   - Copy the bot token

## 📦 Deployment Methods

### Method 1: Docker (Recommended)

**Advantages:**
- Isolated environment
- Easy updates and rollbacks
- Included FFmpeg
- Resource management

**Steps:**

```bash
# 1. Clone repository
git clone <repository-url>
cd Video-Editor-Bot-V22

# 2. Configure environment
cp .env.example .env
# Edit .env with your credentials

# 3. Deploy
docker-compose up -d

# 4. Monitor
docker-compose logs -f video-editor-bot

# 5. Update (when needed)
git pull
docker-compose build
docker-compose up -d
```

**Docker Commands:**
```bash
# View logs
docker-compose logs video-editor-bot

# Stop bot
docker-compose stop video-editor-bot

# Restart bot
docker-compose restart video-editor-bot

# Scale (multiple instances)
docker-compose up -d --scale video-editor-bot=2
```

### Method 2: Manual Deployment

**Advantages:**
- Full system control
- Direct file access
- Custom configurations

**Steps:**

```bash
# 1. Clone repository
git clone <repository-url>
cd Video-Editor-Bot-V22

# 2. Run deployment script
chmod +x deploy.sh
./deploy.sh

# 3. Configure environment
nano .env

# 4. Start bot
./start_bot.sh
```

**Manual Commands:**
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start bot
python -m main
```

### Method 3: Systemd Service

**For production servers:**

```bash
# 1. Deploy manually first
./deploy.sh

# 2. Create systemd service (requires root)
sudo nano /etc/systemd/system/video-editor-bot.service

# 3. Service content:
[Unit]
Description=Telegram Video Editor Bot
After=network.target

[Service]
Type=simple
User=bot
WorkingDirectory=/path/to/Video-Editor-Bot-V22
Environment=PATH=/path/to/Video-Editor-Bot-V22/venv/bin
ExecStart=/path/to/Video-Editor-Bot-V22/venv/bin/python -m main
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target

# 4. Enable and start
sudo systemctl daemon-reload
sudo systemctl enable video-editor-bot
sudo systemctl start video-editor-bot

# 5. Monitor
sudo systemctl status video-editor-bot
sudo journalctl -u video-editor-bot -f
```

## 🛠️ Maintenance

### Monitoring

**Docker:**
```bash
# Check logs
docker-compose logs -f video-editor-bot

# Check resource usage
docker stats video-editor-bot

# Health check
docker-compose ps
```

**Manual/Systemd:**
```bash
# Check logs
tail -f logs/bot.log

# Check process
ps aux | grep python

# System resources
htop
df -h
```

### Updates

**Docker:**
```bash
git pull
docker-compose build
docker-compose up -d
```

**Manual:**
```bash
git pull
source venv/bin/activate
pip install -r requirements.txt
# Restart bot
```

### Backup

**Data to backup:**
- `.env` file
- `logs/` directory
- Database (if using MongoDB)

**Backup script:**
```bash
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
tar -czf backup_$DATE.tar.gz .env logs/
```

## 🔒 Security

### Recommended Security Practices

1. **Environment Variables**:
   - Never commit `.env` to version control
   - Use strong, unique credentials
   - Rotate API keys periodically

2. **File Permissions**:
   ```bash
   chmod 600 .env
   chmod 755 scripts/
   ```

3. **Network Security**:
   - Use firewall to restrict access
   - Only expose necessary ports
   - Use VPN for admin access

4. **Container Security** (Docker):
   ```bash
   # Run as non-root user
   docker-compose exec video-editor-bot whoami

   # Scan for vulnerabilities
   docker scan video-editor-bot
   ```

5. **System Updates**:
   ```bash
   # Regular system updates
   sudo apt update && sudo apt upgrade -y

   # Update Docker images
   docker-compose pull
   ```

## 🚨 Troubleshooting

### Common Issues

**1. Bot Not Starting:**
```bash
# Check .env file
cat .env

# Verify Python version
python3 --version

# Check dependencies
pip list

# Check FFmpeg
ffmpeg -version
```

**2. FFmpeg Not Found:**
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# CentOS/RHEL
sudo yum install epel-release
sudo yum install ffmpeg

# Verify
ffmpeg -version
```

**3. Permission Errors:**
```bash
# Fix directory permissions
chmod 755 temp logs
chown -R $USER:$USER temp logs

# Fix script permissions
chmod +x deploy.sh start_bot.sh
```

**4. Memory Issues:**
```bash
# Check memory usage
free -h
docker stats  # if using Docker

# Reduce processing limits
# Edit .env: MAX_FILE_SIZE=1073741824  # 1GB
```

**5. Network Issues:**
```bash
# Check internet connection
ping telegram.org

# Check firewall
sudo ufw status

# Check ports
netstat -tlnp | grep :8080
```

### Log Analysis

**Docker Logs:**
```bash
# Real-time logs
docker-compose logs -f video-editor-bot

# Recent logs
docker-compose logs --tail=100 video-editor-bot

# Error logs
docker-compose logs video-editor-bot | grep ERROR
```

**Manual Logs:**
```bash
# Bot logs
tail -f logs/bot.log

# System logs
sudo journalctl -u video-editor-bot -f

# Python errors
python -m main 2>&1 | tee logs/bot.log
```

## 📊 Performance Optimization

### System Optimization

```bash
# Increase file descriptor limit
echo "* soft nofile 65536" >> /etc/security/limits.conf
echo "* hard nofile 65536" >> /etc/security/limits.conf

# Optimize network settings
echo "net.core.rmem_max = 134217728" >> /etc/sysctl.conf
echo "net.core.wmem_max = 134217728" >> /etc/sysctl.conf
sysctl -p
```

### Docker Optimization

```yaml
# In docker-compose.yml
deploy:
  resources:
    limits:
      memory: 2G
      cpus: '1.0'
    reservations:
      memory: 512M
      cpus: '0.5'
```

### Bot Configuration

```bash
# In .env file
MAX_FILE_SIZE=1073741824    # 1GB for better performance
PROCESSING_TIMEOUT=180      # 3 minutes
MAX_CONCURRENT_TASKS=3      # Limit concurrent processing
```

## 🆘 Support

### Getting Help

1. **Bot Commands**: Use `/help` in Telegram
2. **Documentation**: Check inline help commands
3. **Logs**: Review error logs for detailed information
4. **Community**: Join support groups/channels

### Debug Mode

Enable debug mode for detailed logging:

```bash
# In .env file
DEBUG=true
LOG_LEVEL=DEBUG

# Restart bot to apply
docker-compose restart video-editor-bot
```

## 📝 Additional Resources

- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)
- [Pyrogram Documentation](https://docs.pyrogram.org/)
- [Docker Documentation](https://docs.docker.com/)

---

**Bot Features After Deployment:**
✅ Video resolution encoding (720p, 480p, 360p)
✅ Audio extraction and addition (MP3, OGG, WAV)
✅ Subtitle extraction and embedding (SRT)
✅ No local downloads - pure streaming
✅ Progress tracking and error handling
✅ Comprehensive command interface

For questions or issues, please check the troubleshooting section or review the bot logs.