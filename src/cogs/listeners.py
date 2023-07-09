import discord
from discord.ext import commands


class Listeners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        content = message.content.lower()
        if "but" in content:
            await message.channel.send("butt")

        if "cow" in message.content:
            await message.channel.send("MOOOOO! <:ANGERY:1021275434823995475>")

        if "egg" in message.content:
            await message.channel.send("egg")

        if "dog" in message.content:
            await message.channel.send("what the dog doin'?")

        if "ass" in message.content:
            with open("assets/gifs/did-you.gif", "rb") as gif_file:
                gif = discord.File(gif_file)
                await message.channel.send(file=gif)


def setup(bot):
    bot.add_cog(Listeners(bot))
