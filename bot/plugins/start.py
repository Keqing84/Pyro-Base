from bot import app, prefix, Db_user
from bot.utils.pre_text import *
from pyrogram import filters
from bot.logging import LOG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(filters.private & filters.incoming & filters.command("start", prefix))
async def start_py(_, msg: Message):
    cmds = msg.commands
    if len(cmds) != 2:
        return await msg.reply_photo(img["start"], caption=start_text.format(msg.from_user.mention(style="md")), reply_markup=start_mark)
    else:
        code = cmds[-1]
        user = Db_users.find_value({"_id": msg.from_user.id})
        ct_time = int(datetime.now().timestamp())
        if not ct_time < user["time"]:
            return await.msg.reply_text("Token Expired. Make A New One By Using /token", quote=True)
        if ((not len(code) == 27) or (not code == user["token"])):
            return await.msg.reply_text("Someone Is Trying To Be Oversmart.", quote=True)
        if user["verified"]:
            return await.msg.reply_text("Already Verified.", quote=True)
        Db_users.replace_value(msg.from_user.id, {"verified": True})
        return await.msg.reply_text("Yayy!!!, Now You Can Use The Bot For 24Hours", quote=True)
