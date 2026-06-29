import asyncio
import logging
import os

from pyrogram import filters, idle
from pyrogram.handlers import MessageHandler

import state
from clients import app, call_py, user_app
from config import DEPLOYED_OWNER_ID
from handlers.router import register_handlers
from handlers.system import active_bots_command, clone_command
from server import start_server

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [KustMusic] - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

if not os.path.exists("downloads"):
    os.makedirs("downloads")


async def main():
    logger.info("Starting KustMusic")

    await start_server()

    await app.start()
    app.clone_owner = DEPLOYED_OWNER_ID
    app.is_main = True
    register_handlers(app)
    app.add_handler(MessageHandler(clone_command, filters.command("clone") & filters.private))
    app.add_handler(MessageHandler(active_bots_command, filters.command("active") & filters.private))
    state.active_clients[app.me.id] = app

    await user_app.start()
    me = await user_app.get_me()
    state.ASSISTANT_ID = me.id
    state.ASSISTANT_USERNAME = me.username
    logger.info(f"Assistant: {state.ASSISTANT_ID} (@{state.ASSISTANT_USERNAME})")

    await call_py.start()
    logger.info(f"Bot running: @{app.me.username}")

    await idle()

    await call_py.stop()
    await user_app.stop()
    for c in list(state.active_clients.values()):
        try:
            await c.stop()
        except Exception:
            pass


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
