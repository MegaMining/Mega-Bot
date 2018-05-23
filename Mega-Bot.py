import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os
import random

Client = discord.Client()
client = commands.Bot(command_prefix = ".")
client.remove_command('help')
@client.event
async def on_ready():
    print("Thank-You For Using Mega BOT!")
    await client.change_presence(game=discord.Game(name=".help | Beta v0.0.1"))

@client.event
async def on_message(message):
    if message.content.startswith('.hello'):
        msg = 'Hello {0.author.mention} How Are You Today'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('.bye'):
        msg = 'Goodbye {0.author.mention} Hope To See You Soon :wave:'.format(message)
        await client.send_message(message.channel, msg)


        
#.help
    if message.content.upper().startswith('.HELP'):
        embed = discord.Embed(title="****MEGA BOT****", description="**A BOT Made by Mr. Mega. List of commands are:**")
        embed.add_field(name=".bye", value="Responds to you", inline=False)
        embed.add_field(name=".hello", value="Responds to you", inline=False)
        embed.add_field(name=".inprogress", value="Shows features that are in Development.", inline=False)
        embed.add_field(name=".help", value="Gives this message.", inline=False)
        embed.add_field(name=".suggestions", value="Shows features that have been suggested and will get added.", inline=False)
        embed.add_field(name=".version", value="Gives you the Version of the BOT", inline=False)
        await client.send_message(message.channel, embed=embed)


#.apply
    if message.content.startswith(".apply"):
        emb = (discord.Embed(description="Apply to join UnknownLogic!", colour=0x3DF270))
        emb.set_author(name="**Apply Now**", icon_url='https://cdn.discordapp.com/icons/401265219759767552/f9d45f5ad85a29b332d3ddae38651ebc.webp')
        await client.send_message(message.channel, embed=emb)

#.inprogress
    if message.content.startswith('.inprogress'):
        embed = discord.Embed(title="****IN PROGRESS****", description="**THESE FEATURES ARE NOT COMPLETE**", color=0xeee657)
        await client.send_message(message.channel, embed=embed)

#.meme
    if message.content.startswith(".meme"):
        await client.send_message(message.channel, random.choice(["Whats 9+10? : 21:",
                                                                  "Mega NEVER Dies",
                                                                  "Wheres your logic ? : It is UnknownLogic",
                                                                  "WHAT ARE THOSE!"]))

#.suggestions
    if message.content.startswith('.suggestions'):
        embed = discord.Embed(title="****SUGGESTION LIST****", description="**SUGGESTIONS I HAVE BEEN GIVEN. THEY ARE ON MY TO DO LIST.**", color=0xeee657)
        await client.send_message(message.channel, embed=embed)

#.version
    if message.content.startswith('.version'):
        embed = discord.Embed(title="****Version****", description="Beta V0.0.1 | Build:10", color=0xeee657)
        embed.add_field(name="To Display Changes of a version type the version", value="e.g: .v0.0.1", inline=False)
        await client.send_message(message.channel, embed=embed)

#version list
    if message.content.startswith('.changelog v0.0.1'):
        embed = discord.Embed(title="****Version v0.0.1****", colour=0x3DF270)
        embed.add_field(name="Changelog:", value="Mega BOT up and Running", inline=False)
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('.changelog v0.0.2'):
        embed = discord.Embed(title="****Version v0.0.2 Changelog****", colour=0x3DF270)
        embed.add_field(name="Added", value=".apply", inline=False)
        embed.add_field(name="-", value=".inprogress", inline=False)
        embed.add_field(name="-", value=".meme", inline=False)
        embed.add_field(name="-", value=".suggestions", inline=False)
        embed.add_field(name="-", value=".version", inline=False)
        embed.add_field(name="-", value=".version list", inline=False)
        await client.send_message(message.channel, embed=embed)

client.run(os.getenv('TOKEN'))
