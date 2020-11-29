import aiohttp
import asyncio

async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            return html

loop = asyncio.get_event_loop()
coroutines = [get("http://127.0.0.1:8000") for _ in range(100)]
results = loop.run_until_complete(asyncio.gather(*coroutines))
for i in results:
    print(i)