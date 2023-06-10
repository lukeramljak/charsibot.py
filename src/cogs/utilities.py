import discord
from discord.ext import commands
import os

guild_id = os.getenv('GUILD_ID')

class Utilities(commands.Cog):
    
    def __init__(self, client):
        self.bot = client
        
    async def is_owner(ctx):
        return ctx.author.id == 729571283645366293
        
    @discord.slash_command(
        name = 'clear',
        description = 'Clear a specified number of messages',
        guild_ids = [guild_id],
    )
    @commands.check(is_owner)
    async def clear(self, ctx, amount: int):            
        if not 1 <= amount <= 100:
            return await ctx.respond('Please provide a valid number of messages to clear (1-100).', ephemeral = True)
        
        try:
            messages = await ctx.channel.purge(limit = amount)
            message_count = len(messages)
            response = f'{message_count} {"message" if message_count == 1 else "messages"}'
            await ctx.respond(f'Successfully cleared {response}.', ephemeral = True)
        except Exception as e:
            print(e)
            await ctx.respond('An error occurred while trying to clear messages.', ephemeral=True)
    
def setup(client):
    client.add_cog(Utilities(client))