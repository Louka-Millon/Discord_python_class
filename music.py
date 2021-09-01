import discord
from discord.ext import commands
from builtins import client
import youtube_dl
import os



@client.command(
    pass_context=True,
    name="play"
)
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    VoiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    try :
        await VoiceChannel.connect()
    except PermissionError:
        print("tkt")
        return
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors':[{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file,"song.mp3")
        
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command(
    pass_context=True,
    name="leave"
)
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to the voice channel.")


@client.command(
    pass_context=True,
    name="pause"
)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        await voice.pause()
    else:
        await ctx.send("currently no audio is playing.")

@client.command(
    pass_context=True,
    name="resume"
)
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        await voice.resume()
    else:
        await ctx.send("The bot is not paused.")


@client.command(
    pass_context=True,
    name="stop"
)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()