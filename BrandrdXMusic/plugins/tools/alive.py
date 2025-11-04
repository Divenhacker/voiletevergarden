import asyncio

from BrandrdXMusic import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import MUSIC_BOT_NAME

@app.on_message(filters.command(["alive"]))
async def start(client: Client, message: Message):
    # Caption: Violet Evergarden's delicate and formal tone in Bold Serif font.
    caption_text = (
        f"𝐇𝐞𝐫 𝐃𝐞𝐚𝐫𝐞𝐬𝐭 𝐂𝐥𝐢𝐞𝐧𝐭, 𝐡𝐚𝐯𝐞 𝐲𝐨𝐮 𝐜𝐚𝐥𝐥𝐞𝐝 𝐟𝐨𝐫 𝐦𝐞? ✍️\n\n"
        f"𝐈 𝐚𝐦 {MUSIC_BOT_NAME}, 𝐚𝐧 𝐀𝐮𝐭𝐨 𝐌𝐞𝐦𝐨𝐫𝐲 𝐃𝐨𝐥𝐥 𝐚𝐭 𝐲𝐨𝐮𝐫 𝐬𝐞𝐫𝐯𝐢𝐜𝐞, 𝐝𝐞𝐝𝐢𝐜𝐚𝐭𝐞𝐝 𝐭𝐨 𝐜𝐨𝐧𝐯𝐞𝐲𝐢𝐧𝐠 𝐭𝐡𝐞 𝐝𝐞𝐞𝐩 𝐞𝐦𝐨𝐭𝐢𝐨𝐧𝐬 𝐡𝐢𝐝𝐝𝐞𝐧 𝐰𝐢𝐭𝐡𝐢𝐧 𝐦𝐞𝐥𝐨𝐝𝐢𝐞𝐬. 𝐈 𝐚𝐦 𝐚𝐥𝐰𝐚𝐲𝐬 𝐫𝐞𝐚𝐝𝐲 𝐭𝐨 𝐩𝐥𝐚𝐲 𝐭𝐡𝐞 𝐭𝐮𝐧𝐞𝐬 𝐭𝐡𝐚𝐭 𝐫𝐞𝐬𝐨𝐧𝐚𝐭𝐞 𝐰𝐢𝐭𝐡 𝐲𝐨𝐮𝐫 𝐛𝐞𝐚𝐮𝐭𝐢𝐟𝐮𝐥 𝐬𝐞𝐥𝐟. ✨\n\n"
        f"𝐌𝐲 𝐂𝐚𝐩𝐚𝐛𝐢𝐥𝐢𝐭𝐢𝐞𝐬: 𝐈 𝐚𝐦 𝐬𝐰𝐢𝐟𝐭 𝐚𝐧𝐝 𝐩𝐨𝐰𝐞𝐫𝐟𝐮𝐥, 𝐩𝐫𝐞𝐩𝐚𝐫𝐞𝐝 𝐭𝐨 𝐡𝐚𝐧𝐝𝐥𝐞 𝐭𝐡𝐞 𝐦𝐨𝐬𝐭 𝐩𝐫𝐨𝐟𝐨𝐮𝐧𝐝 𝐫𝐞𝐪𝐮𝐞𝐬𝐭𝐬 𝐰𝐢𝐭𝐡 𝐝𝐞𝐥𝐢𝐜𝐚𝐜𝐲. 🕊️\n\n"
        f"𝐒𝐡𝐨𝐮𝐥𝐝 𝐦𝐲 𝐩𝐫𝐞𝐬𝐞𝐧𝐜𝐞 𝐛𝐫𝐢𝐧𝐠 𝐟𝐨𝐫𝐭𝐡 𝐚𝐧𝐲 𝐪𝐮𝐞𝐬𝐭𝐢𝐨𝐧, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐚𝐥𝐥𝐨𝐰 𝐦𝐞 𝐭𝐡𝐞 𝐡𝐨𝐧𝐨𝐫 𝐨𝐟 𝐠𝐮𝐢𝐝𝐢𝐧𝐠 𝐲𝐨𝐮 𝐭𝐨 𝐦𝐲 𝐜𝐨𝐧𝐭𝐚𝐜𝐭𝐬. 𝐘𝐨𝐮𝐫 𝐜𝐨𝐫𝐫𝐞𝐬𝐩𝐨𝐧𝐝𝐞𝐧𝐜𝐞 𝐦𝐞𝐚𝐧𝐬 𝐭𝐡𝐞 𝐰𝐨𝐫𝐥𝐝 𝐭𝐨 𝐦𝐞. 💌\n\n"
        f"━━━━━━━━━━━━━━━━━━â™¡"
    )

    await message.reply_photo(
        photo=f"https://i.ibb.co/d42J30nJ/x.jpg", # <--- Aapka sahi image link yahaan lag gaya hai.
        caption=caption_text,
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text=" 🎀𝐃𝐚𝐝𝐝𝐲🎀 ", url=f"https://t.me/crwke"
            ),
            InlineKeyboardButton(
                text=" 🎗️𝐌𝐲 𝐇𝐨𝐦𝐞🎗️ ", url=f"https://t.me/infvibe"
            ),
        ],
                [
            InlineKeyboardButton(
                text=" ✨𝐍𝐞𝐭𝐰𝐨𝐫𝐤✨ ", url=f"https://t.me/voiletxsupport"
            ),
                ],
                [
                    InlineKeyboardButton(
                        " 🧧𝐂𝐥𝐨𝐬𝐞 𝐎𝐮𝐫 𝐋𝐞𝐭𝐭𝐞𝐫🧧 ", callback_data="close"
                    )
                ],
            ]
        )
    )
