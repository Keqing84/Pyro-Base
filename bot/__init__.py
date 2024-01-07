import uvloop

from pyrogram import Client
from bot.config import Config

uvloop.install() # Pyrogram Speed Up

admins = list(Config.admins)
prefix = ["/","!","#","-","?"]

app = Client("Pyro-Base",
        api_id=Config.api_id,
        api_hash=Config.api_hash,
        bot_token=Config.bot_token,
        workdir="./",
        plugins=dict(root="Pyro-Base/plugins")
     )
