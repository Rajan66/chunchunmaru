import discord
from discord.ext import commands

from bot.main import GUILD, TOKEN
from core.intents import intents

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command(name="mods")
async def mods(ctx):
    await ctx.send("mods ban this guy")


@bot.command(name="slur")
async def slur(ctx):
    if ctx.message.mentions:
        target = ctx.message.mentions[0]
        await ctx.send(f"{target.mention} is a doggy bhai")
    else:
        await ctx.send("beer bhai is a doggy bhai")


@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(f"{bot.user} is running on server: {guild.name}")
    for channel in guild.text_channels:
        if "workshop" in channel.name.lower():
            await channel.send(f"{bot.user} is online.")


# @bot.event
# async def on_message(message):
#     print("am i running?")
#     print(message)
#     if message.author == "icecoldreaper":
#         await message.channel.send("bleh bleh")
#

bot.run(TOKEN)
