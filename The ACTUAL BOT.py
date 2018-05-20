import discord
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "!")
@client.event
async def on_ready():
    print("Thank-You For Using MegaBot")
    await client.change_presence(game=discord.Game(name="Mega Bot"))

@client.event
async def on_message(message):
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention} How are you Today'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!bye'):
        msg = 'Goodbye {0.author.mention} Hope to See You Again Soon :wave:'.format(message)

client.run(os.getenv('TOKEN'))
