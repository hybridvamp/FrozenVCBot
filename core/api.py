import time
import urllib.parse

import aiohttp

from config import DOWNLOAD_API_BASE, SEARCH_API_URL


async def fetch_youtube_link(query):
    try:
        async with aiohttp.ClientSession() as session:
            url = f"{SEARCH_API_URL}/search?q={urllib.parse.quote(query)}"
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
                if response.status == 200:
                    data = await response.json()
                    if isinstance(data, dict):
                        return data
                    if isinstance(data, list) and data:
                        return data[0]
        return None
    except Exception:
        return None


async def download_song(youtube_url):
    try:
        file_name = f"downloads/{time.time()}.mp3"
        download_url = f"{DOWNLOAD_API_BASE}{youtube_url}"
        async with aiohttp.ClientSession() as session:
            async with session.get(download_url, timeout=aiohttp.ClientTimeout(total=600)) as response:
                if response.status == 200:
                    with open(file_name, "wb") as f:
                        async for chunk in response.content.iter_chunked(1024):
                            f.write(chunk)
                    return file_name
        return None
    except Exception:
        return None
