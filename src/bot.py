import discord
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('TOKEN')
guild_id = os.getenv('GUILD_ID')

client = discord.Bot(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    print('----------')
    
client.load_extension('cogs.fun')
        
client.run(token)