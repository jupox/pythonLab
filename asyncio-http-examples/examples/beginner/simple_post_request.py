import aiohttp
import asyncio
import json

async def post_data(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            response_data = await response.text()
            print(response_data)

async def main():
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }
    await post_data(url, data)

if __name__ == '__main__':
    asyncio.run(main())