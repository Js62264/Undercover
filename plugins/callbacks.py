import os
import ast


from pyrogram.errors import UserBannedInChannel, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from plugins.pm_filter import *
import logging
logger = logging.getLogger(__name__)

from Script import script
from assets.picture import *
from assets.Quote import quote


@Client.on_callback_query()
async def cb_handler(client, query):
  if query.data == "stranger_things_H_480p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADXwQAAl3T6FbdhkzTtRmN8xYE'),
              InlineKeyboardButton('Season 02', url='https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADYAQAAl3T6FbMlJE3uvCd1xYE')
           ],
           [
              InlineKeyboardButton('Season 03', url='https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADYQQAAl3T6FZy54s5vRvKcxYE'),
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
