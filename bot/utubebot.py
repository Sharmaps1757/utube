from pyrogram import Client

from .config import Config


class UtubeBot(Client):
    def __init__(self):
        super().__init__(
            bot_token= "5226403177:AAEwSR3tC9uo9DrIwxqvWe5RmmWl13earqc",
            api_id= "13593326",
            api_hash= "36366cef731c918dd557ac681e3fe993",
            plugins=dict(root="bot.plugins"),
            workers=6,
            )
        self.DOWNLOAD_WORKERS = 6
        self.counter = 0
        self.download_controller = {}
        
