import discord
from utils.muter import mute_member, unmute_member
from discord.ext import commands
import asyncio
import data

channels = ['chatting', 'chatting-2']

traffic = {}

mute_words = ['fuck', 'shit']
muted = []

class Modeator:
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        data.allowed_channels = message.server.channels
        # Mute if inappropriate words
        for mute_word in mute_words:
            if mute_word in message.content.lower():
                # mute_member(self.bot, message, message.author)
                await self.bot.delete_message(message)
                tmp = await self.bot.send_message(message.channel, 'Inappropriate words are not allowed! ')
                await asyncio.sleep(10)
                await self.bot.delete_message(tmp)

        # Self bot messages
        if message.author.bot:
            return
        # Detecting spam
        if message.author.id not in traffic:
            traffic[message.author.id] = 0
        traffic[message.author.id] += 1
        print(traffic)

    @commands.command(pass_context=True)
    @commands.has_role('Admin')
    async def mute(self, ctx, member: discord.Member):
        all_channels = data.allowed_channels
        print(data.allowed_channels)
        for channel in all_channels:
            print('Muting in {}'.format(channel.name))
            await mute_member(self.bot, channel, member)
        tmp = await self.bot.say('{} muted'.format(member.display_name))
        await asyncio.sleep(10)
        await self.bot.delete_message(tmp)

    @commands.command(pass_context=True)
    @commands.has_role('Admin')
    async def unmute(self, ctx, member: discord.Member):
        all_channels = data.allowed_channels
        for channel in all_channels:
            await unmute_member(self.bot, channel, member)
        tmp = await self.bot.say('{} unmuted'.format(member.display_name))
        await asyncio.sleep(10)
        await self.bot.delete_message(tmp)


async def mute_task(bot: commands.Bot):
    while not bot.is_closed:
        await asyncio.sleep(10)
        for id in traffic:
            if traffic[id] > 15:
                member = discord.utils.find(lambda x: x.id == id, bot.get_all_members())
                all_channels = data.allowed_channels
                for channel in all_channels:
                    await mute_member(bot, channel, member)
                muted.append(member)
            traffic[id] = 0


async def unmute_task(bot: commands.Bot):
    while not bot.is_closed:
        await asyncio.sleep(2700)
        for member in muted:
            all_channels = data.allowed_channels
            for channel in all_channels:
                await unmute_member(bot, channel, member)
            muted.remove(member)


def setup(bot: commands.Bot):
    bot.add_cog(Modeator(bot))
    bot.loop.create_task(mute_task(bot))
    bot.loop.create_task(unmute_task(bot))


