import discord
from discord.ext import commands
import builtins
from discord_slash import ButtonStyle, SlashCommand
from discord_slash.utils.manage_components import *


client = commands.Bot(command_prefix="/", help_command=None)
slash = SlashCommand(client, sync_commands=True)
builtins.client = client
builtins.slash = slash

import admin_command
import information
import log_server
import music


client.run("ODc1Mzk5MDk4NzkzMDg3MDE2.YRU88Q.Q2irhdKSaUmDRjoTgZWS_afSRdk")