# imports
import discord
from discord.ext import commands
import asyncio 
import random
import requests
import json

# Vars
with open("config.json", "r") as f:
    my_dict = json.load(f)
TOKEN = (my_dict["Your_Token"])
prefix = (my_dict["Your_Prefix"])
bot = commands.Bot(command_prefix=prefix, self_bot=True)
pingSwitch = False
headPictures = ()
tailPictures = ()


# Spam

@bot.command()
async def pingSpam(ctx, *, message):
    global pingSwitch
    if pingSwitch:
        await asyncio.sleep(1)
        await ctx.send(message)
        await pingSpam(ctx, message)
    else: 
        await ctx.send(f'This command is disabled, use {prefix}toggle, to toggle it back on.')

@bot.command()
async def toggle(ctx):
    global pingSwitch
    if pingSwitch:
        pingSwitch = False
        await ctx.send("OFF!")
    else: 
        pingSwitch = True
        await ctx.send("ON!")

# Stats

@bot.command()
async def diceRoll(ctx, message=1):
    diceOut = 0
    for x in range(0, message):
        diceOut += random.randint(1,6)
    await ctx.send(f"You rolled a {diceOut}!")

@bot.command()
async def coinflip(ctx):
    if random.randint(1,2) == 1:
        await ctx.send(f" # You got head!  ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||https://images-ext-1.discordapp.net/external/OK46gCwJMG5XlB6wvYRMFQI5tNwxg-bsgt9i4mghgT0/https/s3-us-west-2.amazonaws.com/s.cdpn.io/4273/spiritedaway-head.png?width=330&height=372")
    else:
        await ctx.send(f" # You didn't get head (tails)!  ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||https://images-ext-1.discordapp.net/external/RP5rDW2jl8MFPL3c5raE3tMbtJMA7cAa0h4m8DfQ1nc/%3Fcb%3D20220427053256%26path-prefix%3Dprotagonist/https/static.wikia.nocookie.net/p__/images/b/bf/TailsSO.png/revision/latest?width=869&height=674")

# NSFW

@bot.command()
async def blowjob(ctx):
    hentaiPayload = requests.get("https://waifu.pics/api/nsfw/blowjob")
    hentaiJSON = hentaiPayload.json()
    justhentai = hentaiJSON["url"]
    await ctx.send(f"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| {justhentai}")

# Moderation

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = "no reason"):
    await ctx.guild.ban(member, reason = reason)
    await ctx.send(f"**{member}** successfully banned for {reason}.")

@bot.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, member:discord.User):
    await ctx.guild.unban(member)
    await ctx.send(f"Successfully unbanned **{member}**!")

@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member:discord.Member, *, reason = "no reason"):
    await ctx.guild.kick(member, reason = reason)
    await ctx.send(f"Successfully kicked the ass of \"{member}\" because of the reason of {reason}")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, limit: int):
    await ctx.message.delete()
    await ctx.channel.purge(limit=limit)
    botMessage = await ctx.send(f"**{limit}** messages were successfully purged!")
    await asyncio.sleep(5)
    await botMessage.delete()

print("OMG I SALF BOOT")
# Construction
bot.run(TOKEN)