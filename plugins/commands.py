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
import english *
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
    #return
    chat_id = message.from_user.id
    if not await database.is_user_exist(chat_id):
        data = await client.get_me()
        BOT_USERNAME = data.username
        await database.add_user(chat_id)
        if -1001645328504:
            await client.send_message(
                -1001645328504,
                f"#NEWUSER: \n\n**User:** [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n\**ID:**{message.from_user.id}\n Started @{BOT_USERNAME} !!",
            )
        else:
            logging.info(f"#NewUser :- Name : {message.from_user.first_name} ID : {message.from_user.id}")
    file_id = "CAACAgUAAxkBAAEFIihiuYjFehkzzJg6fBsp9NSddE2QSQACsAYAAseOyVXbaQF75owUgCkE"
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
  await message.reply_photo("https://telegra.ph/file/6b3bee7715543e8fd6afa.jpg",caption=helps_msg,reply_markup=Help_backbtn)


DATABASE_URI=DATABASE_URI
database = Database(DATABASE_URI, "epic_bot")     
#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
#Callbacks

@Client.on_callback_query()  
async def tgm(bot, update):  
    if update.data == "add": 
        await update.answer(
             text="Epic Devs",
        )
    elif update.data == "DevsCallback":
         await update.message.edit_text(
             text=DEVS_MG,
             reply_markup=DEVS_BTN,
             disable_web_page_preview=True
         )
         await update.answer(
             text="</ᴇᴘɪᴄ ʙᴏᴛs <s/ʟ>🇱🇰",
         )  
    elif update.data == "back_Clbs":
         await update.message.edit_text(
             text=Back_Msg,
             reply_markup=Backbuttons
         )
         await update.answer(
             text="Menu 🔙"
         )
    elif update.data == "HELP_CLB":
         await update.message.edit_text(
             text=helps_msg,
             reply_markup=Help_backbtn
         )
         await update.answer(
             text="This Is Help Menu🌹"
         )
    elif update.data == "HELP_BACK":
         await update.message.edit_text(
             text=Back_Msg,
             reply_markup=Backbuttons
         )
         await update.answer(
             text="Help🔙"
         )
    elif update.data == "START_SI":
         await update.message.edit_text(
             text=SI_STARTM,
             reply_markup=SI_STARB
         )
         await update.answer(
             text="සාදරයෙන් පිළිගනිමු"
         )
    elif update.data == "cloce":
        await update.message.delete()

#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
#State chek

@Client.on_message(filters.command("state") & filters.user(ADMINS))   
async def startprivate(bot, message):
    countb = await database.total_users_count()
    countb = await database.total_users_count()
    count = await bot.get_chat_members_count(-1001620454933)
    counta = await bot.get_chat_members_count(-1001620454933)
    text=f"""**🏅Bot Total Users**
**Members Count In Bot & Chane**
╔═════════════════════════════════════════════╗
   **🌱Chanel Members**  🏅`{count}`
   **⚡Epic App Store Bot Users**  🏅`{countb}`
╚═════════════════════════════════════════════╝
"""

    await bot.send_sticker(message.chat.id, random.choice(STAT_STICKER))
    await bot.send_message(message.chat.id, text=text)


#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
#send mg#

@Client.on_message(filters.command("send"))
async def semrov(bot, message):
    if message.from_user.id not in ADMINS:
        await message.delete()
        return
    mesg=message.reply_to_message
    f= message.text
    s=f.replace('/send ' ,'')
    fid=s.replace('%20', ' ')
    await send_msg(user_id=fid, message=mesg)
    await message.delete()
    await bot.send_message(message.chat.id, text=f"Ur Msg Sent To [User](tg://user?id={fid})", reply_markup=CLOSE_BUTTON)
    await bot.send_message(PRIVATE_LOG,text=f"""#SEND_LOG
• **Send By:** {message.from_user.mention} [`{message.from_user.id}`]
• **Send To:** [User](tg://user?id={fid}) [`{fid}`]
• **Message:-**
""")
    await send_msg(PRIVATE_LOG, message=mesg)

#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#

@Client.on_message(filters.private & filters.text)
async def pm_text(bot, message):
    if message.from_user.id == 5196689118:
        await replay_text(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.send_message(
        chat_id=-1001645328504,
        text=PM_TXT_ATT.format(reference_id, info.first_name, message.text)
    )
    await bot.send_message(
        chat_id=-1001645328504,
        text=PM_TXT_ATT.format(reference_id, info.first_name, message.text)
    )
    

@Client.on_message(filters.private & filters.sticker)
async def pm_media(bot, message):
    if message.from_user.id == 5196689118:
        await replay_media(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.copy_message(
        chat_id=5196689118,
        from_chat_id=message.chat.id,
        message_id=message.id
    )
    await bot.send_message(5196689118, text=PM_TXT_ATTS.format(reference_id, info.first_name))
    await bot.copy_message(
        chat_id=-1001645328504,
        from_chat_id=message.chat.id,
        message_id=message.id
    )
    await bot.send_message(-1001645328504, text=PM_TXT_ATTS.format(reference_id, info.first_name))
    

USER_DETAILS = "<b>PM FROM:</b>\nName: {} {}\nId: {}\nUname: @{}\nScam: {}\nRestricted: {}\nStatus: {}\nDc Id: {}"
PM_TXT_ATT = "<b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}"
PM_TXT_ATTS = "<b>Message from:</b> {}\n<b>Name:</b> {}"
PM_MED_ATT = "<b>Message from:</b> {} \n<b>Name:</b> {}\n<b>Caption</b>:{}"
#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#

@Client.on_message(filters.text & filters.private)
async def send(bot, message):
     await bot.send_message(message.chat.id, f'🔥Search Results For **{message.text}**', reply_markup=InlineKeyboardMarkup([[
                 InlineKeyboardButton("✴️Click Here",switch_inline_query_current_chat=message.text)
                 ]]
                  ))

