#----------------------------------- https://github.com/konay1122/clonebot --------------------------------------------#
import os
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "clonebot-ui.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5702032481:AAHT6e-8c9pKSt-GXDOoqRAOtjS9DO4i6UA")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "22452863"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "de45f792f245a3c984c1a8cab1c1a57a")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5662002039").split())

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQFWmn8AMuR0Yx_10-A0Cff3dTPNmZPhvqjqPeSMEnL1XhGvGImPFogEofPZXNIT46HFuo2cKQDz9w3Ym-gNFBvYpOx9vmwELK6bGL2ntf6isKrrOHwAZjH7Hwvd5gMr1RJrgl1kKmfcGzn96Mnbx3lrYnPI3Ueg0Qw3MQkO12NqsKbhie7_yxFJsW8z7QmBv8c188X3eLwynzHyYGrRhY5i65BuQlnOapAshhOFx4-4kOME7-Sj4YT46VZyWG3Ulpas4Q44SXpxwtB0p_kYRVJMzcXgRy-h7U64xzsnX-_xllWxzUE9XOoBhG9y4zjqwxY__VDvlg24_k1KUa0w3uWzhd0NugAAAAFRe0t3AA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://vcyjywgi:Vc7-y59ujOoCQFgvFrO1xd0LO6eDIpFs@mahmud.db.elephantsql.com/vcyjywgi")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
