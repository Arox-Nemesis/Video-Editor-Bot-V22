# 🚀 Deploy Your Video Encoder Bot

Complete guide to deploy your Video Encoder Bot on free hosting platforms.

## 🏆 **Recommended: Railway (Free & Easiest)**

Railway provides the best free hosting with $5 monthly credit - perfect for this bot!

### **Quick 3-Minute Deployment**

**Step 1: Get Your Credentials**
- **API ID & API Hash**: Go to https://my.telegram.org
- **Bot Token**: Message @BotFather on Telegram

**Step 2: Deploy on Railway**
1. Go to https://railway.app
2. Click "Login with GitHub" (free)
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your "video-encoder" repository
5. Click "Import Repo"

**Step 3: Add Environment Variables**
In Railway dashboard:
- Go to "Variables" tab
- Add these variables:
  ```
  API_ID=your_api_id_here
  API_HASH=your_api_hash_here
  BOT_TOKEN=your_bot_token_here
  ```
- Click "Redeploy"

**Your bot is now live 24/7 for free!** 🎉

## 📋 **Alternative Free Options**

### **Render.com** (Second Choice)
- **Free Tier**: 750 hours/month (enough for 24/7)
- **How to Deploy**:
  1. Go to https://render.com
  2. Click "New+" → "Web Service"
  3. Connect your GitHub repository
  4. Set Environment: Docker
  5. Add environment variables
  6. Deploy

### **Replit** (For Testing)
- **Always Free**: Perfect for development
- **Limitations**: Less resources, not for production
- **How to Deploy**:
  1. Go to https://replit.com
  2. Create new Python Repl
  3. Upload all files
  4. Add secrets (environment variables)
  5. Click "Run"

## 🔧 **Environment Variables**

All platforms require these variables:

```bash
API_ID=your_api_id_here          # From my.telegram.org
API_HASH=your_api_hash_here      # From my.telegram.org
BOT_TOKEN=your_bot_token_here     # From @BotFather
```

**Optional Variables:**
```bash
MAX_FILE_SIZE=2147483648         # 2GB max file size
PROCESSING_TIMEOUT=300            # 5 minutes timeout
DEBUG=false                       # Debug mode
LOG_LEVEL=INFO                    # Log level
```

## 🐳 **Docker Deployment**

If you prefer Docker:

```bash
# 1. Clone repository
git clone https://github.com/yourusername/video-encoder.git
cd video-encoder

# 2. Configure environment
cp .env.example .env
# Edit .env with your credentials

# 3. Deploy with Docker
docker-compose up -d
```

## 📊 **Platform Comparison**

| Platform | Free Tier | Ease of Use | Uptime | Best For |
|----------|-----------|-------------|--------|----------|
| **Railway** | $5/month | ⭐⭐⭐⭐⭐ | 99.9% | ✅ **Production** |
| Render.com | 750h/month | ⭐⭐⭐⭐ | 99.5% | Production |
| Replit | Unlimited | ⭐⭐⭐⭐⭐ | 95% | Development |
| Glitch | Unlimited | ⭐⭐⭐⭐ | 90% | Testing |

## 🛠️ **Manual Deployment**

For advanced users who want to host on their own server:

### **Prerequisites**
- Python 3.8+
- FFmpeg 4.0+
- 2GB RAM minimum
- Linux/Windows/macOS

### **Steps**
```bash
# 1. Clone repository
git clone https://github.com/yourusername/video-encoder.git
cd video-encoder

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Install FFmpeg
# Ubuntu/Debian:
sudo apt update && sudo apt install ffmpeg

# CentOS/RHEL:
sudo yum install epel-release && sudo yum install ffmpeg

# 4. Configure environment
cp .env.example .env
# Edit .env with your credentials

# 5. Run bot
python main.py
```

### **Systemd Service (Linux)**
Create `/etc/systemd/system/video-encoder.service`:
```ini
[Unit]
Description=Video Encoder Bot
After=network.target

[Service]
Type=simple
User=bot
WorkingDirectory=/path/to/video-encoder
Environment=PATH=/path/to/video-encoder/venv/bin
ExecStart=/path/to/video-encoder/venv/bin/python main.py
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable video-encoder
sudo systemctl start video-encoder
```

## 🔍 **Post-Deployment Checklist**

### **Test Your Bot**
After deployment, test these commands:
- `/start` - Should show welcome message
- `/help` - Should show all commands
- `/encode720` - Should ask for video file

### **Monitor Performance**
- **Railway**: Check dashboard logs
- **Render**: View logs in dashboard
- **Manual**: Check `logs/bot.log`

### **Common Issues**
- **Bot not starting**: Check environment variables
- **Processing failed**: Verify file format and size
- **Timeout errors**: Increase PROCESSING_TIMEOUT
- **Memory issues**: Reduce MAX_FILE_SIZE

## 📈 **Scaling Considerations**

### **When to Upgrade**
- **More than 100 users/day**: Consider paid plan
- **Large files (>1GB)**: Need more RAM/CPU
- **High concurrency**: Multiple bot instances

### **Optimization Tips**
- Use smaller max file size for stability
- Implement caching for repeated encodings
- Monitor resource usage regularly
- Set up alerting for errors

## 🎯 **Production Best Practices**

### **Security**
- Use environment variables for secrets
- Enable rate limiting
- Monitor for abuse
- Keep dependencies updated

### **Reliability**
- Set up health checks
- Monitor bot uptime
- Implement error logging
- Have backup deployment ready

### **Performance**
- Optimize FFmpeg settings
- Use CDN for static assets
- Monitor processing times
- Implement caching strategies

## 🆘 **Getting Help**

### **Troubleshooting**
1. **Check logs** for error messages
2. **Verify environment variables** are correct
3. **Test with small files** first
4. **Check platform status** for outages

### **Support Resources**
- **Railway**: https://docs.railway.app
- **Render**: https://render.com/docs
- **GitHub**: Create issue in repository
- **Telegram**: Use bot help commands

---

## 🎉 **You're Ready to Deploy!**

**Your Video Encoder Bot is ready for production deployment!**

**Quick Start:**
1. Get credentials from my.telegram.org and @BotFather
2. Deploy on Railway (recommended)
3. Add environment variables
4. Your bot is live 24/7!

**Deploy Now:** https://railway.app

**Your bot will encode videos without downloading them to any device - completely free!** 🚀