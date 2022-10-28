import os


class Config:

    BOT_TOKEN = "5226403177:AAEwSR3tC9uo9DrIwxqvWe5RmmWl13earqc"

    SESSION_NAME = "youtubeitbot"

    API_ID = "13593326"

    API_HASH = "36366cef731c918dd557ac681e3fe993"

    CLIENT_ID = "169050201647-dsfn3821df1pinlsgfajpbrua8ke3rj7.apps.googleusercontent.com"

    CLIENT_SECRET = "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"

    BOT_OWNER = "1941962687"

    AUTH_USERS_TEXT= "1941962687"

    AUTH_USERS = [BOT_OWNER, 1941962687] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = ""

    VIDEO_CATEGORY = ""
  
    VIDEO_TITLE_PREFIX = ""

    VIDEO_TITLE_SUFFIX = ""

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
