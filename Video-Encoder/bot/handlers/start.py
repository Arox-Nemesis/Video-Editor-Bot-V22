"""
Start and Help handlers for Video Encoder Bot
"""

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

def register(app):
    """Register start and help handlers"""

    @app.on_message(filters.command("start") & filters.private)
    async def start_command(client, message: Message):
        """Handle /start command"""
        welcome_text = """
🎬 **Video Encoder Bot**

Edit videos directly on Telegram without downloading them to your device!

🚀 **✨ Amazing Features:**
• 📹 **Video Encoding**: Convert to 720p, 480p, 360p
• 🎵 **Audio Operations**: Extract/add audio tracks
• 📝 **Subtitle Operations**: Extract/embed subtitles
• ⚡ **Streaming**: No downloads required
• 📊 **Progress**: Real-time processing updates

🎯 **Quick Start:**
• `/encode` - Change video resolution
• `/audio` - Audio operations
• `/subtitle` - Subtitle operations
• `/help` - Show all commands

💡 **How it works:**
All processing is done in memory - your videos never touch our servers!

🆘 **Need Help?**
• `/encodehelp` - Encoding help
• `/audiohelp` - Audio help
• `/subtitlehelp` - Subtitle help

**Ready to encode your first video? 🎬**
        """

        await message.reply_text(
            welcome_text,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("📹 Encode Video", callback_data="encode"),
                    InlineKeyboardButton("🎵 Audio Tools", callback_data="audio")
                ],
                [
                    InlineKeyboardButton("📝 Subtitles", callback_data="subtitle"),
                    InlineKeyboardButton("❓ Help", callback_data="help")
                ]
            ])
        )

    @app.on_message(filters.command("help") & filters.private)
    async def help_command(client, message: Message):
        """Handle /help command"""
        help_text = """
🎬 **Video Encoder Bot - Complete Help**

📹 **🔥 Video Encoding:**
• `/encode720` - Convert to 720p HD
• `/encode480` - Convert to 480p SD
• `/encode360` - Convert to 360p Mobile
• `/encodehelp` - Encoding details

🎵 **🎵 Audio Operations:**
• `/extractaudio` - Extract audio from video
• `/extractMP3` - Extract as MP3
• `/extractOGG` - Extract as OGG
• `/extractWAV` - Extract as WAV
• `/addaudio` - Add audio to video
• `/replaceaudio` - Replace video audio
• `/audiohelp` - Audio details

📝 **📝 Subtitle Operations:**
• `/extractsub` - Extract subtitles
• `/addsub` - Add subtitles to video
• `/subtitlehelp` - Subtitle details

🔄 **🔧 Management:**
• `/cancel` - Cancel current operation
• `/status` - Check bot status

💡 **📱 File Support:**
• Video: MP4, AVI, MOV, MKV
• Audio: MP3, OGG, WAV
• Subtitles: SRT files
• Max size: 2GB per file

⚡ **⚡ Features:**
✅ Process videos without downloading
✅ Real-time progress tracking
✅ Multiple resolution options
✅ High-quality audio extraction
✅ Subtitle support
✅ 24/7 availability

🆘 **Need more help?**
• Try any command to see specific help
• Processing is done without file downloads
• Bot works with files up to 2GB

**Start encoding now! 🚀**
        """

        await message.reply_text(
            help_text,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("📹 Try Encoding", callback_data="encode_demo"),
                    InlineKeyboardButton("🎵 Try Audio", callback_data="audio_demo")
                ],
                [
                    InlineKeyboardButton("📝 Try Subtitles", callback_data="subtitle_demo"),
                    InlineKeyboardButton("📖 Full Guide", url="https://github.com/yourusername/video-encoder")
                ]
            ])
        )

    @app.on_callback_query()
    async def handle_callback(client, callback_query):
        """Handle inline keyboard callbacks"""
        data = callback_query.data

        if data == "encode":
            await callback_query.message.edit_text(
                "📹 **Video Encoding**\n\n"
                "Choose your target resolution:\n"
                "• `/encode720` - 720p HD Quality\n"
                "• `/encode480` - 480p SD Quality\n"
                "• `/encode360` - 360p Mobile\n\n"
                "Send a command, then upload your video file!"
            )
        elif data == "audio":
            await callback_query.message.edit_text(
                "🎵 **Audio Operations**\n\n"
                "Available operations:\n"
                "• `/extractaudio` - Extract audio\n"
                "• `/addaudio` - Add audio to video\n"
                "• `/replaceaudio` - Replace audio\n\n"
                "Choose an operation to get started!"
            )
        elif data == "subtitle":
            await callback_query.message.edit_text(
                "📝 **Subtitle Operations**\n\n"
                "Available operations:\n"
                "• `/extractsub` - Extract subtitles\n"
                "• `/addsub` - Add subtitles to video\n\n"
                "Supports SRT subtitle files!"
            )
        elif data == "help":
            help_text = """
🆘 **Quick Help**

**Need to encode a video?**
1. Send `/encode720` (for HD)
2. Upload your video file
3. Wait for processing!

**Need to extract audio?**
1. Send `/extractMP3`
2. Upload your video
3. Get MP3 file!

**Need to add subtitles?**
1. Send `/addsub`
2. Upload SRT file, then video
3. Get video with subtitles!

**All processing is done without downloading files!** ⚡
            """
            await callback_query.message.edit_text(help_text)
        else:
            await callback_query.answer("Coming soon!")

        await callback_query.answer()