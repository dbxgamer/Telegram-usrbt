"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

    input_str = event.pattern_match.group(1)

    if input_str == "call":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Telegram Headquarters...`",
            "`Call Connected.`",
            "`Telegram: Hello This is Telegram HQ. Who is this?`",
            "`Me: Yo this is` @darkbeast842 ,`Please Connect me to ANTIRIPPER hq`",
            "`User Authorised.`",
            "`Calling ANTIRIPPER Gawd`  `At +916969420420`",
            "`Private  Call Connected...`",
            "`Me: Hello Sir, Please Ban This Telegram Account.`",    
            "`AR_gawd: May I Know Who Is This?`",
            "`Me: Yo brother, Its me @darkbeast842 `",
            "`AR_gawd: OMG!!! Long time no see, Wassup Brother...\nI'll Make Sure That Gay Account Will Get Blocked Within 24Hrs.`",
            "`Me: Thanks, See You Later Bro.`",
            "`AR_gawd: Please Don't Thank Bro, Telegram Is Our's. Just Gimme A Call When You Become Free.`",
            "`Me: Is There Any Issue/Emergency???`",
            "`AR_gawd: Yes Sur, There Is are many rippers In Telegram.\nI Am Not Able To Fix this issue. We people are so less.`",
            "`Me: OK!!! Let's Spread awareness and collect people!!!`",
            "`AR_gawd: Sure Sur..Good IDEA \nTC Bye Bye :)`",
            "`Private Call Disconnected.`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 18])
