import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"ErYx AI is online as {bot.user}")


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # Reply when ErYx AI is mentioned
    if bot.user and bot.user in message.mentions:
        await message.channel.send(
            f"Yo {message.author.mention} 👀 ErYx AI online."
        )

    await bot.process_commands(message)


token = os.getenv("DISCORD_TOKEN")

if not token:
    raise RuntimeError("DISCORD_TOKEN is missing!")

bot.run(token)