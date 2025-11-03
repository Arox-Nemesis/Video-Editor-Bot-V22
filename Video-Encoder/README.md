# 🎬 Video Encoder Bot

A powerful Telegram bot that encodes videos directly in memory without downloading them to your device. Perfect for converting videos to different resolutions for sharing and storage!

## ✨ Features

### 🚀 **Streaming Technology**
- **No Downloads**: Process videos directly in memory
- **Fast Processing**: Efficient FFmpeg pipeline
- **Real-time Progress**: Live tracking with time estimates
- **Memory Safe**: Handles large files safely

### 📹 **Video Encoding**
- **720p HD**: High quality for YouTube/social media
- **480p SD**: Balanced for WhatsApp/Telegram sharing
- **360p Mobile**: Small size for limited storage
- **Smart Compression**: Reduces file size while maintaining quality

### 🎯 **Key Benefits**
- ✅ **Privacy**: Videos never touch our servers
- ✅ **Speed**: Usually 1-10 minutes processing time
- ✅ **Quality**: Preserves aspect ratio and audio
- ✅ **Convenience**: Simple command interface
- ✅ **Free**: 24/7 hosting on Railway

## 🚀 Quick Deploy

### ⚡ **Railway Deployment (Recommended - Free)**

**1. Get Credentials (2 minutes)**
- **API ID & API Hash**: https://my.telegram.org
- **Bot Token**: https://t.me/BotFather

**2. Deploy (1 minute)**
```bash
# Click the button below or:
# 1. Go to https://railway.app
# 2. Click "Deploy from GitHub repo"
# 3. Add your API_ID, API_HASH, BOT_TOKEN
# 4. Click Deploy!
```

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Fyourusername%2Fvideo-encoder)

## 🤖 Bot Commands

### 📹 **Video Encoding**
```
/encode720    - Convert to 720p HD (best quality)
/encode480    - Convert to 480p SD (balanced)
/encode360    - Convert to 360p Mobile (smallest)
/encodehelp   - Detailed encoding help
```

### 🎯 **Management**
```
/start        - Welcome message with features
/help         - Show all available commands
/cancel       - Cancel current operation
```

## 📖 Usage Examples

### **Example 1: Encode to HD**
```
User: /encode720
Bot: 🎯 Selected Resolution: 720p HD
     Now send me the video file to encode...

User: [Sends 500MB video file]
Bot: ⚙️ Encoding to 720p HD...
     ✅ Video encoded successfully!
```

### **Example 2: Mobile Encoding**
```
User: /encode360
Bot: 🎯 Selected Resolution: 360p Mobile
     Size reduction: ~75%
     Send your video file...

User: [Sends video file]
Bot: ⚙️ Encoding to 360p Mobile...
     ✅ Video ready for sharing!
```

## 🔧 Configuration

Create a `.env` file:
```bash
API_ID=your_api_id_here
API_HASH=your_api_hash_here
BOT_TOKEN=your_bot_token_here
MAX_FILE_SIZE=2147483648    # 2GB in bytes
PROCESSING_TIMEOUT=300      # 5 minutes
```

## 📊 File Support

- **Video Formats**: MP4, AVI, MOV, MKV
- **Max File Size**: 2GB
- **Output Format**: MP4 (universal compatibility)
- **Audio**: Original audio track preserved

## 🏗️ Architecture

### **Streaming Pipeline**
```
User Upload → Telegram → Bot Memory → FFmpeg → Output → User Download
```

### **Key Components**
- **Streaming Processor**: Memory-only video processing
- **FFmpeg Integration**: Professional video encoding
- **Progress Tracker**: Real-time status updates
- **Error Handling**: Comprehensive error management

## 📈 Performance

### **Processing Times**
- **Small Videos** (<100MB): 30 seconds - 2 minutes
- **Medium Videos** (100MB-500MB): 2 - 8 minutes
- **Large Videos** (500MB-2GB): 8 - 20 minutes

### **Quality Settings**
| Resolution | Quality | Size Reduction | Best For |
|------------|---------|----------------|----------|
| 720p | High | ~40% smaller | YouTube, social media |
| 480p | Medium | ~60% smaller | WhatsApp, Telegram |
| 360p | Good | ~75% smaller | Mobile, limited storage |

## 🛠️ Development

### **Local Setup**
```bash
# Clone repository
git clone https://github.com/yourusername/video-encoder.git
cd video-encoder

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your credentials

# Run bot
python main.py
```

### **Project Structure**
```
Video-Encoder/
├── main.py                    # Bot entry point
├── config.py                  # Configuration
├── requirements.txt           # Dependencies
├── Dockerfile                 # Docker configuration
├── docker-compose.yml         # Docker Compose
├── .env.example              # Environment template
├── bot/
│   ├── handlers/             # Command handlers
│   │   ├── start.py         # Start and help
│   │   └── encode.py        # Video encoding
│   └── utils/               # Utilities
│       ├── ffmpeg_utils.py  # FFmpeg commands
│       ├── progress_tracker.py # Progress tracking
│       └── menu_helpers.py  # UI helpers
└── README.md                # This file
```

## 🆓 Free Hosting

### **Railway (Recommended)**
- ✅ $5 free credit per month
- ✅ Automatic deployments
- ✅ Built-in monitoring
- ✅ Custom domains
- ✅ Perfect for this bot

### **Alternative Options**
- **Render.com**: 750 hours free/month
- **Replit**: Free tier for testing
- **Glitch**: Free hosting with limitations

## 🔒 Security

- ✅ **No file storage** - Videos processed in memory only
- ✅ **Input validation** - All files validated
- ✅ **Error boundaries** - Safe error handling
- ✅ **Resource limits** - Memory and time limits
- ✅ **Secure credentials** - Environment variables only

## 🐛 Troubleshooting

### **Common Issues**
- **Bot not responding**: Check API credentials
- **Processing failed**: Verify video format and size
- **Large files**: Reduce file size or increase timeout
- **FFmpeg errors**: Ensure FFmpeg is installed

### **Debug Mode**
```bash
# Enable debug logging
DEBUG=true python main.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Pyrogram**: Excellent Telegram MTProto framework
- **FFmpeg**: Powerful multimedia processing toolkit
- **Telegram**: For providing the Bot API platform
- **Railway**: For free hosting platform

## 📞 Support

- **Documentation**: Check this README
- **Bot Commands**: Use `/help` in Telegram
- **Issues**: Report bugs via GitHub Issues

---

## 🎉 Ready to Deploy?

**Your Video Encoder Bot is ready for free deployment!**

1. **Get credentials** from [my.telegram.org](https://my.telegram.org) and [@BotFather](https://t.me/BotFather)
2. **Deploy on Railway**: [railway.app](https://railway.app)
3. **Your bot is live 24/7!**

**Start encoding videos without downloading them to any device!** 🚀

---

**⭐ Star this repository if you find it useful!**

**Made with ❤️ for the Telegram community**