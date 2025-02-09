import requests
import time
import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.json()


async def running():
    urls = ["https://jsonplaceholder.typicode.com/posts/1"] * 5
    async with aiohttp.ClientSession() as session:
        responses = await asyncio.gather(*[fetch(session, url) for url in urls])

    data = [i for i in range(5000)]
    processed_data = list(dict.fromkeys(data))

    large_list_1 = set(range(3000))
    large_list_2 = set(range(2000, 5000))
    common_elements = list(large_list_1 & large_list_2)

    await asyncio.sleep(2)

    return {"responses": responses, "common_elements": common_elements}


def running_sync():
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(running())