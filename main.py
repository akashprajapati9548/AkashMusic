# main.py

import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from config import Config

# Load environment variables from .env file
load_dotenv()

# Create Pyrogram Client instance
app = Client(
    name="music_bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
)

# /start command handler
@app.on_message(filters.command("start") & filters.private)
async def start_handler(client: Client, message: Message):
    user = message.from_user
    await message.reply_photo(
        photo="https://telegra.ph/file/bb95fa8ecad2696b0440c.jpg",  # Replace with your image if you want
        caption=(
            f"👋 Hello {user.first_name}!\n\n"
            "I'm a powerful Telegram music bot. Add me to your group and enjoy high-quality music!\n\n"
            "Use /help to see available commands."
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👤 Owner", url=Config.OWNER_URL),
                    InlineKeyboardButton("💬 Support", url=Config.SUPPORT_CHAT_URL),
                    InlineKeyboardButton("📢 Updates", url=Config.UPDATES_CHANNEL_URL),
                ]
            ]
        )
    )

# Run the bot
if name == "main":
    print("🎧 Bot is starting...")
    app.run()
