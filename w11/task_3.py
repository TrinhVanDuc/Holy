import asyncio
import aiofile
import aiohttp
import re

async def fetch_html(url, session):
    async with session.request(method="GET", url=url) as resp:
        html = await resp.text()
        html = re.split(r'[\n]', html)
        for i in html:
            if i.startswith("<a >"):
                async with aiofile.async_open('found.txt', 'w') as f:
                    f.write(i)

async def parse(url):
    async with aiofile.async_open(url, 'r') as f:
        async for line in aiofile.LineReader(f):
            async with aiohttp.ClientSession() as session:
                asyncio.ensure_future(fetch_html(line, session))

loop = asyncio.get_event_loop()
loop.run_until_complete(parse('urls.txt'))