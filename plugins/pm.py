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

@Client.on_message(filters.chat(LOG_CHANNEL) & filters.command("info"))
async def replay_media(bot, message):
    file = message.reply_to_message
    reference_id = file.text.split()[2]
    info = await bot.get_users(user_ids=reference_id)
    await bot.send_message(message.from_user.id, text=f"""
    **User Info**
    
    **••User id:** [`{info.id}`]
    **••First Name:** {info.first_name}
    **••UserName:** @{info.username}
    
    """)

@Client.on_message(filters.private & filters.text)
async def pm_text(bot, message):
    if message.from_user.id == OWNER_ID:
        await reply_text(bot, message)
        return
    if await forcesub(bot, message):
       return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.send_message(
        chat_id=OWNER_ID,
        text=PM_TXT_ATT.format(reference_id, info.first_name, message.text)
    )
    await bot.send_message(
        chat_id=LOG_CHANNEL,
        text=PM_TXT_ATT.format(reference_id, info.first_name, message.text)
    )
    

@Client.on_message(filters.private & filters.sticker)
async def pm_sticker(bot, message):
    if message.from_user.id == OWNER_ID:
        await replay_media(bot, message)
        return
    if await forcesub(bot, message):
       return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.copy_message(
        chat_id=OWNER_ID,
        from_chat_id=message.chat.id,
        message_id=message.id
    )
    await bot.send_message(OWNER_ID, text=PM_TXT_ATTS.format(reference_id, info.first_name))
    await bot.copy_message(
        chat_id=LOG_CHANNEL,
        from_chat_id=message.chat.id,
        message_id=message.id
    )
    await bot.send_message(LOG_CHANNEL, text=PM_TXT_ATTS.format(reference_id, info.first_name))
    
@Client.on_message(filters.private & filters.media)
async def pm_media(bot, message):
    if message.from_user.id == OWNER_ID:
        await replay_media(bot, message)
        return
    if await forcesub(bot, message):
       return
    await message.reply_text(text=f"Ur Photo Sent To @{force_subchannel} Admins", reply_markup=CLOSE_BUTTON)
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    msg=message.caption
    await bot.copy_message(
        chat_id=OWNER_ID,       
        from_chat_id=message.chat.id,
        message_id=message.id,
        caption=PM_MED_ATT.format(reference_id, message.from_user.mention, msg)
    )

#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
USER_DETAILS = "<b>PM FROM:</b>\nName: {} {}\nId: {}\nUname: @{}\nScam: {}\nRestricted: {}\nStatus: {}\nDc Id: {}"
PM_TXT_ATT = "<b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}"
PM_TXT_ATTS = "<b>Message from:</b> {}\n<b>Name:</b> {}"
PM_MED_ATT = "<b>Message from:</b> {} \n<b>Name:</b> {}\n<b>Caption</b>:{}"
#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#

