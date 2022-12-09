import discord
from discord.ext import commands
import asyncio

# Defining a Base class,within the class, passing client to make the discord module applicable here.

class base(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context = False)
    # Defining the base command with race as an argument
    async def base(self, ctx, race: str):
        # Introducing asyncio.cleep with ctx.typing. This will make the bot appear as it's typing,
        # for a given duration of time.
        async with ctx.typing():
            await asyncio.sleep(2)
        # Defining the user to later mention them.
        user = ctx.message.author
        # Defining Stat values along with their Stat costs.
        intel = races[race.lower()]['intel'][0]
        intelval = races[race.lower()]['intel'][1]
        strength = races[race.lower()]['strength'][0]
        strengthval = races[race.lower()]['strength'][1]
        agility = races[race.lower()]['agility'][0]
        agilityval = races[race.lower()]['agility'][1]
        health = races[race.lower()]['health'][0]
        healthval = races[race.lower()]['health'][1]
        endurance = races[race.lower()]['endurance'][0]
        enduranceval = races[race.lower()]['endurance'][1]
        instinct = races[race.lower()]['instinct'][0]
        instinctval = races[race.lower()]['instinct'][1]
        will = races[race.lower()]['will'][0]
        willval = races[race.lower()]['will'][1]

        # Defining the straight and diagonal movement costs of given race.
        racep1 = mvps[race.lower()]['Plains'][0]
        racep2 = mvps[race.lower()]['Plains'][1]
        racef1 = mvps[race.lower()]['Forest'][0]
        racef2 = mvps[race.lower()]['Forest'][1]
        racew1 = mvps[race.lower()]['Waste'][0]
        racew2 = mvps[race.lower()]['Waste'][1]
        raced1 = mvps[race.lower()]['Desert'][0]
        raced2 = mvps[race.lower()]['Desert'][1]
        races1 = mvps[race.lower()]['Snow'][0]
        races2 = mvps[race.lower()]['Snow'][1]
        racem11 = mvps[race.lower()]['Mountain1'][0]
        racem12 = mvps[race.lower()]['Mountain1'][1]
        racem21 = mvps[race.lower()]['Mountain2'][0]
        racem22 = mvps[race.lower()]['Mountain2'][1]
        racec1 = mvps[race.lower()]['Capitol'][0]
        racec2 = mvps[race.lower()]['Capitol'][1]
        racer1 = mvps[race.lower()]['Road'][0]
        racer2 = mvps[race.lower()]['Road'][1]

        # Checking the user's race and then allocating the respective image.
        if race.lower() == 'dwarr':
            image = dwarr_image
        elif race.lower() == 'leafborn':
            image = leafborn_image
        elif race.lower() == 'lightfoot':
            image = lightfoot_image
        elif race.lower() == 'mythos':
            image = mythos_image
        elif race.lower() == 'giant':
            image = giant_image
        elif race.lower() == 'norsk':
            image = norsk_image
        elif race.lower() == 'kiith':
            image = kiith_image
        elif race.lower() == 'nuruk':
            image = nuruk_image

        # Defining the embed for the race info.

        baseembed = discord.Embed(
            title = f'Base stats and costs for the {race.capitalize()} tribe',
            description = f'Requested by {user}',
            color = discord.Color.dark_gold()
        )
        baseembed.set_footer(text='Forsaken!')
        baseembed.set_thumbnail(url='https://agonialands.com/assets/images/logos/Agonia_Mini_logo_alpha.png')
        baseembed.set_author(name='Calc Bot')
        baseembed.add_field(name='Intel', value=f'Base Stat: {intel}\n Cost: {intelval}', inline=True)
        baseembed.add_field(name='Strength', value=f'Base Stat: {strength}\n Cost: {strengthval}', inline=True)
        baseembed.add_field(name='Agility', value=f'Base Stat: {agility}\n Cost: {agilityval}', inline=True)
        baseembed.add_field(name='Health', value=f'Base Stat: {health}\n Cost: {healthval}', inline=True)
        baseembed.add_field(name='Endurance', value=f'Base Stat: {endurance}\n Cost: {enduranceval}', inline=True)
        baseembed.add_field(name='Instinct', value=f'Base Stat: {instinct}\n Cost: {instinctval}', inline=True)
        baseembed.add_field(name='Will', value=f'Base Stat: {will}\n Cost: {willval}', inline=True)
        baseembed.add_field(name='Movement Points', value=f'Plains: {racep1}/{racep2}\nForest: {racef1}/{racef2}\nWaste: {racew1}/{racew2}\nDesert: {raced1}/{raced2}\nSnow: {races1}/{races2}\nMountain Level 1: {racem11}/{racem12}\nMountain Level 2: {racem21}/ {racem22}\nRoad: {racer1}/{racer2}\nCapitol: {racec1}/{racec2}', inline=False)
        # Adds an entra field under subheading of "Speciality" for Lightfoot and Kiith races.
        if race.lower() == 'kiith':
            baseembed.add_field(name="Speciality", value="Lava: 200/282")
        elif race.lower() == 'lightfoot':
            baseembed.add_field(name="Speciality", value='Water: 200/282')
        else:
            pass
        baseembed.set_image(url=image)
        await ctx.send(embed = baseembed)

# Making a list with all the races stats and their respective costs.
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
            "intel": [15,16],
            "strength": [14,7],
            "agility": [18,5.5],
            "health": [17,6],
            "endurance": [8,5],
            "instinct": [15,6],
            "will": [15,7]
        }
    }
# Making a list with all the races straight and diagonal movement costs.
mvps = {
        "dwarr": {
            "Plains": [22, 31],
            "Forest": [31, 43],
            "Waste": [22, 31],
            "Desert": [23, 32],
            "Snow": [35, 49],
            "Mountain1": [25, 35],
            "Mountain2": [36, 50],
            "Capitol": [5, 7],
            "Road": [13, 18]
        },

        "leafborn": {
            "Plains": [20, 28],
            "Forest": [18, 25],
            "Waste": [24, 33],
            "Desert": [25, 35],
            "Snow": [36, 50],
            "Mountain1": [48, 67],
            "Mountain2": [68, 96],
            "Capitol": [5, 7],
            "Road": [13, 18]
        },

        "lightfoot": {
            "Plains": [21, 29],
            "Forest": [22, 31],
            "Waste": [22, 31],
            "Desert": [22, 31],
            "Snow": [33, 46],
            "Mountain1": [40, 56],
            "Mountain2": [57, 80],
            "Capitol": [5, 7],
            "Road": [13, 18]
        },

        "mythos": {
            "Plains": [18, 25],
            "Forest": [27, 38],
            "Waste": [22, 31],
            "Desert": [22, 31],
            "Snow": [35, 49],
            "Mountain1": [35, 49],
            "Mountain2": [50, 70],
            "Capitol": [5, 7],
            "Road": [13, 18]
        },

        "giant": {
            "Plains": [19, 26],
            "Forest": [38, 53],
            "Waste": [20, 28],
            "Desert": [22, 31],
            "Snow": [32, 45],
            "Mountain1": [32, 45],
            "Mountain2": [45, 63],
            "Capitol": [5, 7],
            "Road": [13, 18]
        },

        "kiith": {
            "Plains": [22, 31],
            "Forest": [22, 31],
            "Waste": [19, 26],
            "Desert": [18, 25],
            "Snow": [38, 53],
            "Mountain1": [46, 65],
            "Mountain2": [65, 91],
            "Capitol": [5, 7],
            "Road": [13, 18]
        },

        "norsk": {
            "Plains": [20, 28],
            "Forest": [26, 36],
            "Waste": [23, 32],
            "Desert": [24, 33],
            "Snow": [27, 38],
            "Mountain1": [31, 43],
            "Mountain2": [44, 62],
            "Capitol": [5, 7],
            "Road": [13, 18]
        },

        "nuruk": {
            "Plains": [18, 25],
            "Forest": [22, 31],
            "Waste": [18, 25],
            "Desert": [20, 28],
            "Snow": [31, 43],
            "Mountain1": [28, 39],
            "Mountain2": [40, 56],
            "Capitol": [5, 7],
            "Road": [13, 18]
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
    await client.add_cog(base(client))
