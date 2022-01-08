from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Shalom...`")
# Salam


@register(outgoing=True, pattern="^.l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Om Swastiastu...`")
# Menjawab Salam


@register(outgoing=True, pattern="^.istigfar(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit("`Astaga...`")
# Istigfar


@register(outgoing=True, pattern="^.perkenalan(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Hai Guys , Perkenalkan Nama Gw {DEFAULTUSER}`")
    sleep(2)
    await event.edit(f"`Gw Tinggal Di bekasi abiez`")
    sleep(2)
    await event.edit("`Salam Kenal...`")
    sleep(2)
    await event.edit("`Udah Gitu Aja :v`")
# Perkenalan


CMD_HELP.update({
    "gabut": "**Modules** - `Gabut`\
    \n\n Cmd : `.l`\
    \nUsage : Untuk Menjawab Salam\
    \n\n Cmd : `.perkenalan`\
    \nUsage : Memperkenalkan Diri\
    \n\n Cmd : `.p`\
    \nUsage : Untuk Memberi Salam."
})
