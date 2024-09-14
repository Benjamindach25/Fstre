import os
import logging
from logging.handlers import RotatingFileHandler

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7260195533:AAH2iB_OY7M1G3DQmQa_-U4Mm47ADPjAT2c")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("API_ID", "21113240"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "cf60d4f8ad97d15080c0252d9af22321")

# Your db channel ID
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002232357982"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6824677167"))

# Port
PORT = os.environ.get("PORT", "8080")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Maya:Maya@cluster0.9ntjs0d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Maya")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "1"))

# Start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in a specified channel and other users can access it via a special link.")

# Admins setup
try:
    ADMINS = [int(x) for x in os.environ.get("ADMINS", "").split()]
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")
if OWNER_ID not in ADMINS:
    ADMINS.append(OWNER_ID)

# Set your custom caption here, Keep None to disable custom caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Set True if you want to disable your channel posts share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "False") == "True"

# Bot stats text
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"

# User reply text
USER_REPLY_TEXT = "❌ Don't send me messages directly, I'm only a file-sharing bot!"

LOG_FILE_NAME = "filesharingbot.txt"

# Force subscription setup
all_fsub = open("fsub.txt", "r").read().splitlines()
FORCE_SUB_CHANNELS = []
FORCE_SUB_CHANNEL_IDS = []
for x in all_fsub:
    if x.startswith("-"):
        _id, link = x.split(", ")
        FORCE_SUB_CHANNELS.append([int(_id), link])
        FORCE_SUB_CHANNEL_IDS.append(int(_id))

# Logging setup
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
    
