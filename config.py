# config.py

import os

class Config:
    # Telegram Bot Token (from BotFather)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token_here")

    # Telegram API ID and Hash (from my.telegram.org)
    API_ID = int(os.environ.get("API_ID", 123456))
    API_HASH = os.environ.get("API_HASH", "your_api_hash_here")

    # Your Telegram user ID (to make yourself admin)
    OWNER_ID = int(os.environ.get("OWNER_ID", 123456789))

    # MongoDB URI for database (optional)
    MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/yourdbname")

    # Pyrogram Session string (optional)
    SESSION_STRING = os.environ.get("SESSION_STRING", "")

    # Duration limits in minutes
    DURATION_LIMIT = int(os.environ.get("DURATION_LIMIT", 180))  # default: 3 hours

    # Logging group/chat ID
    LOG_GROUP_ID = int(os.environ.get("LOG_GROUP_ID", -1001234567890))

    # Command prefix
    COMMAND_PREFIX = "/"

    # Spotify API (optional)
    SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID", "")
    SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET", "")

    # === Custom Buttons (URLs) ===
    OWNER_URL = os.environ.get("OWNER_URL", "https://t.me/YourOwnerUsername")
    SUPPORT_CHAT_URL = os.environ.get("SUPPORT_CHAT_URL", "https://t.me/YourSupportGroup")
    UPDATES_CHANNEL_URL = os.environ.get("UPDATES_CHANNEL_URL", "https://t.me/YourUpdatesChannel")
