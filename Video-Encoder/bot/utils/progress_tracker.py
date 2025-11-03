"""
Progress tracking utilities for Video Encoder Bot
"""

import time
import asyncio
from pyrogram import Client
from pyrogram.types import Message

class ProgressTracker:
    """Handles progress reporting for video processing operations"""

    def __init__(self, client: Client, message: Message, operation_name: str):
        self.client = client
        self.message = message
        self.operation_name = operation_name
        self.start_time = time.time()
        self.total_bytes = 0
        self.processed_bytes = 0
        self.last_update_time = 0
        self.update_interval = 5  # Update every 5 seconds
        self.progress_message = None

    async def start_processing(self, estimated_size: Optional[int] = None):
        """Initialize progress tracking"""
        self.estimated_size = estimated_size

        text = f"⚙️ **{self.operation_name} Started**\n\n"
        text += f"⏱️ **Status:** Initializing...\n"
        text += f"📊 **Progress:** 0%"

        self.progress_message = await self.message.reply_text(text)
        self.last_update_time = time.time()

    async def update_progress(self, processed_bytes: int, total_bytes: int):
        """Update progress information"""
        self.processed_bytes = processed_bytes
        self.total_bytes = total_bytes

        current_time = time.time()
        time_since_last_update = current_time - self.last_update_time

        # Only update if enough time has passed
        if time_since_last_update < self.update_interval and processed_bytes < total_bytes:
            return

        elapsed_time = int(current_time - self.start_time)

        # Calculate progress percentage
        if total_bytes > 0:
            progress_percent = min(100, (processed_bytes / total_bytes) * 100)
        else:
            progress_percent = 0

        # Build progress message
        text = f"⚙️ **{self.operation_name} in Progress**\n\n"
        text += f"📊 **Progress:** {progress_percent:.1f}%\n"
        text += f"⏱️ **Time elapsed:** {elapsed_time}s\n"

        # Add file size information
        if self.total_bytes > 0:
            processed_mb = processed_bytes / (1024 * 1024)
            total_mb = total_bytes / (1024 * 1024)
            text += f"📦 **Processed:** {processed_mb:.1f} MB / {total_mb:.1f} MB\n"

        # Add speed calculation
        if elapsed_time > 0 and processed_bytes > 0:
            speed_mbps = (processed_bytes / (1024 * 1024)) / elapsed_time
            text += f"🚀 **Speed:** {speed_mbps:.1f} MB/s"

        # Edit the progress message
        try:
            await self.progress_message.edit_text(text)
            self.last_update_time = current_time
        except Exception:
            # Message might have been deleted or edited by user
            pass

    async def set_phase(self, phase: str):
        """Update the processing phase"""
        if self.progress_message:
            try:
                current_text = self.progress_message.text
                if "Phase:" in current_text:
                    # Replace existing phase
                    lines = current_text.split('\n')
                    for i, line in enumerate(lines):
                        if "Phase:" in line:
                            lines[i] = f"🔄 **Phase:** {phase}"
                            break
                    new_text = '\n'.join(lines)
                else:
                    # Add phase
                    new_text = current_text + f"\n🔄 **Phase:** {phase}"

                await self.progress_message.edit_text(new_text)
            except Exception:
                pass

    async def complete(self, success: bool = True, error_message: Optional[str] = None):
        """Mark processing as complete"""
        elapsed_time = int(time.time() - self.start_time)

        if success:
            text = f"✅ **{self.operation_name} Completed!**\n\n"
            text += f"⏱️ **Total time:** {elapsed_time}s\n"
            text += f"📦 **Status:** Processing completed successfully"
        else:
            text = f"❌ **{self.operation_name} Failed!**\n\n"
            text += f"⏱️ **Time elapsed:** {elapsed_time}s\n"
            if error_message:
                text += f"🔍 **Error:** {error_message}"

        try:
            if self.progress_message:
                await self.progress_message.edit_text(text)
            else:
                await self.message.reply_text(text)
        except Exception:
            # Fallback if message editing fails
            await self.message.reply_text(text)

class EncodeProgressTracker(ProgressTracker):
    """Progress tracker specifically for video encoding"""

    def __init__(self, client: Client, message: Message, target_resolution: str):
        super().__init__(client, message, f"Encoding to {target_resolution}")
        self.target_resolution = target_resolution

    async def complete(self, success: bool = True, error_message: Optional[str] = None):
        if success:
            await self.set_phase(f"Encoding to {self.target_resolution} complete")
        await super().complete(success, error_message)