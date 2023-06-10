import discord
from discord.ext import commands
import os
import random
import requests

guild_id = os.getenv('GUILD_ID')

class Fun(commands.Cog):
        
    def __init__(self, client):
        self.bot = client
        
    @commands.slash_command(
        description='Ask the magic 8-ball a question',
        guild_ids=[guild_id]
    )
    async def magic8ball(
        self,
        ctx,
        question: discord.Option(
            description = 'Ask a question',
            required = True
        )
    ):
        responses = [
            'It is certain.',
            'It is decidedly so.',
            'Without a doubt.',
            'Yes, definitely.',
            'You may rely on it.',
            'As I see it, yes.',
            'Most likely.',
            'Outlook good.',
            'Yes.',
            'Signs point to yes.',
            'Reply hazy, try again.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            'Don\'t count on it.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Very doubtful.',
            'No way.',
			'Maybe',
			'The answer is hiding inside you',
			'No.',
			'||No||',
			'||Yes||',
			'Hang on',
			'It\'s over',
			'It\'s just the beginning',
			'Good luck',
        ]
        
        response = random.choice(responses)
        await ctx.respond(f"{question}\n\n 🎱 {response}")
            
    @discord.slash_command(
        description = 'Bonk someone!',
        guild_ids = [guild_id]
    )
    async def bonk(
        self,
        ctx,
        name: discord.Option(
            discord.SlashCommandOptionType.user, 'Bonk someone!',
            required = True
        )
    ):
        await ctx.respond(f'{ctx.author.name} has bonked {name.mention}. Oh my...')
        
    @discord.slash_command(
        description = 'Brain not working?',
        guild_ids = [guild_id]
    )
    async def brain(
        self,
        ctx,
        name: discord.Option(
            discord.SlashCommandOptionType.user, 'Brain not working?',
            required = True
        )
    ):
        await ctx.respond(f'Oh dear, it looks like {name.mention}\'s brain has stopped working... Please wait a moment while it restarts. <:rip:1057489640636035102>')
        
    @discord.slash_command(
        description = 'Tuck someone into bed',
        guild_ids = [guild_id]
    )
    async def burrito(
        self,
        ctx,
        name: discord.Option(
            discord.SlashCommandOptionType.user, 'Tuck someone into bed',
            required = True
        )
    ):
        await ctx.respond(f'{ctx.author.name} has tucked {name.mention} into a burrito blanket. awwwww goodnight {name.name} <:BurritoBlanket:1021275794678497291>')
        
            
    @discord.slash_command(
        description = 'Get a random dad joke',
        guild_ids = [guild_id]
    )
    async def dadjoke(
        self,
        ctx
    ):
        response = requests.get('https://icanhazdadjoke.com', headers = {'Accept': 'application/json'})
        joke_data = response.json()
        joke = joke_data['joke']
        await ctx.respond(joke)
        
    @discord.slash_command(
        description = 'Hug another user',
        guild_ids = [guild_id]
    )
    async def hug(
        self,
        ctx,
        name: discord.Option(
            discord.SlashCommandOptionType.user, 'Hug another user',
            required = True
        )
    ):
        await ctx.respond(f'_hugs {name.mention}_')
        
    @discord.slash_command(
        description = 'Having a bad day? Get a random positive quote',
        guild_ids = [guild_id]
    )
    async def quote(
        self,
        ctx
    ):
        response = requests.get('https://zenquotes.io/api/random')
        quote_data = response.json()
        quote = quote_data[0]['q']
        await ctx.respond(quote)
        
    @discord.slash_command(
        description = 'Give someone a nice big smooch',
        guild_ids = [guild_id]
    )
    async def smooch(
        self,
        ctx,
        name: discord.Option(
            discord.SlashCommandOptionType.user, 'Give someone a nice big smooch',
            required = True
        )
    ):
        await ctx.respond(f'{ctx.author.name} has given {name.mention} a big smooch. MWAHHH! <:Witch:1021275389508734987>')
        
    @discord.slash_command(
        description = 'Toss a tomato!',
        guild_ids = [guild_id]
    )
    async def tomato(
        self,
        ctx,
        name: discord.Option(
            discord.SlashCommandOptionType.user, 'Pick your target!',
            required = True
        )
    ):
        await ctx.respond(f'{ctx.author.name} threw a tomato at {name.mention}. tomato tomato tomato! <:rip:1057489640636035102>')
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        content = message.content.lower()
        if 'but' in content:
            await message.channel.send('butt')
            
        if 'cow' in message.content:
            await message.channel.send('MOOOOO! <:ANGERY:1021275434823995475>')
            
        if 'egg' in message.content:
            await message.channel.send('egg')
        
        if 'dog' in message.content:
            await message.channel.send('what the dog doin\'?')

def setup(client):
    client.add_cog(Fun(client))