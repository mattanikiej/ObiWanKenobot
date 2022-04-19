import discord
from discord.ext import commands

import os
from time import sleep
import random

from model.model import Model
from SecretJarJar.secret_jarjar import SecretJarJar
from YTDLSource import YTDLSource

# sets up client and command prefix
client = commands.Bot(command_prefix='ob!', help_command=None)
token = os.getenv("OBI_WAN_KENOBOT_TOKEN")

# load pretrained model in
model = Model(data_path='data/obiwanintents.json')
model.load_model('model/saved_models/obiwankenobot')


@client.event
async def on_ready():
    """
    controls bot behavior on start up
    """
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Podracing"))


# command ob!help
@client.command()
async def help(ctx):
    """
    Use case: ob!help
    Displays all commands
    :param ctx: context of the client
    """
    help_msg = """
    Obi-Wan Kenobot Commands (prefix=ob!):
    **chat <message>** -  use to send a message to obiwan and he will respond in chat
    **talk** - use while in a voice channel to invite obiwan and have him say a line
    **sjj** - use to play Secret JarJar NOT FINISHED
    """
    await ctx.send(help_msg)


# command ob!chat
@client.command()
async def chat(ctx, *message):
    """
    Use case: ob!chat <message>
    Used to talk to the chat bot by sending a message, and then the bot replies.
    If no message is sent then the bot responds with 'Hello there!'
    :param ctx: context of the client
    :param message: message user sends the bot
    """
    if len(message) == 0:
        await ctx.send("Hello there! Send me a message after the command: /obichat message")
    else:
        # message is a tuple of variable length where each word is an index and must be joined into one string
        message_str = ' '.join(message)
        response = model.chat(message_str)
        await ctx.send(response)


# command ob!talk
@client.command(pass_context=True)
async def talk(ctx):
    """
    Use case: ob!talk
    Used for obiwan to talk in the voice channel the user is currently connected to
    :param ctx: context of the call
    """

    # make sure user is connected to a voice chat
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
        await channel.connect()

    # set of urls for the bot to choose from
    urls = [
            'https://www.youtube.com/watch?v=iIQUrrbNW_Q&ab_channel=QuoteTheGuy',
            'https://www.youtube.com/watch?v=58JwbQCnpmA&list=PLlrQRD4Rfv_CM6byFKlMYeBWAs9dWDm_7&index=2&ab_channel=QuoteTheGuy',
            'https://www.youtube.com/watch?v=Xzbyp8rjGLU&list=PLlrQRD4Rfv_CM6byFKlMYeBWAs9dWDm_7&index=10&ab_channel=QuoteTheGuy',
            'https://www.youtube.com/watch?v=Pqn3zMghf4A&list=PLlrQRD4Rfv_CM6byFKlMYeBWAs9dWDm_7&index=21&ab_channel=QuoteTheGuy',
            'https://www.youtube.com/watch?v=aNmZ9U8lE6g&list=PLlrQRD4Rfv_CM6byFKlMYeBWAs9dWDm_7&index=36&ab_channel=QuoteTheGuy',
            'https://www.youtube.com/watch?v=41hvkx77nAU&list=PLlrQRD4Rfv_CVrEGTWM3r9EZa3jYUXs0N&index=5&ab_channel=QuoteTheGuy',
            'https://www.youtube.com/watch?v=LH2-Ha6PgpA&list=PLlrQRD4Rfv_CVrEGTWM3r9EZa3jYUXs0N&index=35&ab_channel=QuoteTheGuy',
            'https://www.youtube.com/watch?v=v-iDFxFC_9E&list=PLlrQRD4Rfv_CVrEGTWM3r9EZa3jYUXs0N&index=36&ab_channel=QuoteTheGuy',
            'https://www.youtube.com/watch?v=frszEJb0aOo&list=PLlrQRD4Rfv_CNLUjhLBJg_pUfq207fPyD&index=7&ab_channel=QuoteTheGuy',
            'https://www.youtube.com/watch?v=BOvcSLpOp4o&list=PLlrQRD4Rfv_CNLUjhLBJg_pUfq207fPyD&index=8&ab_channel=QuoteTheGuy',
            'https://www.youtube.com/watch?v=37Q0fx5r-H8&list=PLlrQRD4Rfv_CNLUjhLBJg_pUfq207fPyD&index=15&ab_channel=QuoteTheGuy',
            'https://www.youtube.com/watch?v=jBOMlWl7fFk&list=PLlrQRD4Rfv_CNLUjhLBJg_pUfq207fPyD&index=17&ab_channel=QuoteTheGuy',
            'https://www.youtube.com/watch?v=J0BciHfsU7k&list=PLlrQRD4Rfv_CNLUjhLBJg_pUfq207fPyD&index=22&ab_channel=QuoteTheGuy'
            ]

    # select a random url
    i = random.randint(0, len(urls)-1)
    url = urls[i]

    voice_channel = ctx.message.guild.voice_client

    player = await YTDLSource.from_url(url, loop=client.loop)

    voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    # don't have bot disconnect before it finishes
    while voice_channel.is_playing():
        sleep(1)

    if voice_channel.is_connected():
        await voice_channel.disconnect()


# command ob!sjj
@client.command()
async def sjj(ctx, num_players=5):
    """
    Use case: ob!sjj <num_players>
    Used to start a game of secret jar jar.
    The game begins when all players reacted to the message to join.
    :param ctx: context of the command
    :param num_players: number of players to join. Must be >= 5
    """
    # minimum number of players is 5
    if num_players < 5:
        await ctx.send('How did this happen, we\'re smarter than this! The number of players must be greater than 5')
        return
    game = SecretJarJar([num_players])

# run bot
client.run(token)
