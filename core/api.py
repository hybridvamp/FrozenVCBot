import asyncio
import os
import time
import urllib.parse

import aiohttp
import yt_dlp

from config import COOKIES_FILE, SEARCH_API_URL


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


def _yt_download(youtube_url, output_template):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_template,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "quiet": True,
        "no_warnings": True,
        "noplaylist": True,
    }
    if os.path.exists(COOKIES_FILE):
        ydl_opts["cookiefile"] = COOKIES_FILE
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])


async def download_song(youtube_url):
    try:
        unique = str(time.time())
        output_template = f"downloads/{unique}.%(ext)s"
        final_path = f"downloads/{unique}.mp3"
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, _yt_download, youtube_url, output_template)
        if os.path.exists(final_path):
            return final_path
        for ext in ["m4a", "webm", "opus", "ogg"]:
            alt = f"downloads/{unique}.{ext}"
            if os.path.exists(alt):
                return alt
        return None
    except Exception:
        return None
