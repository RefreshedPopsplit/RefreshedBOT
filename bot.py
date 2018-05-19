import discord
from discord.ext import commands
prefix = ["-"]
bot = commands.Bot(command_prefix=prefix)
@bot.command
async def hello():
    await bot.say("Hello :wave:" )
bot.run("NDQ2Nzc0NTg0NjM3NjUyOTky.DeH-LA.NERXRC5-flgNWtw6sMqxNwhSnUc")
