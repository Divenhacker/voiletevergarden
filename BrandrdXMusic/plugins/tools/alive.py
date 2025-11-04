import asyncio

from BrandrdXMusic import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import MUSIC_BOT_NAME

@app.on_message(filters.command(["alive"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://graph.org/file/e999c40cb700e7c684b75.mp4",
        caption=f"**Oh, my dear, you seek my presence?**\n\n**I am {MUSIC_BOT_NAME}, an Auto Memory Doll, here solely to transcribe your deepest musical desires.**\n\n**I am swift, powerful, and ready to serve your lovely group with enchanting melodies.**\n\n**Should any profound question arise, please allow me the honor of assisting you in my place of work. I await your contact.**\n\n━━━━━━━━━━━━━━━━━━â™¡",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="â™¡ DADDY â™¡ ", url=f"https://t.me/crwke"
            ),
            InlineKeyboardButton(
                text="â™¡ MY HOME â™¡", url=f"https://t.me/infvibe"
            ),
        ],
                [
            InlineKeyboardButton(
                text="â™¡ WORK PLACE â™¡", url=f"https://t.me/voiletxsupport"
            ),
                ],
                [
                    InlineKeyboardButton(
                        "âœŒ Close Our Letter âœŒ", callback_data="close"
                    )
                ],
            ]
        )
    )
