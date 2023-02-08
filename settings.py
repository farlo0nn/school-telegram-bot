import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

BOT_TOKEN = os.getenv('BOT_TOKEN')
STICKERS_FOLDER_PATH = os.getenv('STICKERS_FOLDER_PATH')
SAD_STICKER_ID = os.getenv('SAD_STICKER_ID')
ADMIN_SECRET_KEY = os.getenv('ADMIN_SECRET_KEY')
