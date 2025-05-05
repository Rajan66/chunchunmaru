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


def find_guild(client):
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    if guild:
        print(f"{client.user} is now rescuing the server: {guild.name}")
        print(f"{guild.name} has the ID: {guild.id}")
    else:
        print(f"{GUILD} not found.")
    return guild


@client.event
async def on_ready():
    greet(client.user)
    # guild = find_guild(client)

    # using find()
    # - takes predicate (another func) i.e. lambda func in this case
    # - and an iterable (list)
    # guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    guild = discord.utils.get(client.guilds, name=GUILD)

    for member in guild.members:
        if member.name in dog_members:
            print(f"{member.name} is a doggy bhai")


@client.event
async def on_message(message):
    print(f"{message.author} is sending a message")

    if message.author == client.user:
        return

    if message.content == "bleh":
        response = "bleh bleh bleh"
        await message.channel.send(response)

    if str(message.author) == "icecoldreaper" and message.content == "yo chunchunmaru":
        response = "hi boss"
        await message.channel.send(response)

    if str(message.author) == "x_lord":
        response = "dhwang khatey chup lol"
        await message.channel.send(response)

    if message.content.startswith("h"):
        response = "chunchunmaru"
        await message.channel.send(response)


client.run(TOKEN)
