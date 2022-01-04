import os
import sys
import json
import platform

import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext import tasks, commands
from disnake.ext.commands import Bot

version = "0.0.1A"

try:
    with open("config.json", "r") as c:
        config = json.load(c)
except FileNotFoundError:
    print ("Config not found, making one")
    with open("config.json","w") as c:
        json.dump({
        'Discord_TOKEN': 'TOKEN',
        'Activity': 'Bot activity here',
        'Prefix': 'y, ',
        'Embed_Title': 'Yung Bot',
        'Embed_Title_URL': 'https://yungcz.com',
        'Embed_Description': 'A Brilliant Bot',
        'Embed_Colour': 0xFFFFFF,
        'Embed_Thumbnail': 'https://i.imgur.com/U067iC8.jpg'
        }, c, indent=2)
    raise Exception ("Fill in your config.json before continuing")
    exit()

async def checkVersion():
    if version[0] == 0:
        released = False
    else:
        released = True
    return released

bot = Bot(command_prefix=config["Prefix"])
bot.remove_command("help")

@bot.event
async def on_ready():
    print ("===============================================")
    print ("             This is Yung Bot V3               ")
    print (f"        You're running version {version}       ")
    if await checkVersion() == True:
        print ("")
    else:
        print ("      YOU'RE RUNNING AN UNRELEASED VERSION!    ")
        print ("        WARNING THIS MAY BREAK YOUR BOT        ")
    print ("")
    print (f"  > You're logged in as {bot.user.name}")
    print (f"  > You're running Disnake version {disnake.__version__}")
    print (f"  > You're running Python version {platform.python_version()}")
    print ("")
    print ("===============================================")

import importlib
print(dir(importlib.import_module('cogs.general')))

if __name__ == "__main__":
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")

bot.run(config["Discord_TOKEN"])



