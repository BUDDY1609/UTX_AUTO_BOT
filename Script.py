import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://t.me/+ONSD-vaHdJliOWQ9')
    START_TXT = environ.get("START_TXT", '''<b>Hello {} 👋🏻 Im Search Bot I can share Movies and Series 😁.</b>
    
  𝙅𝙤𝙞𝙣 @nvsmovielink

○ Notice 📙:-

○Dont Spam Me...🤒

😎 Powered by @tgnvs

©️ Maintained By @nvscloudx''')
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙷𝙴𝙻𝙿 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """<b><i>🤖 ᴍʏ ɴᴀᴍᴇ : <a href=https://t.me/angel_luciferbot><b>𝐋𝐔𝐂𝐈𝐅𝐄𝐑 𝐌𝐎𝐑𝐍𝐈𝐍𝐆𝐒𝐓𝐀𝐑</b></a>\n
👨‍💻 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 : <a href=https://t.me/tgnvs><b>🆃🅶🅽🆅🆂</b></a>\n
📝 𝐋𝐀𝐍𝐆𝐔𝐀𝐆𝐄 : 𝐏𝐘𝐑𝐎𝐆𝐑𝐀𝐌\n
📚 𝐅𝐑𝐀𝐌𝐄𝐖𝐎𝐑𝐊 : 𝐏𝐘𝐓𝐇𝐎𝐍 𝟑\n
📡 𝐇𝐎𝐒𝐓𝐄𝐃 𝐎𝐍 : 𝐕𝐏𝐒\n
📢 𝐔𝐏𝐃𝐀𝐓𝐄𝐒 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 : <a href=https://t.me/tgnvs><b></b>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n
🌟 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 : 𝐕 𝟒.𝟎\n</b></i>"""
    SOURCE_TXT = """<b>𝐈𝐟 𝐘𝐨𝐮 𝐀𝐫𝐞 𝐢𝐧𝐭𝐞𝐫𝐞𝐬𝐭𝐞𝐝 𝐈𝐧 𝐃𝐨𝐧𝐚𝐭𝐢𝐨𝐧</b>

» 𝐘𝐨𝐮 𝐂𝐚𝐧 𝐇𝐞𝐥𝐩 𝐌𝐞 𝐊𝐞𝐞𝐩 𝐒𝐡𝐚𝐫𝐢𝐧𝐠 𝐄𝐯𝐞𝐫𝐲 𝐃𝐚𝐲 𝐁𝐲 𝐌𝐚𝐤𝐢𝐧𝐠 𝐀𝐧 𝐀𝐧𝐨𝐧𝐲𝐦𝐨𝐮𝐬 𝐃𝐨𝐧𝐚𝐭𝐢𝐨𝐧 𝐕𝐢𝐚 𝐔𝐏𝐈<b>
» 𝐘𝐨𝐮 𝐂𝐚𝐧 𝐒𝐞𝐧𝐝 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭<b>
» 𝐨𝐟 𝟏𝟎₹ , 𝟐𝟎₹ , 𝟑𝟎₹ 𝐎𝐫 𝟓𝟎₹<b>
  𝙊𝙍<b>
» 𝐃𝐨𝐧𝐚𝐭𝐞 𝐎𝐧𝐥𝐲 𝐎𝐧𝐞 𝐑𝐮𝐩𝐞𝐞<b>

» 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐌𝐞𝐭𝐡𝐨𝐝𝐬:<b>
  𝐔𝐏𝐈 𝐎𝐧𝐥𝐲<b>
  <code>tgnvs@airtel</code>

» 𝐓𝐡𝐚𝐧𝐤 𝐘𝐨𝐮 𝐀𝐧𝐝 𝐄𝐧𝐣𝐨𝐲 𝐓𝐡𝐞 𝐘𝐨𝐮𝐫 𝐌𝐨𝐯𝐢𝐞<b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Search Bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. This Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Search Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Search Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/tgnvs)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
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
these are the extra features of Search Bot

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

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
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>᚛› 𝐆𝐫𝐨𝐮𝐩 ⪼ {}(<code>{}</code>)</b>
<b>᚛› 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ <code>{}</code></b>
<b>᚛› 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {}</b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫  
    
<b>᚛› 𝐈𝐃 - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞 - {}</b>
"""
