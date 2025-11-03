"""
FFmpeg utilities for Video Encoder Bot
Handles video encoding without downloads
"""

import subprocess
import tempfile
import os
from typing import Optional

def get_resolution_encode_cmd(resolution: str) -> list:
    """Get FFmpeg command for resolution encoding"""
    resolution_settings = {
        '720p': {'width': 1280, 'height': 720, 'bitrate': '2000k'},
        '480p': {'width': 854, 'height': 480, 'bitrate': '1000k'},
        '360p': {'width': 640, 'height': 360, 'bitrate': '500k'}
    }

    if resolution not in resolution_settings:
        raise ValueError(f"Unsupported resolution: {resolution}")

    settings = resolution_settings[resolution]

    return [
        'ffmpeg', '-i', 'pipe:0',  # Read from stdin
        '-vf', f'scale={settings["width"]}:{settings["height"]}',  # Scale
        '-c:v', 'libx264',  # Video codec
        '-preset', 'medium',  # Encoding speed
        '-crf', '23',  # Quality
        '-maxrate', settings['bitrate'],  # Max bitrate
        '-bufsize', f'{int(settings["bitrate"][:-1]) * 2}k',  # Buffer
        '-pix_fmt', 'yuv420p',  # Pixel format
        '-c:a', 'aac',  # Audio codec
        '-b:a', '128k',  # Audio bitrate
        '-ar', '44100',  # Sample rate
        '-f', 'mp4',  # Output format
        '-movflags', 'faststart',  # Optimize for streaming
        'pipe:1'  # Write to stdout
    ]

async def encode_video_stream(client, message, resolution: str, caption: Optional[str] = None):
    """Encode video to specified resolution using streaming"""
    try:
        # Get FFmpeg command
        cmd = get_resolution_encode_cmd(resolution)

        # Create temporary file for output (Pyrogram needs file path)
        with tempfile.NamedTemporaryFile(suffix='.mp4', delete=False) as temp_file:
            temp_path = temp_file.name

        # Download and process video
        file_path = await message.download()

        # Run FFmpeg command
        subprocess.run(
            ['ffmpeg', '-i', file_path] + cmd[1:] + [temp_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Clean up input file
        os.unlink(file_path)

        # Send result back to user
        final_caption = caption or f"✅ Video encoded to {resolution}"

        await message.reply_video(
            temp_path,
            caption=final_caption
        )

        # Clean up temp file
        os.unlink(temp_path)

    except Exception as e:
        # Clean up on error
        if 'file_path' in locals():
            try:
                os.unlink(file_path)
            except:
                pass
        if 'temp_path' in locals():
            try:
                os.unlink(temp_path)
            except:
                pass
        raise e

def get_supported_resolutions():
    """Get list of supported video resolutions"""
    return ['720p', '480p', '360p']

def validate_resolution(resolution):
    """Validate if resolution is supported"""
    return resolution in get_supported_resolutions()

def estimate_output_size(input_size, resolution):
    """Estimate output file size based on resolution"""
    size_factors = {
        '720p': 0.6,
        '480p': 0.4,
        '360p': 0.25
    }
    return input_size * size_factors.get(resolution, 0.5)