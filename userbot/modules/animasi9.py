from time import sleep

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.sange$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("SAYANGGGGGGGGG 💕")
        sleep(1)
        await e.edit("💝💘💓💗")
        sleep(1)
        await e.edit("💞💕💗💘")
        sleep(1)
        await e.edit("💝💘💓💗")
        sleep(1)
        await e.edit("💞💕💗💘")
        sleep(1)
        await e.edit("💘💞💗💕")
        sleep(1)
        await e.edit("💘💞💕💗")
        sleep(1)
        await e.edit("EMMMMMM🥺🥺🥺")
        sleep(1)
        await e.edit("💝💘💓💗")
        await e.edit("💞💕💗💘")
        await e.edit("💘💞💕💗")
        await e.edit("SAYANG")
        sleep(1)
        await e.edit("AKU 👉👈")
        sleep(1)
        await e.edit("SANGE 👉👈 😘😘")
        sleep(1)
        await e.edit("💘💘💘💘")
        sleep(1)
        await e.edit("SAYANG")
        sleep(1)
        await e.edit("AYO NGEWE🤭🤭")
        sleep(1)
        await e.edit("PLISS🥺🥺")
        sleep(1)
        await e.edit("AKU SANGE😋😋")
        sleep(1)
        await e.edit("I LOVE YOUUUU")
        sleep(1)
        await e.edit("AH AH AH BEIBB")
        sleep(1)
        await e.edit("💦💦💦💦")
        sleep(1)
        await e.edit("OH BABY")
        sleep(1)
        await e.edit("AKU SAYANG KAMU💞")


CMD_HELP.update({
    "animasi9": "`.sange`\
    \nUsage: Sange Ke Oranh.\
})
