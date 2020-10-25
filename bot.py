import discord
from discord.ext import commands

TOKEN = "Token of your bot"

bot = commands.Bot(command_prefix = "!", description = "LEVEL UP!")

@bot.event
async def on_ready():
	print("Ready !")

bot.run(TOKEN)
