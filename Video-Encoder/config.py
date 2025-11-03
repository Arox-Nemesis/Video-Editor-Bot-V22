import os

# Telegram API Configuration
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Processing Configuration
MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", 2147483648))  # 2GB
PROCESSING_TIMEOUT = int(os.getenv("PROCESSING_TIMEOUT", 300))  # 5 minutes

# Optional: Database Configuration (for future features)
MONGO_URI = os.getenv("MONGO_URI", "")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", 0))