import discord
from command_handler import CommandHandler
from dotenv import load_dotenv
import os

load_dotenv('C:\\Users\\asim_\\IdeaProjects\\wuw-bot\\config.env')
TOKEN = os.getenv('TOKEN')
commands = CommandHandler()


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')
        channel = client.get_channel(1038401470900482130)
        await channel.send('Wok u Won bot is online! !info for a commands list!')

    async def on_message(self, message):
        if message.author == client.user:
            return
        await commands.on_message(message)


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

client.run(TOKEN)
