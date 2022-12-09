import discord
from discord.ext import commands
import datetime

# Defining an Evo class, within the class, passing client to make the discord module applicable here.
class time(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command()
    # Defining the command "time" as an embed with user's current movement points and target movement points as positional arguments.
    async def time(self, ctx, a: int, b: int, amount=1):
        # Finds net moves needed, converts to seconds and converts seconds to hours, minutes and seconds format.
        net_moves = b - a
        net_time = (net_moves * 24)
        conversion = datetime.timedelta(seconds=net_time)
        converted_time = str(conversion)

        # Defining the embed for move-time calc.
        time = discord.Embed(
            title='Movement-time Calculator',
            description='Calculates the time needed to attain the desired amount of moves.',
            color=discord.Color.dark_orange()
        )
        time.set_footer(text='Forsaken!')
        time.set_thumbnail(url='https://agonialands.com/assets/images/logos/Agonia_Mini_logo_alpha.png')
        time.set_author(name='Calc Bot')
        time.add_field(name='Current Moves', value=a, inline=True)
        time.add_field(name='Target Moves', value=b, inline=True)
        time.add_field(name='Net Moves', value=net_moves, inline=True)
        time.add_field(name='Net Time', value=converted_time, inline=True)
        # Sending the embed in the respective channel.
        await ctx.send(embed=time)

# Basic setup of a command. Necessary for loading the commands with the actual main.py file.
async def setup(client):
    await client.add_cog(time(client))