# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper




import os
import logging
from logging.handlers import RotatingFileHandler




TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7438884533:AAGcwQr_aC9UHDkMnJTeHYSstMet3XkoCtQ")
APP_ID = int(os.environ.get("APP_ID", "26254064"))
API_HASH = os.environ.get("API_HASH", "72541d6610ae7730e6135af9423b319c")


OWNER = os.environ.get("OWNER", "Bʀᴏᴏᴋ") #Owner username
OWNER_ID = int(os.environ.get("OWNER_ID", "5296584067")) #Owner user id
DB_URL = os.environ.get("DB_URL", "mongodb+srv://abidabdullahown1:hFTXerM9QmTxrwpE@cluster0.wk8gjpc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "robinqueat")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002191732189"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002125561929"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002219567279"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1002092136573"))
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "-1002003740934"))


SECONDS = int(os.getenv("SECONDS", "86400")) # auto delete in seconds



PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))




START_MSG = os.environ.get("START_MESSAGE", "Iᴀᴍ ɴɪᴄᴏ ʀᴏʙɪɴ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴀɴɪᴍᴇ ғɪʟᴇs ғʀᴏᴍ ᴍʏ sᴇɴᴘᴀɪ ᴄʜᴀɴɴᴀʟ ")

try:
    ADMINS=[5296584067]
    for x in (os.environ.get("ADMINS", "5296584067").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")


FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Wʜʏ ʏᴏᴜ ᴅɪᴅɴ'ᴛ ᴊᴏɪɴ ᴍʏ sᴇɴᴘᴀɪ ᴄʜᴀɴɴᴀʟs ᴊᴏɪɴ ɴᴏᴡ")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴀᴋᴀ ɪᴀᴍ ɴᴏᴛ ᴡᴀɴɴᴀ ᴛᴀʟᴋ ᴛᴏ ʏᴏᴜ ɪ ᴡɪʟʟ ᴏɴʟʏ ɢɪᴠᴇ ʏᴏᴜ ᴀɴɪᴍᴇ ᴇᴘɪsᴏᴅᴇs."

ADMINS.append(OWNER_ID)
ADMINS.append(5296584067)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
