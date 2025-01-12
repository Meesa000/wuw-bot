import random
import discord
from ai_response import AIResponse
from discord.ext import commands
from discord import app_commands


class CommandHandler:
    async def on_message(self, message):

        if message.content.startswith('!hi'):
            await message.add_reaction('\U0001F919')
            await message.reply('Hello!')

        elif message.content.startswith('!info'):
            embed = discord.Embed(title="Wok u Won Bot", description="Information for the wok u won bot - this is a bot"
                                                                     " that is used to help me learn the discord.py API.",
                                  colour=discord.Colour.default())
            embed.add_field(name="Commands", value="!hi\n!info\n!kosmi\n!pin\n!ask then your query to ask ai "
                                                   "something (please do not spam"
                                                   "due to rate limits\n!flip to flip a coin")
            embed.add_field(name='Features', value='This bot has an OSRS loot tracker, in built Google gemini AI.\n'
                                                   '\nTo use the loot tracker, install the RL plugin Discord Loot Logger,'
                                                   'and put in the webhook URL that is pinned' )
            embed.set_footer(text="Bot created by Meesa")
            await message.reply(embed=embed)

        elif message.content.startswith('!kosmi'):
            await message.reply('The Kosmi link is: https://app.kosmi.io/vx4sgv')

        elif message.content.startswith('!pin'):
            await message.reply(f'{message.author.global_name} pinned the following: {message.content}')
            await message.pin()

        elif message.content.startswith('!ask'):
            response = AIResponse.get_ai_response(str(message.content))
            await message.reply(response)

        elif message.content.startswith('!flip'):
            coin = ['Heads', 'Tails']
            side = random.randint(0, 1)
            await message.reply(file=discord.File('C:\\Users\\asim_\\IdeaProjects\\wuw-bot\\images\\de-fi-land-coin-flip.gif'))
            await message.reply(f'The coin landed on: {coin[side]}')




