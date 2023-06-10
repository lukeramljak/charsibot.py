import discord
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('TOKEN')
guild_id = os.getenv('GUILD_ID')
owner_id = os.getenv('OWNER_ID')

client = discord.Bot(owner_id=owner_id, intents=discord.Intents.all())

client.remove_application_command('help')

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    print('----------')

cogs_list = [
    'fun'
    'utilities'
]

for cog in cogs_list:
    client.load_extension(f'cogs.{cog}')
        
client.run(token)