# © 2022 kalanakt | Hashminner.
 
import re 
import asyncio
from pyromod import listen 
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram import Client, filters
from pyrogram.errors import PeerIdInvalid, MessageIdInvalid, FloodWait
from pyrogram.errors.exceptions.bad_request_400 import FileReferenceEmpty, FileReferenceExpired, MediaEmpty

from helper_func import encode, get_message_id
 
@Client.on_message(filters.command("batch") & filters.private & ~filters.bot, group=3) 
async def batch(bot:Client, update:Message): 
 
    user_id = update.from_user.id 
 
    post1:Message = await bot.ask(chat_id=update.chat.id, text="➭ Forward the First Message from Your Channel (with Quotes).. \n➭ Make Sure I'm Admin In that Channel", timeout=360) 
    if not post1: return 
 
    if not post1.forward_from_chat: 
 
        await update.reply_text("Please Forward The Message With Quotes (ie : Forwarded From ...)") 
        return 
 
    chat_id1 = post1.forward_from_chat.id 
    try : 
 
        msg_id1 = post1.forward_from_message_id 
        await bot.get_messages( 
            chat_id=chat_id1, 
            message_ids=msg_id1 
        ) 
    except PeerIdInvalid: 
        return await update.reply_text("Looks like Im Not A Member Of The Chat Where This Message Is Posted") 
    except MessageIdInvalid: 
        return await update.reply_text("Looks Like The Message You Forwarded No Longer Exists") 
    except Exception as e: 
        print(e) 
        return await update.reply_text("Something Went Wrong Please Try Again Later") 
 
    post2 = await bot.ask(chat_id=update.chat.id, text="Now Forward The Last Message From The Same Channel", timeout=360) 
    if not post2 : return 
 
    chat_id2 = post2.forward_from_chat.id 
    if not chat_id1==chat_id2 : 
        return await update.reply_text("These Two Messages Arent From The Same Chat") 
 
    try : 
 
        msg_id2 = post2.forward_from_message_id 
        await bot.get_messages( 
            chat_id=chat_id2, 
            message_ids=msg_id2 
        ) 
    except PeerIdInvalid: 
        return await update.reply_text("Looks like Im Not A Member Of The Chat Where This Message Is Posted") 
    except MessageIdInvalid: 
        return await update.reply_text("Looks Like The Message You Forwarded No Longer Exists") 
    except Exception as e: 
        print(e) 
        return await update.reply_text("Something Went Wrong Please Try Again Later") 
 
    if not msg_id1<=msg_id2: 
        return await update.reply_text("The First Message Has To Be Posted Above The Second In The Channel To Generate A Batch") 
    
    
    rng = [msg_id1]
    Files = []
    try:
     for i in range(msg_id1, (msg_id2+1)):
      xx = await bot.copy_message(chat_id = bot.db_channel.id, from_chat_id=chat_id2,message_id = i, disable_notification=True)
      await asyncio.sleep(0.5)
      Files.append(xx)
    except MediaEmpty:
     pass
    
    except FloodWait as e:
     await asyncio.sleep(e.x)
     
    except Exception as e:
     pass
      
    #for i in range(msg_id1, (msg_id2+1)):
     #xx = await bot.copy_message(chat_id = bot.db_channel.id, from_chat_id=chat_id2,message_id = i, disable_notification=True)
     #await asyncio.sleep(1)
     #Files.append(xx)
    
    converted_id1 = Files[0].message_id * abs(bot.db_channel.id)
    converted_id2 = Files[-1].message_id * abs(bot.db_channel.id)
     

    string = f"get-{converted_id1}-{converted_id2}"
    base64_string = await encode(string)
    url = f"https://t.me/SpaciousUniverseBot?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={url}')]])
    await update.reply_text(f"<b>➭ Here is your link : </b>\n\n{url}", reply_markup=reply_markup, disable_web_page_preview = True)
    
    
   
 
@Client.on_message(filters.private & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    req_message = await client.ask(text = "➭ Forward Any Post, File ,Video \n➭ Send /cancel To Stop Procees", chat_id = message.from_user.id, filters=((filters.all) & filters.private & filters.incoming))
    if req_message.text == "/cancel":
        return await message.reply_text('Cancelled Successfully...')
    try:
        post_message = await req_message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await req_message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await client.send_message(message.chat.id, "Something went Wrong..!")
        return
    converted_id = post_message.message_id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/SpaciousUniverseBot?start={base64_string}"

    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])

    await client.send_message(message.chat.id, text=f"<b>➭ Here is your link :</b>\n\n{link}", reply_markup=reply_markup, disable_web_page_preview = True)
    await client.send_message(chat_id = client.db_channel.id, text=f"<b>➭ Here is your link :</b>\n\n{link}", disable_notification=True)
