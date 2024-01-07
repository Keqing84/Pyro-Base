from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_text = """Hey {}👋,
**I am Just A Normal Bot Made By @kaito_network**
"""

start_mark = InlineKeyboardMarkup(
   [
     [ # 1st Row
        InlineKeyboardButton("🌾Channel", url="https://t.me/Kaito_Network")
     ],
     [ # 2nd Row
        InlineKeyboardButton("👤Dev", url="https://t.me/Kai8_4")
     ],
     [ # 3rd Row
        InlineKeyboardButton("📱Help", callback_data="helpp"),
        InlineKeyboardButton("🗑️Close", callback_data="closee")
     ]
   ]
 )

help_text = """
**__Nothin' Much Here__**

**⚠️ __Made By @Kaito_network__ ⚠️**
"""

help_mark = InlineKeyboardMarkup(
   [
     [ # 1st Row
        InlineKeyboardButton("🌾Channel", url="https://t.me/Kaito_Network")
     ],
     [ # 2nd Row
        InlineKeyboardButton("🏠Main", callback_data="mainn"),
        InlineKeyboardButton("🗑️Close", callback_data="closee")
     ]
   ]
 )
