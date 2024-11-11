import os, uvloop
from pyrogram import Client
from bot.config import Config
from bot.database.mongo import MongoPy

uvloop.install() # Pyrogram Speed Up

admins = list(Config.admins)
prefix = ["/","!","#","-","?"]
db_uri = Config.db_url

Db = MongoPy(db_uri)

app = Client(
    "Pyro-Base",
    api_id=Config.api_id,
    api_hash=Config.api_hash,
    bot_token=Config.bot_token,
    workdir="bot",
    plugins={'root': 'bot.plugins'}
    )
