import discord # Discord Bot library
from discord import app_commands
from discord.ext import commands
from config import botToken # Hides token for GitHub
from crypto import * # Gets functions from Crypto API

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

# Lets you see the value of a coin with its name
@bot.tree.command(name="getcoin")
async def getCoin(interaction: discord.Interaction, coin_name: str):
    try:
        await interaction.response.send_message(getCoinValue(coin_name))
    except Exception as e:
        await interaction.response.send_message("Invalid input, try again", ephemeral=True)

@bot.tree.command(name="trending")
async def getTrending(interaction: discord.Interaction):
    try:
        await interaction.response.send_message(trending())
    except Exception as e:
        await interaction.response.send_message(e, ephemeral=True)

@bot.command() # Test command
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

bot.run(botToken)