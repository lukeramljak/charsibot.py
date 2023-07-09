import discord
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("TOKEN")
guild_id = os.getenv("GUILD_ID")

bot = discord.Bot(intents=discord.Intents.all())
activity = discord.Activity(name="Big Chungus", type=discord.ActivityType.listening)


@bot.event
async def on_ready():
    await bot.change_presence(activity=activity)
    print(f"Logged in as {bot.user}")


cogs_list = ["cogs.error", "cogs.fun", "cogs.listeners", "cogs.utilities"]

for cog in cogs_list:
    bot.load_extension(cog)

bot.run(token)
