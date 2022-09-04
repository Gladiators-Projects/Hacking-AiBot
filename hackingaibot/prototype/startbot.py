# Gladiators - Hacking-AiBot
# Copyright (C) 2022-Present Gladiators-Projects
# This was licensed under GNU General Public License v3.0 < https://github.com/Gladiators-Projects/Hacking-AiBot/blob/main/LICENSE >
#
# This file is a part of < https://github.com/Gladiators-Projects/Hacking-AiBot >


###################### HELP MENU + START COMMAND ONLY #####################

import asyncio
from hackingaibot import BotClient, StartTime, OWNER_ID, BOT_USERNAME, REPO_NAME, SUDO_USERS, DEV_USERS
from telethon import events, custom, Button
from datetime import datetime
import time

def get_uptime(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    uptime_ret = (
        ((str(weeks) + "ᴡ:") if weeks else "")
        + ((str(days) + "ᴅ:") if days else "")
        + ((str(hours) + "ʜ:") if hours else "")
        + ((str(minutes) + "ᴍ:") if minutes else "")
        + ((str(seconds) + "s:") if seconds else "")
    )
    if uptime_ret.endswith(":"):
        return uptime_ret[:-1]
    else:
        return uptime_ret

REPO_NAME = "Hacking-AiBot"

glad_logo = "https://telegra.ph/file/ec3c057fcba5594151601.jpg"

help_img = "https://telegra.ph/file/ec3c057fcba5594151601.jpg"

dev_caption = """
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**

**/logs:** Get logs of your heroku app.

Pro Tip: Dev commands includes sudo commands too...

©️ @Gladiators_Projects
"""

sudo_caption = """
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**

**/usage:** Check usage of your heroku app.

**/restart:** Restarts the bot!!(Too fast!! **Supersonic**)

©️ @Gladiators_Projects
"""
hack_caption = f"""
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**

Use the following buttons to access the whole help menu.

Give a star ❤️ to our [repository](https://github.com/Gladiators-Projects/Hacking-AiBot) if you like it.

©️ @Gladiators_Projects
"""

login_caption = """
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**

**To login use these commands:-**

/pass: To check if there's any 2FA password or not!!

/phone: To get Phone number of that user.

/otp: To get last otp on that account.

©️ @Gladiators_Projects
"""

account_caption = """
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**

Here are following commands to access his account:

/first: Changes first name of the user.
Syntax: /first <first name>

/last: Changes last name of the user.
Syntax: /last <last name>

/about: Changes about section of the user.
Syntax: /about <new about>

/username: Changes about section of the user.
Syntax: /about <new username> (without '@')

/profilepic: Changes profile picture of the user.
Syntax: /profilepic <replying to image>

/username: Changes username of that user.
Syntax: /username <new username> (Don't give any used username)

/details: Gives you important details of that account.
Syntax: /details

/whole: Gives you whole data of the user as a file. 
Syntax: /whole


/terminate: Terminates all session except bot.
Syntax: /terminate

/delete:- Deletes that user's account.
Syntax: /delete <reason>(optional)

©️ @Gladiators_Projects
"""

chat_caption = f"""
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**

Help text for chat gear is too long so we divided it into 2 parts, use the below button to work with chats...

Give a star ❤️ to our [repository](https://github.com/Gladiators-Projects/Hacking-AiBot) if you like it.

©️ @Gladiators_Projects
"""

chat_caption1 = """
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**

Here are some commands to work with chats:

/promote: promotes a user as admin in a chat with all rights.
Syntax: /promote <chat id> <username> <title>
Note: Dont use emoji in title.
This gives all rights except remain anonymous one if you want that too better use:
/promoteanon <chat id> <username> <title>

/demote: demotes a user as admin in a chat with all rights.
Syntax: /demote <chat id> <username>

/demoteall: Demotes all admnis of particular chat.
Syntax: /demoteall <chat id>

/ban: demotes a user as admin in a chat with all rights.
Syntax: /ban <chat id> <username>

/banall: Bans all memebers in a chat.
Syntax: /banall <chat id>

©️ @Gladiators_Projects
"""
chat_caption2 = """
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**

Here are some commands to work with chats:

/send: sends message to any specific chat.
Syntax: /send <chat id> <message>

/leave: Kicks himself from that chat.
Syntax: /leave <chat id>

/join: Joins group/channel.
Syntax: /join <link>

/pjoin: Joins private group/channel.
Syntax: /join <hash>

Note: If all you have is a link like this one: https://t.me/joinchat/AAAAAFFszQPyPEZ7wgxLtd, The part after the https://t.me/joinchat/, this is, AAAAAFFszQPyPEZ7wgxLtd on this example, is the hash of the chat or channel.

©️ @Gladiators_Projects
"""
global_caption = """
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**

Here are following commands for global tools:

/gcast: Globally casts any message(To all private chats, group chats and channels)
Syntax: /gcast <Message>

/gpromote: Promotes user globally in all group chats.(Allow victim to add you in groups so that you can get globally promoted where he is admin with add admins right!)
Syntax: /gpromote <username>

/gdemote: Demotes user globally in all mutual chats where victim is admin with add admin right.
Syntax: /gdemote <username>

/gban: Globally bans user in all chats.
Syntax: /gban <username>

©️ @Gladiators_Projects
"""

start_img = "https://telegra.ph/file/ec3c057fcba5594151601.jpg"

help_caption = """
**Hᴇʏ ᴍᴀsᴛᴇʀ,
ʏᴏᴜ ᴄᴀɴ ᴀᴄᴄᴇss ᴛʜᴇ ᴡʜᴏʟᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ʙʏ ᴜsɪɴɢ ᴛʜᴇ ɢɪᴠᴇɴ ʙᴜᴛᴛᴏɴs!**

[©️](https://telegra.ph/file/ec3c057fcba5594151601.jpg) @Gladiators_Projects
"""
start_caption = f"""
**Nᴏᴡ ᴍᴇ ᴛᴏ ɪɴᴛʀᴏᴅᴜᴄᴇ ᴍʏsᴇʟғ.
I ᴀᴍ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟʟ ʙᴏᴛ ᴇᴠᴇʀ ᴍᴀᴅᴇ!
I ᴄᴀɴ ᴀʟʟᴏᴡ ʏᴏᴜ ᴛᴏ ᴀᴄᴄᴇss ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ʙʏ ᴜsɪɴɢ ʏᴏᴜʀ sᴛʀɪɴɢ sᴇssɪᴏɴ!
I ᴄᴀɴ ᴀssɪsᴛ ʏᴏᴜ ᴡɪᴛʜ ᴠᴀʀɪᴇᴛʏ ᴏғ ᴛᴀsᴋs, ᴀs ʙᴇsᴛ I ᴄᴀɴ.
24 ʜᴏᴜʀs ᴀ ᴅᴀʏ, 7 ᴅᴀʏs ᴀ ᴡᴇᴇᴋ!
Sʏsᴛᴇᴍs ᴀʀᴇ ɴᴏᴡ ғᴜʟʟʏ ᴏᴘʀᴇᴛɪᴏɴᴀʟ!**

Give a star ❤️ to our [repository](https://github.com/Gladiators-Projects/Hacking-AiBot) if you like it.

[©️](https://telegra.ph/file/ec3c057fcba5594151601.jpg) @Gladiators_Projects
"""
close_caption = """
**Hᴇʟᴘ ᴍᴇɴᴜ ʜᴀs ʙᴇᴇɴ ᴄʟᴏsᴇᴅ!!**

©️ @Gladiators_Projects
"""

redirectcaption = """
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**

Use me in my dm. Click on the below button to redirect.

©️ @Gladiators_Projects
"""


helpbuttons = [
    [
        Button.inline("Hack Tools", data="hacktools"),
    ],
    [
        Button.inline("Sudo Tools", data="sudocmds"),
        Button.inline("Dev Tools", data="devcmds"),
    ],
    [
        Button.inline("Check Ping", data="pings"),
        Button.inline("Close", data="close"),
    ]
]

help_buttons = [
    [
        Button.inline("Back", data="back"),
        Button.inline("Close", data="close"),
    ]
]

chat_buttons = [
    [
        Button.inline("Chat Gear[1]", data="chatgear1"),
        Button.inline("Chat Gear[2]", data="chatgear2"),
    ],
    [
        Button.inline("Back", data="hacktools"),
        Button.inline("Close", data="close"),
    ]
]
chatgear =  [
    [
        Button.inline("Back", data="chatgear"),
        Button.inline("Close", data="close"),
    ]
]

hack_help = [
    [
        Button.inline("Back", data="hacktools"),
        Button.inline("Close", data="close"),
    ]
]

hack_buttons = [
    [
        Button.inline("Login Gear", data="logingear"),
        Button.inline("Account Gear", data="accgear"),
    ],
    [
        Button.inline("Chat Gear", data="chatgear"),
        Button.inline("Global Gear", data="globalgear"),
    ],
    [
        Button.inline("Back", data="back"),
        Button.inline("Close", data="close"),
    ]
]

back_buttons = [
    [
        Button.inline("Back", data="back"),
    ]
]
startbuttons = [
    [
        (Button.url("Projects", url="https://t.me/Gladiators_Projects")),
        (Button.url("Support", url="https://t.me/ProjectsChat")),
    ],
    [
        (Button.url("Organisation", url="https://github.com/Gladiators-Projects")),
        (Button.url("Source Code", url="https://github.com/Gladiators-Projects/Hacking-AiBot")),
    ],
    [
        Button.inline("Help Menu", data="open"),
    ]
]
  
openbuttons = [
    [
        Button.inline("Open Again", data="open"),
    ]
]

redirectbutton = [
    [
        Button.url("Redirect", url=f"t.me/{BOT_USERNAME}?start=help"),
    ]
]



@BotClient.on(events.NewMessage(incoming=True, pattern="^/ping(?: |$)(.*)"))
async def start(e):
    ping_start = datetime.now()
    ping_end = datetime.now()
    ms = (ping_end-ping_start).microseconds
    uptime = get_uptime((time.time() - StartTime) * 1000)
    pomg = f"•• Pᴏɴɢ !! ••\n⏱ Pɪɴɢ sᴘᴇᴇᴅ : {ms}ᴍs\n⏳ Uᴘᴛɪᴍᴇ - {uptime}"
    await e.client.send_message(e.chat_id, "🎆")
    await e.reply(pomg)

@BotClient.on(events.NewMessage(incoming=True, pattern="^/help(?: |$)(.*)"))
async def alive(e):
    xd = str(e.chat_id)
    if '-' not in xd:
        try:
            await e.client.send_file(e.chat_id, glad_logo, caption = help_caption, buttons=helpbuttons)
        except:
            await e.client.send_message(e.chat_id, help_caption, buttons=helpbuttons)
    else:
        await e.client.send_message(e.chat_id, redirectcaption, buttons=redirectbutton)
@BotClient.on(events.NewMessage(incoming=True, pattern="^/start(?: |$)(.*)", func=lambda e: e.is_private))
async def start(e):
    xd = str(e.chat_id)
    try:
        await e.client.send_file(e.chat_id, glad_logo, caption = start_caption, buttons=startbuttons)
    except:
        await e.client.send_message(e.chat_id, start_caption, buttons=startbuttons)

@BotClient.on(events.CallbackQuery())
async def chat(event):
    if event.data == b"hacktools":
        await event.edit(
            hack_caption,
            buttons=hack_buttons,
        )
    elif event.data == b"pings":
        ping_start = datetime.now()
        ping_end = datetime.now()
        ms = (ping_end-ping_start).microseconds
        uptime = get_uptime((time.time() - StartTime) * 1000)
        pomg = f"•• Pᴏɴɢ !! ••\n⏱ Pɪɴɢ sᴘᴇᴇᴅ : {ms}ᴍs\n⏳ Uᴘᴛɪᴍᴇ - {uptime}"
        await event.edit(
            pomg,
            buttons=help_buttons,
        )
    elif event.data == b"back":
        await event.edit(
            help_caption,
            buttons=helpbuttons,
        )
    elif event.data == b"open":
        await event.edit(
            help_caption,
            buttons=helpbuttons,
        )
    elif event.data == b"close":
        await event.edit(
            close_caption,
            buttons=openbuttons,
        )
    elif event.data == b"logingear":
        await event.edit(
            login_caption,
            buttons=hack_help,
        )
    elif event.data == b"accgear":
        await event.edit(
            account_caption,
            buttons=hack_help,
        )
    elif event.data == b"chatgear":
        await event.edit(
            chat_caption,
            buttons=chat_buttons,
        )
    elif event.data == b"chatgear1":
        await event.edit(
            chat_caption1,
            buttons=chatgear,
        )
    elif event.data == b"chatgear2":
        await event.edit(
            chat_caption2,
            buttons=chatgear,
        )
    elif event.data == b"globalgear":
        await event.edit(
            global_caption,
            buttons=hack_help,
        )
    elif event.data == b"devcmds":
        chcksudo = int(event.chat_id)
        if chcksudo not in DEV_USERS:
            return
        await event.edit(
            dev_caption,
            buttons=help_buttons,
        )
    elif event.data == b"sudocmds":
        chcksudo = int(event.chat_id)
        if chcksudo in DEV_USERS or chcksudo in SUDO_USERS:
            await event.edit(
                sudo_caption,
                buttons=help_buttons,
            )
