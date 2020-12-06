import aiohttp
import asyncio
import aiofile

async def func(url, session, outfi):
    async with session.get(url) as response:
        html = await response.text()
        for i in html:
            if i.startswith('a'):
                await outfi.write(str(i) + '\n')

async def main(in_file, out_file):
    with open(in_file, 'r') as f:
        urls = [line.strip() for line in f.readline()]
    async with aiofile.async_open(out_file, 'a') as outfi:
            async with aiohttp.ClientSession() as session:
                task = [asyncio.create_task(func(url, session, outfi)) for url in urls]
            await asyncio.gather(*task)

loop = asyncio.get_event_loop()
loop.run_until_complete(main('urls.txt', 'found.txt'))
