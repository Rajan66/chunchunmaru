from bot.main import GUILD


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
