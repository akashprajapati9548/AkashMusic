from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import Config

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client, message: Message):
    user = message.from_user

    await message.reply_photo(
        photo="https://telegra.ph/file/21d27866c00a6e6bcb5ca.jpg",  # You can replace with your own image
        caption=(
            f"✨ Hello {user.first_name}!\n\n"
            "🎧 I'm a high-quality Telegram Music Bot designed to stream music in your group voice chats.\n\n"
            "Features:\n"
            "• Play music from YouTube\n"
            "• Easy command system\n"
            "• Fast and stable performance\n\n"
            "⚡ Developed with ❤️ by Rishant Thakur"
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👑 Owner", url="https://t.me/oy_baby"),
                    InlineKeyboardButton("💬 Support", url="https://t.me/ganaasupport"),
                    InlineKeyboardButton("📢 Updates", url="https://t.me/ganaasupport"),
                ]
            ]
        )
    )
