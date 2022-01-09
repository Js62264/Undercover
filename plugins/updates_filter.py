import asyncio
import re
import ast
from assets.Quote import quote
import pyrogram
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters

@Client.on_message(filters.group & filters.text & filters.incoming)
async def up_filter(client,message):
  if message.text == 'Maradona':
    buttons = [[
         InlineKeyboardButton('English', callback_data='Maradona_E'),
         InlineKeyboardButton('Multi', callback_data='Maradona_M')
      ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(
      photo='https://github.com/kalanakt/Bae-Suzy/blob/master/assets/English/Maradona%20Blessed%20Dream.jpg',
      caption=quote.MARADONA_TXT,
      reply_markup=reply_markup,
      parse_mode='html'
    )
    return
