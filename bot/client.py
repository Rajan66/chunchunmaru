import discord

from core.utils import greet

from .main import GUILD, client

dog_members = ["deadxyndrome5763", "x_lord", "y_k03"]


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

    if str(message.author) == "y_k03":
        response = "masale gay chup"
        await message.channel.send(response)

    if message.content.startswith("h"):
        response = "chunchunmaru"
        await message.channel.send(response)
