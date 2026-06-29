import time

import aiohttp
import psutil
from pyrogram import Client as PyroClient
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import state
from config import API_ID, API_HASH, CURRENT_DYNO, DOWNLOAD_API_BASE, MAIN_OWNER, MAX_BOTS_PER_DYNO
from core.guards import check_abuse
from core.helpers import get_readable_time, to_bold_unicode


async def ping_handler(client, message):
    start = time.time()
    response = await message.reply_text("🏓 **Pinging...**")
    tg_ping = round((time.time() - start) * 1000)

    api_ping = "N/A"
    try:
        api_start = time.time()
        async with aiohttp.ClientSession() as session:
            async with session.get(DOWNLOAD_API_BASE, timeout=aiohttp.ClientTimeout(total=5)):
                pass
        api_ping = f"{round((time.time() - api_start) * 1000)}ms"
    except Exception:
        api_ping = "Timeout"

    uptime = get_readable_time(int(time.time() - state.bot_start_time))
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    msg = (
        f"🏓 **Pong!**\n\n"
        f"📱 **Telegram Latency:** `{tg_ping}ms`\n"
        f"📥 **Download API:** `{api_ping}`\n\n"
        f"💻 **System Stats:**\n"
        f"├ **Uptime:** `{uptime}`\n"
        f"├ **CPU:** `{cpu}%`\n"
        f"├ **RAM:** `{mem}%`\n"
        f"└ **Disk:** `{disk}%`"
    )
    await response.edit_text(msg, parse_mode=ParseMode.MARKDOWN)


async def start_handler(client, message):
    if await check_abuse(message.from_user.id):
        return

    user_link = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot_name_bold = to_bold_unicode(client.me.first_name.upper())
    owner_id = getattr(client, "clone_owner", MAIN_OWNER)

    caption = (
        f"👋 **Hello** {user_link} **!**\n\n"
        f"**Welcome to {bot_name_bold}**\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"✨ **Premium Music Experience**\n"
        f"🎧 **Audio:** High Stability Playback\n"
        f"🛡️ **Security:** Built-in Group Protection\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"💡 _Click the buttons below to explore!_"
    )

    buttons = [
        [InlineKeyboardButton("➕ Add Me to Your Group", url=f"https://t.me/{client.me.username}?startgroup=true")],
        [
            InlineKeyboardButton("📜 Commands", callback_data="show_help"),
            InlineKeyboardButton("📢 Updates", url="https://t.me/kustbots"),
        ],
        [InlineKeyboardButton("👤 Owner", url=f"tg://user?id={owner_id}")],
    ]
    await message.reply_text(caption, parse_mode=ParseMode.MARKDOWN, reply_markup=InlineKeyboardMarkup(buttons))


async def clone_command(client, message):
    user_id = message.from_user.id
    if len(message.command) < 2:
        return await message.reply_text("❌ **Usage:** `/clone <BOT_TOKEN>`")

    token = message.command[1]
    clones_on_dyno = [c for c in state.active_clients.values() if not getattr(c, "is_main", False)]
    if len(clones_on_dyno) >= MAX_BOTS_PER_DYNO:
        return await message.reply_text(f"❌ **Dyno limit of {MAX_BOTS_PER_DYNO} bots reached.**")

    status = await message.reply_text("⏳ **Initializing Clone...**")
    try:
        new_client = PyroClient(
            f"clone_{token.split(':')[0]}", api_id=API_ID, api_hash=API_HASH, bot_token=token
        )
        await new_client.start()
        me = await new_client.get_me()
        new_client.clone_owner = user_id
        new_client.is_main = False

        from handlers.router import register_handlers
        register_handlers(new_client)
        state.active_clients[me.id] = new_client

        await status.edit_text(
            f"✅ **Bot @{me.username} cloned successfully!**\n"
            f"👑 **Owner ID:** `{user_id}`\n"
            f"🖥 **Dyno:** `{CURRENT_DYNO}`"
        )
    except Exception as e:
        await status.edit_text(f"❌ **Failed to clone:** `{e}`")


async def active_bots_command(client, message):
    if message.from_user.id != MAIN_OWNER:
        return await message.reply_text("❌ **Restricted to Main Owner.**")

    if not state.active_clients:
        return await message.reply_text("❌ **No active bots found.**")

    text = f"🌐 **Active Bots** (Total: {len(state.active_clients)})\n\n"
    for _, c in state.active_clients.items():
        username = c.me.username if c.me else "Unknown"
        owner = getattr(c, "clone_owner", "Main")
        tag = "✅ Main" if getattr(c, "is_main", False) else f"🔗 Clone | Owner: `{owner}`"
        text += f"├ @{username} | {tag}\n"

    await message.reply_text(text)
