import discord
from discord.ext import commands

# Defining a Purge class,w ithin the class, passing client to make the discord module applicable here.

class purge(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    # Checking if the requested user has "manage_messages" privileges.
    @commands.has_permissions(manage_messages = True)
    # Defining the purge command with 1 extra argument being the amount of messages to be purged.
    async def purge(self, ctx, amount: int):
        # Checking if the user input is in  channel or DM, If in channel, purge continues. 
        # If in DM, Purge will not take place.
        if isinstance(ctx.channel, discord.channel.DMChannel):
            pass
        else:
            await ctx.channel.purge(limit = amount+1)

# Basic setup of a command. Necessary for loading the commands with the actual main.py file.
async def setup(client):
    await client.add_cog(purge(client))
