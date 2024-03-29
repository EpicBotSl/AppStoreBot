import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')

API_ID = environ['API_ID']
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
PRIVATE_LOG = environ['PRIVATE_LOG']
# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
OWNER_ID = environ['OWNER_ID']
LOG_CHANNEL = environ['LOG_CHANNEL']

# Messages
default_start_msg = """
**Hi, I'm Media Search bot**
Here you can search files in inline mode. Just press following buttons and start searching.
"""

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = environ.get('INVITE_MSG', 'Please join @EpicBotsSl to use this bot')
