import discord
from discord.commands import slash_command
from discord.ext import commands
import random
import requests
from bot import guild_id


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Ask the magic 8-ball a question", guild_id=[guild_id])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def magic8ball(self, ctx, question: str):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes, definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful.",
            "No way.",
            "Maybe",
            "The answer is hiding inside you",
            "No.",
            "||No||",
            "||Yes||",
            "Hang on",
            "It's over",
            "It's just the beginning",
            "Good luck",
        ]
        response = random.choice(responses)
        await ctx.respond(f"{question}\n\n 🎱 {response}")

    @slash_command(description="Bonk someone!", guild_id=[guild_id])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def bonk(self, ctx, name: discord.Member):
        await ctx.respond(f"{ctx.author.mention} has bonked {name.mention}. Oh my...")

    @slash_command(description="Brain not working?", guild_id=[guild_id])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def brain(self, ctx, name: discord.Member):
        await ctx.respond(
            f"Oh dear, it looks like {name.mention}'s brain has stopped working... "
            "Please wait a moment while it restarts. <:rip:1057489640636035102>"
        )

    @slash_command(description="Tuck someone into bed", guild_id=[guild_id])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def burrito(self, ctx, name: discord.Member):
        await ctx.respond(
            f"{ctx.author.mention} has tucked {name.mention} into a burrito blanket. "
            f"awwwww goodnight {name.mention} <:BurritoBlanket:1021275794678497291>"
        )

    @slash_command(description="Flip a coin", guild_id=[guild_id])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def coinflip(self, ctx):
        result = ["heads", "tails"]
        await ctx.respond(f"The coin landed on {random.choice(result)}.")

    @slash_command(description="Get a random dad joke", guild_id=[guild_id])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def dadjoke(self, ctx):
        response = requests.get(
            "https://icanhazdadjoke.com", headers={"Accept": "application/json"}
        )
        joke_data = response.json()
        joke = joke_data["joke"]
        await ctx.respond(joke)

    @slash_command(description="Hug another user", guild_id=[guild_id])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def hug(self, ctx, name: discord.Member):
        await ctx.respond(f"_hugs {name.mention}_")

    @slash_command(
        description="Having a bad day? Get a random positive quote",
        guild_id=[guild_id],
    )
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def quote(self, ctx):
        response = requests.get("https://zenquotes.io/api/random")
        quote_data = response.json()
        quote = quote_data[0]["q"]
        await ctx.respond(quote)

    @slash_command(description="Give someone a nice big smooch", guild_id=[guild_id])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def smooch(self, ctx, name: discord.Member):
        await ctx.respond(
            f"{ctx.author.mention} has given {name.mention} a big smooch. "
            "MWAHHH! <:Witch:1021275389508734987>"
        )

    @slash_command(description="Toss a tomato!", guild_id=[guild_id])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def tomato(self, ctx, name: discord.Member):
        await ctx.respond(
            f"{ctx.author.mention} threw a tomato at {name.mention}. "
            "tomato tomato tomato! <:rip:1057489640636035102>"
        )


def setup(bot):
    bot.add_cog(Fun(bot))
