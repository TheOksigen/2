from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from time import sleep as t
from asyncio import sleep
from userbot import bot
import os 

@register(outgoing=True, pattern="^.ters(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("ℹ️ **Zəhmət olmasa bir mətnə cavab ver.**")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("ℹ️ **Zəhmət olmasa bir mətnə cavab ver.**")
        return
    chat = "@thestringsBot"
    await event.delete()
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            q=await conv.send_message(reply_message)
            t(1)
            await bot.send_message(chat,
            f"/reverse", reply_to=q.id)
            reply = await conv.get_response()
            await bot.send_message(event.chat_id,reply, reply_to=reply_message.id,)
            await event.delete()
        except YouBlockedUserError:
            await event.client.send_message("**@thestringsBot'u blokdan çıxardın zəhmət olmasa.**")

            
            
PRINTABLE_ASCII = range(0x21, 0x7F)

def aesthetify(string):
    for c in string:
        c = ord(c)
        if c in PRINTABLE_ASCII:
            c += 0xFF00 - 0x20
        elif c == ord(" "):
            c = 0x3000
        yield chr(c)


@register(outgoing=True, pattern=r"^\.ae(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text = event.pattern_match.group(1)
    else:
        await event.edit("ℹ️ **Zəhmət olmasa bir söz/mətn ver.**")
        return
    text = "".join(aesthetify(text))
    await event.edit(text=text, parse_mode=None, link_preview=False)
    raise events.StopPropagation


Help = CmdHelp('font').add_command(
  "ters <Mətn/Sözə cavab>", None,"Cavab verdiyiniz sözü tərs yönə çevirər."
).add_command(
  "ae <Mətn/Söz>",None,"Verdiyiniz mətnləri Aesthetic fontla yazar."
).add_info(
  "**@Esebj Tərəfindən Yaradılıb.**"
).add()
