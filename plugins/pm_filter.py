#Kanged From @TroJanZheX | 
import asyncio
import re
import ast

from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty, MessageEmpty
from Script import script
from assets.picture import *
from assets.Quote import quote
import pyrogram
from database.connections_mdb import active_connection, all_connections, delete_connection, if_active, make_active, make_inactive
from info import ADMINS, AUTH_CHANNEL, AUTH_USERS, CUSTOM_FILE_CAPTION, AUTH_GROUPS, P_TTI_SHOW_OFF, IMDB, SINGLE_BUTTON, SPELL_CHECK_REPLY, IMDB_TEMPLATE
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid
from utils import get_size, is_subscribed, get_poster, search_gagala, temp, get_name
from database.users_chats_db import db
from plugins.heroku import *
from database.ia_filterdb import Media, get_file_details, get_search_results
from database.filters_mdb import(
   del_all,
   find_filter,
   get_filters,
)
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

BUTTONS = {}
SPELL_CHECK = {}

@Client.on_message(filters.group & filters.text & ~filters.edited & filters.incoming)
async def give_filter(client,message):
    name = message.text
    k = await manual_filters(client, message)
    if k == False:
        await auto_filter(client, message)

    if ('stranger' and 'things') in name.lower():
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
    if 'maradona' in name.lower():
         buttons = [
            [
                InlineKeyboardButton('English', callback_data='Maradona_E')
            ],
            [
               InlineKeyboardButton('Multi Audio', callback_data='Maradona_M')
            ]

         ]
         reply_markup = InlineKeyboardMarkup(buttons)
         await message.reply_photo(
            photo=MARADONA_PIC,
            caption=quote.MARADONA_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
         )
    if (
        'money' and 'heist'
    ) in name.lower() or name.lower() == 'la casa de papel':
        buttons = [
           [
               InlineKeyboardButton('English', callback_data='money_heist_E'),
               InlineKeyboardButton('Spanish', callback_data='money_heist_S')
           ],
           [
               InlineKeyboardButton('Hindi', callback_data='money_heist_H'),
               InlineKeyboardButton('Telugu', callback_data='money_heist_Te')
           ],
           [
               InlineKeyboardButton('Tamil', callback_data='money_heist_Ta')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
           photo=MONEY_HEIST_PIC,
           caption=quote.MONEY_HEIST_TXT_1,
           reply_markup=reply_markup,
           parse_mode='html'
        )
    if name.lower() == 'you':
         buttons = [
            [
                InlineKeyboardButton('720p', callback_data='you_720p')
            ],
            [
                InlineKeyboardButton('1080p', callback_data='you_1080p')
            ]
         ]
         reply_markup = InlineKeyboardMarkup(buttons)
         await message.reply_photo(
            photo=YOU_PIC,
            caption=quote.YOU_2 ,
            reply_markup=reply_markup,
            parse_mode='html'
         )
    if ('cobra' and 'kai') in name.lower():
         buttons = [
            [
                InlineKeyboardButton('480p', callback_data='cobra_kai_480p'),
                InlineKeyboardButton('720p', callback_data='cobra_kai_720p')
            ],
            [
                InlineKeyboardButton('1080p', callback_data='cobra_kai_1080p')
            ]
         ]
         reply_markup = InlineKeyboardMarkup(buttons)
         await message.reply_photo(
            photo=COBRA_KAI_PIC,
            caption=quote.COBRA_KAI_2 ,
            reply_markup=reply_markup,
            parse_mode='html'
         )

    if ('all' and 'of' and 'us' and 'are') in name.lower():
         buttons = [
            [
                InlineKeyboardButton('480p', callback_data='AOUAD_480p'),
                InlineKeyboardButton('720p', callback_data='AOUAD_720p')
            ],
            [
                InlineKeyboardButton('1080p', callback_data='AOUAD_1080p')
            ]
         ]
         reply_markup = InlineKeyboardMarkup(buttons)
         await message.reply_photo(
            photo=AOUAD_PIC,
            caption=quote.AOUAD_2 ,
            reply_markup=reply_markup,
            parse_mode='html'
         )

    if ('ted' and 'lasso') in name.lower():
         buttons = [
            [
                InlineKeyboardButton('Season 1', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADkgQAAis54FeL_X5eSJGx3xYE'),
                InlineKeyboardButton('Season 2', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADlAQAAis54FcJM2SicgziaxYE')
            ],
            [
                InlineKeyboardButton('Close', callback_data='cls')
            ]
         ]
         reply_markup = InlineKeyboardMarkup(buttons)
         await message.reply_photo(
            photo=TED_LASSO_PIC,
            caption=script.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
         )

    if 'witcher' in name.lower():
         buttons = [
            [
                InlineKeyboardButton('480p', callback_data='witcher_480p'),
                InlineKeyboardButton('720p', callback_data='witcher_720p')
            ],
            [
                InlineKeyboardButton('1080p', callback_data='witcher_1080p')
            ]
         ]
         reply_markup = InlineKeyboardMarkup(buttons)
         await message.reply_photo(
            photo=WITCHER_PIC,
            caption=quote.WITCHER_2 ,
            reply_markup=reply_markup,
            parse_mode='html'
         )

    if ('peaky' and 'blinders') in name.lower():
         buttons = [
            [
                InlineKeyboardButton('720p', callback_data='peaky_blinders_720p')
            ],
            [
                InlineKeyboardButton('1080p', callback_data='peaky_blinders_1080p')
            ]
         ]
         reply_markup = InlineKeyboardMarkup(buttons)
         await message.reply_photo(
            photo=PEAKY_BLINDERS_PIC,
            caption=quote.PEAKY_BLINDERS ,
            reply_markup=reply_markup,
            parse_mode='html'
         )

    if 'vikings' in name.lower() or 'viking' in name.lower():
         buttons = [
            [
                InlineKeyboardButton('480p', callback_data='vikings_480p'),
                InlineKeyboardButton('720p', callback_data='vikings_720p')
            ],
            [
                InlineKeyboardButton('1080p', callback_data='vikings_1080p')
            ]
         ]
         reply_markup = InlineKeyboardMarkup(buttons)
         await message.reply_photo(
            photo=VIKINGS_PIC,
            caption=quote.VIKINGS_2 ,
            reply_markup=reply_markup,
            parse_mode='html'
         )

@Client.on_callback_query(filters.regex(r"^next"))
async def next_page(bot, query):

    ident, req, key, offset = query.data.split("_")
    if int(req) not in [query.from_user.id, 0]:
        return await query.answer("It's Not For You...", show_alert=True)
    try:
        offset = int(offset)
    except:
        offset = 0
    search = BUTTONS.get(key)
    if not search:
        await query.answer("You are using one of my old messages, please send the request again.",show_alert=True)
        return

    files, n_offset, total = await get_search_results(search, offset=offset, filter=True)
    try:
        n_offset = int(n_offset)
    except:
        n_offset = 0

    if not files:
        return

    if SINGLE_BUTTON:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{get_size(file.file_size)}┆{get_name(file.file_name)}", callback_data=f'files#{file.file_id}'
                ),
            ]
            for file in files
        ]

    else:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{file.file_name}", callback_data=f'files#{file.file_id}'
                ),
                InlineKeyboardButton(
                    text=f"{get_size(file.file_size)}",
                    callback_data=f'files_#{file.file_id}',
                ),
            ]
            for file in files
        ]

    if 0 < offset <= 10:
        off_set = 0
    elif offset == 0:
        off_set = None
    else:
        off_set = offset - 10
    if n_offset == 0:
        btn.append(
           [[
              InlineKeyboardButton(
                 "《", callback_data=f"next_{req}_{key}_{off_set}"
              ),
              InlineKeyboardButton(
                 f"📃 {round(offset / 10) + 1} / {round(total/10)}",
                 callback_data="pages",
              ),
              InlineKeyboardButton(
                 text="Check PM", url='https://t.me/SpaciousUniverseBot'
              ),
           ],
           [
              InlineKeyboardButton(
                 text="🔰 How To Download 🔰", url="https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADXAUAAvvEGVWDT7ebLu5AbhYE"
              )
           ]]
        )


    elif off_set is None:
        btn.append(
           [[
              InlineKeyboardButton(
                 f"📃 {round(offset / 10) + 1} / {round(total/10)}",
                 callback_data="pages",
              ),
              InlineKeyboardButton(
                 text="Check PM 📨", url ='https://t.me/SpaciousUniverseBot'
              ), 
              InlineKeyboardButton(
                 "》", callback_data=f"next_{req}_{key}_{n_offset}"
              ),
           ],
           [
              InlineKeyboardButton(
                 text="🔰 How To Download 🔰", url="https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADXAUAAvvEGVWDT7ebLu5AbhYE"
              )
           ]]
        )

    else:
        btn.append(
           [
              InlineKeyboardButton("《", callback_data=f"next_{req}_{key}_{off_set}"),
              InlineKeyboardButton(
                 f" 📃 {round(offset / 10) + 1} / {round(total/10)}  ",
                 callback_data="pages",
              ),
              InlineKeyboardButton("》", callback_data=f"next_{req}_{key}_{n_offset}")
           ],
        )
        btn.append(
            [
                InlineKeyboardButton(
                    text="🔰 How To Download 🔰", url="https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADXAUAAvvEGVWDT7ebLu5AbhYE"
                )
            ]
        )

    try:
        await query.edit_message_reply_markup( 
            reply_markup=InlineKeyboardMarkup(btn)
        )
    except MessageNotModified:
        pass
    await query.answer()

@Client.on_callback_query(filters.regex(r"^spolling"))
async def advantage_spoll_choker(bot, query):
    _, user, movie_ = query.data.split('#')
    if int(user) != 0 and query.from_user.id != int(user):
        return await query.answer("It's Not For You 😈", show_alert=True)
    if movie_  == "close_spellcheck":
        return await query.message.delete()
    movies = SPELL_CHECK.get(query.message.reply_to_message.message_id)
    if not movies:
        return await query.answer("You are clicking on an old button which is expired.", show_alert=True)
    movie = movies[(int(movie_))]
    await query.answer('Checking for Movie in database...')
    files, offset, total_results = await get_search_results(movie, offset=0, filter=True)
    if files:
        k = (movie, files, offset, total_results)
        await auto_filter(bot, query, k)
    else:
        k = await query.message.edit('This Movie Not Found In DataBase')
        await asyncio.sleep(10)
        await k.delete()


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "close_data":
        await query.message.delete()
    
    elif query.data == "delallconfirm":
        userid = query.from_user.id
        chat_type = query.message.chat.type

        if chat_type == "private":
            grpid  = await active_connection(str(userid))
            if grpid is not None:
                grp_id = grpid
                try:
                    chat = await client.get_chat(grpid)
                    title = chat.title
                except:
                    await query.message.edit_text("Make sure I'm present in your group!!", quote=True)
                    return
            else:
                await query.message.edit_text(
                    "I'm not connected to any groups!\nCheck /connections or connect to any groups",
                    quote=True
                )
                return

        elif chat_type in ["group", "supergroup"]:
            grp_id = query.message.chat.id
            title = query.message.chat.title

        else:
            return

        st = await client.get_chat_member(grp_id, userid)
        if (st.status == "creator") or (str(userid) in ADMINS):    
            await del_all(query.message, grp_id, title)
        else:
            await query.answer("You need to be Group Owner or an Auth User to do that!",show_alert=True)

    elif query.data == "delallcancel":
        userid = query.from_user.id
        chat_type = query.message.chat.type

        if chat_type == "private":
            await query.message.reply_to_message.delete()
            await query.message.delete()

        elif chat_type in ["group", "supergroup"]:
            grp_id = query.message.chat.id
            st = await client.get_chat_member(grp_id, userid)
            if (st.status == "creator") or (str(userid) in ADMINS):
                await query.message.delete()
                try:
                    await query.message.reply_to_message.delete()
                except:
                    pass
            else:
                await query.answer("Thats not for you!!",show_alert=True)


    elif "groupcb" in query.data:
        await query.answer()

        group_id = query.data.split(":")[1]
        title = query.data.split(":")[2]
        act = query.data.split(":")[3]
        user_id = query.from_user.id

        if act == "":
            stat = "CONNECT"
            cb = "connectcb"
        else:
            stat = "DISCONNECT"
            cb = "disconnect"

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(f"{stat}", callback_data=f"{cb}:{group_id}:{title}"),
                InlineKeyboardButton("DELETE", callback_data=f"deletecb:{group_id}")],
            [InlineKeyboardButton("BACK", callback_data="backcb")]
        ])

        await query.message.edit_text(
            f"Group Name : **{title}**\nGroup ID : `{group_id}`",
            reply_markup=keyboard,
            parse_mode="md"
        )
        return

    elif "connectcb" in query.data:
        await query.answer()

        group_id = query.data.split(":")[1]
        title = query.data.split(":")[2]
        user_id = query.from_user.id

        mkact = await make_active(str(user_id), str(group_id))

        if mkact:
            await query.message.edit_text(
                f"Connected to **{title}**",
                parse_mode="md"
            )
        else:
            await query.message.edit_text('Some error occured!!', parse_mode="md")
        return
    elif "disconnect" in query.data:
        await query.answer()

        title = query.data.split(":")[2]
        user_id = query.from_user.id

        mkinact = await make_inactive(str(user_id))

        if mkinact:
            await query.message.edit_text(
                f"Disconnected from **{title}**",
                parse_mode="md"
            )
        else:
            await query.message.edit_text('Some error occured!!', parse_mode="md")
        return
    elif "deletecb" in query.data:
        await query.answer()

        user_id = query.from_user.id
        group_id = query.data.split(":")[1]

        delcon = await delete_connection(str(user_id), str(group_id))

        if delcon:
            await query.message.edit_text(
                "Successfully deleted connection"
            )
        else:
            await query.message.edit_text('Some error occured!!', parse_mode="md")
        return
    elif query.data == "backcb":
        await query.answer()

        userid = query.from_user.id

        groupids = await all_connections(str(userid))
        if groupids is None:
            await query.message.edit_text(
                "There are no active connections!! Connect to some groups first.",
            )
            return
        buttons = []
        for groupid in groupids:
            try:
                ttl = await client.get_chat(int(groupid))
                title = ttl.title
                active = await if_active(str(userid), str(groupid))
                act = " - ACTIVE" if active else ""
                buttons.append(
                    [
                        InlineKeyboardButton(
                            text=f"{title}{act}", callback_data=f"groupcb:{groupid}:{title}:{act}"
                        )
                    ]
                )
            except:
                pass
        if buttons:
            await query.message.edit_text(
                "Your connected group details ;\n\n",
                reply_markup=InlineKeyboardMarkup(buttons)
            )

    elif "alertmessage" in query.data:
        grp_id = query.message.chat.id
        i = query.data.split(":")[1]
        keyword = query.data.split(":")[2]
        reply_text, btn, alerts, fileid = await find_filter(grp_id, keyword)
        if alerts is not None:
            alerts = ast.literal_eval(alerts)
            alert = alerts[int(i)]
            alert = alert.replace("\\n", "\n").replace("\\t", "\t")
            await query.answer(alert,show_alert=True)

    if query.data.startswith("file"):
        ident, file_id = query.data.split("#")
        files_ = await get_file_details(file_id)
        if not files_:
            return await query.answer('No such file exist.')
        files = files_[0]
        title = files.file_name
        size=get_size(files.file_size)
        f_caption=files.caption
        if CUSTOM_FILE_CAPTION:
            try:
                f_caption=CUSTOM_FILE_CAPTION.format(file_name=title, file_size=size, file_caption=f_caption)
            except Exception as e:
                logger.exception(e)
            f_caption=f_caption
        if f_caption is None:
            f_caption = f"{files.file_name}"
            
        buttons = [[
           InlineKeyboardButton('💠 Verify 💠', url=f'https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/{temp.U_NAME}?start={file_id}')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        k = await client.send_message(
           chat_id=query.from_user.id,
           text='<b>Please verify your identity within 30s.This is Protects the bot from spammers</b>',
           reply_markup=reply_markup,
        )
        await query.answer('Check My Privet Chat, I have sent message to You', show_alert=True)
        await asyncio.sleep(30)
        await k.delete()
        
#        except UserIsBlocked:
#             await query.answer('You Blocked Me!!. Start Me In privet chat and try Again.',show_alert = True)
#        except PeerIdInvalid:
#             await query.answer(url=f"https://t.me/{temp.U_NAME}?start={file_id}")
#        except Exception as e:
#             await query.answer(url=f"https://t.me/{temp.U_NAME}?start={file_id}")
      
#             if AUTH_CHANNEL and not await is_subscribed(client, query):
#                 await query.answer(url=f"https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/{temp.U_NAME}?start={file_id}")
#                 return
#             elif P_TTI_SHOW_OFF:
#                 await query.answer(url=f"https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/{temp.U_NAME}?start={file_id}")
#                 return
#             else:
#                 await client.send_cached_media(
#                     chat_id=query.from_user.id,
#                     file_id=file_id,
#                     caption=f_caption
#                     )
#                 await query.answer('Check My Privet Chat, I have sent files to You')
#         except UserIsBlocked:
#             await query.answer('You Blocked Me!!. Start Me In privet chat and try Again.',show_alert = True)
#         except PeerIdInvalid:
#             await query.answer(url=f"https://t.me/{temp.U_NAME}?start={file_id}")
#         except Exception as e:
#             await query.answer(url=f"https://t.me/{temp.U_NAME}?start={file_id}")
            
    elif query.data.startswith("checksub"):
        if AUTH_CHANNEL and not await is_subscribed(client, query):
            await query.answer("I Like Your Smartness, But Don't Be Oversmart 😒",show_alert=True)
            return
        ident, file_id = query.data.split("#")
        files_ = await get_file_details(file_id)
        if not files_:
            return await query.answer('No such file exist.')
        files = files_[0]
        title = files.file_name
        size=get_size(files.file_size)
        f_caption=files.caption
        if CUSTOM_FILE_CAPTION:
            try:
                f_caption=CUSTOM_FILE_CAPTION.format(file_name=title, file_size=size, file_caption=f_caption)
            except Exception as e:
                logger.exception(e)
                f_caption=f_caption
        if f_caption is None:
            f_caption = f"{title}"
        await query.answer()
        await client.send_cached_media(
            chat_id=query.from_user.id,
            file_id=file_id,
            caption=f_caption
            )

    elif query.data == "pages":
        await query.answer()
    elif query.data == "start":
        buttons = [[
            InlineKeyboardButton('➕ Add Me To Your Groups ➕', url='http://t.me/SpaciousUniverseBot?startgroup=true')
            ],[
            InlineKeyboardButton('🔍 Search', switch_inline_query_current_chat=''),
            InlineKeyboardButton('🤖 Updates', url='https://t.me/TMWAD')
            ],[
            InlineKeyboardButton('🛠️Tools', callback_data='help'),
            InlineKeyboardButton('♻️About', callback_data='about')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.START_TXT.format(query.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "help":
        buttons = [[
            InlineKeyboardButton('Manual', callback_data='manuelfilter'),
            InlineKeyboardButton('Auto', callback_data='autofilter')
            ],[
            InlineKeyboardButton('Connection', callback_data='coct'),
            InlineKeyboardButton('Admin', callback_data='admin')
            ],[
            InlineKeyboardButton('《', callback_data='lftp'),
            InlineKeyboardButton('Close', callback_data='cls'),
            InlineKeyboardButton('》', callback_data='rigp')
            ],[
            InlineKeyboardButton('🏠 Home', callback_data='start'),
            InlineKeyboardButton('🔮 Status', callback_data='stats')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        )
        
    elif query.data == "lftp":
        buttons = [[
            InlineKeyboardButton('IMDb', callback_data='imdb'),
            InlineKeyboardButton('Search', callback_data='search')
            ],[
            InlineKeyboardButton('ID', callback_data='id'),
            InlineKeyboardButton('Info', callback_data='info')
            ],[
            InlineKeyboardButton('《', callback_data='rigp'),
            InlineKeyboardButton('Close', callback_data='cls'),
            InlineKeyboardButton('》', callback_data='help')
            ],[
            InlineKeyboardButton('🏠 Home', callback_data='start'),
            InlineKeyboardButton('🔮 Status', callback_data='stats')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        ) 
        
     
    elif query.data == "rigp":
        buttons = [[
            InlineKeyboardButton('Batch', callback_data='batch'),
            InlineKeyboardButton('link', callback_data='genlink')
            ],[
            InlineKeyboardButton('Spell Check', callback_data='spell'),
            InlineKeyboardButton('Info', callback_data='info')
            ],[
            InlineKeyboardButton('《', callback_data='help'),
            InlineKeyboardButton('Close', callback_data='cls'),
            InlineKeyboardButton('》', callback_data='lftp')
            ],[
            InlineKeyboardButton('🏠 Home', callback_data='start'),
            InlineKeyboardButton('🔮 Status', callback_data='stats')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
        ) 
   
   
    elif query.data == "about":
        buttons= [[
            InlineKeyboardButton('🏠 Home', callback_data='start'),
            InlineKeyboardButton('🔐 Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ABOUT_TXT.format(temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode='html'
        )
   
    elif query.data == "you_720p":
        buttons= [
           [
              InlineKeyboardButton('English', callback_data='you_E_720p')
           ],
           [
              InlineKeyboardButton('Hindi', callback_data='you_H_720p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.YOU_1,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "cobra_kai_720p":
        buttons= [
           [
              InlineKeyboardButton('English', callback_data='cobra_kai_E_720p')
           ],
           [
              InlineKeyboardButton('Hindi', callback_data='cobra_kai_H_720p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.COBRA_KAI_1,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "AOUAD_720p":
        buttons= [
           [
              InlineKeyboardButton('Korean', callback_data='AOUAD_K_720p'),
              InlineKeyboardButton('English', callback_data='AOUAD_E_720p')
           ],
           [
              InlineKeyboardButton('Hindi', callback_data='AOUAD_H_720p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.AOUAD_1,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "AOUAD_1080p":
        buttons= [
           [
              InlineKeyboardButton('Korean', callback_data='AOUAD_K_1080p'),
              InlineKeyboardButton('English', callback_data='AOUAD_E_1080p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.AOUAD_1,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "witcher_720p":
        buttons= [
           [
              InlineKeyboardButton('English', callback_data='witcher_E_720p')
           ],
           [
              InlineKeyboardButton('Hindi | English', callback_data='witcher_H_720p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.WITCHER_1,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "vikings_480p":
        buttons= [
           [
              InlineKeyboardButton('English', callback_data='vikings_E_480p')
           ],
           [
              InlineKeyboardButton('Hindi | English', callback_data='vikings_H_480p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.VIKINGS_1,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "vikings_720p":
        buttons= [
           [
              InlineKeyboardButton('English', callback_data='vikings_E_720p')
           ],
           [
              InlineKeyboardButton('Hindi | English', callback_data='vikings_H_720p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.VIKINGS_1,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "peaky_blinders_1080p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADiAUAAl3T4FZO4run3aptrhYE'),
            InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADiQUAAl3T4FaZY4qa50xxhhYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADigUAAl3T4FY6-VVIJyU6gRYE'),
            InlineKeyboardButton('Season 04', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADiwUAAl3T4FYRj4313xH2-BYE')
           ],
           [
            InlineKeyboardButton('Season 05', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADjAUAAl3T4FZD-AGvkPy3RhYE'),
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "peaky_blinders_720p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADgwUAAl3T4FZ_vXYWm6_RihYE'),
            InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADhAUAAl3T4FYs2i8dmfXbWRYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADhQUAAl3T4FbkVy6TbLw6BhYE'),
            InlineKeyboardButton('Season 04', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADhgUAAl3T4FZLIvZI9glbVRYE')
           ],
           [
            InlineKeyboardButton('Season 05', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADhwUAAl3T4FbPmysvVK5xYE'),
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        ) 
    elif query.data == "AOUAD_E_720p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADsgQAAmghuFfhzpUzn8q-3BYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "AOUAD_K_720p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADswQAAmghuFdeBlfcPT876xYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
        
    elif query.data == "AOUAD_H_720p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADtQQAAmghuFd8MdJOKa7p0xYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "AOUAD_E_1080p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADuAQAAmghuFeB0uCGlKWG_RYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "AOUAD_K_1080p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADtgQAAmghuFcqh_6rddMYTxYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
        
    elif query.data == "AOUAD_480p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADuQQAAmghuFfURi5n72bSsRYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "vikings_E_480p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADKQUAAl3T4FZJbZ6k4WOdaRYE'),
            InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADKgUAAl3T4FYOAzTSbZkZ_xYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADKwUAAl3T4FYvnfNQJdGUQxYE'),
            InlineKeyboardButton('Season 04', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADLAUAAl3T4FbBL_9e4DwUoBYE')
           ],
           [
            InlineKeyboardButton('Season 05', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADLQUAAl3T4Fav05wAAdcC_gIWBA'),
            InlineKeyboardButton('Season 06', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADLgUAAl3T4FZSixE-mFYKIRYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "cobra_kai_E_720p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADzwMAAnIV8FaEQE3QmdsYLhYE'),
            InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQAD0AMAAnIV8FbKs6ghnG3lbBYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQAD0QMAAnIV8FYDzjqIBpiRqxYE'),
            InlineKeyboardButton('Season 04', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQAD0gMAAnIV8FaKZOa8tzZP0xYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "cobra_kai_H_720p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADygMAAnIV8FYvCQsxC0Nw5xYE'),
            InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADywMAAnIV8FbDEfP0yRWauRYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADzAMAAnIV8FbQZ8jKN_DTbBYE'),
            InlineKeyboardButton('Season 04', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADzQMAAnIV8Fau_SwQ1uV1DBYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "cobra_kai_1080p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQAD0wMAAnIV8FYRppcjsEuDdBYE'),
            InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQAD1AMAAnIV8FYXnA9mUtIGVxYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQAD1QMAAnIV8FbgBmoS0nX9FRYE'),
            InlineKeyboardButton('Season 04', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQAD1gMAAnIV8FYeAnZ2qeHkLhYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "cobra_kai_480p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADxgMAAnIV8FZJvPGNNC2B1RYE'),
            InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADxwMAAnIV8FZqAAHGq1BSvqQWBA')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADyAMAAnIV8Fa9I9r6TkeYZRYE'),
            InlineKeyboardButton('Season 04', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADyQMAAnIV8FZUK9rOCp4ppRYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "vikings_E_720p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADLwUAAl3T4Fa9gPR7PpiUwRYE'),
            InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADMAUAAl3T4FZ5nmXXc5_1yhYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADMgUAAl3T4FZTXhAKREQ9SRYE'),
            InlineKeyboardButton('Season 04', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADMwUAAl3T4FbsGsGUVewXoBYE')
           ],
           [
            InlineKeyboardButton('Season 05', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADNAUAAl3T4FZOBJpa2bVYrxYE'),
            InlineKeyboardButton('Season 06', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADNQUAAl3T4Fbo2-gXuCS_sBYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "vikings_1080p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADNgUAAl3T4FboLgvktY-LoBYE'),
            InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADNwUAAl3T4Fbl4GyZGN03OBYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADOAUAAl3T4FbAWQ_zd9ngiBYE'),
            InlineKeyboardButton('Season 04', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADOQUAAl3T4FYhyyfIUMpMHhYE')
           ],
           [
            InlineKeyboardButton('Season 05', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADOwUAAl3T4FawMXAIRhw3GBYE'),
            InlineKeyboardButton('Season 06', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADPAUAAl3T4FbV-lDpzT71-BYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "vikings_H_480p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADPQUAAl3T4FbfGeUhXI-cORYE'),
            InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADPgUAAl3T4FYnlmtea-D8nhYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADPwUAAl3T4Fbz_-8T6QbqqxYE'),
            InlineKeyboardButton('Season 04', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADQAUAAl3T4FZ6Ih8Uxxe3SBYE')
           ],
           [
            InlineKeyboardButton('Season 05', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADQQUAAl3T4FakyV4tLvtLWxYE'),
            InlineKeyboardButton('Season 06', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADQgUAAl3T4FaMVywpzyw71BYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "vikings_H_720p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADQwUAAl3T4FbRN8rM-_5XnxYE'),
            InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADRQUAAl3T4FatXVKwqSQAAaAWBA')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADRgUAAl3T4FZ5Op1c98J_4RYE'),
            InlineKeyboardButton('Season 04', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADSAUAAl3T4FbZlhplgBdhqBYE')
           ],
           [
            InlineKeyboardButton('Season 05', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADSQUAAl3T4Fba8TYCKe5kfRYE'),
            InlineKeyboardButton('Season 06', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADSgUAAl3T4FYOVW2iVjImpRYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "stranger_things_H":
        buttons= [
           [
              InlineKeyboardButton('480p', callback_data='stranger_things_H_480p')
           ],
           [
              InlineKeyboardButton('720p', callback_data='stranger_things_H_720p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.STRANGER_THINGS_2,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "stranger_things_E":
        buttons= [
           [
              InlineKeyboardButton('480p', callback_data='stranger_things_E_480p'),
              InlineKeyboardButton('720p', callback_data='stranger_things_E_720p')
           ],
           [
              InlineKeyboardButton('1080p', callback_data='stranger_things_E_1080p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.STRANGER_THINGS_2,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "you_E_720p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADfQQAAl3T6FZ8DJvke9vqZRYE'),
              InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADfgQAAl3T6FZ2eH8NWh1i2RYE')
           ],
           [
              InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADfwQAAl3T6Fbzc8Et6wHCwRYE'),
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "you_1080p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADgAQAAl3T6FbuqT-DhLGPdxYE'),
              InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADgQQAAl3T6FY0yFe5QE5hghYE')
           ],
           [
              InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADggQAAl3T6FZtvsWSsyCDZBYE'),
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "you_H_720p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADgwQAAl3T6FanF7X48mofdRYE'),
              InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADhAQAAl3T6FbqrBNsk4qfMRYE')
           ],
           [
              InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADhQQAAl3T6FaZgBRBcWD88RYE'),
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "stranger_things_H_480p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADXwQAAl3T6FbdhkzTtRmN8xYE'),
              InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADYAQAAl3T6FbMlJE3uvCd1xYE')
           ],
           [
              InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADYQQAAl3T6FZy54s5vRvKcxYE'),
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "stranger_things_H_720p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADYgQAAl3T6Fbm5zVUL6gnIBYE'),
              InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADYwQAAl3T6FaoG8nuaRjTMxYE')
           ],
           [
              InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADZAQAAl3T6FZDBI_pnxR5yRYE'),
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "stranger_things_E_480p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADVgQAAl3T6FZQAAH3OYLLikMWBA'),
              InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADVwQAAl3T6Fa-nEMqzqwCwRYE')
           ],
           [
              InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADWAQAAl3T6FZ6ERhcmA4wsxYE'),
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        ) 
    elif query.data == "stranger_things_E_720p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADWQQAAl3T6FblxoZg1uLucBYE'),
              InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADWgQAAl3T6FaKCLCUcAoeShYE')
           ],
           [
              InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADWwQAAl3T6Faafy61Ka5HMxYE'),
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        ) 
         
    elif query.data == "stranger_things_E_1080p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADXAQAAl3T6FZDTrbVr7TVyBYE'),
              InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADXQQAAl3T6FYNUxhZsgJy0hYE')
           ],
           [
              InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADXgQAAl3T6FacSWBEe6lK3hYE'),
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "money_heist_E":
        buttons= [
           [
              InlineKeyboardButton('480p', callback_data='money_heist_E_480p'),
              InlineKeyboardButton('720p', callback_data='money_heist_E_720p')
           ],
           [
              InlineKeyboardButton('1080p', callback_data='money_heist_E_1080p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.MONEY_HEIST_TXT_2,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
         
    elif query.data == "money_heist_E_480p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADpAQAAl3T4FYpYkX1xeLM1xYE'),
            InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADpQQAAl3T4FZC6fytqDmy4RYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADpgQAAl3T4FbZVZGYXr0vAxYE'),
            InlineKeyboardButton('Season 04', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADpwQAAl3T4FaUG0krWJaSRxYE')
           ],
           [
            InlineKeyboardButton('Season 05-A', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADqAQAAl3T4FbgL57bctSXiRYE'),
            InlineKeyboardButton('Season 05-B', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADqQQAAl3T4Fb6wBfPwSUBPRYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "money_heist_E_720p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADqgQAAl3T4FZSwZdE3f5t_RYE'),
            InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADqwQAAl3T4FbVIucr7FCSJhYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADrAQAAl3T4Fba0Y6imbKihxYE'),
            InlineKeyboardButton('Season 04', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADrQQAAl3T4FY-zbRFnTFqdBYE')
           ],
           [
            InlineKeyboardButton('Season 05-A', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADrwQAAl3T4FaPaRYZhG1txhYE'),
            InlineKeyboardButton('Season 05-B', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADrgQAAl3T4FYTG5e6yCvt7RYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "money_heist_E_1080p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADsAQAAl3T4FbYzM9x7NsV8xYE'),
            InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADsQQAAl3T4FZTKVKTVjAErhYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADsgQAAl3T4FZ1KUgquVDofxYE'),
            InlineKeyboardButton('Season 04', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADswQAAl3T4FbYksLNcgrG2xYE')
           ],
           [
            InlineKeyboardButton('Season 05-A', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADtAQAAl3T4FYK09-mn2Do2BYE'),
            InlineKeyboardButton('Season 05-B', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADtQQAAl3T4Fa4y_87l1to_RYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "money_heist_S":
        buttons= [
           [
              InlineKeyboardButton('480p', callback_data='money_heist_S_480p'),
              InlineKeyboardButton('720p', callback_data='money_heist_E_720p')
           ],
           [
              InlineKeyboardButton('1080p', callback_data='money_heist_E_1080p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.MONEY_HEIST_TXT_2,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "money_heist_S_480p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=DSTORE-OV85Xy0xMDAxNjE1MDA4MDgz'),
            InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADpQQAAl3T4FZC6fytqDmy4RYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADpgQAAl3T4FbZVZGYXr0vAxYE'),
            InlineKeyboardButton('Season 04', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADpwQAAl3T4FaUG0krWJaSRxYE')
           ],
           [
            InlineKeyboardButton('Season 05-A', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADtgQAAl3T4FYdkOYLlRdGnhYE'),
            InlineKeyboardButton('Season 05-B', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=DSTORE-OV85Xy0xMDAxNjE1MDA4MDgz')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "money_heist_H":
        buttons= [
           [
              InlineKeyboardButton('480p', callback_data='money_heist_H_480p'),
              InlineKeyboardButton('720p', callback_data='money_heist_H_720p')
           ],
           [
              InlineKeyboardButton('1080p', callback_data='money_heist_H_1080p')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.MONEY_HEIST_TXT_2,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "money_heist_H_480p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADtwQAAl3T4FaiQnIAAUQ8Z74WBA'),
            InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADuAQAAl3T4FZHoU3KBaYE1xYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADuQQAAl3T4FbQz2CMBZwIuxYE'),
            InlineKeyboardButton('Season 04', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADugQAAl3T4FZrIXOt9hX1NRYE')
           ],
           [
            InlineKeyboardButton('Season 05-A', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADqAQAAl3T4FbgL57bctSXiRYE'),
            InlineKeyboardButton('Season 05-B', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADuwQAAl3T4Fbc-4FWKDviCRYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "money_heist_H_720p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADvAQAAl3T4FataDJzQy1lZhYE'),
            InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADvQQAAl3T4FaOzm5qkMeiGxYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADvgQAAl3T4FZTR2jzY_R4LBYE'),
            InlineKeyboardButton('Season 04', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADvwQAAl3T4FYh3CTCXnXQihYE')
           ],
           [
            InlineKeyboardButton('Season 05-A', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADwAQAAl3T4FYRBFaD-HeocxYE'),
            InlineKeyboardButton('Season 05-B', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADwQQAAl3T4FaTvZTRIGeHNxYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "money_heist_H_1080p":
        buttons= [
           [
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADwgQAAl3T4FZJ-EDog8EBchYE'),
            InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADwwQAAl3T4FZc1VXSRyelRRYE')
           ],
           [
            InlineKeyboardButton('Season 03', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADxAQAAl3T4FZRdaTaC_-OURYE'),
            InlineKeyboardButton('Season 04', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADxQQAAl3T4FZXLcMLISujdxYE')
           ],
           [
            InlineKeyboardButton('Season 05-A', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADxgQAAl3T4FZlGLXWsWmJThYE'),
            InlineKeyboardButton('Season 05-B', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADwQQAAl3T4FaTvZTRIGeHNxYE')
           ],
           [
            InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "money_heist_Te":
        buttons= [[
            InlineKeyboardButton('720p', callback_data='money_heist_H_720p'),
            InlineKeyboardButton('1080p', callback_data='money_heist_H_1080p')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.MONEY_HEIST_TXT_2,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "money_heist_Ta":
        buttons= [[
            InlineKeyboardButton('720p', callback_data='money_heist_H_720p'),
            InlineKeyboardButton('1080p', callback_data='money_heist_H_1080p')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.MONEY_HEIST_TXT_2,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "Maradona_E":
        buttons= [[
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADcgYAAl3T2FbbHTYq9l3UVhYE'),
            InlineKeyboardButton('Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )     
   
    elif query.data == "witcher_480p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADZQUAAl3T4FaSp0tPpnC_FRYE'),
              InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADZgUAAl3T4FYCt4c90GA-xRYE')
           ],
           [
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "witcher_E_720p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADYwUAAl3T4FZ-T9d_UWRvLRYE'),
              InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADZAUAAl3T4Fa1xeB6Pb4PzxYE')
           ],
           [
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "witcher_H_720p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADaAUAAl3T4FaUA2gouf12xRYE'),
              InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADaQUAAl3T4FaRIaUSzd8_IxYE')
           ],
           [
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "witcher_1080p":
        buttons= [
           [
              InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADagUAAl3T4FboEr8VzcAiYBYE'),
              InlineKeyboardButton('Season 02', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADawUAAl3T4FYsgCfUSD_S7RYE')
           ],
           [
              InlineKeyboardButton('Close', callback_data='cls')
           ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "Maradona_M":
        buttons= [[
            InlineKeyboardButton('Season 01', url='https://shorturllink.in/st?api=3ef6a62253efbe7a63dd29201b2f9c661bd15795&url=https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADcwYAAl3T2FY-Wv5WgKODjhYE'),
            InlineKeyboardButton('Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=quote.RESULT_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "manuelfilter":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='help'),
            InlineKeyboardButton('Buttons', callback_data='button')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.MANUELFILTER_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "button":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='manuelfilter'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.BUTTON_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "autofilter":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='help'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.AUTOFILTER_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "spell":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='help'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.SPELL_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
        
    elif query.data == "id":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='help'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ID_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "search":
        buttons = [[
            InlineKeyboardButton(' Back', callback_data='help'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.SEARCH_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
        
    elif query.data == "imdb":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='help'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.IMDB_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "genlink":
        buttons = [[
            InlineKeyboardButton(' Back', callback_data='help'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.GENLINK_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "batch":
        buttons = [[
            InlineKeyboardButton(' Back', callback_data='help'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.BATCH_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "info":
        buttons = [[
            InlineKeyboardButton(' Back', callback_data='help'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.INFO_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
         
    elif query.data == "coct":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='help'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.CONNECTION_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "extra":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='help'),
            InlineKeyboardButton('Admin', callback_data='admin')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.EXTRAMOD_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "admin":
        buttons = [[
            InlineKeyboardButton(' Back', callback_data='help'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ADMIN_TXT,
            reply_markup=reply_markup,
            parse_mode='html'
        )
    elif query.data == "stats":
        buttons = [[
            InlineKeyboardButton(' Back', callback_data='help'),
            InlineKeyboardButton(' Close', callback_data='cls')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        timeleft = dyno
        total = await Media.count_documents()
        users = await db.total_users_count()
        chats = await db.total_chat_count()
        monsize = await db.get_db_size()
        free = 536870912 - monsize
        monsize = get_size(monsize)
        free = get_size(free)
        await query.message.edit_text(
            text=script.STATUS_TXT.format(total, users, chats, monsize, free, timeleft),
            reply_markup=reply_markup,
            parse_mode='html'
        )
        
    elif query.data == "cls":
        await query.message.delete()
      
async def auto_filter(client, msg, spoll=False):  
    if not spoll:
        message = msg
        if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
            return
        if not 2 < len(message.text) < 100:
            return
        try:
           search = message.text
           files, offset, total_results = await get_search_results(search.lower(), offset=0, filter=True)
        except MessageEmpty:
           pass

        if not files:
            if SPELL_CHECK_REPLY:
                return await advantage_spell_chok(msg)
            else:
                return
    else:
        message = msg.message.reply_to_message # msg will be callback query
        search, files, offset, total_results = spoll

    if SINGLE_BUTTON:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{get_size(file.file_size)}┆{get_name(file.file_name)}", callback_data=f'files#{file.file_id}'
                ),
            ]
            for file in files
        ]
    else:
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{file.file_name}",
                    callback_data=f'files#{file.file_id}',
                ),
                InlineKeyboardButton(
                    text=f"{get_size(file.file_size)}",
                    callback_data=f'files_#{file.file_id}',
                ),
            ]
            for file in files
        ]

    if offset != "":
        key = f"{message.chat.id}-{message.message_id}"
        BUTTONS[key] = search
        req = message.from_user.id if message.from_user else 0
        btn.append(
            [InlineKeyboardButton(text=f"📃 1/{round(int(total_results)/10)}",callback_data="pages"),InlineKeyboardButton(text="Check PM 📨", url ='https://t.me/SpaciousUniverseBot'),  InlineKeyboardButton(text="》",callback_data=f"next_{req}_{key}_{offset}")]
        )
        btn.append(
           [InlineKeyboardButton(text="🔰 How To Download 🔰", url="https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADIgUAAtukGFWHg1_Qgy7OiRYE")]
        )
    else:
        btn.append(
            [InlineKeyboardButton(text="📃 1/1",callback_data="pages"),InlineKeyboardButton(text="Check PM 📨", url ='https://t.me/SpaciousUniverseBot')]
        )
        btn.append(
           [InlineKeyboardButton(text="🔰 How To Download 🔰", url="https://t.me/SpaciousUniverseBot?start=BATCH-BQADBQADIgUAAtukGFWHg1_Qgy7OiRYE")]
        )
    imdb = await get_poster(search, file=(files[0]).file_name) if IMDB else None
    if imdb:
        cap = IMDB_TEMPLATE.format(
            query = search,
            title = imdb['title'],
            votes = imdb['votes'],
            aka = imdb["aka"],
            seasons = imdb["seasons"],
            box_office = imdb['box_office'],
            localized_title = imdb['localized_title'],
            kind = imdb['kind'],
            imdb_id = imdb["imdb_id"],
            cast = imdb["cast"],
            runtime = imdb["runtime"],
            countries = imdb["countries"],
            certificates = imdb["certificates"],
            languages = imdb["languages"],
            director = imdb["director"],
            writer = imdb["writer"],
            producer = imdb["producer"],
            composer = imdb["composer"],
            cinematographer = imdb["cinematographer"],
            music_team = imdb["music_team"],
            distributors = imdb["distributors"],
            release_date = imdb['release_date'],
            year = imdb['year'],
            genres = imdb['genres'],
            poster = imdb['poster'],
            plot = imdb['plot'],
            rating = imdb['rating'],
            url = imdb['url']
        )

    if imdb and imdb.get('poster'):
        try:
            await message.reply_photo(photo=imdb.get('poster'), caption=cap[:1024], reply_markup=InlineKeyboardMarkup(btn))

        except (MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty):
            pic = imdb.get('poster')
            poster = pic.replace('.jpg', "._V1_UX360.jpg")
            await message.reply_photo(photo=poster, caption=cap[:1024], reply_markup=InlineKeyboardMarkup(btn))

        except Exception as e:
            logger.exception(e)
            cap = f"Here is what i found for your Request {search}"
            await message.reply_text(cap, reply_markup=InlineKeyboardMarkup(btn))
    else:
        cap = f"Here is what i found for your Request {search}"
        await message.reply_text(cap, reply_markup=InlineKeyboardMarkup(btn))
    if spoll:
        await msg.message.delete()
        

async def advantage_spell_chok(msg):
    query = re.sub(r"\b(pl(i|e)*?(s|z+|ease|se|ese|(e+)s(e)?)|((send|snd|giv(e)?|gib)(\sme)?)|movie(s)?|new|latest|br((o|u)h?)*|^h(e)?(l)*(o)*|mal(ayalam)?|tamil|file|that|find|und(o)*|kit(t(i|y)?)?o(w)?|thar(o)*w?|kittum(o)*|aya(k)*(um(o)*)?|full\smovie|any(one)|with\ssubtitle)", "", msg.text, flags=re.IGNORECASE) # plis contribute some common words 
    query = f"{query.strip()} movie"
    g_s = await search_gagala(query)
    g_s += await search_gagala(msg.text)
    gs_parsed = []
    if not g_s:
        k = await msg.reply("I couldn't find any movie in that name.")
        await asyncio.sleep(8)
        await k.delete()
        return
    regex = re.compile(r".*(imdb|wikipedia).*", re.IGNORECASE) # look for imdb / wiki results
    gs = list(filter(regex.match, g_s))
    gs_parsed = [re.sub(r'\b(\-([a-zA-Z-\s])\-\simdb|(\-\s)?imdb|(\-\s)?wikipedia|\(|\)|\-|reviews|full|all|episode(s)?|film|movie|series)', '', i, flags=re.IGNORECASE) for i in gs]
    if not gs_parsed:
        reg = re.compile(r"watch(\s[a-zA-Z0-9_\s\-\(\)]*)*\|.*", re.IGNORECASE) # match something like Watch Niram | Amazon Prime 
        for mv in g_s:
            if match := reg.match(mv):
                gs_parsed.append(match.group(1))
    user = msg.from_user.id if msg.from_user else 0
    movielist = []
    gs_parsed = list(dict.fromkeys(gs_parsed)) # removing duplicates https://stackoverflow.com/a/7961425
    if len(gs_parsed) > 3:
        gs_parsed = gs_parsed[:3]
    if gs_parsed:
        for mov in gs_parsed:
            imdb_s = await get_poster(mov.strip(), bulk=True) # searching each keyword in imdb
            if imdb_s:
                movielist += [movie.get('title') for movie in imdb_s]
    movielist += [(re.sub(r'(\-|\(|\)|_)', '', i, flags=re.IGNORECASE)).strip() for i in gs_parsed]
    movielist = list(dict.fromkeys(movielist)) # removing duplicates
    if not movielist:
        k = await msg.reply("I couldn't find anything related to that. Check your spelling")
        await asyncio.sleep(8)
        await k.delete()
        return
    SPELL_CHECK[msg.message_id] = movielist
    btn = [[
                InlineKeyboardButton(
                    text=movie.strip(),
                    callback_data=f"spolling#{user}#{k}",
                )
            ] for k, movie in enumerate(movielist)]
    btn.append([InlineKeyboardButton(text="Close", callback_data=f'spolling#{user}#close_spellcheck')])
    m = await msg.reply("I couldn't find anything related to that\nDid you mean any one of these?", reply_markup=InlineKeyboardMarkup(btn))
    await asyncio.sleep(16)
    await k.delete()
    return
      
async def manual_filters(client, message, text=False):
    group_id = message.chat.id
    name = text or message.text
    reply_id = message.reply_to_message.message_id if message.reply_to_message else message.message_id
    keywords = await get_filters(group_id)
    for keyword in reversed(sorted(keywords, key=len)):
        pattern = r"( |^|[^\w])" + re.escape(keyword) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            reply_text, btn, alert, fileid = await find_filter(group_id, keyword)

            if reply_text:
                reply_text = reply_text.replace("\\n", "\n").replace("\\t", "\t")

            if btn is not None:
                try:
                    if fileid == "None":
                        if btn == "[]":
                            await client.send_message(group_id, reply_text, disable_web_page_preview=True)
                        else:
                            button = eval(btn)
                            await client.send_message(
                                group_id, 
                                reply_text,
                                disable_web_page_preview=True,
                                reply_markup=InlineKeyboardMarkup(button),
                                reply_to_message_id = reply_id
                            )
                    elif btn == "[]":
                        await client.send_cached_media(
                            group_id,
                            fileid,
                            caption=reply_text or "",
                            reply_to_message_id = reply_id
                        )
                    else:
                        button = eval(btn) 
                        await message.reply_cached_media(
                            fileid,
                            caption=reply_text or "",
                            reply_markup=InlineKeyboardMarkup(button),
                            reply_to_message_id = reply_id
                        )
                except Exception as e:
                    logger.exception(e)
                break
    else:
        return False
