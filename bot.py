import discord
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Bot()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    print('----------')
        
client.run(token)