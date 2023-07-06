import discord
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("TOKEN")
guild_id = os.getenv("GUILD_ID")

bot = discord.Bot(intents=discord.Intents.default())
activity = discord.Activity(name="Big Chungus", type=discord.ActivityType.listening)


@bot.event
async def on_ready():
    await bot.change_presence(activity=activity)
    print(f"Logged in as {bot.user}")


for folder in os.listdir("./cogs"):
    for file in os.listdir(f"./cogs/{folder}"):
        if file.endswith(".py"):
            bot.load_extension(f"cogs.{folder}.{file[:-3]}")

bot.run(token)
