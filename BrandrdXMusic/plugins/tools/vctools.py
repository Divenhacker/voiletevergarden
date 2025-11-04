from pyrogram import Client, filters
from pyrogram.types import Message
from BrandrdXMusic import app
from pyrogram import *
from pyrogram.types import *
from config import OWNER_ID
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall
from BrandrdXMusic.utils.database import get_assistant
from telethon.tl.functions.phone import (
    CreateGroupCallRequest,
    DiscardGroupCallRequest,
    GetGroupCallRequest,
    InviteToGroupCallRequest,
)

# Missing imports for the search function:
import aiohttp
import re

# vc on
@app.on_message(filters.video_chat_started)
async def brah(_, msg):
    # Easy Language Style
    await msg.reply("**💖 So lovely! The call has started! 🎶**")


# vc off
@app.on_message(filters.video_chat_ended)
async def brah2(_, msg):
    # Easy Language Style
    await msg.reply("**💔 The call has ended. I miss your voice already! 🕰️**")


# invite members on vc
@app.on_message(filters.video_chat_members_invited)
async def brah3(app: app, message: Message):
    # Easy Language Style Text
    text = f"✍️ **{message.from_user.mention} has invited others to the call!**\n\n**Joining the conversation:**\n\n**🌸 **"
    x = 0
    for user in message.video_chat_members_invited.users:
        try:
            text += f"[{user.first_name}](tg://user?id={user.id}) "
            x += 1
        except Exception:
            pass

    try:
        invite_link = await app.export_chat_invite_link(message.chat.id)
        add_link = f"https://t.me/{app.username}?startgroup=true"
        # Easy Language Style Reply Text
        reply_text = f"{text} **Please come and chat with us! 🥂**"

        await message.reply(
            reply_text,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="💌 Join Our Chat 💌", url=add_link)], # Easy Language Button
                ]
            ),
        )
    except Exception as e:
        print(f"Error: {e}")


####


@app.on_message(filters.command("math", prefixes="/"))
def calculate_math(client, message):
    # Simple check for input
    if len(message.text.split("/math ", 1)) < 2:
        return message.reply("Please give me something to calculate! Example: /math 5*9")
    
    expression = message.text.split("/math ", 1)[1]
    try:
        # Evaluate the math expression
        result = eval(expression)
        # Easy Language Style Success Message
        response = f"🧮 **My calculation shows the answer is: {result}**"
    except:
        # Easy Language Style Error Message
        response = "😢 **Oops! I can't solve that math problem. Please check your numbers!**"
    message.reply(response)


@app.on_message(filters.command(["spg"], ["/", "!", "."]))
async def search(event):
    # Easy Language Style Initial Message
    if len(event.text.split()) < 2:
        return await event.respond("Please tell me what to search for! Example: /spg Violet Evergarden")
        
    msg = await event.respond("🔎 **I am searching for your request now...**")
    
    # ... (Rest of the search logic remains the same for functionality)
    
    async with aiohttp.ClientSession() as session:
        start = 1
        async with session.get(
            f"https://content-customsearch.googleapis.com/customsearch/v1?cx=ec8db9e1f9e41e65e&q={event.text.split()[1]}&key=AIzaSyAa8yy0GdcGPHdtD083HiGGx_S0vMPScDM&start={start}",
            headers={"x-referer": "https://explorer.apis.google.com"},
        ) as r:
            response = await r.json()
            result = ""

            if not response.get("items"):
                # Easy Language Style No Results Message
                return await msg.edit("**Sorry, I found nothing related to your search! 😔**")
            
            for item in response["items"]:
                title = item["title"]
                link = item["link"]
                if "/s" in item["link"]:
                    link = item["link"].replace("/s", "")
                elif re.search(r"\/\d", item["link"]):
                    link = re.sub(r"\/\d", "", item["link"])
                if "?" in link:
                    link = link.split("?")[0]
                if link in result:
                    # remove duplicates
                    continue
                result += f"{title}\n{link}\n\n"
            
            # Easy Language Style Button
            prev_and_next_btns = [
                InlineKeyboardButton("Next Page ❯", callback_data=f"next {start+10} {event.text.split()[1]}")
            ]
            
            await msg.edit(result, link_preview=False, reply_markup=InlineKeyboardMarkup(prev_and_next_btns))
            await session.close()


__mod__ = "COUPLES"
__help__ = """
**» /couples** - Find today's cutest couple in the group! 💖
"""
