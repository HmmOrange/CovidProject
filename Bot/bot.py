import sys, os
sys.path.append(os.path.abspath(os.path.join('.')))

import discord
from discord.ext import commands, tasks
import os
import asyncio
import json
from datetime import datetime
import requests


intent = discord.Intents.all()
client = commands.Bot(command_prefix = ">", case_insensitive = True, intents = intent)
activity = discord.Activity(name = 'with data', type = discord.ActivityType.playing)

@client.event
async def on_ready():
    print("Hi!")
    await client.change_presence(activity = activity)

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                client.load_extension(f'cogs.{filename[:-3]}')
                print(f"{filename}: ok!")
            except Exception as e:
                print(f"{filename}: not ok!! - {e}")
    client.load_extension("jishaku")

client.run('')
