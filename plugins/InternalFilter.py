import asyncio
import re
import ast

from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from Script import script
from assets.picture import *
from assets.Quote import quote
import pyrogram
from info import ADMINS, AUTH_CHANNEL, AUTH_USERS, CUSTOM_FILE_CAPTION, AUTH_GROUPS, P_TTI_SHOW_OFF, IMDB, SINGLE_BUTTON, SPELL_CHECK_REPLY, IMDB_TEMPLATE
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

BUTTONS = {}
SPELL_CHECK = {}

@Client.on_message(filters.text & ~filters.edited & filters.incoming)
async def give_filter(client,message):
    name = message.text
    if name.lower() == 'stranger':
         buttons = [
            [
                InlineKeyboardButton('English', callback_data='stranger_things_E'),
                InlineKeyboardButton('Hindi', callback_data='stranger_things_H')
            ]
         ]
         reply_markup = InlineKeyboardMarkup(buttons)
         await message.reply_photo(
            photo=STRANGER_THINGS_PIC,
            caption=quote.STRANGER_THINGS_1,
            reply_markup=reply_markup,
            parse_mode='html'
         )
