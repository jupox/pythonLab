import aiohttp
import asyncio

async def fetch_with_headers(url, headers):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            return await response.text()

async def main():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    headers = {
        'User-Agent': 'aiohttp-client',
        'Accept': 'application/json'
    }
    response = await fetch_with_headers(url, headers)
    print(response)

if __name__ == '__main__':
    asyncio.run(main())