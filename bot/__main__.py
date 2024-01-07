from bot import app, LOG
import asyncio
from pyrogram import idle

async def main():
   await app.start()
   LOG.info("<--Bot Started-->")
   await idle()

if __name__ == "__main__":
   asyncio.get_event_loop().run_until_complete(main())
