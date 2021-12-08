import os

class Config(object):
    # get a token from https://chatbase.com
    CHAT_BASE_TOKEN = os.environ.get("CHAT_BASE_TOKEN", "3c235fcb-1e09-4366-86cc-1051b22aab7d")
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1797949864:AAEiJwy0ejel5cPi_jaXYdyoRpJTVUOInls")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", "3952215"))
    API_HASH = os.environ.get("API_HASH", "81343f8b93bdc2367a3ab9722b80c8ab")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1312054275").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 1572864000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://telegra.ph/file/673e8f2b25d6939fb8dd2.jpg")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = "https://telegra.ph/file/673e8f2b25d6939fb8dd2.jpg"
    # Array to store users who are authorized to use the Plan D of the bot
    SUPER7X_DLBOT_USERS = set(int(x) for x in os.environ.get("SUPER7X_DLBOT_USERS", "1312054275").split())
    # Array to store users who are authorized to use the Plan C of the bot
    SUPER3X_DLBOT_USERS = set(int(x) for x in os.environ.get("SUPER3X_DLBOT_USERS", "1312054275").split())
    # Array to store users who are authorized to use the Plan B of the bot
    SUPER_DLBOT_USERS = set(int(x) for x in os.environ.get("SUPER_DLBOT_USERS", "1312054275").split())
    AUTH_USERS = int(os.environ.get("AUTH_USERS", "3952215"))
    G_DRIVE_AUTH_DRQ = int(os.environ.get("G_DRIVE_AUTH_DRQ", "3952215"))
