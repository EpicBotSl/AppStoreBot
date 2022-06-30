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


#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
#Callbacks

@Client.on_callback_query()  
async def tgm(bot, update):  
    if update.data == "add": 
        await update.answer(
             text="Epic Devs",
        )
    elif update.data == "START_EN":
         await update.message.edit_text(
             text=ENSTART_MSG,
             reply_markup=ENSTART_BTN,
             disable_web_page_preview=True
         )
         await update.answer(
             text="Bot Started In English 🇬🇧",
         )  
    elif update.data == "HELP_CLB":
         await update.message.edit_text(
             text=helps_msg,
             reply_markup=HelpBack_Btn
         )
         await update.answer(
             text=" Welcome to Help Menu 🌱"
         )
    elif update.data == "HELP_BACK":
         await update.message.edit_text(
             text=ENSTART_MSG,
             reply_markup=ENSTART_BTN
         )
         await update.answer(
             text="Help Menu Backed 🖐️"
         )
    elif update.data == "DevsCallback":
         await update.message.edit_text(
             text=DEVS_MG,
             reply_markup=DEVS_BTN
         )
         await update.answer(
             text="</ᴇᴘɪᴄ ʙᴏᴛs <s/ʟ>🇱🇰"
         )
    elif update.data == "SI_CHANGE":
         await update.message.edit_text(
             text=STARTCMD,
             reply_markup=COMMAND_LANGBTN
         )
         await update.answer(
             text="Switch Language 🔄"
         )
    elif update.data == "START_SI":
         await update.message.edit_text(
             text=SI_STARTM,
             reply_markup=SI_STARB
         )
         await update.answer(
             text="ස:අපිට අපි ස:ට😏"
         )
    elif update.data == "SIHELP_CLB":
         await update.message.edit_text(
             text=SIHELP_MSG,
             reply_markup=SIHelp_backbtn
         )
         await update.answer(
             text="ආයි බොක්කෙන්ම ඈ මේ උදව්ව"
         )
    elif update.data == "SIHELP_BACK":
         await update.message.edit_text(
             text=SI_STARTM,
             reply_markup=SI_STARB
         )
         await update.answer(
             text="මේ සැප ලෝකේ 🤭"
         )
    elif update.data == "Si_Devs":
         await update.message.edit_text(
             text=DEVS_MGSI,
             reply_markup=DEVS_BTNSI
         )
         await update.answer(
             text="ගැම්මක් තමයි හරිත😌"
         )
    elif update.data == "SiDEVS_BAC":
         await update.message.edit_text(
             text=SI_STARTM,
             reply_markup=SI_STARB
         )
         await update.answer(
             text="මේ සැප ලෝකේ 🤭"
         )
    elif update.data == "CHANGE_LNG":
         await update.message.edit_text(
             text=STARTCMD,
             reply_markup=COMMAND_LANGBTN
         )
         await update.answer(
             text="මේ සැප ලෝකේ 🤭"
         )
    elif update.data == "back_Clbs":
         await update.message.edit_text(
             text=ENSTART_MSG,
             reply_markup=ENSTART_BTN
         )
         await update.answer(
             text="Menu Backed 🔙"
         )
    elif update.data == "cloce":
        await update.message.delete()

#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=
