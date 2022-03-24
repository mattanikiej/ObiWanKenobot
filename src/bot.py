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
    """
    controls bot behavior on start up
    """
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Podracing"))


# command /obiwan
@client.command()
async def obiwan(ctx, *message):
    """
    Use case: /obiwan <message>
    Used to talk to the chat bot by sending a message, and then the bot replies.
    If no message is sent then the bot responds with 'Hello there!'
    :param ctx: context of the client
    :param message: message user sends the bot
    """
    if len(message) == 0:
        await ctx.send("Hello there! Send me a message after the command: /obiwan message")
    else:
        # message is a tuple of variable length where each word is an index and must be joined into one string
        message_str = ' '.join(message)
        response = model.chat(message_str)
        await ctx.send(response)


# run bot
client.run(token)
