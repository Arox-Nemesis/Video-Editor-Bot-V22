# 🎬 Telegram Video Editor Bot - Streaming Edition

A revolutionary Telegram bot that edits videos directly on Telegram without downloading them to your device. Features include resolution encoding, audio extraction/addition, and subtitle handling using pure streaming technology.

## ✨ Key Features

### 🚀 **Streaming Processing (NEW!)**
- **No Downloads**: Process videos directly in memory - no device storage needed
- **Fast Processing**: Efficient FFmpeg pipeline with stdin/stdout streaming
- **Progress Tracking**: Real-time progress updates with time estimates
- **Memory Safe**: Chunked processing (1MB chunks) for large files up to 2GB
- **Async Operations**: Non-blocking processing for better user experience

### 📹 **Video Operations**
- **Resolution Encoding**: Convert to 720p, 480p, 360p with quality preservation
- **Format Support**: MP4, AVI, MOV, MKV video formats
- **Aspect Ratio**: Automatic preservation during encoding
- **Quality Control**: Optimized encoding settings for file size vs quality

### 🎵 **Audio Operations**
- **Extraction**: Extract audio as MP3, OGG, WAV (multiple bitrates)
- **Addition**: Add external audio tracks to videos
- **Replacement**: Replace existing video audio completely
- **Mixing**: Combine video audio with new audio tracks

### 📝 **Subtitle Operations**
- **Extraction**: Extract embedded subtitles as SRT files
- **Embedding**: Add SRT subtitle files to videos
- **Multi-track**: Support for multiple subtitle tracks
- **Styling**: Custom subtitle appearance and positioning

## 🚀 Quick Deploy

### One-Click Docker Deployment (Recommended)

```bash
# 1. Clone the repository
git clone <repository-url>
cd Video-Editor-Bot-V22

# 2. Configure environment
cp .env.example .env
# Edit .env with your Telegram credentials:
# API_ID=your_api_id
# API_HASH=your_api_hash
# BOT_TOKEN=your_bot_token

# 3. Deploy with Docker
docker-compose up -d

# 4. Monitor deployment
docker-compose logs -f video-editor-bot
```

### Manual Deployment

```bash
# 1. Run deployment script
chmod +x deploy.sh
./deploy.sh

# 2. Configure environment
nano .env

# 3. Start bot
./start_bot.sh
```

## 📋 Requirements

### Minimum System Requirements
- **CPU**: 1 core (2+ recommended for faster processing)
- **RAM**: 2GB (4GB+ recommended for large files)
- **Storage**: 10GB free space
- **Network**: Stable internet connection

### Software Requirements
- **FFmpeg**: 4.0+ (installed automatically with Docker)
- **Python 3.8+**: Runtime environment
- **Docker & Docker Compose**: For containerized deployment

### Telegram Credentials
1. **API ID & API Hash**: Get from [my.telegram.org](https://my.telegram.org)
2. **Bot Token**: Get from [@BotFather](https://t.me/BotFather)

## 🤖 Bot Commands

### 📹 Video Encoding (Streaming)
```
/encode          - Show encoding options
/encode720       - Encode to 720p (HD Quality)
/encode480       - Encode to 480p (SD Quality)
/encode360       - Encode to 360p (Mobile Friendly)
/encodehelp      - Detailed encoding help
```

### 🎵 Audio Operations (Streaming)
```
/audio           - Audio operations menu
/extractaudio    - Extract audio from video
/extractMP3      - Extract as MP3 (most compatible)
/extractOGG      - Extract as OGG (open source)
/extractWAV      - Extract as WAV (highest quality)
/addaudio        - Add audio to video (mix with existing)
/replaceaudio    - Replace video audio completely
/audiohelp       - Audio operations help
/cancelaudio     - Cancel audio operation
```

### 📝 Subtitle Operations (Streaming)
```
/subtitle        - Subtitle operations menu
/extractsub      - Extract subtitles from video
/addsub          - Add subtitles to video
/subtitlehelp    - Subtitle operations help
/cancelsub       - Cancel subtitle operation
```

### 🔄 Other Features
```
/start           - Welcome message with features
/help            - Show all available commands
/merge           - Merge multiple videos (existing feature)
/cancel          - Cancel current operation
```

## 📖 Usage Examples

### Example 1: Encode Video to 720p (Streaming)
```
User: /encode720
Bot: 🎯 Selected resolution: 720p (HD)
     📹 Now send me the video file to encode...
     💡 Supported formats: MP4, AVI, MOV, MKV

User: [Sends 500MB video file]
Bot: ⚙️ Encoding video to 720p...
     📊 Status: Encoding video (45% complete)
     ⏱️ Time elapsed: 2m 15s
     📈 Progress: 45%
     ⚡ Processing speed: 3.5 MB/s

Bot: ✅ Video encoded to 720p
     📊 Original: 500.0 MB
     📹 Resolution: 720p
     ⏱️ Total time: 5m 30s
```

### Example 2: Extract Audio (Streaming)
```
User: /extractaudio
Bot: 🎵 Choose audio format:
     1. /extractMP3 - MP3 (Most compatible)
     2. /extractOGG - OGG (Open source)
     3. /extractWAV - WAV (Highest quality)

User: /extractMP3
Bot: 🎯 Selected format: MP3
     📹 Now send me the video file to extract audio from...

User: [Sends video file]
Bot: ⚙️ Extracting MP3 audio...
     📊 Status: Processing audio (80% complete)
     ⏱️ Time elapsed: 1m 45s

Bot: ✅ Audio extracted as MP3
     📊 Original video: 800.0 MB
     🎵 Format: MP3
```

### Example 3: Add Subtitles (Streaming)
```
User: /addsub
Bot: 🎯 Subtitle Embedding Mode
     📝 First, send me the subtitle file (SRT format).

User: [Sends movie.srt file]
Bot: ✅ Subtitle file received!
     📹 Now send me the video file to embed subtitles into...

User: [Sends video file]
Bot: ⚙️ Embedding subtitles...
     📊 Status: Embedding subtitles (60% complete)
     ⏱️ Time elapsed: 3m 20s

Bot: ✅ Subtitles embedded into video
     📊 Original video: 1.2 GB
     📝 Subtitles: Added successfully
```

## 🏗️ Streaming Architecture

### Processing Pipeline
```
User Upload → Telegram Servers → Pyrogram stream_media() →
FFmpeg stdin (pipe:0) → FFmpeg Processing → FFmpeg stdout (pipe:1) →
Bot Upload → User Download
```

### Key Advantages
- **No Local Downloads**: Videos never touch your device storage
- **Memory Efficient**: 1MB chunk processing prevents memory overflow
- **Fast Processing**: Direct streaming without intermediate files
- **Scalable**: Handle large files up to 2GB efficiently
- **Secure**: No residual files left on server

### Technical Implementation
- **Stream Processor**: `bot/utils/stream_processor.py`
- **FFmpeg Commands**: `bot/utils/ffmpeg_stream.py`
- **Progress Tracking**: `bot/utils/progress_tracker.py`
- **Async Operations**: Full asyncio implementation

## 🔧 Configuration

Create a `.env` file:

```bash
# Required: Telegram API Credentials
API_ID=your_api_id_here
API_HASH=your_api_hash_here
BOT_TOKEN=your_bot_token_here

# Optional: Database (for future features)
MONGO_URI=mongodb://localhost:27017/video_editor_bot

# Optional: Logging Channel
LOG_CHANNEL=your_log_channel_id_here

# Processing Configuration
MAX_FILE_SIZE=2147483648  # 2GB in bytes
PROCESSING_TIMEOUT=300     # 5 minutes in seconds
DEBUG=false                # Enable debug logging
LOG_LEVEL=INFO             # Log verbosity
```

## 📊 Performance Benchmarks

### Processing Times (approximate)
- **Small Videos** (<100MB): 30 seconds - 2 minutes
- **Medium Videos** (100MB-500MB): 2 - 8 minutes
- **Large Videos** (500MB-2GB): 8 - 20 minutes

### Resource Usage
- **Memory**: 512MB - 2GB (depending on file size)
- **CPU**: 1 core required, 2+ recommended
- **Storage**: Only temporary files (<100MB)
- **Network**: Stable connection required

### Optimization Tips
1. **Use SSD storage** for better I/O performance
2. **Allocate sufficient RAM** for processing large files
3. **Use multiple CPU cores** for faster encoding
4. **Monitor system resources** during heavy usage

## 🛠️ Development Setup

### Local Development

```bash
# 1. Clone repository
git clone <repository-url>
cd Video-Editor-Bot-V22

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install FFmpeg (if not already installed)
# Ubuntu/Debian:
sudo apt install ffmpeg

# 5. Configure environment
cp .env.example .env
# Edit .env with your credentials

# 6. Run bot
python -m main
```

### Development Commands

```bash
# Code formatting
black bot/

# Linting
flake8 bot/

# Run tests
pytest tests/

# Debug mode
DEBUG=true python -m main
```

## 🔒 Security Features

### Built-in Protections
- ✅ **Input Validation**: All user inputs are validated
- ✅ **File Size Limits**: Configurable maximum file sizes
- ✅ **Processing Timeouts**: Prevent hanging operations
- ✅ **Memory Management**: Chunked processing prevents overflow
- ✅ **Error Handling**: No sensitive information in errors
- ✅ **Resource Limits**: Protection against resource exhaustion

### Security Best Practices
- Use strong, unique API credentials
- Never commit `.env` file to version control
- Regularly update dependencies
- Monitor system resources and logs
- Use firewall to restrict unnecessary access

## 🐛 Troubleshooting

### Common Issues

**Bot Not Starting:**
```bash
# Check configuration
cat .env

# Verify credentials
python3 -c "from configs import API_ID, API_HASH, BOT_TOKEN; print('OK')"

# Check dependencies
pip list
ffmpeg -version
```

**Streaming Processing Failed:**
```bash
# Check FFmpeg functionality
echo "test" | ffmpeg -i pipe:0 -f null - 2>&1

# Check system resources
free -h
htop

# Enable debug mode
# In .env: DEBUG=true, LOG_LEVEL=DEBUG
```

**Memory Issues:**
```bash
# Reduce file size limit
# In .env: MAX_FILE_SIZE=1073741824  # 1GB

# Monitor memory usage
watch -n 1 free -h

# Check Docker limits (if using Docker)
docker stats video-editor-bot
```

### Debug Mode
```bash
# Enable debug logging
# In .env:
DEBUG=true
LOG_LEVEL=DEBUG

# Restart bot to apply changes
```

## 📦 Deployment Options

### 1. Docker (Recommended)
- Easiest setup and maintenance
- Includes all dependencies
- Isolated environment
- Resource management
- Easy scaling

### 2. Manual Deployment
- Full system control
- Custom configurations
- Direct file access
- Performance optimization

### 3. Cloud Deployment
- Heroku, Railway, Okteto support
- Easy scaling options
- Managed infrastructure
- Automatic updates

## 📄 File Structure

```
Video-Editor-Bot-V22/
├── bot/
│   ├── handlers/              # Command handlers
│   │   ├── encode.py         # Video encoding (NEW)
│   │   ├── audio.py          # Audio operations (NEW)
│   │   ├── subtitle.py       # Subtitle operations (NEW)
│   │   ├── start.py          # Start and help commands
│   │   └── merge.py          # Video merging (existing)
│   ├── utils/                # Core utilities
│   │   ├── stream_processor.py    # Streaming logic (NEW)
│   │   ├── ffmpeg_stream.py      # FFmpeg commands (NEW)
│   │   ├── progress_tracker.py   # Progress tracking (NEW)
│   │   └── ffmpeg_utils.py       # FFmpeg utilities
├── main.py                    # Bot entry point
├── configs.py                 # Configuration
├── requirements.txt           # Python dependencies
├── deploy.sh                  # Deployment script
├── docker-compose.yml         # Docker configuration
├── Dockerfile                 # Docker image
├── .env.example              # Environment template
└── README_STREAMING.md       # This file
```

## 🆘 Support

### Getting Help
1. **Bot Commands**: Use `/help` in Telegram for inline help
2. **Specific Help**: `/encodehelp`, `/audiohelp`, `/subtitlehelp`
3. **Documentation**: Check `DEPLOYMENT.md` for detailed setup
4. **Debug Logs**: Enable debug mode for detailed error information

### Common Solutions
- **FFmpeg Issues**: Ensure FFmpeg is properly installed
- **Permission Errors**: Check file and directory permissions
- **Memory Issues**: Reduce MAX_FILE_SIZE or increase system RAM
- **Network Issues**: Verify internet connection and API access

## 🚀 What's New

### v2.2.0 - Streaming Edition
- ✅ **Complete Streaming Architecture**: Process videos without downloading
- ✅ **Resolution Encoding**: 720p, 480p, 360p with quality preservation
- ✅ **Audio Operations**: Extract, add, replace audio tracks
- ✅ **Subtitle Operations**: Extract and embed SRT subtitles
- ✅ **Progress Tracking**: Real-time updates with time estimates
- ✅ **Docker Support**: Complete containerized deployment
- ✅ **Enhanced Error Handling**: Comprehensive error management
- ✅ **Memory Management**: Safe processing of large files
- ✅ **Async Operations**: Non-blocking user experience

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Areas
- Additional video effects and filters
- More audio format support
- Advanced subtitle styling options
- Performance optimizations
- User interface improvements

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Pyrogram**: Excellent Telegram MTProto API framework
- **FFmpeg**: Powerful multimedia processing toolkit
- **Telegram**: For providing the Bot API platform
- **Docker**: Containerization technology
- **Community**: For feedback, testing, and contributions

---

**⭐ Star this repository if you find the streaming technology useful!**

**Made with ❤️ for the Telegram community - Revolutionizing video editing without downloads!**

## 🔗 Quick Links

- **[📖 Full Deployment Guide](DEPLOYMENT.md)** - Detailed deployment instructions
- **[🐳 Docker Hub](https://hub.docker.com/)** - Container images
- **[📚 API Documentation](https://core.telegram.org/bots/api)** - Telegram Bot API
- **[🔧 Pyrogram Docs](https://docs.pyrogram.org/)** - Python Telegram framework
- **[🎬 FFmpeg Docs](https://ffmpeg.org/documentation.html)** - Video processing