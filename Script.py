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
    START_TXT = environ.get("START_TXT", '''<b>Hello {} ๐๐ป Im Search Bot I can share Movies and Series ๐.</b>
    
  ๐๐ค๐๐ฃ @nvsmovielink

โ Notice ๐:-

โDont Spam Me...๐ค

๐ Powered by @tgnvs

ยฉ๏ธ Maintained By @nvscloudx''')
    HELP_TXT = """๐ท๐ด๐ {}
๐ท๐ด๐๐ด ๐ธ๐ ๐ผ๐ ๐ท๐ด๐ป๐ฟ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐."""
    ABOUT_TXT = """<b><i>๐ค แดส ษดแดแดแด : <a href=https://t.me/angel_luciferbot><b>๐๐๐๐๐๐๐ ๐๐๐๐๐๐๐๐๐๐๐</b></a>\n
๐จโ๐ป ๐๐๐๐๐๐๐๐๐ : <a href=https://t.me/tgnvs><b>๐๐ถ๐ฝ๐๐</b></a>\n
๐ ๐๐๐๐๐๐๐๐ : ๐๐๐๐๐๐๐๐\n
๐ ๐๐๐๐๐๐๐๐๐ : ๐๐๐๐๐๐ ๐\n
๐ก ๐๐๐๐๐๐ ๐๐ : ๐๐๐\n
๐ข ๐๐๐๐๐๐๐ ๐๐๐๐๐๐๐ : <a href=https://t.me/tgnvs><b></b>แดสษชแดแด สแดสแด</a>\n
๐ ๐๐๐๐๐๐๐ : ๐ ๐.๐\n</b></i>"""
    SOURCE_TXT = """<b>๐๐ ๐๐จ๐ฎ ๐๐ซ๐ ๐ข๐ง๐ญ๐๐ซ๐๐ฌ๐ญ๐๐ ๐๐ง ๐๐จ๐ง๐๐ญ๐ข๐จ๐ง</b>

ยป ๐๐จ๐ฎ ๐๐๐ง ๐๐๐ฅ๐ฉ ๐๐ ๐๐๐๐ฉ ๐๐ก๐๐ซ๐ข๐ง๐  ๐๐ฏ๐๐ซ๐ฒ ๐๐๐ฒ ๐๐ฒ ๐๐๐ค๐ข๐ง๐  ๐๐ง ๐๐ง๐จ๐ง๐ฒ๐ฆ๐จ๐ฎ๐ฌ ๐๐จ๐ง๐๐ญ๐ข๐จ๐ง ๐๐ข๐ ๐๐๐<b>
ยป ๐๐จ๐ฎ ๐๐๐ง ๐๐๐ง๐ ๐๐ง๐ฒ ๐๐ฆ๐จ๐ฎ๐ง๐ญ<b>
ยป ๐จ๐ ๐๐โน , ๐๐โน , ๐๐โน ๐๐ซ ๐๐โน<b>
  ๐๐<b>
ยป ๐๐จ๐ง๐๐ญ๐ ๐๐ง๐ฅ๐ฒ ๐๐ง๐ ๐๐ฎ๐ฉ๐๐<b>

ยป ๐๐๐ฒ๐ฆ๐๐ง๐ญ ๐๐๐ญ๐ก๐จ๐๐ฌ:<b>
  ๐๐๐ ๐๐ง๐ฅ๐ฒ<b>
  <code>tgnvs@airtel</code>

ยป ๐๐ก๐๐ง๐ค ๐๐จ๐ฎ ๐๐ง๐ ๐๐ง๐ฃ๐จ๐ฒ ๐๐ก๐ ๐๐จ๐ฎ๐ซ ๐๐จ๐ฏ๐ข๐<b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Search Bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. This Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
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
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Search Bot

<b>Commands and Usage:</b>
โข /id - <code>get id of a specified user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """โ ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐๐๐ด๐๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐ฒ๐ท๐ฐ๐๐: <code>{}</code>
โ ๐๐๐ด๐ณ ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ
โ ๐ต๐๐ด๐ด ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ"""
    LOG_TEXT_G = """#๐๐๐ฐ๐๐ซ๐จ๐ฎ๐ฉ
    
<b>แโบ ๐๐ซ๐จ๐ฎ๐ฉ โชผ {}(<code>{}</code>)</b>
<b>แโบ ๐๐จ๐ญ๐๐ฅ ๐๐๐ฆ๐๐๐ซ๐ฌ โชผ <code>{}</code></b>
<b>แโบ ๐๐๐๐๐ ๐๐ฒ โชผ {}</b>
"""
    LOG_TEXT_P = """#๐๐๐ฐ๐๐ฌ๐๐ซ  
    
<b>แโบ ๐๐ - <code>{}</code></b>
<b>แโบ ๐๐๐ฆ๐ - {}</b>
"""
