import discord
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('TOKEN')
guild_id = os.getenv('GUILD_ID')

client = discord.Bot(intents=discord.Intents.all())
activity = discord.Activity(name='Big Chungus', type=discord.ActivityType.listening)

@client.event
async def on_ready():
    await client.change_presence(activity=activity)
    print(f'Logged in as {client.user.name}')

for foldername in os.listdir('src/cogs'): # for every folder in cogs
    for filename in os.listdir(f'src/cogs/{foldername}'): # for every file in a folder in cogs
        if filename.endswith('.py') and not filename in ['util.py', 'error.py']: # if the file is a python file and if the file is a cog
            client.load_extension(f'cogs.{foldername}.{filename[:-3]}') # load the extension
        
client.run(token)