import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def fetch_all(urls):
    tasks = [fetch(url) for url in urls]
    return await asyncio.gather(*tasks)

async def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://jsonplaceholder.typicode.com/posts/2',
        'https://jsonplaceholder.typicode.com/posts/3'
    ]
    responses = await fetch_all(urls)
    for response in responses:
        print(response)

if __name__ == '__main__':
    asyncio.run(main())