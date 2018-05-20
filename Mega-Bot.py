import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os
import random

Client = discord.Client()
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Thank-You For Using Mega BOT!")
    await client.change_presence(game=discord.Game(name=".help | v0.0.1"))

@client.event
async def on_message(message):
    if message.content.startswith('.hello'):
        msg = 'Hello {0.author.mention} How Are You Today'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('.bye'):
        msg = 'Goodbye {0.author.mention} Hope To See You Soon :wave:'.format(message)
        await client.send_message(message.channel, msg)


        
#.help

@client.event
async def on_message(message):
  if message.content.startswith('.help'):
    embed = discord.Embed(title="**Mega BOT**", description="A BOT Made by Mr. Mega. List of commands are:", color=0xeee657)
    embed.add_field(name=".help", value="Gives this message.", inline=False)
    embed.add_field(name=".hello", value="Responds to you", inline=False)
    embed.add_field(name=".bye", value="Responds to you", inline=False)
    embed.add_field(name=".version", value="Gives you the Version of the BOT", inline=False)
    await client.send_message(message.channel, embed=embed)

    
#.version

@client.event
async def on_message(message):
  if message.content.startswith('.version'):
    embed = discord.Embed(title="****Version****", description="V0.0.1 Beta | Build:3", color=0xeee657)
    await client.send_message(message.channel, embed=embed)

