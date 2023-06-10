import discord
from discord.ext import commands
import os

guild_id = os.getenv('GUILD_ID')

class Fun(commands.Cog):
    
    def __init__(self, client):
        self.bot = client
        
    @discord.slash_command(description='Bonk someone!')
    async def bonk(
        self,
        ctx,
        name: discord.Option(discord.SlashCommandOptionType.user, 'Who\'s getting bonked?', required = True)
    ):
        await ctx.respond(f'{ctx.author.name} has bonked {name.mention}. Oh my...')
    
    @discord.slash_command(guild_ids=[guild_id])
    async def ping(self, ctx):
        await ctx.respond('Pong!')
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        if 'but' in message.content.lower():
            await message.reply('butt')
            
        if 'cow' in message.content.lower():
            await message.reply('MOOOOO! <:ANGERY:1021275434823995475>')
            
        if 'egg' in message.content.lower():
            await message.reply('egg')
        
        if 'dog' in message.content.lower():
            await message.reply('what the dog doin\'?')

def setup(client):
    client.add_cog(Fun(client))