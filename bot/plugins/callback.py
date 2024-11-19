from bot import app
from bot.utils.pre_text import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


@app.on_callback_query()
async def call_back(_, cb_query: CallbackQuery):
     data = cb_query.data
     msg = cb_query.message
     if data == "closee":
         try:
             await msg.delete()
         except:
             pass
     elif data == "mainn":
         try:
             await msg.edit_caption(start_text.format(f"[{msg.chat.first_name}](tg://user?id={msg.chat.id})"), reply_markup=start_mark)
         except:
             pass
     elif data == "helpp":
         try:
             await msg.edit_caption(help_text, reply_markup=help_mark)
         except:
             pass
     else:
         try:
             await msg.edit_caption(data+"\nData Passed On.")
         except:
             pass
