import os 
import random
from datetime import datetime 
from telegraph import upload_file
from PIL import Image , ImageDraw
from pyrogram import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import *

#BOT FILE NAME
from BrandrdXMusic import app as app
# from BrandrdXMusic.mongo.couples_db import _get_image, get_couple, save_couple # Commented out as in original

# Violet Evergarden Themed Button
POLICE = [
    [
        InlineKeyboardButton(
            text="🤤 My Daddy 🤤", # Changed as requested
            url=f"https://t.me/crwke", # Changed as requested
        ),
    ],
]


def dt():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    dt_list = dt_string.split(" ")
    return dt_list
    

def dt_tom():
    # This logic assumes the next day is simply +1
    a = (
        str(int(dt()[0].split("/")[0]) + 1)
        + "/"
        + dt()[0].split("/")[1]
        + "/"
        + dt()[0].split("/")[2]
    )
    return a

tomorrow = str(dt_tom())
today = str(dt()[0])

@app.on_message(filters.command("couples"))
async def ctest(_, message):
    cid = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        # Violet Evergarden Message
        return await message.reply_text("My apologies, dear one. This command is exclusively for group correspondence.") 
    try:
     #  is_selected = await get_couple(cid, today)
     #  if not is_selected:
         # Violet Evergarden Message
         msg = await message.reply_text("Diligently preparing a lovely portrait for today's chosen pair...") 
         
         #GET LIST OF USERS
         list_of_users = []

         async for i in app.get_chat_members(message.chat.id, limit=50):
             if not i.user.is_bot:
               list_of_users.append(i.user.id)

         c1_id = random.choice(list_of_users)
         c2_id = random.choice(list_of_users)
         while c1_id == c2_id:
              c1_id = random.choice(list_of_users)


         photo1 = (await app.get_chat(c1_id)).photo
         photo2 = (await app.get_chat(c2_id)).photo
 
         N1 = (await app.get_users(c1_id)).mention 
         N2 = (await app.get_users(c2_id)).mention
         
         try:
            # Saving to a temporary location
            p1 = await app.download_media(photo1.big_file_id, file_name=f"downloads/{c1_id}_pfp.png")
         except Exception:
            p1 = "BrandrdXMusic/assets/upic.png"
         try:
            # Saving to a temporary location
            p2 = await app.download_media(photo2.big_file_id, file_name=f"downloads/{c2_id}_pfp1.png")
         except Exception:
            p2 = "BrandrdXMusic/assets/upic.png"
            
         img1 = Image.open(f"{p1}")
         img2 = Image.open(f"{p2}")

         img = Image.open("BrandrdXMusic/assets/cppicbranded.jpg")

         img1 = img1.resize((437,437))
         img2 = img2.resize((437,437))

         mask = Image.new('L', img1.size, 0)
         draw = ImageDraw.Draw(mask) 
         draw.ellipse((0, 0) + img1.size, fill=255)

         mask1 = Image.new('L', img2.size, 0)
         draw = ImageDraw.Draw(mask1) 
         draw.ellipse((0, 0) + img2.size, fill=255)


         img1.putalpha(mask)
         img2.putalpha(mask1)

         draw = ImageDraw.Draw(img)

         img.paste(img1, (116, 160), img1)
         img.paste(img2, (789, 160), img2)

         img.save(f'test_{cid}.png')
    
         # Violet Evergarden Message
         TXT = f"""
**💌 Today's Harmonious Correspondence 💌**

**{N1} and {N2} have been delicately paired for this lovely day. You are truly meant to compose beautiful music together!**

**I shall diligently select the next cherished couple on {tomorrow}. Until then, may your hearts be filled with warmth.**
"""
    
         await message.reply_photo(f"test_{cid}.png", caption=TXT, reply_markup=InlineKeyboardMarkup(POLICE),
    )
         await msg.delete()
         a = upload_file(f"test_{cid}.png")
         for x in a:
           img_url = "https://graph.org/" + x
           couple = {"c1_id": c1_id, "c2_id": c2_id}
          # await save_couple(cid, today, couple, img_url)
    
         
      # elif is_selected:
      #   ... (Rest of the commented code for already selected couple)
        
    except Exception as e:
        print(f"An error occurred during couple selection: {e}")
    try:
      # Clean up temporary files
      os.remove(p1)
      os.remove(p2)
      os.remove(f"test_{cid}.png")
    except Exception:
       pass
         

__mod__ = "COUPLES"
__help__ = """
**» /couples** - To request the lovely portrait of Today's Harmonious Couple.
"""
