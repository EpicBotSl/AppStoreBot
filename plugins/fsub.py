from pyrogram.types import *
from pyrogram.errors import *
from config import *
from pyrogram import *
from pyrogram import InlineKeyboardMarkup, InlineKeyboardButton 


async def forcesub(bot, update):
        try:
            await bot.get_chat_member(force_subchannel, update.from_user.id)
        except UserNotParticipant:
            file_id = "CAACAgUAAxkBAAEFIihiuYjFehkzzJg6fBsp9NSddE2QSQACsAYAAseOyVXbaQF75owUgCkE"
            await bot.send_sticker(update.from_user.id, file_id)
            text = FORCESUB_TEXT
            reply_markup = FORCESUB_BUTTONS
            return await bot.send_message(update.from_user.id,
            text=text,
            reply_markup=reply_markup,
            disable_web_page_preview=True) 

FORCESUB_TEXT = "WTF Join Our Chanel humm 😒.."

FORCESUB_BUTTONS = InlineKeyboardMarkup([
[InlineKeyboardButton('Join Chanel🌱', url='https://t.me/EpicBotsSl)]
])

print("fsub Working")
