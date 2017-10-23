import discord

async def mute_member(bot, channel, member):
    overwrite = channel.overwrites_for(member) or \
                discord.PermissionOverwrite()
    overwrite.send_messages = False
    await bot.edit_channel_permissions(
        channel,
        member,
        overwrite
    )

async def unmute_member(bot, channel, member):
    overwrite = channel.overwrites_for(member) or \
                discord.PermissionOverwrite()
    overwrite.send_messages = True
    await bot.edit_channel_permissions(
        channel,
        member,
        overwrite
    )
