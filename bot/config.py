import os, re
from dotenv import load_dotenv


load_dotenv()

def get_env(name: str):
  return os.environ.get(name, None)

def admin_panel():
  setup = get_env("ADMIN")
  admins = set()
  if any(s in setup for s in ["-"," ",","]):
    for admin in re.split(r"-| |,", setup):
      admins.add(int(admin))
  else:
     admins.add(int(setup))
  return admins

class Config:
  api_id = int(get_env("API_ID"))
  api_hash = get_env("API_HASH")
  bot_token = get_env("BOT_TOKEN")
  db_url = get_env("DATABASE")
  channel_id = int(get_env("CHANNEL"))
  admins = admin_panel()
