import os, uvloop
from pyrogram import Client
from bot.config import Config
from bot.database.mongo import MongoPy

admins = list(Config.admins)
prefix = ["/","!","#","-","?"]
db_uri = Config.db_url

user_load = []

Db_bot = MongoPy(db_uri, "pyro-base", "bot")
Db_user = MongoPy(db_uri, "pyro-base", "user")

uvloop.install() # Pyrogram Speed Up
app = Client(
    "Pyro-Base",
    api_id=Config.api_id,
    api_hash=Config.api_hash,
    bot_token=Config.bot_token,
    workdir="bot",
    plugins={'root': 'bot.plugins'}
)
