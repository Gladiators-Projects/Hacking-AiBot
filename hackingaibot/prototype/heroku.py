# Gladiators - Hacking-AiBot
# Copyright (C) 2022-Present Gladiators-Projects
# This was licensed under GNU General Public License v3.0 < https://github.com/Gladiators-Projects/Hacking-AiBot/blob/main/LICENSE >
#
# This file is a part of < https://github.com/Gladiators-Projects/Hacking-AiBot >



import asyncio
import math
import os
import time
from datetime import datetime
import sys
import heroku3
import requests
from telethon import events, custom, Button
from hackingaibot import hn, BotClient, HEROKU_APP_NAME, HEROKU_API_KEY, SUDO_USERS, DEV_USERS

heroku_api = "https://api.heroku.com"
Heroku = heroku3.from_key(HEROKU_API_KEY)


@BotClient.on(events.NewMessage(incoming=True, pattern=r"^/restart(?: |$)(.*)", forwards=False))
@BotClient.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hn, forwards=False))
async def dyno_usage(dyno):
    if dyno.fwd_from:
        return
    if int(dyno.sender_id) in DEV_USERS or int(dyno.sender_id) in SUDO_USERS:
        pass
    else:
        return
    lol = await dyno.reply("**Processing...**")
    await lol.edit("**Restarting bot...**\nPlease wait 5 seconds atmost...\nTo check if bot is awake use /ping command.")
    args = [sys.executable, "-m", "hackingaibot"]
    os.execl(sys.executable, *args)


@BotClient.on(events.NewMessage(incoming=True, pattern=r"^/(log|logs)(?: |$)(.*)", forwards=False))
@BotClient.on(events.NewMessage(incoming=True, pattern=r"\%s(log|logs)(?: |$)(.*)" % hn, forwards=False))
async def _(logg):
    if logg.fwd_from:
        return
    if int(logg.sender_id) in DEV_USERS:
        pass
    else:
        return
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        herokuapp = Heroku.app(HEROKU_APP_NAME)
    except:
        return await logg.reply(
            "Check if your Heroku API Key, Your App name are configured correctly in the heroku"
        )
    v = await logg.reply("Getting Logs....")
    with open("logs.txt", "w") as logstxt:
        logstxt.write(herokuapp.get_log())
    await v.edit("Got the logs wait a sec")
    await logg.client.send_file(
        logg.chat_id,
        "logs.txt",
        thumb="hackingaibot/resources/Gladiators.jpeg",
        reply_to=logg.id,
        caption="@Gladiators_Projects Logs.",
    )

    await asyncio.sleep(5)
    await v.delete()
    return os.remove("logs.txt")


@BotClient.on(events.NewMessage(incoming=True, pattern=r"^/(usage|heroku)(?: |$)(.*)", forwards=False))
@BotClient.on(events.NewMessage(incoming=True, pattern=r"\%s(usage|heroku)(?: |$)(.*)" % hn, forwards=False))
async def dyno_usage(dyno):
    if dyno.fwd_from:
        return
    if int(dyno.sender_id) in DEV_USERS or int(dyno.sender_id) in SUDO_USERS:
        pass
    else:
        return
    """
    Get your account Dyno Usage
    """
    die = await dyno.reply("**Processing...**")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await die.edit(
            "`Error: something bad happened`\n\n" f">.`{r.reason}`\n"
        )
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    """ - Used - """
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)

    """ - Current - """
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)

    await asyncio.sleep(1.5)

    return await die.edit(
        "**Dyno Usage**:\n\n"
        f" ☞ `Dyno usage for`  **{HEROKU_APP_NAME}**:\n"
        f"     ✰  `{AppHours}`**h**  `{AppMinutes}`**m**  "
        f"**|**  [`{AppPercentage}`**%**]"
        "\n\n"
        " ☞ `Dyno hours quota remaining this month`:\n"
        f"     ✰  `{hours}`**h**  `{minutes}`**m**  "
        f"**|**  [`{percentage}`**%**]"
    )
