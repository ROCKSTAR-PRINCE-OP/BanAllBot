# CREATED BY @PIROXPOWER || @OpFriDay

from choot import Var
import logging
import re
import os
import sys
import asyncio
from telethon import TelegramClient, events
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


Blaze = TelegramClient(None, Var.API_KEY, Var.API_HASH)
Blaze.start(bot_token=Var.TOKEN)

print("STARTING BANALL BOT SERVER....") 

"""
MOVING TO COMMANDS NOW
"""

GANDU = []
for x in Var.OWNER_ID: 
    GANDU.append(x)


@Blaze.on(events.NewMessage(pattern="^/ping"))  
async def ping(e):
    if e.sender_id in GANDU:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"**I'm Active🔥\nStart Fucking Any Group** \n\n **__ᏢᎾᏁᎶ🏓__ !!** `{ms}` ms")

"""
 RESTART COMMANDS 
"""
@Blaze.on(events.NewMessage(pattern="^/restart"))
async def restart(e):
    if e.sender_id in GANDU:
        text = "2𝙢𝙞𝙣𝙩 𝙧𝙪𝙠 𝙖𝙮𝙖 𝙛𝙞𝙧 𝙖𝙖𝙠𝙚 𝙘𝙝𝙤𝙙𝙩𝙖🤣...!!!"
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await Blaze.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

"""
 BANALL COMMAND
"""
 
@Blaze.on(events.NewMessage(pattern="^/fuck"))
async def testing(event):
  if event.sender_id in GANDU:
   if not event.is_group:
        Reply = f"𝘾𝙝𝙪𝙩𝙞𝙮𝙚 𝙮𝙚 𝘾𝙈𝘿 𝙜𝙧𝙤𝙪𝙥 𝙢𝙚 𝙪𝙨𝙚 𝙠𝙖𝙧 𝙤𝙪𝙧 𝙢𝙖𝙖 𝙘𝙝𝙤𝙙 𝙙𝙚 𝙜𝙧𝙤𝙪𝙥 𝙠𝙞🔥."
        await event.reply(Reply, parse_mode=None, link_preview=None )
   else:
       await event.delete()
       Raichu = await event.get_chat()
       RaichUB = await event.client.get_me()
       admin = Raichu.admin_rights
       creator = Raichu.creator
       if not admin and not creator:
           await event.reply("I Don't have sufficient Rights !!")
           return
       await event.reply("**𝙁𝙪𝙘𝙠𝙚𝙙 𝙮𝙤𝙪𝙧 𝙜𝙪𝙤𝙪𝙥 𝙗𝙮 @ROCKSTAR_PRINCE_OP...**")
       everyone = await event.client.get_participants(event.chat_id)
       for user in everyone:
           if user.id == RaichUB.id:
               pass
           try:
               await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
           except Exception as e:
               await event.edit(str(e))
           await sleep(0.3)


"""
  LEAVE COMMAND 
"""
print("Leave Command Soon Currently Am Busy") 
print("BOT CHALU HAI JA MAA CHOD DE SABKI...") 
Blaze.run_until_disconnected()
