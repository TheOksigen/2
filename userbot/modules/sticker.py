# Copyright (C) 2020 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
# Esebj 
# Neon User Bot 

from telethon import events
from userbot import bot
from userbot import CMD_HELP
from userbot.events import register
from PIL import Image
import io
import os
import asyncio
from userbot import bot
from userbot.cmdhelp import CmdHelp

# Credit:: https://github.com/mrismanaziz/Man-Userbot/blob/Man-Userbot/userbot/modules/stickers_v2.py

# ================ 1-ci əmr ================

@register(pattern=r"^\.foto(?: |$)(.*)" , outgoing=True)
async def cevir(event):
    islem = event.pattern_match.group(1)
    if islem == "":
        rep_msg = await event.get_reply_message()

        if not event.is_reply or not rep_msg.sticker:
            await event.edit(
                "**Zəhmət olmasa bir stikerə cavab ver.** 🗂"
            )
            return
        await event.edit(
            "**Uğurla foto'ya çevrildi.** 🌟"
                            )
        foto = io.BytesIO()
        foto = await event.client.download_media(rep_msg.sticker, 
                                                 foto
                                                 )

        im = Image.open(foto).convert("RGB")
        im.save("sticker.png", "png")
        await bot.send_file(
            event.chat_id, 
            "sticker.png", 
            reply_to=rep_msg, 
            caption=f"**@NeonUserBot**"
        )

        await event.delete()
        os.remove("sticker.png")

# ================ 2-ci əmr ================

@register(outgoing=True, pattern=r"^\.png$")
async def sticker_to_png(sticker):
    if not sticker.is_reply:
        await sticker.edit("**Zəhmət olmasa bir stikerə cavab ver.** 🗂")
        return False

    img = await sticker.get_reply_message()
    if not img.document:
        await sticker.edit("**Üzr istəyirəm. Lakin, bu sticker deyil!** ❌")
        return False

    await sticker.edit("**Uğurla png'ə çevrildi.** 🌟")
    image = io.BytesIO()
    await sticker.client.download_media(img, image)
    image.name = "sticker.png"
    image.seek(0)
    await sticker.client.send_file(
        sticker.chat_id, image, reply_to=img.id, force_document=True
    )
    await sticker.delete()
    return

# ================ 3-cü əmr ================

@register(outgoing=True, pattern=r"^\.stik$")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("**Zəhmət olmasa hər hansısa şəkilə cavab verin.** 🗂")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("**Bu şəkil deyil.** 🗂")
        return
    chat = "@buildstickerbot"
    await event.edit("**Sticker hazırlanır...** 🏁")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=164977173)
            )
            msg = await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply(f"**Zəhmət olmasa {chat}'u blokdan çıxarın və yenidən yoxlayın.**")
            return
        if response.text.startswith("Salam!"):
            await event.edit(
                "**Məxfilik parametrlərinizi deaktiv edə bilərsinizmi?**"
            )
        else:
            await event.delete()
            await bot.send_read_acknowledge(conv.chat_id)
            await bot.send_message(event.chat_id, response.message)
            await bot.delete_messages(event.chat_id, 
                                               [msg.id, response.id]
                                              )

from userbot import CMD_HELP
from userbot.events import register
from PIL import Image
import io
import os
import asyncio
from userbot.cmdhelp import CmdHelp

from userbot.language import get_value
LANG = get_value("cevir")

@register(outgoing=True, pattern=r"^\.foto(?: |$)(.*)")
async def cevir(event):
        rep_msg = await event.get_reply_message()

        if not event.is_reply or not rep_msg.sticker:
            await event.edit("**Bir stikerə cavab verməlisən.** 🗂")
            return
        await event.edit("**Fotoya çevirirəm...** 🌟")
        foto = io.BytesIO()
        foto = await event.client.download_media(rep_msg.sticker, foto)

        im = Image.open(foto).convert("RGB")
        im.save("sticker.png", "png")
        await event.client.send_file(
            event.chat_id, 
            "sticker.png", 
            reply_to=rep_msg, 
            caption=f"[N Σ O N](t.me/neonuserbot)")

        await event.delete()
        os.remove("sticker.png")

            
import io
import math
import urllib.request
from PIL import Image

from telethon.tl.types import DocumentAttributeFilename, MessageMediaPhoto, InputPeerNotifySettings
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP, bot, PAKET_ISMI
from userbot.events import register
from userbot.main import PLUGIN_MESAJLAR
from telethon import events
from userbot.cmdhelp import CmdHelp

PACK_FULL = "Whoa! That's probably enough stickers for one pack, give it a break. \
A pack can't have more than 120 stickers at the moment."
PACK_DOESNT_EXIST = "  A <strong>Telegram</strong> user has created the <strong>Sticker&nbsp;Set</strong>."

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("sticker")

# ████████████████████████████████ #


@register(outgoing=True, pattern="^.pack($| )?((?![0-9]).+?)? ?([0-9]*)?")
@register(outgoing=True, pattern="^.dizla($| )?((?![0-9]).+?)? ?([0-9]*)?")
@register(outgoing=True, pattern="^.dızla($| )?((?![0-9]).+?)? ?([0-9]*)?")
async def kang(event):
    await event.edit(f"{PLUGIN_MESAJLAR['dızcı']}")
    user = await bot.get_me()
    pack_username = ''
    if not user.username:
        try:
            user.first_name.decode('ascii')
            pack_username = user.first_name
        except UnicodeDecodeError: 
            pack_username = user.id
    else: pack_username = user.username

    textx = await event.get_reply_message()
    emoji = event.pattern_match.group(2)
    number = int(event.pattern_match.group(3) or 1)
    new_pack = False

    if textx.photo or textx.sticker: message = textx
    elif event.photo or event.sticker: message = event
    else:
        await event.edit(LANG['GIVE_STICKER'])
        return

    sticker = io.BytesIO()
    await bot.download_media(message, sticker)
    sticker.seek(0)

    if not sticker:
        await event.edit(LANG['FAIL_DOWNLOAD'])
        return

    is_anim = message.file.mime_type == "application/x-tgsticker"
    if not is_anim:
        img = await resize_photo(sticker)
        sticker.name = "sticker.png"
        sticker.seek(0)
        img.save(sticker, "PNG")

    # əmrdən istifadə edən zaman istifadəçi emoji seçmeyibse bot bu emojini göndərəcək
    if not emoji:
        if message.file.emoji: 
            emoji = message.file.emoji
        else: 
            emoji = "⚡"

    packname = f"a{user.id}_by_{pack_username}_{number}{'_anim' if is_anim else ''}"
    packtitle = (f"@{user.username or user.first_name} {PAKET_ISMI} "
                f"{number}{' animasyonlu' if is_anim else ''}")
    response = urllib.request.urlopen(
            urllib.request.Request(f'http://t.me/addstickers/{packname}'))
    htmlstr = response.read().decode("utf8").split('\n')
    new_pack = PACK_DOESNT_EXIST in htmlstr

    if new_pack:
        await event.edit("**Paket yaradıla bilmədi.\nYeni paket yaradılır... ✨**")
        await newpack(is_anim, sticker, emoji, packtitle, packname, message)
    else:
        async with bot.conversation("Stickers") as conv:
            
            await conv.send_message('/cancel')
            await conv.get_response()

            # stiker elave eleme emri
            await conv.send_message('/addsticker')
            await conv.get_response()

            # paket adı gönderir
            await conv.send_message(packname)
            x = await conv.get_response()

            
            while x.text == PACK_FULL:
                
                number += 1
                packname = f"a{user.id}_by_{pack_username}_{number}{'_anim' if is_anim else ''}"
                packtitle = (f"@{user.username or user.first_name} {PAKET_ISMI} "
                            f"{number}{' animated' if is_anim else ''}")

                await event.edit(
                    LANG['TOO_STICKERS'].format(number)
                )

                await conv.send_message(packname)
                x = await conv.get_response()
                if x.text == "Invalid pack selected.": # That pack doesn't exist
                    await newpack(is_anim, sticker, emoji, packtitle, packname)

                    # Read all unread messages
                    await bot.send_read_acknowledge("stickers")
                    # Unmute Stickers bot back
                    muted = await bot(UpdateNotifySettingsRequest(
                        peer=429000,
                        settings=InputPeerNotifySettings(mute_until=None))
                    )

                    await event.edit(
                        f"**Sticker {number}{'(animasyonlu)' if is_anim else ''} saylı paketə əlavə olundu, "
                        f"{emoji} emojisi ilə birlikdə! "
                        f"Paket** [buradan](t.me/addstickers/{packname}) **tapıla bilər.**",
                        parse_mode='md')
                    return

            # Upload the sticker file
            if is_anim:
                upload = await message.client.upload_file(sticker, file_name="AnimatedSticker.tgs")
                await conv.send_file(upload, force_document=True)
            else:
                sticker.seek(0)
                await conv.send_file(sticker, force_document=True)
            kontrol = await conv.get_response()
        
            if "Sorry, the image dimensions are invalid." in kontrol.text:
                await event.edit("`Sticker's qəbul etmədi. İkinci yol yoxlanılır...`")
                try:
                    await bot.send_file("@ezstickerbot", message, force_document=True)
                except YouBlockedUserError:
                    return await event.edit("**Zəhmət olmasa @EzStickerBot blokdan çıxarın və yenidən cəhd edin!**")

                try:
                    response = await conv.wait_event(events.NewMessage(incoming=True,from_users=350549033))
                    if "Please temporarily use" in response.text:
                        await bot.send_file("@EzStickerBotBackupBot", message, force_document=True)
                        response = await conv.wait_event(events.NewMessage(incoming=True,from_users=891811251))
                
                    await bot.send_read_acknowledge(350549033)
                    await event.client.forward_messages("stickers", response.message, 350549033)
                except:
                    await bot.send_file("@EzStickerBotBackupBot", message, force_document=True)
                    response = await conv.wait_event(events.NewMessage(incoming=True,from_users=891811251))
                    await bot.send_read_acknowledge(891811251)
                    await event.client.forward_messages("stickers", response.message, 891811251)

            # stiker üçün emoji göndərir
            await conv.send_message(emoji)
            await conv.get_response()

            
            await conv.send_message('/done')
            await conv.get_response()

    
    await bot.send_read_acknowledge(429000)
   
    muted = await bot(UpdateNotifySettingsRequest(
        peer=429000,
        settings=InputPeerNotifySettings(mute_until=None))
    )

    await event.edit(
        f"**Sticker {number}{'(animasyonlu)' if is_anim else ''} saylı paketə əlavə edildi, "
        f"{emoji} emojisi ilə birlikdə! "
        f"Paket** [buradan](t.me/addstickers/{packname}) **tapıla bilər**",
        parse_mode='md')


async def newpack(is_anim, sticker, emoji, packtitle, packname, message):
    async with bot.conversation("stickers") as conv:
        # bota dayandır əmri verir
        await conv.send_message('/cancel')
        await conv.get_response()

        # yeni paket yaratmaq üçün bota komanda verir
        if is_anim:
            await conv.send_message('/newanimated')
        else:
            await conv.send_message('/newpack')
        await conv.get_response()

        # paket üçün ad verir
        await conv.send_message(packtitle)
        await conv.get_response()

        # stiker faylını yükləyir
        if is_anim:
            upload = await bot.upload_file(sticker, file_name="AnimatedSticker.tgs")
            await conv.send_file(upload, force_document=True)
        else:
            sticker.seek(0)
            await conv.send_file(sticker, force_document=True)
        kontrol = await conv.get_response()
        if kontrol.message.startswith("Sorry"):
            await bot.send_file("@ezstickerbot", message, force_document=True)
            try:
                response = await conv.wait_event(events.NewMessage(incoming=True,from_users=350549033))
                if "Please temporarily use" in response.text:
                    await bot.send_file("@EzStickerBotBackupBot", message, force_document=True)
                    response = await conv.wait_event(events.NewMessage(incoming=True,from_users=891811251))
                
                    await bot.send_read_acknowledge(350549033)
                    await bot.forward_messages("stickers", response.message, 350549033)
            except:
                await bot.send_file("@EzStickerBotBackupBot", message, force_document=True)
                response = await conv.wait_event(events.NewMessage(incoming=True,from_users=891811251))
                await bot.send_read_acknowledge(891811251)
                await bot.forward_messages("stickers", response.message, 891811251)

        # Send the emoji
        await conv.send_message(emoji)
        await conv.get_response()

        # Publish the pack
        await conv.send_message("/publish")
        if is_anim:
            await conv.get_response()
            await conv.send_message(f"<{packtitle}>")
        await conv.get_response()

        # Skip pack icon selection
        await conv.send_message("/skip")
        await conv.get_response()

        # Send packname
        await conv.send_message(packname)
        await conv.get_response()

async def resize_photo(photo):
    """ yenidən ölçü verər 512x512 """
    image = Image.open(photo)
    scale = 512 / max(image.width, image.height)
    new_size = (int(image.width*scale), int(image.height*scale))
    image = image.resize(new_size, Image.ANTIALIAS)
    return image


import io
import os
import random
import textwrap

from PIL import Image, ImageChops, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterDocument
from userbot.events import register 
from userbot import CMD_HELP, bot
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("rgb")

# ████████████████████████████████

@register(outgoing=True, pattern="^.rgb(?: |$)(.*)")
async def sticklet(event):
    R = random.randint(0,256)
    G = random.randint(0,256)
    B = random.randint(0,256)

    # Giriş metnini al
    sticktext = event.pattern_match.group(1).strip()

    if len(sticktext) < 1:
        await event.edit(LANG['NEED_TEXT'])
        return

    # Komutu düzenle
    await event.edit("**Sticker hazırlanır...**")

    # https://docs.python.org/3/library/textwrap.html#textwrap.wrap
    sticktext = textwrap.wrap(sticktext, width=10)
    # Listeyi bir dizeye dönüştür
    sticktext = '\n'.join(sticktext)

    image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    fontsize = 230

    FONT_FILE = await get_font_file(event.client, "@xcruzfont")

    font = ImageFont.truetype(FONT_FILE, size=fontsize)

    while draw.multiline_textsize(sticktext, font=font) > (512, 512):
        fontsize -= 10
        font = ImageFont.truetype(FONT_FILE, size=fontsize)

    width, height = draw.multiline_textsize(sticktext, font=font)
    draw.multiline_text(((512-width)/2,(512-height)/2), sticktext, font=font, fill=(R, G, B))

    image_stream = io.BytesIO()
    image_stream.name = "@resim.webp"

    def trim(im):
        bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
        diff = ImageChops.difference(im, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
        return im.crop(bbox) if bbox else im

    image = trim(image)
    image.save(image_stream, "WebP")
    image_stream.seek(0)

    # mesajı sil
    await event.delete()

    await event.client.send_file(event.chat_id, image_stream, reply_to=event.message.reply_to_msg_id)
    # Temizlik
    try:
        os.remove(FONT_FILE)
    except:
        pass


async def get_font_file(client, channel_id):
    font_file_message_s = await client.get_messages(
        entity=channel_id,
        filter=InputMessagesFilterDocument,
        limit=None
    )

    font_file_message = random.choice(font_file_message_s)
    return await client.download_media(font_file_message)


CmdHelp('sticker').add_command(
    'pack / .dizla', '{emoji(lər)} {rəqəm}', 'Stickeri yada Şəkli seçilən paketə əlavə edər və seçdiyiniz emoji stickerin emojisi olaraq işlədər.'
).add_command(
    "stik","{Foto'ya Cavab}","Cavab verdiyiniz Fotonu sticker'ə çevirər."
).add_command(
    "png","{Stikerə cavab}","Cavab verdiyiniz stikeri PNG formaya çevirin.."
).add_command(
    "foto","{Stikerə cavab}","Cavab verdiyiniz stikeri foto'ya çevirər."
).add_command(
    'rbg', '<söz/mətn/mesaja cavab>', 'Mətninizi RGB Stickerə çevirin.'
).add()
