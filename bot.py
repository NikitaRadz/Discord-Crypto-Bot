import discord # Discord Bot library
from discord import app_commands
from discord.ext import commands
import requests # HTTP request library
from config import botToken

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user: # So it doesn't reply to itself
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@bot.tree.command(name="jello")
async def jello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command!")

bot.run(botToken)