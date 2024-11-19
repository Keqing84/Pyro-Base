from bot import app, prefix
from bot.utils.pre_text import *
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

img = "https://r4.wallpaperflare.com/wallpaper/714/495/609/landscape-artwork-digital-art-fantasy-art-wallpaper-9960e89d112afd2ba6e738ff70b1e63d.jpg"

@app.on_message(filters.private & filters.incoming & filters.command("start", prefix))
async def start_py(_, msg: Message):
    return await msg.reply_photo(img, caption=start_text.format(msg.from_user.mention(style="md")), reply_markup=start_mark)
