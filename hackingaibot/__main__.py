# Gladiators - Hacking-AiBot
# Copyright (C) 2022-Present Gladiators-Projects
# This was licensed under GNU General Public License v3.0 < https://github.com/Gladiators-Projects/Hacking-AiBot/blob/main/LICENSE >
#
# This file is a part of < https://github.com/Gladiators-Projects/Hacking-AiBot >


import glob
import os
import sys
from pathlib import Path
import logging
import importlib
from hackingaibot import BotClient, OWNER_ID

#logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


def load_prototype(glad_prototype):
    path = Path(f"hackingaibot/prototype/{glad_prototype}.py")
    prototypes = "hackingaibot.prototype.{}".format(glad_prototype)
    spec = importlib.util.spec_from_file_location(prototypes, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(glad_prototype)
    spec.loader.exec_module(load)
    sys.modules["hackingaibot.prototype." + glad_prototype] = load
    print("Successfully loaded " + glad_prototype + " prototype.")


def get_readable_time(seconds: int) -> str:
    count = 0
    pingtime = ""
    timearray = []
    timedetail = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        timearray.append(int(result))
        seconds = int(remainder)

    for i in range(len(timearray)):
        timearray[i] = str(timearray[i]) + timedetail[i]
    if len(time_list) == 4:
        pingtime += timearray.pop() + ", "

    timearray.reverse()
    pingtime += ":".join(timearray)

    return pingtime




path = "hackingaibot/prototype/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_prototype(plugin_name.replace(".py", ""))

print("Deployed Hacking-AiBot succesfully!!")

if __name__ == "__main__":
    if BotClient:
        BotClient.run_until_disconnected()
    else:
        pass
