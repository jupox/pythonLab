import aiohttp
import asyncio

async def fetch_with_error_handling(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()  # Raise an error for bad responses
                return await response.text()
    except aiohttp.ClientError as e:
        print(f"Client error occurred: {e}")
    except aiohttp.http_exceptions.HttpProcessingError as e:
        print(f"HTTP processing error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

async def main():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    response = await fetch_with_error_handling(url)
    if response:
        print(response)

if __name__ == '__main__':
    asyncio.run(main())