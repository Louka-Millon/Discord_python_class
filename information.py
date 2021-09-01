import discord
from discord.activity import create_activity
from discord.ext import commands
from discord_slash import ButtonStyle, SlashCommand
from discord_slash.utils.manage_components import *
from builtins import client,slash
from time import sleep
import datetime as DT


 
Timesup = DT.datetime



@client.event
async def on_ready():
    global Timesup
    Timesup = DT.datetime.now()
    print("Le bot est prêt !")

@client.command(
    pass_context=True,
    name="info",
    help="This command gives you information about the server and the bot.",
    brief="You want some help or invite someone ?"
)
async def info(ctx):
    embed = discord.Embed(
        color = discord.Color.blue()
    )
    embed.add_field(name="Need Help?", value="You can get help by asking operator in this server, or create an issue ticket in the channel #issue")
    embed.add_field(name="Add someone to the Server", value="Adding someone was not realy hard just send him this link : https://discord.gg/fgTD72wUFY")
    await ctx.send(embed=embed)


@client.command(
    pass_context=True,
    name="uptime",
    help="Give the bot uptime.",
    brief="Give the bot uptime."
)
async def uptime(ctx):
    timenow = DT.datetime.now()
    
    timenow = timenow.replace(microsecond=0) - Timesup.replace(microsecond=0)
    embed = discord.Embed(
        color = discord.Color.blue()
    )
    embed.add_field(name="Uptime:", value=timenow)
    await ctx.send(embed=embed)

@client.command(
    pass_context=True,
    name="help"
)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        color = discord.Color.blue()
    )
    embed.set_author(name="Help")
    embed.add_field(name="Operator command:",value="----------------",inline=False)
    embed.add_field(name="/ban", value="Ban member from the server.",inline=False)
    embed.add_field(name="Moderator command:",value="----------------",inline=False)
    embed.add_field(name="User command:",value="----------------",inline=False)
    embed.add_field(name="/info", value="This command gives you information about the server and the bot.", inline=False)
    embed.add_field(name="/uptime", value="Give the bot uptime.", inline=False)
    embed.add_field(name="/issue",value="Send to the admin information for an issue",inline=False)
    await author.send(embed=embed)


@client.command(
    pass_context=True,
    name="support"
)
async def support(ctx):
    buttons = [
        create_button(
            style=ButtonStyle.green,
            label="Report un bug",
            custom_id="oui"
        ),
        create_button(
            style=ButtonStyle.blue,
            label="Poser une question",
            custom_id="ask_question"
        )
    ]
    action_row = create_actionrow(*buttons)
    await ctx.message.delete()
    text = await ctx.send(":tickets: CRÉER UN TICKET ! \n que voulez vous faire ?", components=[action_row])


    
    button_ctx = await wait_for_component(client, components=action_row)
    if button_ctx.custom_id == "oui":
        await button_ctx.send("Votre ticket vient d'être créé, vous pouvez le voir ici : #bug-xmimilou-7090")
        print("test")
    else:
        await button_ctx.send("Votre ticket vient d'être créé, vous pouver le voir ici : #ask-xmimilou-7090")
        print("test2")
    