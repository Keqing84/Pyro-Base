import os, uvloop

from logging import (
    getLogger,
    FileHandler,
    StreamHandler,
    INFO,
    basicConfig
)
from pyrogram import Client
from bot.config import Config

uvloop.install() # Pyrogram Speed Up

if os.path.exists('log.txt'):
    with open('log.txt', 'w+') as f:
        f.truncate(0)

basicConfig(
    format="%(asctime)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s",
    handlers=[FileHandler("log.txt"), StreamHandler()],
    level=INFO,
)

LOG = getLogger(__name__)

admins = list(Config.admins)
prefix = ["/","!","#","-","?"]

app = Client("Pyro-Base",
        api_id=Config.api_id,
        api_hash=Config.api_hash,
        bot_token=Config.bot_token,
        workdir=os.path.dirname(__file__),
        plugins=dict(root=os.path.join(os.path.dirname(__file__),"plugins"))
     )
