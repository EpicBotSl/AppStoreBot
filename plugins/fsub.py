from pyrogram.types import *
from pyrogram.errors import *
from info import *
from pyrogram import Client, filters
from pyrogram import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 


async def forcesub(bot, update):
        try:
            await bot.get_chat_member(AUTH_CHANNEL, update.from_user.id)
        except UserNotParticipant:
            file_id = "CAACAgUAAxkBAAEFLhBiwRivNxzc72HIqCe1jxIBr7-5oAAC9QUAAmAVAVa6G5_a1mBwvCkE"
            await bot.send_sticker(update.from_user.id, file_id)
            text = FORCESUB_TEXT
            reply_markup = FORCESUB_BUTTONS
            return await bot.send_message(update.from_user.id,
            text=text,
            reply_markup=reply_markup,
            disable_web_page_preview=True) 

FORCESUB_TEXT = """
        ❌Aƈƈҽʂʂ Dҽɳιҽԃ❌ 
♻️𝐏𝐥𝐞𝐚𝐬𝐞 𝐉𝐨𝐢𝐧 𝐨𝐮𝐫 𝐜𝐡𝐚𝐧𝐞 & 𝐓𝐫𝐲 𝐚𝐠𝐚𝐢𝐧♻️
"""

FORCESUB_BUTTONS = InlineKeyboardMarkup([[
                InlineKeyboardButton('🔰 ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 🔰', url='https://t.me/EpicBotsSl')
            ]])
print("fsub Working")
