# N Σ O N / Esebj 
# 
# Credit: AsenaUserBot - Fusuf
#
  
import logging
import time

from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from userbot.cmdhelp import CmdHelp
from userbot.events import register

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
logger = logging.getLogger(__name__)




@register(outgoing=True, pattern=r"^.melumat(?: |$)(.*)") 
async def stats(event: NewMessage.Event) -> None: 
    waiting_message = await event.edit('**Məlumatlarınız toplanana qədər gözləyin zəhmət olmsa.**')
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0
    largest_group_member_count = 0
    largest_group_with_admin = 0
    dialog: Dialog
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        
        if isinstance(entity, Channel):
            # participants_count = (await event.get_participants(dialog, limit=0)).total
            if entity.broadcast:
                broadcast_channels += 1
                if entity.creator or entity.admin_rights:
                    admin_in_broadcast_channels += 1
                if entity.creator:
                    creator_in_channels += 1

            elif entity.megagroup:
                groups += 1
                # if participants_count > largest_group_member_count:
                #     largest_group_member_count = participants_count
                if entity.creator or entity.admin_rights:
                    # if participants_count > largest_group_with_admin:
                    #     largest_group_with_admin = participants_count
                    admin_in_groups += 1
                if entity.creator:
                    creator_in_groups += 1

        elif isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1

        elif isinstance(entity, Chat):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1

        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count
    stop_time = time.time() - start_time

    full_name = inline_mention(await event.client.get_me())
    response = f'🔸 {full_name} **Hesabının bütün məlumatları** ⤵️\n\n'
    response += f'**Şəxsi mesajların :** {private_chats} \n'
    response += f'   📊 `Kontaktlar : {private_chats - bots}` \n'
    response += f'   📊 `Botlar :  {bots}` \n'
    response += f'**Qruplar :** {groups} \n\n'
    response += f'**Kanallar :** {broadcast_channels} \n\n'
    response += f'**Admin olduğun qruplar :** {admin_in_groups} \n'
    response += f'   📊 `Sahibi olduğun qruplar : {creator_in_groups}` \n'
    response += f'   📊 `Admin olduğun qruplar : {admin_in_groups - creator_in_groups}` \n'
    response += f'**Admin olduğun kanallar :** {admin_in_broadcast_channels} \n'
    response += f'   📊 `Qurucu olduğun kanallar : {creator_in_channels}` \n'
    response += f'   📊 `Admin olduğun kanallar : {admin_in_broadcast_channels - creator_in_channels}` \n'
    response += f'✉️ Oxumadığın Mesajlar: {unread} \n\n'
    response += f'🌀 Baxmadığın taglar: {unread_mentions} \n\n'
    response += f'__Bunları hesablamaq üçün__ {stop_time:.02f} __saniyə vaxt sərf olundu__ \n'

    await event.edit(response)


def make_mention(user):
    if user.username:
        return f"@{user.username}"
    else:
        return inline_mention(user)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = ' '.join(names)
    return full_name
  
  
  
Help = CmdHelp("melumat")
Help.add_command(
    'melumat',None,
    'Hesabınız haqqında bütün məlumatları verər.'
).add_info("**@Esebj tərəfinfən hazırlandı.**").add()

