from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.vxin(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Nama gua πππΈπ½`")
    sleep(3)
    await typew.edit("`17 Tahun`")
    sleep(1)
    await typew.edit("`Tinggal Di bekasi, Salam Kenal:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`gua sayang bangat sama shinta`")
    sleep(1)
    await typew.edit("`I LOVE YOU π`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart


CMD_HELP.update({
    "oi": "πΎπ€π’π’ππ£π: `Kayzu`\
    \nβ³ : perkenalan Kayzu\
    \n\nπΎπ€π’π’ππ£π: `.sayang`\
    \nβ³ : Gombalan maut`\
    \n\nπΎπ€π’π’ππ£π: `.semangat`\
    \nβ³ : Jan Lupa Semangat."
})
