import asyncio
import logging
import os
import time

from pyrogram.enums import ParseMode
from pyrogram.errors import RPCError, UserAlreadyParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytgcalls import filters as fl
from pytgcalls.types import StreamEnded

import state
from clients import call_py, user_app
from core.api import download_song
from core.helpers import get_progress_bar, one_line_title, parse_duration_str

logger = logging.getLogger(__name__)


async def _check_assistant_in_chat(client, chat_id, who):
    try:
        member = await client.get_chat_member(chat_id=chat_id, user_id=who)
        status = getattr(member, "status", None)
        if hasattr(status, "value"):
            return status.value
        if isinstance(status, str):
            return status
        return str(status) if status is not None else False
    except Exception as e:
        if "UserNotParticipant" in type(e).__name__:
            return False
        if isinstance(e, RPCError) and "USER_BANNED" in str(e).upper():
            return "banned"
        return False


async def update_progress_caption(chat_id, message, start_time, total_duration, base_caption):
    try:
        while True:
            elapsed = time.time() - start_time
            if total_duration > 0 and elapsed > total_duration:
                elapsed = total_duration

            progress_bar = get_progress_bar(elapsed, total_duration)
            new_keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton(text=progress_bar, callback_data="progress")],
                [
                    InlineKeyboardButton(text="▷", callback_data="resume"),
                    InlineKeyboardButton(text="II", callback_data="pause"),
                    InlineKeyboardButton(text="‣‣I", callback_data="skip"),
                    InlineKeyboardButton(text="▢", callback_data="stop"),
                ],
            ])

            try:
                await message.edit_caption(
                    caption=base_caption, reply_markup=new_keyboard, parse_mode=ParseMode.HTML
                )
            except Exception as e:
                if "MESSAGE_NOT_MODIFIED" not in str(e):
                    break

            if total_duration > 0 and elapsed >= total_duration:
                break
            await asyncio.sleep(10)
    except asyncio.CancelledError:
        pass
    except Exception as e:
        logger.error(f"Progress update error: {e}")


async def play_music_core(client, chat_id, song_info, status_msg=None, retry_attempt=False):
    try:
        if chat_id not in state.assistant_cache or retry_attempt:
            is_participant = await _check_assistant_in_chat(client, chat_id, state.ASSISTANT_ID)
            if not is_participant:
                if status_msg:
                    await status_msg.edit_text("🔍 **Assistant not in chat.**\nGenerating invite link...")
                try:
                    try:
                        invite_link = await client.export_chat_invite_link(chat_id)
                    except Exception:
                        link_obj = await client.create_chat_invite_link(chat_id)
                        invite_link = link_obj.invite_link

                    try:
                        if "+" in invite_link:
                            await user_app.join_chat(invite_link)
                        else:
                            await user_app.join_chat(chat_id)
                    except Exception as join_err:
                        err_s = str(join_err).lower()
                        if "invite_hash_expired" in err_s or "expired" in err_s or "invalid" in err_s:
                            if status_msg:
                                await status_msg.edit_text("🔄 **Link expired. Generating a fresh one...**")
                            new_link_obj = await client.create_chat_invite_link(chat_id)
                            await user_app.join_chat(new_link_obj.invite_link)
                        else:
                            raise join_err

                    if status_msg:
                        await status_msg.edit_text("✅ **Assistant Joined.**")
                    await asyncio.sleep(2)

                except UserAlreadyParticipant:
                    if status_msg:
                        await status_msg.edit_text("✅ **Assistant Already in Chat.**")
                    await asyncio.sleep(1)

                except Exception as e:
                    if status_msg:
                        ast_mention = f"@{state.ASSISTANT_USERNAME}" if state.ASSISTANT_USERNAME else "the assistant"
                        verify_btn = InlineKeyboardMarkup([[
                            InlineKeyboardButton("✅ I have added the assistant", callback_data="verify_assistant")
                        ]])
                        await status_msg.edit_text(
                            f"❌ **Assistant Join Failed:**\n`{e}`\n\n"
                            f"Please add {ast_mention} manually and click below.",
                            reply_markup=verify_btn,
                        )
                    return

            state.assistant_cache[chat_id] = True
            try:
                await user_app.get_chat(chat_id)
            except Exception:
                pass

        file_path = song_info.get("file_path")
        if not file_path or not os.path.exists(file_path):
            if status_msg:
                await status_msg.edit_text("⬇️ **Downloading Audio...**")
            file_path = await download_song(song_info["url"])
            if not file_path or not os.path.exists(file_path):
                if status_msg:
                    await status_msg.edit_text("❌ **Download Failed.**")
                if chat_id in state.chat_queues and state.chat_queues[chat_id]:
                    state.chat_queues[chat_id].pop(0)
                    if state.chat_queues[chat_id]:
                        asyncio.create_task(
                            play_music_core(client, chat_id, state.chat_queues[chat_id][0], status_msg)
                        )
                return
            song_info["file_path"] = file_path

        if status_msg:
            await status_msg.edit_text("🎧 **Starting Playback...**")

        try:
            await call_py.play(chat_id, file_path)
        except Exception as e:
            err_s = str(e).lower()
            if any(k in err_s for k in ["peeridinvalid", "channelprivate", "invalid", "not in chat"]):
                if status_msg:
                    ast_mention = f"@{state.ASSISTANT_USERNAME}" if state.ASSISTANT_USERNAME else "the assistant"
                    verify_btn = InlineKeyboardMarkup([[
                        InlineKeyboardButton("✅ I have added the assistant", callback_data="verify_assistant")
                    ]])
                    await status_msg.edit_text(
                        f"❌ **VC unavailable or Assistant missing:**\n`{e}`\n\n"
                        f"Please start the VC, add {ast_mention} manually, and click below.",
                        reply_markup=verify_btn,
                    )
                state.assistant_cache.pop(chat_id, None)
                return
            if not retry_attempt:
                state.assistant_cache.pop(chat_id, None)
                if status_msg:
                    await status_msg.edit_text("🔄 **Connection Error. Refreshing...**")
                await asyncio.sleep(1.5)
                return await play_music_core(client, chat_id, song_info, status_msg, retry_attempt=True)
            raise e

        if chat_id in state.progress_tasks:
            state.progress_tasks[chat_id].cancel()
            del state.progress_tasks[chat_id]

        bot_name = client.me.first_name or "Music Bot"
        title_short = one_line_title(song_info["title"])
        total_duration = parse_duration_str(song_info.get("duration", "0"))

        base_caption = (
            "<blockquote>"
            f"<b>🎧 {bot_name} ✘ ᴍᴜsɪᴄ sᴛʀєᴀᴍɪɴɢ ⏤͟͞●</b></blockquote>\n\n"
            f"<blockquote>❍ <b>ᴛɪᴛʟᴇ:</b> {title_short}\n"
            f"❍ <b>ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:</b> {song_info['req']}</blockquote>"
        )

        control_buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton(text=get_progress_bar(0, total_duration), callback_data="progress")],
            [
                InlineKeyboardButton(text="▷", callback_data="resume"),
                InlineKeyboardButton(text="II", callback_data="pause"),
                InlineKeyboardButton(text="‣‣I", callback_data="skip"),
                InlineKeyboardButton(text="▢", callback_data="stop"),
            ],
        ])

        if status_msg:
            await status_msg.delete()

        player_message = None
        if song_info.get("thumb") and song_info["thumb"].startswith("http"):
            try:
                player_message = await client.send_photo(
                    chat_id,
                    photo=song_info["thumb"],
                    caption=base_caption,
                    reply_markup=control_buttons,
                    parse_mode=ParseMode.HTML,
                )
            except Exception:
                pass

        if not player_message:
            player_message = await client.send_message(
                chat_id,
                base_caption,
                reply_markup=control_buttons,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )

        if player_message:
            task = asyncio.create_task(
                update_progress_caption(chat_id, player_message, time.time(), total_duration, base_caption)
            )
            state.progress_tasks[chat_id] = task

    except Exception as e:
        logger.error(f"Playback error in chat {chat_id}: {e}")
        if status_msg:
            try:
                await status_msg.edit_text(f"❌ **Error:** {str(e)}")
            except Exception:
                pass
        if chat_id in state.chat_queues and state.chat_queues[chat_id]:
            state.chat_queues[chat_id].pop(0)


@call_py.on_update(fl.stream_end())
async def on_stream_end(_, update: StreamEnded):
    chat_id = update.chat_id

    if chat_id in state.progress_tasks:
        state.progress_tasks[chat_id].cancel()
        del state.progress_tasks[chat_id]

    if chat_id not in state.chat_queues or not state.chat_queues[chat_id]:
        try:
            await call_py.leave_call(chat_id)
        except Exception:
            pass
        return

    finished_song = state.chat_queues[chat_id].pop(0)
    fp = finished_song.get("file_path")
    if fp and os.path.exists(fp):
        try:
            os.remove(fp)
        except Exception:
            pass

    if state.chat_queues[chat_id]:
        next_song = state.chat_queues[chat_id][0]
        target_client = state.active_clients.get(next_song.get("bot_id"))
        if target_client:
            await play_music_core(target_client, chat_id, next_song)
        else:
            try:
                await call_py.leave_call(chat_id)
            except Exception:
                pass
    else:
        try:
            await call_py.leave_call(chat_id)
        except Exception:
            pass
