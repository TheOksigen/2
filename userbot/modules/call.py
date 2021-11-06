import os 
os.system("pip install tgcalls")
from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc
from userbot.events import register
from userbot import bot, get_call
from userbot.cmdhelp import CmdHelp


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]

ADMIN = "**Bunu edə bilmək üçün admin səlahiyyətlərinə sahib olmalısan.**"
@register(outgoing=True, groups_only=True, pattern="^.call$")
@register(outgoing=True, groups_only=True, pattern="^.startvc$")
@register(outgoing=True, groups_only=True, pattern="^.vcba[şs]lat$")
async def start_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    photo = None

    if not admin and not creator:
        await c.edit(ADMIN)
        return
    try:
        await c.client(startvc(c.chat_id))
        await c.edit("**Səsli söhbət başladı!** 🌟")
    except Exception as ex:
        await c.edit(f"**Bir xəta yarandı\nXəta:** ```{ex}```")

@register(outgoing=True, groups_only=True, pattern="^.callstop$")
@register(outgoing=True, groups_only=True, pattern="^.stopvc$")
@register(outgoing=True, groups_only=True, pattern="^.vcb[ıi]t[ıi]r$")
async def stop_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    photo = None

    if not admin and not creator:
        await c.edit(ADMIN)
        return
    try:
        await c.client(stopvc(await get_call(c)))
        await c.edit("**Səsli söhbət uğurla sonlandırıldı!**")
    except Exception as ex:
        await c.edit(f"**Bir hata oluştu\nHata:** ```{ex}```")



@register(outgoing=True, groups_only=True, pattern="^.vcd[eə]v[eə]t")
@register(outgoing=True, groups_only=True, pattern="^.vctag")
@register(outgoing=True, groups_only=True, pattern="^.tagvc(?: |$)(.*)")
async def _(c):
    await c.edit("**İstifadəçilər səsli söhbətə dəvət edilir...** 🗣")
    users = []
    z = 0
    async for x in c.client.iter_participants(c.chat_id):
        if not x.bot:
            users.append(x.id)
    hm = list(user_list(users, 6))
    for p in hm:
        try:
            await c.client(invitetovc(call=await get_call(c), users=p))
            z += 6
        except BaseException:
            pass
    await c.edit(f"{z} **İstifadəçi(lər) çağırıldı...** 🗣")
    
Help = CmdHelp("call")
Help.add_command("startvc | .call | .vcbaslat",None,"N Σ O N Qrupda səsli söhbət başladar.")
Help.add_command("stopvc | .callstop | .vcbitir",None,"Səsli söhbəti sonlandırar.")
Help.add_command("vctag | .tagv | .vcdevet",None,"İnsanları səsli söhbətə dəvət edər.")
Help.add()
