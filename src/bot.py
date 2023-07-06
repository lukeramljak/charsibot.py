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


@bot.event
async def on_member_join(member: discord.Member):
    guild = member.guild
    if guild.system_channel is not None:
        await guild.system_channel.send(f"{member.mention} has become a charsipal!")


for folder in os.listdir("./cogs"):
    for file in os.listdir(f"./cogs/{folder}"):
        if file.endswith(".py"):
            bot.load_extension(f"cogs.{folder}.{file[:-3]}")

bot.run(token)
