# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
"""Userbot help command"""

import asyncio

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^help(?: |$)(.*)")
async def help(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
            await asyncio.sleep(15)
            await event.delete()
        else:
            await event.edit("Please specify a valid module name.")
            await asyncio.sleep(5)
            await event.delete()
    else:
        string = ""
        string1 = "Please specify which module do you want help for !!\nUsage: help <module name>\n\n"
        string2 = "List for all available commands below: "
        string3 = "-------------------------------------------------------------"
        for i in CMD_HELP:
            string += "-> `" + str(i)
            string += "`\n"
        await event.edit(
            f"{string1}" f"{string2}" f"{string3}\n" f"{string}" f"{string3}"
        )
        await asyncio.sleep(60)
        await event.delete()
