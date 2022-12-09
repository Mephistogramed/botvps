import discord
from discord.ext import commands

# Defining an Evo class, within the class, passing client to make the discord module applicable here.
class evo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    # Defining the command "evo" as an embed with user's race, stat, current value and target value as positional arguments.
    async def evo(self, ctx, race: str, stat: str, current_stat: int, target_stat: int, amount=1):
        # Finds the base stat and base cost of user's race.
        user_stat_value = races[race.lower()][stat.lower()][0]
        user_stat_cost = races[race.lower()][stat.lower()][1]

        # Using Arithmetic Progression, calculates net stats needed, current evos spent and evos needed to attain target stat. 
        race_stat_current_statdif = (current_stat - user_stat_value)
        race_stat_target_statdif = (target_stat - user_stat_value)
        race_stat_current_cost = (user_stat_cost + (race_stat_current_statdif - 1) * user_stat_cost)
        race_stat_total_current_evo = ((race_stat_current_statdif / 2) * (user_stat_cost + race_stat_current_cost))
        race_stat_target_cost = (user_stat_cost + (race_stat_target_statdif - 1) * user_stat_cost)
        race_stat_total_target_evo = ((race_stat_target_statdif / 2) * (user_stat_cost + race_stat_target_cost))
        race_stat_net_evos = (race_stat_total_target_evo - race_stat_total_current_evo)

        # Defining the image with respect to the user's race.
        if race == 'dwarr':
            image = dwarr_image
        elif race == 'leafborn':
            image = leafborn_image
        elif race == 'lightfoot':
            image = lightfoot_image
        elif race == 'mythos':
            image = mythos_image
        elif race == 'giant':
            image = giant_image
        elif race == 'norsk':
            image = norsk_image
        elif race == 'kiith':
            image = kiith_image
        elif race == 'nuruk':
            image = nuruk_image

        # Defining the embed for the evo-calc.
        evocalc = discord.Embed(
            title='Evolution Points Calculator',
            description='Calculates the Evolution points needed to attain a desired stat.',
            color=discord.Color.blurple()
        )
        evocalc.set_footer(text='Forsaken!')
        evocalc.set_thumbnail(url='https://agonialands.com/assets/images/logos/Agonia_Mini_logo_alpha.png')
        evocalc.set_author(name='Calc Bot')
        evocalc.add_field(name='Race', value=race, inline=True)
        evocalc.add_field(name='Stat', value=stat, inline=True)
        evocalc.add_field(name='Current Stat', value=current_stat, inline=True)
        evocalc.add_field(name='Target Stat', value=target_stat, inline=True)
        evocalc.add_field(name='Net Stats', value=(target_stat - current_stat), inline=True)
        evocalc.add_field(name='Current Spent', value=race_stat_total_current_evo, inline=True)
        evocalc.add_field(name='Net Evos Needed', value=race_stat_net_evos, inline=True)
        evocalc.set_image(url=image)
        # Sending the embed in respective channel.
        await ctx.send(embed=evocalc)

# Making a list of all the races along with their stat values and their respective costs.
races = {
        "dwarr": {
            "intel": [14,8],
            "strength": [20,5],
            "agility": [12,9],
            "health": [19,4.5],
            "endurance": [7,6],
            "instinct": [11,8],
            "will": [19,6]
        },

        "leafborn": {
            "intel": [19,5],
            "strength": [13,8],
            "agility": [25,4],
            "health": [12,8],
            "endurance": [7,7],
            "instinct": [19,5],
            "will": [11,6]
        },

        "lightfoot": {
            "intel": [21,4],
            "strength": [10,10],
            "agility": [26,4],
            "health": [13,8],
            "endurance": [7,6],
            "instinct": [19,6],
            "will": [11,6]
        },

        "mythos": {
            "intel": [13,7],
            "strength": [21,4.5],
            "agility": [23,4],
            "health": [10, 10],
            "endurance": [6,7],
            "instinct": [12,7],
            "will": [15,7]
        },

        "giant": {
            "intel": [6,18],
            "strength": [23,4],
            "agility": [8,12],
            "health": [23,4],
            "endurance": [7,6],
            "instinct": [10,11],
            "will": [15,10]
        },

        "kiith": {
            "intel": [19,5],
            "strength": [13,8],
            "agility": [22,4.5],
            "health": [14,7],
            "endurance": [8,6],
            "instinct": [16,7],
            "will": [14,6]
        },

        "norsk": {
            "intel": [11,10],
            "strength": [21,4.5],
            "agility": [11,9],
            "health": [19,5],
            "endurance": [8,4.5],
            "instinct": [12,8],
            "will": [18,6]
        },

        "nuruk": {
            "intel": [15,6],
            "strength": [14,7],
            "agility": [18,5.5],
            "health": [17,6],
            "endurance": [8,5],
            "instinct": [15,6],
            "will": [15,7]
        }
    }

# Defining image links of all the races.
dwarr_image = "https://i.ibb.co/6cMDP6z/dwarr.jpg"
leafborn_image = "https://i.ibb.co/vxFW0m1/leafborn.jpg"
lightfoot_image = "https://i.ibb.co/mv42WVs/lightfoot.jpg"
mythos_image = "https://i.ibb.co/qBLG7wy/mythos.jpg"
giant_image = "https://i.ibb.co/sHjr2j2/giant.jpg"
kiith_image = "https://i.ibb.co/Z28L0Nb/kiith.jpg"
norsk_image = "https://i.ibb.co/SvHF1qC/norsk.jpg"
nuruk_image = "https://i.ibb.co/1qpmtwR/nuruk.jpg"

# Basic setup of a command. Necessary for loading the commands with the actual main.py file.
async def setup(client):
    await client.add_cog(evo(client))
