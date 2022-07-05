import re
import uuid
import socket
import platform
import time
import math
import json
import string
import traceback
import psutil
import asyncio
import wget
import motor.motor_asyncio
import pymongo
import aiofiles
import datetime
import os
import random
import logging
from sinhala import *
from english import *
from plugins.fsub import *
from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram.types import *
from helper.decorators import humanbytes
from asyncio import *
import requests
from utils.database import Database
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import *
from pyrogram.types import Message

from info import START_MSG, CHANNELS, ADMINS, INVITE_MSG, DATABASE_URI, PRIVATE_LOG
from utils import Media, unpack_new_file_id

logger = logging.getLogger(__name__)

async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : user is blocked\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception as e:
        return 500, f"{user_id} : {traceback.format_exc()}\n"
        

@Client.on_message(filters.command("start"))
async def startprivates(client, message):
    if await forcesub(client, message):
       return
    chat_id = message.from_user.id
    if not await database.is_user_exist(chat_id):
        data = await client.get_me()
        BOT_USERNAME = data.username
        await database.add_user(chat_id)
        if -1001741009206:
            await client.send_message(
                -1001741009206,
                f"#NEWUSER: \n\n**User:** [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n\**ID:**{message.from_user.id}\n Started @{BOT_USERNAME} !!",
            )
        else:
            logging.info(f"#NewUser :- Name : {message.from_user.first_name} ID : {message.from_user.id}")
    file_id = "CAACAgEAAxkBAAEFMjNixCgfZ2QSo2CR9f-O-jbi2C5KUwACogAEl8MXWi2okCDiQEMpBA"
    await message.delete()
    await client.send_sticker(message.chat.id, file_id)
    text = f"Hi {message.from_user.mention}, 🌼Choose language To Continue "
    reply_markup = COMMAND_LANGBTN
    await message.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )
        
        
@Client.on_message(filters.command("help"))
async def help(bot, message):
  await message.delete()
  await bot.send_sticker(message.chat_id, "CAACAgEAAxkBAAEFMjNixCgfZ2QSo2CR9f-O-jbi2C5KUwACogAEl8MXWi2okCDiQEMpBA")
  await message.reply_photo("https://telegra.ph/file/6b3bee7715543e8fd6afa.jpg",caption=helps_msg,reply_markup=HelpBack_Btn)


DATABASE_URI=DATABASE_URI
database = Database(DATABASE_URI, "epic_bot") 
    
#•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
#State chek

@Client.on_message(filters.command("state") & filters.user(ADMINS))   
async def startprivate(bot, message):
    countb = await database.total_users_count()
    countb = await database.total_users_count()
    count = await bot.get_chat_members_count(-1001620454933)
    counta = await bot.get_chat_members_count(-1001620454933)
    text=f"""**🏅Bot Total Users**
**Members Count In Bot & Chanel**
╔═════════════════════════════════════════════╗
   **🌱Chanel Members**  🏅`{count}`
   **⚡Epic App Store Bot Users**  🏅`{countb}`
╚═════════════════════════════════════════════╝
"""
    await bot.send_sticker(message.chat.id, random.choice(STAT_STICKER))
    await bot.send_message(message.chat.id, text=text)

#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
print("Commands.py Started🔥🌹")
