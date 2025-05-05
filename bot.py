import os

import discord
from dotenv import load_env

load_env()

TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.client()


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord")


client.run(TOKEN)
