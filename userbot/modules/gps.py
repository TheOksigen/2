from telethon.tl import types
import os
os.system("pip install geopy")
from geopy.geocoders import Nominatim
from userbot.events import register
from userbot.cmdhelp import CmdHelp


@register(outgoing=True, pattern=r"^.gps(?: |$)(.*)")
async def gps(event):
    if event.fwd_from:
        return
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    input_str = event.pattern_match.group(1)

    if not input_str:
        return await event.edit(f"**Ad verməsəniz N Σ O N Bölgə Tapa bilməz.**")

    await event.edit(f"[Tapıram...](https://t.me/neonsup)")

    geolocator = Nominatim(user_agent="theoksigen")
    geoloc = geolocator.geocode(input_str)
    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await event.reply(
            input_str,
            file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon)),
            reply_to=reply_to_id,
        )
        await event.delete()
    else:
        await event.edit(f"**Üzr istəyirəm bu sahəni yaxşı tapa bilmədim səhv edə bilərsən :(**")


Help = CmdHelp("gps").add_command(
  "gps {Bölgə adı}",
  "Yazdığınız bölgəni Telegram konumu kimi atar.",
  "gps Baku"
).add_info(f"**@Esebj / @TheOksigen / @NeonUserBot**").add()
