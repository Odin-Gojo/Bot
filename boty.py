import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random

# Load environment variables from .env file
load_dotenv()

# Set up the bot token
TOKEN = os.getenv('BOT_TOKEN')

# Create a new bot instance
bot = commands.Bot(command_prefix='!')

# Set up the bot's presence
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Basic Gaming Bot'))

# Set up the bot's message event
@bot.event
async def on_message(msg):
    if msg.channel.id == int(os.getenv('TEST_CHANNEL')) and msg.content.lower() == "arrr you ready kids?!":
        replies = [
            'Aye Aye, Captain! ',
            'I can\'t hear youuuuu! ',
            'Who lives in a under the sea?'
        ]
        await msg.channel.send(random.choice(replies))

# Login to Discord
bot.run(TOKEN)
