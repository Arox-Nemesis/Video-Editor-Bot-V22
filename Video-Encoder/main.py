#!/usr/bin/env python3
"""
🎬 Video Encoder Bot - Main Entry Point

A powerful Telegram bot that encodes videos without downloading them to your device.
Features include resolution encoding, audio extraction/addition, and subtitle handling.

Deployment: https://railway.app (Free hosting)
"""

import logging
import asyncio
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN
from bot.handlers import encode, audio, subtitle, start

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Pyrogram client
app = Client(
    "video_encoder_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

def register_handlers():
    """Register all bot handlers"""
    try:
        # Register handlers
        start.register(app)
        encode.register(app)
        audio.register(app)
        subtitle.register(app)

        logger.info("✅ All handlers registered successfully")
    except Exception as e:
        logger.error(f"❌ Failed to register handlers: {e}")
        raise

async def main():
    """Main bot function"""
    try:
        # Register all handlers
        register_handlers()

        logger.info("🚀 Starting Video Encoder Bot...")
        print("📡 Video Encoder Bot is starting up!")
        print("🎬 Features: Video encoding, audio extraction, subtitle handling")
        print("⚡ Processing: No downloads required - pure streaming!")
        print("🔗 Get your free hosting: https://railway.app")

        # Start the bot
        await app.start()

        # Get bot info
        bot_info = await app.get_me()
        logger.info(f"✅ Bot started successfully: @{bot_info.username}")
        print(f"🎉 Bot is live! @{bot_info.username}")

        # Keep bot running
        await idle()

    except Exception as e:
        logger.error(f"❌ Failed to start bot: {e}")
        print(f"❌ Bot failed to start: {e}")
        raise

async def idle():
    """Keep the bot running"""
    try:
        await asyncio.Event().wait()
    except KeyboardInterrupt:
        logger.info("🛑 Bot stopped by user")
        print("🛑 Bot stopped")

if __name__ == "__main__":
    # Validate configuration
    if not API_ID or not API_HASH or not BOT_TOKEN:
        print("❌ Configuration Error!")
        print("Please set up your environment variables:")
        print("1. API_ID from https://my.telegram.org")
        print("2. API_HASH from https://my.telegram.org")
        print("3. BOT_TOKEN from https://t.me/BotFather")
        print("\nCopy .env.example to .env and fill in your credentials")
        exit(1)

    print("🚀 Video Encoder Bot - Starting...")
    print("📋 Ready to encode videos without downloading!")

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"💥 Fatal error: {e}")
        exit(1)