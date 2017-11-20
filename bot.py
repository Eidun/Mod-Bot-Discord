import sys
import traceback
import discord
from discord.ext import commands
import data


description = '''Bip bop, I'm a bot'''

modules = {'cogs.nopics', 'cogs.mod'}

bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    print('Bot initiating...')
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(game=discord.Game(name='Bot on Tatomexus Server!'))

    print('Loading systems...')
    if __name__ == '__main__':
        for module in modules:
            try:
                bot.load_extension(module)
                print('\t' + module)
            except Exception as e:
                print(f'Error loading module {module}', file=sys.stderr)
                traceback.print_exc()
    print('Systems 100%')
    print('------')

# Testbot-9000
bot.run('')
