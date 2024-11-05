import discord # Discord Bot library
from discord import app_commands
from discord.ext import commands
from config import botToken # Hides token for GitHub
from crypto import * # Gets functions from Crypto API
from database import * # Gets functions from data.py (sqlite)

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
@bot.tree.command(name="getcoin", description="Gets the value of a coin with its name")
async def getCoin(interaction: discord.Interaction, coin_name: str):
    try:
        await interaction.response.send_message(getCoinValue(coin_name))
    except Exception as e:
        await interaction.response.send_message("Invalid input, try again", ephemeral=True)

# Lets you see the top trending coins
@bot.tree.command(name="trending", description="Gets the top trending coins")
async def getTrending(interaction: discord.Interaction):
    try:
        await interaction.response.send_message(trending())
    except Exception as e:
        await interaction.response.send_message(e, ephemeral=True)

# Lets you see your list of coins
@bot.tree.command(name="checklist", description="Checks your list of coins")
async def checkList(interaction: discord.Interaction):
    userID = interaction.user.id
    try:
        await interaction.response.send_message(getUserList(userID))
    except Exception as e:
        await interaction.response.send_message(e, ephemeral=True)

@bot.tree.command(name="addcoin", description="Adds a coin to your list")
async def addCoin(interaction: discord.Interaction, coin_name: str):
    userID = interaction.user.id
    try:
        await interaction.response.send_message(addUserList(userID, coin_name))
    except Exception as e:
        await interaction.response.send_message(e, ephemeral=True)

@bot.command() # Test command
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

bot.run(botToken)