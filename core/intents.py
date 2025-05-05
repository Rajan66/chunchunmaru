import discord

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.message_content = True
