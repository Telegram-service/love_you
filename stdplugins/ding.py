"""Emoji

Available Commands:

.ding"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 10)

    input_str = event.pattern_match.group(1)

    if input_str == "ding":

        await event.edit(input_str)

        animation_chars = [
        
            "馃敶猬涒瑳猬溾瑴\n猬溾瑴猬溾瑴猬淺n猬溾瑴猬溾瑴猬�",
            "猬溾瑴猬涒瑴猬淺n猬溾瑳猬溾瑴猬淺n馃敶猬溾瑴猬溾瑴",
            "猬溾瑴猬涒瑴猬淺n猬溾瑴猬涒瑴猬淺n猬溾瑴馃敶猬溾瑴",
            "猬溾瑴猬涒瑴猬淺n猬溾瑴猬溾瑳猬淺n猬溾瑴猬溾瑴馃敶",
            "猬溾瑴猬涒瑳馃敶\n猬溾瑴猬溾瑴猬淺n猬溾瑴猬溾瑴猬�",    
            "猬溾瑴猬涒瑴猬淺n猬溾瑴猬溾瑳猬淺n猬溾瑴猬溾瑴馃敶",
            "猬溾瑴猬涒瑴猬淺n猬溾瑴猬涒瑴猬淺n猬溾瑴馃敶猬溾瑴",
            "猬溾瑴猬涒瑴猬淺n猬溾瑳猬溾瑴猬淺n馃敶猬溾瑴猬溾瑴",
            "馃敶猬涒瑳猬溾瑴\n猬溾瑴猬溾瑴猬淺n猬溾瑴猬溾瑴猬�",
            "猬溾瑴猬溾瑴猬淺n猬� [love_you](https://github.com/Telegram-service/love_you/) 猬淺n猬溾瑴猬溾瑴猬�"

 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])
