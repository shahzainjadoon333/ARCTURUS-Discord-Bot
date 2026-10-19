
import os
import random
import logging
from datetime import datetime

import discord
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

if not DISCORD_TOKEN or DISCORD_TOKEN == "Enter_Your_Discord_Token_Here":
    raise RuntimeError("Please add your Discord bot token to .env")

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"ARCTURUS is online as {bot.user}!")
    print(f"Connected to {len(bot.guilds)} server(s).")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # In servers, respond only when mentioned or given a command.
    mentioned = bot.user in message.mentions if bot.user else False
    text = message.content

    if bot.user:
        text = text.replace(f"<@{bot.user.id}>", "")
        text = text.replace(f"<@!{bot.user.id}>", "")

    text = text.strip()
    command = text.lower()

    if message.guild and not mentioned and not command.startswith("!"):
        return

    if command in ("!help", "help"):
        await message.reply(
            "**ARCTURUS Commands**\n"
            "`!help` — Show commands\n"
            "`!ping` — Check response time\n"
            "`!about` — About the bot\n"
            "`!time` — Show UTC time\n"
            "`!roll` — Roll a dice\n"
            "`!choose option1, option2` — Pick an option\n"
            "`!clear` — Clear the current chat"
        )

    elif command == "!ping":
        ms = round(bot.latency * 1000)
        await message.reply(f"Pong! Latency: **{ms} ms**")

    elif command == "!about":
        await message.reply(
            "I'm **ARCTURUS**, a Python-powered Discord bot. "
            "I provide useful commands and simple built-in responses."
        )

    elif command == "!time":
        now = datetime.now().astimezone()
        await message.reply(
            f"Current UTC time: {datetime.utcnow().strftime('%H:%M:%S')}"
        )

    elif command == "!roll":
        await message.reply(f"You rolled **{random.randint(1, 6)}**!")

    elif command.startswith("!choose "):
        options = [
            item.strip()
            for item in text[8:].split(",")
            if item.strip()
        ]

        if len(options) < 2:
            await message.reply(
                "Give me at least two options, e.g. `!choose Python, Java`"
            )
        else:
            await message.reply(f"I choose: **{random.choice(options)}**")

    elif command == "!clear":
        await message.reply(
            "I don't store conversation history in this version, "
            "so there's nothing to clear."
        )

    elif not command.startswith("!"):
        if any(word in command for word in ["hello", "hi", "hey"]):
            await message.reply(
                f"Hey {message.author.display_name}! how can I help?"
            )
        elif "your name" in command or "who are you" in command:
            await message.reply("I'm ARCTURUS, your Discord bot! ")
        elif "thank" in command:
            await message.reply("You're welcome! ")
        else:
            await message.reply(
                "I can help with built-in commands! Try `!help` to see them."
            )

bot.run(DISCORD_TOKEN)
