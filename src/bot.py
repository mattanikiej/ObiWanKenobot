import discord
from discord.ext import commands
from model.model import Model
import os

# sets up client and command prefix
client = commands.Bot(command_prefix='/')
token = os.getenv("OBI_WAN_KENOBOT_TOKEN")

# train the model
# Since this is only ran once and is a fairly inexpensive computation,
# it is better to train since loading weights tends to make it have a lower accuracy
# due to LSTM cell sates not saving.
# THIS WILL MOST LIKELY BE CHANGED IN THE FUTURE WHEN I FIGURE OUT HOW TO BETTER SAVE MODEL!!!!
model = Model()
model.train()


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Podracing"))


# command /obiwan is used to talk to the bot
@client.command()
async def obiwan(ctx):
    await ctx.send('hello')


# has model run
client.run(token)
