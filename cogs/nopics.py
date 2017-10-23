from utils.muter import mute_member
import asyncio
import cogs.mod
channels = ['chatting', 'chatting-2']


class NoPics:
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):

        if message.channel.name in channels:
            if message.attachments.__len__() > 0:
                await self.bot.delete_message(message)
                tmp = await self.bot.send_message(message.channel,
                                            '```\nHey, pics are not allowed in chatting channels!!\n```')
                await mute_member(self.bot, message.channel, message.author)
                cogs.mod.muted.append(message.author)
                await asyncio.sleep(10)
                await self.bot.delete_message(tmp)


def setup(bot):
    bot.add_cog(NoPics(bot))
