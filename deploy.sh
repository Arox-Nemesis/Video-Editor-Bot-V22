#!/bin/bash

# Telegram Video Editor Bot Deployment Script
# This script sets up the bot for production deployment

set -e

echo "🚀 Starting Telegram Video Editor Bot Deployment..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if running as root for system-wide installation
if [[ $EUID -eq 0 ]]; then
   print_warning "Running as root. This will install FFmpeg system-wide."
fi

# Update system packages
print_status "Updating system packages..."
if command -v apt-get &> /dev/null; then
    sudo apt-get update
    sudo apt-get upgrade -y
elif command -v yum &> /dev/null; then
    sudo yum update -y
elif command -v dnf &> /dev/null; then
    sudo dnf update -y
else
    print_warning "Package manager not detected. Please update your system manually."
fi

# Install FFmpeg
print_status "Installing FFmpeg..."
if command -v apt-get &> /dev/null; then
    sudo apt-get install -y ffmpeg
elif command -v yum &> /dev/null; then
    sudo yum install -y epel-release
    sudo yum install -y ffmpeg
elif command -v dnf &> /dev/null; then
    sudo dnf install -y ffmpeg
else
    print_error "FFmpeg installation failed. Please install FFmpeg manually."
    exit 1
fi

# Verify FFmpeg installation
if command -v ffmpeg &> /dev/null; then
    FFMPEG_VERSION=$(ffmpeg -version | head -n 1)
    print_status "FFmpeg installed: $FFMPEG_VERSION"
else
    print_error "FFmpeg installation failed"
    exit 1
fi

# Check Python version
print_status "Checking Python installation..."
PYTHON_VERSION=$(python3 --version 2>&1)
if [[ $? -eq 0 ]]; then
    print_status "Python found: $PYTHON_VERSION"

    # Check if version is 3.8 or higher
    PYTHON_MAJOR=$(python3 -c 'import sys; print(sys.version_info[0])')
    PYTHON_MINOR=$(python3 -c 'import sys; print(sys.version_info[1])')

    if [[ $PYTHON_MAJOR -eq 3 && $PYTHON_MINOR -ge 8 ]]; then
        print_status "Python version is compatible (3.8+)"
    else
        print_error "Python 3.8 or higher is required. Current version: $PYTHON_VERSION"
        exit 1
    fi
else
    print_error "Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Create virtual environment
print_status "Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
print_status "Upgrading pip..."
pip install --upgrade pip

# Install Python dependencies
print_status "Installing Python dependencies..."
pip install -r requirements.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    print_warning ".env file not found. Creating from template..."
    cp .env.example .env
    print_warning "Please edit .env file with your Telegram Bot credentials before running the bot."
    echo ""
    echo "Required configuration:"
    echo "1. Get API_ID and API_HASH from https://my.telegram.org"
    echo "2. Get BOT_TOKEN from @BotFather on Telegram"
    echo "3. Edit .env file with these values"
    echo ""
else
    print_status ".env file found"
fi

# Create necessary directories
print_status "Creating necessary directories..."
mkdir -p temp
mkdir -p logs

# Set permissions
print_status "Setting permissions..."
chmod +x deploy.sh
chmod 755 temp
chmod 755 logs

# Create systemd service file (optional)
if [[ $EUID -eq 0 ]]; then
    print_status "Creating systemd service file..."
    cat > /etc/systemd/system/video-editor-bot.service << EOF
[Unit]
Description=Telegram Video Editor Bot
After=network.target

[Service]
Type=simple
User=bot
WorkingDirectory=$(pwd)
Environment=PATH=$(pwd)/venv/bin
ExecStart=$(pwd)/venv/bin/python -m main
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF
    print_status "Systemd service file created at /etc/systemd/system/video-editor-bot.service"
    print_warning "Remember to create a 'bot' user and adjust file ownership if needed"
fi

# Test the bot configuration
print_status "Testing bot configuration..."
source .env 2>/dev/null || print_warning "Could not load .env file"

if [ -z "$API_ID" ] || [ -z "$API_HASH" ] || [ -z "$BOT_TOKEN" ]; then
    print_warning "Bot credentials not properly configured in .env file"
    print_warning "Please configure API_ID, API_HASH, and BOT_TOKEN in .env file"
else
    print_status "Bot credentials appear to be configured"
fi

# Create startup script
print_status "Creating startup script..."
cat > start_bot.sh << 'EOF'
#!/bin/bash

# Telegram Video Editor Bot Startup Script

# Activate virtual environment
source venv/bin/activate

# Set environment variables
export PYTHONPATH=$(pwd):$PYTHONPATH

# Start the bot
echo "🚀 Starting Telegram Video Editor Bot..."
python -m main
EOF

chmod +x start_bot.sh

# Print deployment summary
echo ""
print_status "🎉 Deployment completed successfully!"
echo ""
echo "📋 Next Steps:"
echo "1. Configure your .env file with Telegram Bot credentials"
echo "2. Test the bot: ./start_bot.sh"
echo "3. For production, consider using the systemd service"
echo ""
echo "📁 Important Files:"
echo "  - .env: Configuration file"
echo "  - start_bot.sh: Startup script"
echo "  - requirements.txt: Python dependencies"
echo "  - logs/: Log files directory"
echo "  - temp/: Temporary files directory"
echo ""
echo "🔧 Management Commands:"
echo "  - Start bot: ./start_bot.sh"
echo "  - Stop bot: Ctrl+C"
echo "  - View logs: tail -f logs/bot.log"
echo "  - Systemd: sudo systemctl start video-editor-bot"
echo ""
echo "📚 Documentation:"
echo "  - Bot commands: /help in Telegram"
echo "  - Help files: Use /encodehelp, /audiohelp, /subtitlehelp"
echo ""
if [[ $EUID -eq 0 ]]; then
    echo "🔧 Systemd Service:"
    echo "  - Start: sudo systemctl start video-editor-bot"
    echo "  - Stop: sudo systemctl stop video-editor-bot"
    echo "  - Status: sudo systemctl status video-editor-bot"
    echo "  - Enable on boot: sudo systemctl enable video-editor-bot"
    echo ""
fi

print_status "Deployment completed! Ready to start your Telegram Video Editor Bot."