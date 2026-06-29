import asyncio

from pyrogram.enums import ParseMode
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

import state
from config import MAIN_OWNER
from core.guards import is_admin
from core.playback import play_music_core
from handlers.music import clear_command, pause_command, resume_command, skip_command, stop_command
from handlers.system import start_handler


async def callback_handler(client, query: CallbackQuery):
    data = query.data
    chat_id = query.message.chat.id
    user_id = query.from_user.id

    if data == "progress":
        return await query.answer("❄️ Live Playback")

    if data == "verify_assistant":
        if not await is_admin(client, chat_id, user_id):
            return await query.answer("❌ Admin only!", show_alert=True)
        if chat_id in state.chat_queues and state.chat_queues[chat_id]:
            await query.message.edit_text("🔄 **Continuing playback...**")
            asyncio.create_task(play_music_core(client, chat_id, state.chat_queues[chat_id][0], query.message))
        else:
            await query.message.edit_text("❌ **Queue is empty.**")
        return

    if data == "show_help":
        buttons = [
            [
                InlineKeyboardButton("🎵 Music", callback_data="help_music"),
                InlineKeyboardButton("🛡️ Admin", callback_data="help_admin"),
            ],
            [InlineKeyboardButton("🏠 Home", callback_data="go_back")],
        ]
        return await query.message.edit_text("📜 **Commands:**", reply_markup=InlineKeyboardMarkup(buttons))

    if data == "go_back":
        return await start_handler(client, query.message)

    if data == "help_music":
        return await query.message.edit_text(
            "🎵 *Music*\n\n`/play` - Play song\n`/stop` - Stop\n`/skip` - Skip\n`/pause` - Pause\n`/resume` - Resume",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="show_help")]]),
        )

    if data == "help_admin":
        return await query.message.edit_text(
            "🛡️ *Admin*\n\n`/kick`, `/ban`, `/unban`, `/mute`, `/unmute`",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="show_help")]]),
        )

    if data in ["stop", "skip", "pause", "resume", "clear"]:
        if not await is_admin(client, chat_id, user_id):
            return await query.answer("❌ Admin only!", show_alert=True)
        if data == "stop":
            await stop_command(client, query.message)
        elif data == "skip":
            await skip_command(client, query.message)
        elif data == "pause":
            await pause_command(client, query.message)
        elif data == "resume":
            await resume_command(client, query.message)
        elif data == "clear":
            if chat_id in state.chat_queues and len(state.chat_queues[chat_id]) > 1:
                state.chat_queues[chat_id] = [state.chat_queues[chat_id][0]]
                await query.answer("🗑 Queue cleared.")
                await query.message.edit_text("🗑 **Queue cleared by admin.**")
            else:
                await query.answer("❌ Queue is already empty.")
        try:
            await query.answer()
        except Exception:
            pass
