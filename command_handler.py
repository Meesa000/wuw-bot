import discord
import google.generativeai as genai
from ai_response import AIResponse


class CommandHandler:
    async def on_message(self, message):

        if message.content.startswith('!hi'):
            await message.add_reaction('\U0001F919')
            await message.reply('Hello!')

        elif message.content.startswith('!info'):
            embed = discord.Embed(title="Wok u Won Bot", description="Information for the wok u won bot - this is a bot"
                                                                     "that is used to help me learn the discord.py API.",
                                  colour=discord.Colour.default())
            embed.add_field(name="Commands", value="!hi\n!info\n!kosmi\n!pin\n!ask then your query to ask ai "
                                                   "something (please do not spam"
                                                   "due to rate limits")
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
