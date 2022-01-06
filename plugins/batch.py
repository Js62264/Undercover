# © 2022 kalanakt | Hashminner.
 
import re 
import asyncio
from pyromod import listen 
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram import Client, filters
from pyrogram.errors import PeerIdInvalid, MessageIdInvalid, FloodWait
from pyrogram.errors.exceptions.bad_request_400 import FileReferenceEmpty, FileReferenceExpired, MediaEmpty

from helper_func import encode, get_message_id
 
@Client.on_message(filters.command("oldbatch") & filters.private & ~filters.bot, group=3) 
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
    
    sts = await update.reply("Generating link for your message.\nThis may take time depending upon number of messages")
    
    if chat_id1 in FILE_STORE_CHANNEL:
     string = f"{msg_id1}_{msg_id2}_{chat_id}"
     b_64 = base64.urlsafe_b64encode(string.encode("ascii")).decode().strip("=")
     return await sts.edit(f"Here is your link https://t.me/{temp.U_NAME}?start=DSTORE-{b_64}")
   
    msgs_list = []
    c_msg = msg_id1
    diff = msg_id2 - msg_id1
    
    FRMT = "Generating Link...\nTotal Messages: `{total}`\nDone: `{current}`\nRemaining: `{rem}`\nStatus: `{sts}`"
    if diff <= 200:
     msgs = await bot.get_messages(chat_id1, list(range(msg_id1, msg_id2+1)))
     msgs_list += msgs
    
    else:
     c_msg = msg_id1
     while True:
      new_diff = msg_id2 - c_msg
      if new_diff > 200:
       new_diff = 200
      elif new_diff <= 0:
       break
      print(new_diff, c_msg)
      msgs = await bot.get_messages(f_chat_id, list(range(c_msg, c_msg+new_diff)))
      msgs_list += msgs
      try:
       await sts.edit(FRMT.format(total=diff, current=(c_msg - f_msg_id), rem=(l_msg_id - c_msg), sts="Fetching Messages"))
      except:
       pass
      c_msg += new_diff
     
    outlist = []
    og_msg = 0
    tot = 0
    for msg in msgs_list:
     tot += 1
     if msg.empty or msg.service:
      continue
     if not msg.media:
      continue
     try:
      file_type = msg.media
      file = getattr(msg, file_type)
      if file:
       file = {
        "file_id": file.file_id,
        "caption": msg.caption,
        "title": getattr(file, "file_name", ""),
        "size": file.file_size,
       }
       og_msg +=1
       outlist.append(file)
      
      except:
       pass
      if not og_msg % 20:
       try:
        await sts.edit(FRMT.format(total=diff, current=tot, rem=(diff - tot), sts="Saving Messages"))
       except:
        pass
      
     
     
    with open(f"batchmode_{message.from_user.id}.json", "w+") as out:
     json.dump(outlist, out)
    post = await bot.send_document(LOG_CHANNEL, f"batchmode_{message.from_user.id}.json", file_name="Batch.json", caption="⚠️Generated for filestore.")
    os.remove(f"batchmode_{message.from_user.id}.json")
    file_id, ref = unpack_new_file_id(post.document.file_id)
    await sts.edit(f"Here is your link\nContains `{og_msg}` files.\n https://t.me/{temp.U_NAME}?start=BATCH-{file_id}")
    
    
    
    
   
 
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
