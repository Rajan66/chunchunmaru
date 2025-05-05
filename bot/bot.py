import os

import discord
from dotenv import load_dotenv

from core.intents import intents

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
client = discord.Client(intents=intents)
dog_members = ["deadxyndrome5763", "x_lord", "y_k03"]


def greet(bot):
    print(f"{bot} has connected to Discord")
    print(f"{bot} to the rescue")


@client.event
async def on_ready():
    greet(client.user)

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    if guild:
        print(f"{client.user} is now rescuing the server: {guild.name}")
        print(f"{guild.name} has the ID: {guild.id}")
    else:
        print(f"{GUILD} not found.")

    for member in guild.members:
        if member.name in dog_members:
            print(f"{member.name} is a doggy bhai")


client.run(TOKEN)
