import discord
from discord.ext import commands

# Defining a Help class, within the class, passing client to make the discord module applicable here.

class help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    # Defining the command "help" as an embed, the embed will be sent to the user.
    async def help(self, ctx):
        # Defining a command user, this gets the user's account.
        command_user = ctx.message.author
        # Checking whether the message is sent from a channel or a DM, If sent from a DM, command goes smoothly
        # If input is sent from channel, command purges the input by user.
        if isinstance(ctx.channel, discord.channel.DMChannel):
            pass
        else:
            await ctx.channel.purge(limit = 1)
       
        # Defining the help embed. 
        help = discord.Embed(
            title='HELP',
            description='Help Commands',
            color=discord.Color.blurple()
        )

        help.set_footer(text='Help Page')
        help.set_author(name='Calculator-Bot')                                                                                                                                                                            
        help.add_field(name='-evo (tribe) (stat) (current stat) (target stat)',
                       value="Calculates the net evolutions points needed to attain the desired stat.", inline=False)
        help.add_field(name='-time (current movement points) (target movement points)', value='Calculates the Net amount of time to reach desired moves.', inline=False)
        help.add_field(name='-path (tribe) (x1) (y1) (x2) (y2)', value='Calculates the shortest path possible and send out an image showing the path.', inline=False)
        help.add_field(name='-purge (amount)', value='Clears message by the amount specified. ONLY WORKS IF USER HAS manage_messages PERMISSION.', inline=False)
        help.add_field(name='-base (tribe)', value='Returns an embed with the basse values of a specific tribe.', inline=False) 
        # Using "command_user", we can send a message directly to the user's DM.
        await command_user.send(embed=help)


# Basic setup of a command. Necessary for loading the commands with the actual main.py file.

async def setup(client):
    await client.add_cog(help(client))
