import discord
from discord.ext import commands
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
async def on_application_command_error(
    ctx: discord.ApplicationContext, error: discord.DiscordException
):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.respond("This command is currently on cooldown!")
    else:
        raise error


for cog in ("fun", "listeners", "utilities"):
    bot.load_extension(f"cogs.{cog}")

bot.run(token)
