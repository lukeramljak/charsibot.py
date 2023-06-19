import discord
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('TOKEN')
guild_id = os.getenv('GUILD_ID')

bot = discord.Bot(intents=discord.Intents.all())
activity = discord.Activity(name='Big Chungus', type=discord.ActivityType.listening)

@bot.event
async def on_ready():
    await bot.change_presence(activity=activity)
    print(f'Logged in as {bot.user.name}')

for foldername in os.listdir('./cogs'): # for every folder in cogs
    for filename in os.listdir(f'./cogs/{foldername}'): # for every file in a folder in cogs
        if filename.endswith('.py'): # if the file is a python file and if the file is a cog
            bot.load_extension(f'cogs.{foldername}.{filename[:-3]}') # load the extension
        
bot.run(token)