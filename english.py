import os
import random

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *

#Buttons & Msgs

DEVS_BTN = InlineKeyboardMarkup([[
                 InlineKeyboardButton('Navanjana', url='https://t.me/NA_VA_N_JA_NA1'),
                 InlineKeyboardButton('Wisula', url='https://t.me/wisula4')
                 ],
                 [
                 InlineKeyboardButton('π', callback_data="back_Clbs")
                 ]]
                  )

DEVS_MG = "π±We Are epic Developers π"

helps_msg = """
βΈππππ πΈπ π΄πππ π°ππ πππππ π±πππ π·πππ πππππππ!
How to Use me 
Ex:- `Minecraft`
πYes It Simple Normally Send App No to bot 

**ππππ π²ππ π³π ππππ π±ππ?**
β‘ππππ π±ππ ππππ π±π πππππππ πΎπ πΎπ ππ πππ ππππππππ.
β‘ππππ π±ππ π·πππ 
      βͺπΌππ π°πππ
      βͺπΏππππππ π°πππ
      βͺπ»ππππ π°πππ
β‘ππππ π±ππ ππππ πΎπ½ πΈπππππ πΌπππ ππ ππππ πΈπππππ πΌπππ π°π ππππππ π°πππ
βπΌπππ πππππππ 
     β« @EpicBotsSl
βπππππππππ 
     β« @EpicChats
βπ°ππ π³πππππππ 
     β« @EpicApkDatabase
     
                  `π€πππΌ π£πΎππΎππππΎππ π’ππππΊππΊπππππ±π°`
"""

HelpBack_Btn = InlineKeyboardMarkup([[
                InlineKeyboardButton('π', callback_data="HELP_BACK")
            ]])

ENSTART_BTN = InlineKeyboardMarkup([[
                InlineKeyboardButton('πHELPπ', callback_data="HELP_CLB")
            ],
            [
                InlineKeyboardButton('πApk Databaseπ', url='https://t.me/EpicApkDatabase'),
                InlineKeyboardButton('π©βπ»Bot Devsπ©βπ»', callback_data="DevsCallback")
            ],
            [
                InlineKeyboardButton('</α΄α΄Ιͺα΄ Κα΄α΄s <s/Κ>π±π°', url='https://t.me/EpicBotsSl')
            ],
            [
                InlineKeyboardButton('πSearch hereπ', switch_inline_query_current_chat=''),
                InlineKeyboardButton('βοΈGo inlineβοΈ', switch_inline_query='')
            ],
            [ 
                InlineKeyboardButton('π Switch Language', callback_data="SI_CHANGE")
            ]
        ])

ENSTART_MSG = "Hi Welcome to **Epic App Store Bot**π­ βClick Help To more Helpsβ‘"

STAT_STICKER = ["CAACAgQAAxkBAAEFHRditZFgRBAPm-9bkFJUQKOjSEgxoQACfwsAAmgpeVF2roP_0GLhzykE",
                "CAACAgQAAxkBAAEFHRVitZFYQ_EPOF7Y1GenAAHZOfu6xNIAAj4MAAKd3llQRh5-qJlCwa0pBA",
                "CAACAgQAAxkBAAEFHRNitZFVEBwdq0uFJDOvDRx2IzdoCwAC5wwAAubdSFEk6BkQ4EbQ1ikE",
                "CAACAgQAAxkBAAEFHRFitZFRwzQPYrVUQkxVP4yxF2Uw3gAC4AkAAu9GYFGTgHavjO_HLikE",
                "CAACAgQAAxkBAAEFHQ9itZFNixLf7fEZICaK8DF-Li967wACUAwAAmEq4VF8xFsUvkvQXSkE"              
         ]  

CLOSE_BUTTON = InlineKeyboardMarkup([[
                InlineKeyboardButton('cloce', callback_data="cloce")
            ]])
