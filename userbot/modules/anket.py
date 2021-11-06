# N Σ O N / Nusrets / TheOksigen
# Credit - Ultroid

from telethon.tl.types import InputMediaPoll, Poll, PollAnswer
from userbot.events import register as neon 
import asyncio
from userbot.cmdhelp import CmdHelp 

@neon(groups_only=True,pattern="^.anket(?: |$)(.*)", outgoing=True)
async def uri_poll(e):
    match = e.pattern_match.group(1)
    if not match:
        return await e.edit("**Zəhmət olmasa düzgün məlumat daxil edin.**")
    if ";" not in match:
        return await e.edit("**Seçimləriizi müəyyən edə bilmədim.**")
    ques = match.split(";")[0]
    option = match.split(";")[1::]
    publ = None
    quizo = None
    karzo = None
    mpp = None
    if "|" in match:
        ptype = match.split(" | ")[1]
        option = match.split("|")[0].split(";")[1::]
        if "_" in ptype:
            karzo = [str(int(ptype.split("_")[1]) - 1).encode()]
            ptype = ptype.split("_")[0]
        if ptype not in ["açıq", "test", "çox"]:
            return await e.edit("**Yanlış anket tipi seçdiniz!**")
        if ptype == "açıq":
            publ = True
        if ptype == "test":
            quizo = True
        if ptype == "çox":
            mpp = True
    if len(option) <= 1:
        return await e.edit("**Seçimləriniz 1-dən çox olmalıdır.**")
    m = await e.edit("__Anket hazırlanır...__")
    OUT = []
    for on in range(len(option)):
        OUT.append(PollAnswer(option[on], str(on).encode()))
    await e.client.send_file(
        e.chat_id,
        InputMediaPoll(
            Poll(20, ques, OUT, multiple_choice=mpp, public_voters=publ, quiz=quizo),
            correct_answers=karzo,
        ),
    )
    await m.delete()


Help = CmdHelp("anket")
Help.add_command(
              "anket {Sualınız};{Seçim};{Seçim};{Seçim}",
              'Verdiyiniz sual və cavablara əsasən N Σ O N anket hazırlayar.',
              "anket Sizcə hansı?;Telegram;Instagram;Facebook;TikTok;WhatsApp")
Help.add_command(
              "anket {Sualınız};{Seçim};{Seçim};{Seçim} | {Anket tipi}",
              "N Σ O N verdiyiniz Sual və seçimlərə uyğun qeyd etdiyiniz anket tipini hazırlayar.\nAnket tipləri: Açıq / Test / Çox",
              "anket Ən sevdiyiniz reper hansıdır?;Aslixan;Epi;Paster;Okaber;Ruzgar | çox")
Help.add_info("**@Nusrets tərəfindən @NeonUserBot üçün hazırlandı.**")
Help.add()
