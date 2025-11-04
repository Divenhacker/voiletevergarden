import os
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from BrandrdXMusic import app

LOGGER = getLogger(__name__)

# --- [ Database Classes Remain Unchanged ] ---
class WelDatabase:
    def __init__(self):
        self.data = {}

    async def find_one(self, chat_id):
        return chat_id in self.data

    async def add_wlcm(self, chat_id):
        self.data[chat_id] = {}

    async def rm_wlcm(self, chat_id):
        if chat_id in self.data:
            del self.data[chat_id]

wlcm = WelDatabase()

class temp:
    ME = None
    CURRENT = 2
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None

def circle(pfp, size=(500, 500)):
    pfp = pfp.resize(size, Image.LANCZOS).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.LANCZOS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def welcomepic(pic, user, chatname, id, uname):
    background = Image.open("BrandrdXMusic/assets/Brandedwel2.png")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp)
    pfp = pfp.resize((825, 824))
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('BrandrdXMusic/assets/font.ttf', size=110)
    welcome_font = ImageFont.truetype('BrandrdXMusic/assets/font.ttf', size=60)
    draw.text((2100, 1420), f'ID: {id}', fill=(12000, 12000, 12000), font=font)
    pfp_position = (1990, 435)
    background.paste(pfp, pfp_position, pfp)
    background.save(f"downloads/welcome#{id}.png")
    return f"downloads/welcome#{id}.png"
# --- [ Helper Functions Remain Unchanged ] ---

@app.on_chat_member_updated(filters.group, group=-3)
async def greet_group(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    A = await wlcm.find_one(chat_id)
    if (
        not member.new_chat_member
        or member.new_chat_member.status in {"banned", "left", "restricted"}
        or member.old_chat_member
    ):
        return
    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    try:
        pic = await app.download_media(
            user.photo.big_file_id, file_name=f"pp{user.id}.png"
        )
    except AttributeError:
        pic = "BrandrdXMusic/assets/Brandedwel2.png"
    if (temp.MELCOW).get(f"welcome-{member.chat.id}") is not None:
        try:
            await temp.MELCOW[f"welcome-{member.chat.id}"].delete()
        except Exception as e:
            LOGGER.error(e)
    try:
        welcomeimg = welcomepic(
            pic, user.first_name, member.chat.title, user.id, user.username
        )
        temp.MELCOW[f"welcome-{member.chat.id}"] = await app.send_photo(
            member.chat.id,
            photo=welcomeimg,
            caption=f"""
**𝐖𝐞𝐥𝐜𝐨𝐦𝐞, 𝐃𝐞𝐚𝐫 𝐂𝐥𝐢𝐞𝐧𝐭! 🌹**
**𝐘𝐨𝐮 𝐡𝐚𝐯𝐞 𝐣𝐨𝐢𝐧𝐞𝐝 𝐭𝐡𝐞 𝐜𝐨𝐫𝐫𝐞𝐬𝐩𝐨𝐧𝐝𝐞𝐧𝐜𝐞 𝐨𝐟 {member.chat.title}**
━━━━━━━━━━━━━━━
💌 𝐍𝐀𝐌𝐄: {user.mention}
✨ 𝐈𝐃: `{user.id}`
🌐 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄: @{user.username}
━━━━━━━━━━━━━━━
**𝐈 𝐚𝐦 𝐲𝐨𝐮𝐫 𝐀𝐮𝐭𝐨 𝐌𝐞𝐦𝐨𝐫𝐲 𝐃𝐨𝐥𝐥, 𝐫𝐞𝐚𝐝𝐲 𝐭𝐨 𝐬𝐞𝐫𝐯𝐞.**
**𝐌𝐚𝐝𝐞 𝐁𝐲:** [𝐃𝐀𝐃𝐃𝐘 🤤](https://t.me/crwke)
""",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"🌸 𝐀𝐝𝐝 𝐌𝐞 𝐭𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 🌸", url=f"https://t.me/lnfixbot?startgroup=true")]])
        )
    except Exception as e:
        LOGGER.error(e)
    try:
        os.remove(f"downloads/welcome#{user.id}.png")
        os.remove(f"downloads/pp{user.id}.png")
    except Exception as e:
        pass

# --- [ Bot Welcome Message (Unchanged) ] ---
@app.on_message(filters.new_chat_members & filters.group, group=-1)
async def bot_wel(_, message):
    for u in message.new_chat_members:
        if u.id == app.me.id:
            # Note: LOG_CHANNEL_ID must be defined elsewhere for this to work
            # For simplicity, keeping the original log format here
            # LOG_CHANNEL_ID is not defined in the provided snippet, so this part might error if used directly
            # I am keeping the original log message style as it's not part of the user-facing welcome
            try:
                await app.send_message(LOG_CHANNEL_ID, f"""
𝐍𝐄𝐖 𝐆𝐑𝐎𝐔𝐏
➖➖➖➖➖➖➖➖➖➖➖
𝐍𝐀𝐌𝐄: {message.chat.title}
𝐈𝐃: {message.chat.id}
𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄: @{message.chat.username}
➖➖➖➖➖➖➖➖➖➖➖
""")
            except NameError:
                # Fallback if LOG_CHANNEL_ID is not defined
                LOGGER.error("LOG_CHANNEL_ID is not defined for bot_wel function.")
    
