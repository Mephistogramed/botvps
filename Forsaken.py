import asyncio
from turtle import done
import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix= '-', intents = discord.Intents.all())

client.remove_command('help')
# Defining the load cogs(commands) function, this pulls all the commands in the command folder.
async def load():
    for filename in os.listdir('/root/botvps/commands'):
        if filename.endswith('.py'):
            await client.load_extension(f'commands.{filename[:-3]}')
            print(f'Loaded {filename}')
        else:
            pass

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="-help"))
    print('Bot is now ready!')

async def main():
    async with client:
        await load()
        await client.start("")

# This connects the script with the bot application.

asyncio.run(main())
