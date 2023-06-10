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

cogs_list = [
    'fun',
    'utilities'
]

for cog in cogs_list:
    client.load_extension(f'cogs.{cog}')
        
client.run(token)