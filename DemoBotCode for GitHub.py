import discord
from discord.utils import get
from discord.ext import commands

bot = commands.Bot(command_prefix="!", pm_help=None,
                   case_insensitive=False)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    serverid = "708101352890302475"
    channelid = "708132297563570227"
    server = bot.get_server(serverid)
    await bot.send_message(bot.get_channel(channelid), "Test")

@bot.command
async def status(ctx):
    """This returns a message to see if the bot is running"""
    await ctx.send("Operational")


@bot.command
async def hello(ctx):
    """"This greets the bot"""
    await ctx.send("You have my attention. Now what?")

@bot.event
async def on_message(message):
    if message.content.startswith('why'):
        await message.channel.send('Why not?')


    if message.content.startswith('Why is the bot named that?'):
        await message.channel.send('Because my creator had a chicken at a friends house, but they ate it. I am named for that chicken.')
        

    if message.content.startswith('What does the bot do?'):
        await message.channel.send('Nothing. At all. Except reply with sarcastic comments.')

    if message.content.endswith('/sarc'):
        await message.channel.send('/sarc Means sarcasm intended, or is used to indicate that the writer of the comment in question intended for it to be spoken sarcastically, if it was to be spoken.')
    
    await bot.process_commands(message)        

client.run("INSERT YOUR TOKEN HERE")
