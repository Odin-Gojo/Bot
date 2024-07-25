import discord
from discord.ext import commands
import os
import random
import gdown # type: ignore

url = 'https://drive.google.com/file/d/1AiaWEhdiad4p0zZwdiX4gmQlreCtOni1'
output = 'token.txt'
gdown.download(url, output, quiet=False)

with open('token.txt') as f:
    TOKEN = f.readline()

# Create a new bot instance
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="x", intents=intents)


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
