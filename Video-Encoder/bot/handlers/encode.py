"""
Video encoding handler for Video Encoder Bot
Converts videos to different resolutions without downloading
"""

from pyrogram import filters
from pyrogram.types import Message
from bot.utils.ffmpeg_utils import encode_video_stream
from bot.utils.progress_tracker import EncodeProgressTracker
from bot.utils.menu_helpers import show_operation_menu, show_error, show_success

# Store user encoding states
user_encoding_states = {}

def register(app):
    """Register encoding handlers"""

    @app.on_message(filters.command("encode") & filters.private)
    async def encode_command(client, message: Message):
        """Show encoding options"""
        options = [
            ("/encode720", "Encode to 720p (HD - Best Quality)"),
            ("/encode480", "Encode to 480p (SD - Good Balance)"),
            ("/encode360", "Encode to 360p (Mobile - Small Size)")
        ]

        await show_operation_menu(
            client,
            message,
            "🎬 Video Resolution Encoding",
            "Convert your videos to different resolutions without downloading!",
            options
        )

    @app.on_message(filters.command(["encode720", "encode480", "encode360"]) & filters.private)
    async def encode_resolution_command(client, message: Message):
        """Handle specific resolution encoding commands"""
        user_id = message.from_user.id
        command = message.command[0]

        # Extract resolution from command
        resolution = command.replace("encode", "")

        # Resolution details
        resolution_info = {
            '720p': {'name': '720p HD', 'quality': 'High', 'size_reduction': '~40%'},
            '480p': {'name': '480p SD', 'quality': 'Medium', 'size_reduction': '~60%'},
            '360p': {'name': '360p Mobile', 'quality': 'Good', 'size_reduction': '~75%'}
        }

        if resolution not in resolution_info:
            await show_error(
                client,
                message,
                "Invalid Resolution",
                "Please use: /encode720, /encode480, or /encode360"
            )
            return

        # Store user's encoding preference
        user_encoding_states[user_id] = {
            'resolution': resolution,
            'stage': 'waiting_for_video',
            'info': resolution_info[resolution]
        }

        info = resolution_info[resolution]
        text = f"🎯 **Selected Resolution:** {info['name']}\n\n"
        text += f"📊 **Quality:** {info['quality']}\n"
        text += f"📉 **Size Reduction:** {info['size_reduction']}\n\n"
        text += f"📹 **Now send me the video file you want to encode to {resolution}**\n\n"
        text += "💡 **Supported formats:** MP4, AVI, MOV, MKV\n"
        text += f"⚖️ **Max file size:** 2GB\n"
        text += "⏱️ **Processing time:** Depends on file size (usually 1-10 minutes)"

        await message.reply_text(text)

    @app.on_message(filters.video & filters.private)
    async def handle_video_encoding(client, message: Message):
        """Handle video file for encoding"""
        user_id = message.from_user.id

        # Check if user is in encoding process
        if user_id not in user_encoding_states:
            return  # Not part of encoding operation

        state = user_encoding_states[user_id]
        if state['stage'] != 'waiting_for_video':
            return

        resolution = state['resolution']
        info = state['info']

        # Validate video file
        if not message.video:
            await show_error(
                client,
                message,
                "Invalid File",
                "Please send a video file, not a photo or document"
            )
            return

        # Check file size
        file_size = message.video.file_size
        max_size = 2 * 1024 * 1024 * 1024  # 2GB

        if file_size > max_size:
            await show_error(
                client,
                message,
                "File Too Large",
                f"Maximum file size is {max_size / (1024**3):.1f}GB. Your file is {file_size / (1024**3):.1f}GB."
            )
            return

        # Start processing
        try:
            # Create progress tracker
            tracker = EncodeProgressTracker(client, message, resolution)

            # Estimate output size
            estimated_size = file_size * 0.6  # Rough estimate

            # Start tracking
            await tracker.start_processing(estimated_size)

            # Process video with streaming
            await tracker.set_phase(f"Encoding to {resolution}")

            result = await encode_video_stream(
                client=client,
                message=message,
                resolution=resolution,
                caption=f"✅ **Video Encoded Successfully!**\n\n"
                       f"🎯 **Resolution:** {info['name']}\n"
                       f"📊 **Quality:** {info['quality']}\n"
                       f"📉 **Size reduced by:** {info['size_reduction']}\n"
                       f"📏 **Original:** {file_size / (1024*1024):.1f} MB\n"
                       f"⚡ **Processing:** No downloads required!"
            )

            # Mark as complete
            await tracker.complete(success=True)

            # Clean up user state
            user_encoding_states.pop(user_id, None)

            # Send follow-up message
            await show_success(
                client,
                message,
                "Encoding Complete!",
                f"Your video has been encoded to {info['name']} without downloading to any device. Try another video!"
            )

        except Exception as e:
            # Handle errors
            await tracker.complete(success=False, error_message=str(e))
            await show_error(
                client,
                message,
                "Encoding Failed",
                f"Sorry, I couldn't encode your video. Error: {str(e)}\n\nPlease try again with a different video or smaller file."
            )

            # Clean up user state
            user_encoding_states.pop(user_id, None)

    @app.on_message(filters.command("cancel") & filters.private)
    async def cancel_encoding(client, message: Message):
        """Cancel current encoding operation"""
        user_id = message.from_user.id

        if user_id in user_encoding_states:
            user_encoding_states.pop(user_id, None)
            await message.reply_text("❌ **Encoding operation cancelled**\n\nSend `/encode` to start a new encoding operation.")
        else:
            await message.reply_text("ℹ️ **No active encoding operation to cancel**\n\nSend `/encode` to start encoding a video.")

    @app.on_message(filters.command("encodehelp") & filters.private)
    async def encode_help_command(client, message: Message):
        """Show detailed encoding help"""
        help_text = """
🎬 **Video Encoding Help**

**🎯 What is Video Encoding?**
Video encoding converts your video to different resolutions and qualities. This helps:
• Reduce file size for easier sharing
• Convert videos for different devices
• Save storage space while maintaining quality

**📹 Available Resolutions:**

**🔥 /encode720 - 720p HD**
• **Best quality** with reasonable file size
• **Perfect for:** YouTube, social media, watching on TV
• **Size reduction:** ~40% smaller than original
• **Recommended for:** High-quality videos

**⚖️ /encode480 - 480p SD**
• **Balanced quality and size**
• **Perfect for:** WhatsApp, Telegram sharing, mobile viewing
• **Size reduction:** ~60% smaller than original
• **Recommended for:** Everyday use

**📱 /encode360 - 360p Mobile**
• **Smallest file size**
• **Perfect for:** Limited storage, slow internet, old devices
• **Size reduction:** ~75% smaller than original
• **Recommended for:** Maximum compression

**📋 How to Use:**
1. Send `/encode720`, `/encode480`, or `/encode360`
2. Upload your video file (MP4, AVI, MOV, MKV)
3. Wait for processing to complete
4. Download your encoded video

**⚡ Key Features:**
✅ **No Downloads:** Processing happens in memory only
✅ **Fast Processing:** Usually 1-10 minutes depending on file size
✅ **Quality Preserved:** Maintains original aspect ratio
✅ **Audio Kept:** Original audio track is preserved
✅ **Progress Tracking:** See real-time processing status

**📊 File Information:**
• **Max file size:** 2GB
• **Processing timeout:** 5 minutes
• **Supported formats:** MP4, AVI, MOV, MKV
• **Output format:** MP4 (compatible with all devices)

**🔧 Tips:**
• Choose 720p for best quality
• Choose 480p for balanced size and quality
• Choose 360p for smallest file size
• Processing time depends on video length and resolution

**❓ Common Questions:**
**Q: Does the bot download my video?**
A: No! All processing is done in memory without downloading.

**Q: What happens to the original quality?**
A: The video is converted to your chosen resolution while maintaining good quality.

**Q: Can I process large videos?**
A: Yes, up to 2GB files are supported.

**Q: How long does it take?**
A: Usually 1-10 minutes depending on file size and complexity.

**Ready to encode your first video?**
Send `/encode720`, `/encode480`, or `/encode360` to begin!
        """

        await message.reply_text(help_text)