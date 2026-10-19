# ARCTURUS Discord AI Bot

This version uses **OpenAI**, not Anthropic. It responds in DMs or when mentioned in a server, maintains short per-channel memory in RAM, and supports `reset`.

## 1. Secure your credentials

**Reset your exposed Discord bot token** in Discord Developer Portal > Applications > your application > Bot > Reset Token. Do not reuse the token from your uploaded sample file.

Create an OpenAI API key using the OpenAI Platform setup flow. API usage is billed separately from ChatGPT subscriptions; configure a spending budget in the OpenAI Platform dashboard.

## 2. Configure Discord

At https://discord.com/developers/applications create/select the ARCTURUS application, open the **Bot** tab, and enable **Message Content Intent** under Privileged Gateway Intents.

Invite the bot via the OAuth2 installation flow with the `bot` scope and the permissions **View Channels**, **Send Messages**, and **Read Message History**. (DM availability also depends on Discord settings.)

## 3. Setup on Windows

Install Python 3.10+ and open a terminal inside this folder:

```powershell
py -m pip install -r requirements.txt
Copy-Item .env.example .env
notepad .env
```

In `.env`, paste your **newly regenerated** Discord token and your OpenAI API key. Never post `.env` or your tokens in chat.

## 4. Start

```powershell
py bot.py
```

You should see `ARCTURUS online as ...`. Mention `@ARCTURUS hello` in your Discord server, or send a DM. Mention the bot with `reset` to clear the channel conversation.

## Notes

- The bot stays online only while its Python process is running. For 24/7 operation, deploy it on a suitable hosting service.
- Memory is per Discord channel and resets on restart. Everyone in a channel shares that channel's recent conversation context.
- Images, audio, and Discord slash commands are not implemented in this starter version.
- `OPENAI_MODEL` defaults to `gpt-4.1-mini`; change it if needed to a model available to your project.
