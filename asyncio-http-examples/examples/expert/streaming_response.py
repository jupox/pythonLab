import aiohttp
import asyncio

async def fetch_streaming(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            async for line in response.content:
                print(line.decode('utf-8').strip())

async def main():
    url = 'https://jsonplaceholder.typicode.com/posts'
    await fetch_streaming(url)

if __name__ == '__main__':
    asyncio.run(main())