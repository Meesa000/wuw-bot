import aiohttp
import discord
from command_handler import CommandHandler
from dotenv import load_dotenv
import os

load_dotenv('C:\\Users\\asim_\\IdeaProjects\\wuw-bot\\config.env')
TOKEN = os.getenv('TOKEN')

commands_handler = CommandHandler()


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')
        await self.change_presence(activity=discord.Game('Wok u Won Simulator'))
        webhook_url = 'https://discord.com/api/webhooks/1328044402471604325/c6vKUKbsLCwln8f7n5cfRejX8RLNoK' \
                      '-WmbTRiaZkCD6f3-P05EjRnhQvVWRIFAMwzyvY'
        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.from_url(webhook_url, session=session)
            await webhook.send('OSRS loot tracker is now active')

        channel = self.get_channel(1038401470900482130)
        await channel.send('Wok u Won bot is online! !info for a commands list!')

    async def on_message(self, message):
        if message.author == client.user:
            return
        await commands_handler.on_message(message)


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

client.run(TOKEN)
