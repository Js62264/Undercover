class script(object):
    START_TXT = """π·ππππ {}, πΈ'ππ <a href='https://t.me/Spaciousuniversebot'>π±ππ πππ£π’</a>

π° ππππππ π°πππ π΅πππππ + πΌππππ ππππππ + πΌπππππ π΅πππππ + π΅πππ πππππ π±ππ.  
πΉπππ π°ππ πΌπ ππ ππππ πΆππππ π°ππ π΄ππππ’
"""
    HELP_TXT = """π·ππ’ {}, 
ππππ π° πΌπππππ π°ππ ππππ π²ππππππππ’"""
    
    
    ABOUT_TXT = """
β― πΌπ’ π½πππ : <a href='https://t.me/SpaciousUniverseBot'>π±ππ πππ£π’</a>
β― π»ππππππ’ : <a href='https://docs.pyrogram.org/'>πΏπ’ππππππ vπ·.πΈ.πΈπΆ</a>
β― ππππππ : <a href='https://dashboard.heroku.com/'>π·πππππ</a>
β― π»πππππππ : <a href='https://docs.python.org/3/'>πΏπ’ππππ πΉ.πΏ.πΏ</a>
β― π³ππππ±πππ : <a href='https://mongodb.com/'>πΌπππππ³π±</a>
β― π±πππ ππππππ π²πππ : <a href='https://github.com/EvamariaTG/EvaMaria'>π΄ππ πΌππππ</a>
β― ππππππ π²ππππππ : <a href='https://t.me/TMWAD'>π²ππππ π·πππ</a>
β― πΌππππππππππ : <a href='https://github.com/kalanakt'>π·ππππΌπππππ</a>
"""
    
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and suzy will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>
β’ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bae Suzy supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https//t.me/spaciousuniversebot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    
    
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains cam rip, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    
    
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""
    
    
    SEARCH_TXT = """Help: <b>Search Engine</b>
A Module To Get Info From Google

<b>Commands and Usage:</b>
β’ /search  - <code>get the film information from various sources.</code>"""
    
    SPELL_TXT = """Help: <b>Check Speeling</b>
A Module To Check Spelling From Google

<b>Usage:</b>
β’ If you'r searching with wrong speeling, bot will check your spelling and get correct results</code>"""
    
    
    ID_TXT = """Help: <b>Chat/User Id <b>
A Module To Fetch Telegram Chat ID & User ID

<b>Commands and Usage:</b>
β’ /id  - <code>Use privart for user id and send to group for get chat id.</code>"""
    
    
    IMDB_TXT = """Help: <b>IMDb Info <b>
A Module To Get Movie/Tv Series Info

<b>Commands and Usage:</b>
β’ /imdb  - <code>get the movie/tv series information from IMDb source.</code>"""
    
    
    INFO_TXT ="""Help: <b>User Info<b>
A Module To Fetch Telegram User Info
   
<b>Commands and Usage:</b>
β’ /info  - <code>get information about a user.</code>"""
    GENLINK_TXT ="""Help: <b>Batch Link<b>
A Module To Genarte Link To post
   
<b>Commands and Usage:</b>
β’ /link  - <code>Send As reply</code>"""


    BATCH_TXT ="""Help: <b>Batch Link<b>
A Module To Genarte Link To Batch Files
   
<b>Commands and Usage:</b>
β’ /batch  - <code>Foewad First And Last Messeages And Get Link</code>
 
<b>NOTE:
β’ If Your File Sharing Channel is privet Channel, make bae Suzy Admin in That Channel Before Forward"""
    
    
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /logs - <code>to get the rescent errors</code>
β’ /stats - <code>to get status of files in db.</code>
β’ /users - <code>to get list of my users and ids.</code>
β’ /chats - <code>to get list of the my chats and ids </code>
β’ /leave  - <code>to leave from a chat.</code>
β’ /disable  -  <code>do disable a chat.</code>
β’ /ban  - <code>to ban a user.</code>
β’ /unban  - <code>to unban a user.</code>
β’ /channel - <code>to get list of total connected channels</code>
β’ /broadcast - <code>to broadcast a message to all users</code>"""
    
    STATUS_TXT = """
β πππππ π΅ππππ: <code>{}</code>
β π°πππππ πππππ: <code>{}</code>
β πππππ πΆπππππ: <code>{}</code>
β π³πππ πππππππ: <code>{}</code> 
β π΅πππ πππππππ: <code>{}</code>
β π·πππππ ππππ π»πππ: <code>{}</code> 
"""
    
    LOG_TEXT_G = """#NewGroup #BSB
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    
    LOG_TEXT_P = """#NewUser #BSB
ID - <code>{}</code>
Name - {}
"""
    
    LANG_TEXT = """
β Title: {}
β Year: {}
β Language: {}
β Season: Season {}
β Quality: {}
    
Choose the language you want..
"""
    
    QUALITY_TEXT = """
β Title: {}
β Year: {}
β Language: {}
β Season: Season {}
β Quality: {}
    
Choose the Quality you want..
"""
    
    RESULT_TXT = """
β Here Is Result For Your Request
"""
