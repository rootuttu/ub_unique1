import os

from FIREX.utils import *
from userbot import *

from . import *

DELETE_TIMEOUT = 5
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "γFIRE-Xγ"
eviral = bot.uid
eviral = f"[{DEFAULTUSER}](tg://user?id={eviral})"


@bot.on(admin_cmd(pattern=r"sends (?P<shortname>\w+)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"sends (?P<shortname>\w+)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    thumb = eviral_logo1
    input_str = event.pattern_match.group(1)
    omk = f"**β πΏπππππ ππππ β** `{input_str}`\n**β ππππππππ π±π’ β** {eviral_mention}\n\nβ **[FIRE-X](https://t.me/FirexSupport)** β"
    the_plugin_file = "./userbot/plugins/Spam{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        lauda = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            thumb=thumb,
            caption=omk,
            force_document=True,
            allow_cache=False,
            reply_to=message_id,
        )
        await event.delete()
    else:
        await edit_or_reply(event, "File not found..... Kek")
