import discord
from discord.ext import commands
from builtins import client
from time import sleep
import datetime
import os


@client.event
async def on_message(message):
    timenow = datetime.datetime.now()
    titletime = f"{datetime.datetime.now():%y_%m_%d}"
    timenow = timenow.replace(microsecond=0)
    auteur = (message.author.name).encode("UTF-8")
    logstring = "["+str(timenow) +"] "+ str(auteur) + " / " + str(message.channel.name) + " : " + str(message.content)+"\n"
    filename = "logs/logfile_"+str(message.channel.name)+"-"+str(titletime)+".log"
    if not os.path.exists("logs"):
        os.mkdir("logs")
    
    if os.path.exists(filename):
        f = open(filename, "a")
        f.write(logstring)
        f.close()
    else:
        f = open(filename, "x")
        f.write(logstring)
        f.close()

    with open('badwords.txt') as file:
        file = file.read().split()

    for badword in file:

        if badword in message.content.lower():
            await message.delete()
            embed = discord.Embed(
                color = discord.Color.red()
            )
            embed.set_author(name="Badword détecté")
            embed.add_field(name=message.author.name,value="a dis le mot suivant : "+str(badword))
            await message.channel.send(embed=embed)
    await client.process_commands(message)


@client.command(
    pass_context=True,
    name="issue"
)
async def issue(ctx, *, error):
    author = ctx.message.author
    embed = discord.Embed(
        color = discord.Color.orange()
    )
    await ctx.message.delete()
    embed.set_author(name="Issue de "+str(author))
    embed.add_field(name="Erreur remonté :",value=error)
    channel = client.get_channel(int(877886796430716928))
    await channel.send(embed=embed)

@client.command(
    pass_context=True,
    name="idea"
)
async def idea(ctx, *, idea):
    author = ctx.message.author
    embed = discord.Embed(
        color = discord.Color.green()
    )
    await ctx.message.delete()
    embed.set_author(name="Idea de "+str(author))
    embed.add_field(name="idée proposé :",value=idea)
    channel = client.get_channel(int(877889124441395200))
    await channel.send(embed=embed)

