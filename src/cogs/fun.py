import discord
from discord.ext import commands
import os

guild_id = os.getenv('GUILD_ID')

class Fun(commands.Cog):
    
    def __init__(self, client):
        self.bot = client
        
    @discord.slash_command(
        description='Bonk someone!',
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
        description='Brain not working?',
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
        description='Tuck someone into bed.',
        guild_ids = [guild_id]
    )
    async def burrito(
        self,
        ctx,
        name: discord.Option(
            discord.SlashCommandOptionType.user, 'Tuck someone into bed.',
            required = True
        )
    ):
        await ctx.respond(f'{ctx.author.name} has tucked {name.mention} into a burrito blanket. awwwww goodnight {name.name} <:BurritoBlanket:1021275794678497291>')
        
    @discord.slash_command(
        description='Hug another user.',
        guild_ids = [guild_id]
    )
    async def hug(
        self,
        ctx,
        name: discord.Option(
            discord.SlashCommandOptionType.user, 'Hug another user.',
            required = True
        )
    ):
        await ctx.respond(f'_hugs {name.mention}_')
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        if 'but' in message.content.lower():
            await message.channel.send('butt')
            
        if 'cow' in message.content.lower():
            await message.channel.send('MOOOOO! <:ANGERY:1021275434823995475>')
            
        if 'egg' in message.content.lower():
            await message.channel.send('egg')
        
        if 'dog' in message.content.lower():
            await message.channel.send('what the dog doin\'?')

def setup(client):
    client.add_cog(Fun(client))