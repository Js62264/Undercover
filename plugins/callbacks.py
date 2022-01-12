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
