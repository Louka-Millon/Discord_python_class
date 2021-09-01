from typing import Optional
import discord
from discord.ext import commands
from builtins import client


@client.command(
    help="type the following command with some arguments and the bot ban him/her.",
    brief="Ban member from the server.",
    name="ban"
)
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await ctx.message.delete()
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.add_field(name="Ban reason", value=str(member) + " : à été bannis pour " + reason)
    await ctx.send(embed=embed)
    await member.ban(reason = reason)



@client.command(
    help="With this command can communicated with someone as the discord bot.",
    brief="Send message in another channel with his channelid.",
    name="anonyme"
)
@commands.has_permissions(ban_members = True)
async def anonyme(ctx, channelid, *args):
    text = ""
    for arg in args:
        text += arg + " "
    await ctx.message.delete()
    channel = client.get_channel(int(channelid))
    await channel.send(text)

@client.command(
    help="type the following command with some arguments and the bot mute him/her.",
    brief="Mute member on this server.",
    name="mute"
)
@commands.has_permissions(ban_members = True)
async def mute(ctx, member : discord.Member, mutetime: Optional[int], *, reason = None ):
    await ctx.message.delete()
    embed = discord.Embed(
        color = discord.Color.red()
    )
    
    embed.add_field(name="Mute reason", value=str(member) + " : à été mute pour " + reason + " ; pendant : " + str(mutetime))
    await ctx.send(embed=embed)
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
