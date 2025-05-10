import os

import discord
from dotenv import load_dotenv

from core.intents import intents

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")


client = discord.Client(intents=intents)
