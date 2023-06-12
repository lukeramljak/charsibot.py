import discord
from discord.ext import commands
import os

guild_id = os.getenv('GUILD_ID')

# from pogrammar/Discord-multipurpose-bot

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[guild_id])
    async def poll(ctx,
                   question: str,
                   a: str,
                   b: str):
        embed = discord.Embed(title=question,
                              description=f"🅰️: {a}\n 🅱️: {b}")
        await ctx.respond(embed=embed)
        msg = await ctx.interaction.original_message()
        await msg.add_reaction('🅰️')
        await msg.add_reaction('🅱️')

def setup(bot):
    bot.add_cog(Poll(bot))