#!/usr/bin/env python

import aiohttp
import asyncio

key = ""
hash = ""
action = "info"
params = {"key": key, "hash": hash, "action": action, "bw": "true"}
url = "https://nerdvm.racknerd.com/api/client/command.php"


async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            text_data = await response.text()
            free_bw = round(float(text_data.split(",")[2]) / (1024**3), 1)
            print("流量还有:", free_bw, "GB")


asyncio.run(main())
