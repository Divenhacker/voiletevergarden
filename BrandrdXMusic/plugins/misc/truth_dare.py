from pyrogram import Client, filters
import requests
import random
from BrandrdXMusic import app

# Truth or Dare API URLs
truth_api_url = "https://api.truthordarebot.xyz/v1/truth"
dare_api_url = "https://api.truthordarebot.xyz/v1/dare"


@app.on_message(filters.command("truth"))
def get_truth(client, message):
    try:
        # Make a GET request to the Truth API
        response = requests.get(truth_api_url)
        if response.status_code == 200:
            truth_question = response.json()["question"]
            # Flirty Response for Truth
            message.reply_text(f"**Ah, so you choose the truth!** Tell me your secrets... 😉\n\n**T-R-U-T-H:** {truth_question}")
        else:
            message.reply_text("My magic mirror is cloudy right now! Couldn't fetch a truth question. Try again, sweetie.")
    except Exception as e:
        message.reply_text("Oops! A little spark of trouble happened while fetching the truth. Let's try that again later, okay?")

@app.on_message(filters.command("dare"))
def get_dare(client, message):
    try:
        # Make a GET request to the Dare API
        response = requests.get(dare_api_url)
        if response.status_code == 200:
            dare_question = response.json()["question"]
            # Flirty Response for Dare
            message.reply_text(f"**A dare, huh? I love a rebel!** Let's see how brave you are... 😏\n\n**D-A-R-E:** {dare_question}")
        else:
            message.reply_text("The mischief maker is busy! Couldn't find a good dare. Give me a minute and try again.")
    except Exception as e:
        message.reply_text("An unexpected glitch occurred while I was thinking up a dare for you. Come back later for your punishment! 😉")
        
