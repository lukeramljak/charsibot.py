import discord
from discord.ext import commands
from discord.commands import slash_command
import os

guild_id = os.getenv("GUILD_ID")
owner_id = os.getenv("OWNER_ID")


class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Clear some messages", guild_ids=[guild_id])
    @discord.default_permissions(administrator=True)
    async def clear(self, ctx, amount: int):
        if not 1 <= amount <= 100:
            return await ctx.respond(
                "Please provide a valid number of messages to clear (1-100).",
                ephemeral=True,
            )

        try:
            messages = await ctx.channel.purge(limit=amount)
            message_count = len(messages)
            response = (
                f'{message_count} {"message" if message_count == 1 else "messages"}'
            )
            await ctx.respond(f"Successfully cleared {response}.", ephemeral=True)
        except Exception as e:
            print(e)
            await ctx.respond(
                "An error occurred while trying to clear messages.", ephemeral=True
            )

    @slash_command(description="Check charsibot's ping", guild_ids=[guild_id])
    async def ping(self, ctx):
        await ctx.respond(f"Pong! charsibot latency: {int(ctx.bot.latency * 1000)}ms.")


def setup(bot):
    bot.add_cog(Utilities(bot))
