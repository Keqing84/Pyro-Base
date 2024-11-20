from datetime import datetime, timedelta

from bot import app, Db_users, prefix, admins, bot_username
from bot.format import Format
from bot.utils.generate import *

@app.on_message(filters.private & filters.command("token", prefix=prefix))
async def token_gen(_, msg: Message):
    find = Db_users.find_value({"_id": msg.from_user.id})
    if find:
        diff = find["time"] - int(datetime.now().timestamp())
        if diff >= 0:
            return await msg.reply_text(f"You Have Already Verified Yourself.", quote=True)
    form = Format()
    enc_link = Encrypt.token_text()
    if not bot_username:
        bot = await app.get_me()
        bot_username = bot.username
    link = f"https://t.me/{bot_username}?start={enc_link}"
    if msg.from_user.id in admin:
        return await msg.reply_text(f"Token: [Link]({link})", quote=True)
    strn_link = shortner(link)
    form.tu_button(["Generate Token", strn_link])
    form.tu_button(["Channel", "https://t.me/Kaito_network"])
    Db_users.insert_value({"_id": msg.from_user.id, 
                           "token": strr, 
                           "verified": False
                           "time": int(datetime.now().timestamp() + timedelta(hours=24))
                          })
    return await msg.reply_text("Looks Like You Have Not Got Your Token, So Click On The Link Below And Get Your Token Set Up\n\n\n**Validity:** 24Hours", reply_markup=form.build_(1), quote=True)
