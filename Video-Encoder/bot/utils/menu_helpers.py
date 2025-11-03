"""
Menu helper functions for Video Encoder Bot
"""

from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

async def show_operation_menu(client: Client, message: Message, title: str, description: str, options: list):
    """
    Show a formatted menu of operation options

    Args:
        client: Pyrogram client
        message: Original message
        title: Menu title
        description: Menu description
        options: List of tuples (command, description)
    """
    text = f"🎬 **{title}**\n\n"
    text += f"📝 {description}\n\n"
    text += "**🎯 Available Options:**\n\n"

    keyboard_buttons = []
    current_row = []

    for i, (command, desc) in enumerate(options, 1):
        text += f"**{i}.** `{command}` - {desc}\n"

        # Create inline keyboard button
        button_text = command.replace("/", "").upper()
        current_row.append(InlineKeyboardButton(button_text, callback_data=command[1:]))

        # Add to keyboard (2 buttons per row)
        if len(current_row) == 2:
            keyboard_buttons.append(current_row)
            current_row = []

    # Add remaining buttons
    if current_row:
        keyboard_buttons.append(current_row)

    text += "\n💡 **Send a command or click the buttons below to start!**"

    # Add help button
    keyboard_buttons.append([InlineKeyboardButton("❓ Help", callback_data="help")])

    await message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard_buttons)
    )

async def show_error(client: Client, message: Message, operation: str, error: str):
    """
    Show a formatted error message

    Args:
        client: Pyrogram client
        message: Original message
        operation: Operation that failed
        error: Error description
    """
    text = f"❌ **{operation} Failed!**\n\n"
    text += f"🔍 **Error:** {error}\n\n"
    text += "💡 **What to do:**\n"
    text += "• Check your file format and size\n"
    text += "• Try with a smaller file\n"
    text += "• Use `/help` for more information\n\n"
    text += "🆘 **Need help?** Send `/help` to see all commands"

    await message.reply_text(text)

async def show_success(client: Client, message: Message, operation: str, details: str = ""):
    """
    Show a formatted success message

    Args:
        client: Pyrogram client
        message: Original message
        operation: Operation that succeeded
        details: Additional details
    """
    text = f"✅ **{operation} Successful!**"

    if details:
        text += f"\n\n{details}"

    text += "\n\n💡 **Try another video!** Send `/encode` to start a new operation."

    await message.reply_text(text)