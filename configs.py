import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "14810154"))
  API_HASH = os.environ.get("API_HASH", "8df64055e6f5cc4551bfa20027799c92")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7737002477:AAFE3dG3F10zlIpM5Fdp_BOr2g6R6hNki1g")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "et_byme_file_store_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "Entertainment_time_ByMe"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "shrinkearn.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "b3e559c4e738de42b0a3e038ffa25731e3b33ad1")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "1985104467"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://aniketmaurya23356:xzp4uf76Xx5Xaa5@cluster0.kdeg1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "1001717129525")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "1002154405024"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](http://t.me/et_byme_file_store_bot)
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_ME_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [ME](https://t.me/acuteboy_03)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/acuteboy_03)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
