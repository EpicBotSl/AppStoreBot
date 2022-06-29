import os
import random

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *

STARTCMD = "🌼Choose language To Start bot!"

COMMAND_LANGBTN = InlineKeyboardMarkup([[
      InlineKeyboardButton('සිංහල 🇱🇰', callback_data="START_SI")
      ],
      [
      InlineKeyboardButton('ENGLISH 🇬🇧', callback_data="START_SI")
      ]])

#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
#START_SI Callback Text & Btn

SI_HELP = InlineKeyboardMarkup([[
                InlineKeyboardButton('පෙර මෙනුවට පිවිසෙන්න', callback_data="HELP_BACK")
            ]])

SI_STARB = InlineKeyboardMarkup([[
                InlineKeyboardButton('උදව්❔', callback_data="SIHELP_CLB")
            ],
            [
                InlineKeyboardButton('👩‍💻අපගේ ඇප්ප් ඩේටාබේස් එක👩‍💻', url='https://t.me/EpicApkDatabase'),
                InlineKeyboardButton('බොට් ඩිවලොපර්ස්', callback_data="Si_Devs")
            ],
            [
                InlineKeyboardButton('</ᴇᴘɪᴄ ʙᴏᴛs <s/ʟ>🇱🇰', url='https://t.me/EpicBotsSl')
            ],
            [
                InlineKeyboardButton('🔍ඇප් සර්ච් කරම්න🔄', switch_inline_query_current_chat=''),
                InlineKeyboardButton('↗️ශෙයාර් කරපම්↗️', switch_inline_query='')
            ],
            [
                InlineKeyboardButton('🔄Switch Language', callback_data="CHANGE_LNG")
            ]
        ])

SI_STARTM = "Hi සාදරයෙන් පිළිගනිමු **Epic App Store Bot**🎭 ✓වැඩිදුර උදවු සඳහා උදවු ක්ලික් කරන්න⚡"

#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
SIHELP_MSG = """
⸙ ඔබට අවශ්‍ය app මෙහිදී ලබාගත හැක!

**📖කොහොමද ඇප් search කරන්නෙ ?**
ඔබට අවශ්‍ය ඇප් එකේ නම ලබාදෙන්න

උදා:- `Minecraft`

🪶මේ විදියට normal බොට් ට රිප්ලයි කරන්න එවිට ඔබ ලැබෙන මෙනුව මගින් ඔබට ඔබේ ඇනවුම ලබාගත හැක !


➡බොට් Run වෙන්නෙ අපේ App database එකක් මත
➡අප සතුව,
      ▪𝙼𝚘𝚍 𝙰𝚙𝚔𝚜
      ▪𝙿𝚛𝚎𝚖𝚒𝚞𝚖 𝙰𝚙𝚔𝚜
      ▪𝙻𝚊𝚛𝚐𝚎 𝙰𝚙𝚔𝚜
විශාල ප්‍රමානයක් ඇත.

➡මේ බොට් inline ක්‍රමයට බාවිතා කිරීම වඩාත් සාර්තකය.

✔𝙼𝚘𝚛𝚎 𝚄𝚙𝚍𝚊𝚝𝚎𝚜 
     ▫ @EpicBotsSl
✔𝚀𝚞𝚎𝚜𝚝𝚒𝚘𝚗𝚜 
     ▫ @EpicChats
✔𝙰𝚙𝚔 𝙳𝚊𝚝𝚊𝚋𝚊𝚜𝚎 
     ▫ @EpicApkDatabase
     
       `Epic Developers Community 2022`
"""

SIHelp_backbtn = InlineKeyboardMarkup([[
                InlineKeyboardButton('ආපසු🔙', callback_data="HELP_BACK")
            ]])



