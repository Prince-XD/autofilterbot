class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},
M𝚈 N𝙰𝙼𝙴 I𝚂 <a href=https://t.me/{}>{}</a>
I C𝙰𝙽 P𝚁𝙾𝚅𝙸𝙳𝙴 M𝙾𝚅𝙸𝙴𝚂, J𝚄𝚂𝚃 A𝙳𝙳 M𝙴 T𝙾 Y𝙾𝚄𝚁 G𝚁𝙾𝚄𝙿 A𝙽𝙳 E𝙽𝙹𝙾𝚈 😍"""
    HELP_TXT = """H𝙴𝚈 {}
H𝙴𝚁𝙴 I𝚂 T𝙷𝙴 H𝙴𝙻𝙿 F𝙾𝚁 M𝚈 C𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """✯ M𝚈 N𝙰𝙼𝙴: {}
✯ C𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/PrincexBots>Prince</a>
✯ L𝙸𝙱𝚁𝙰𝚁𝚈: P𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ L𝙰𝙽𝙶𝚄𝙰𝙶𝙴: P𝚈𝚃𝙷𝙾𝙽 𝟹
✯ D𝙰𝚃𝙰 B𝙰𝚂𝙴: M𝙾𝙽𝙶𝙾 D𝙱
✯ B𝙾𝚃 S𝙴𝚁𝚅𝙴𝚁: H𝙴𝚁𝙾𝙺𝚄
✯ B𝚄𝙸𝙻𝙳 S𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """Private Source For Now Soon Public"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Bot should have Admin Privillage.
2. Only admins can Add Filters in a Chat.
3. Alert buttons have a limit of 64 Characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/PrincexBots)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my Admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ T𝙾𝚃𝙰𝙻 F𝙸𝙻𝙴𝚂: <code>{}</code>
★ T𝙾𝚃𝙰𝙻 U𝚂𝙴𝚁𝚂: <code>{}</code>
★ T𝙾𝚃𝙰𝙻 C𝙷𝙰𝚃𝚂: <code>{}</code>
★ U𝚂𝙴𝙳 S𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ F𝚁𝙴𝙴 S𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
