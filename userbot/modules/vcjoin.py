# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Recode By Kayzu - Ubot


from pytgcalls.exceptions import NotConnectedError

from userbot import CMD_HELP
from userbot.events import register


@vc_asst("joinvc")
async def join_(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(get_string("vcbot_2").format(str(e)))
    else:
        chat = event.chat_id
    ultSongs = Player(chat, event)
    if not kayzu.group_call.is_connected:
        await kayzu.vc_joiner()


@vc_asst("(leavevc|stopvc)")
async def leaver(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(get_string("vcbot_2").format(str(e)))
    else:
        chat = event.chat_id
    Kayzu = Player(chat)
    await kayzu.group_call.stop()
    if CLIENTS.get(chat):
        del CLIENTS[chat]
    if VIDEO_ON.get(chat):
        del VIDEO_ON[chat]
    await event.eor(get_string("vcbot_1"))

CMD_HELP.update({
   "vcjoin": 
n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.joinvc`
\n↳: 'Join Voice Chat.'
\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.leavevc`
\n↳: `Leave The Voice Chat.`
})
