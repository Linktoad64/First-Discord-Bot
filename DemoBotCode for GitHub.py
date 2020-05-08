import discord
from discord.utils import get
from discord.ext import commands
client = discord.Client()
commands.Bot(command_prefix="!", pm_help=None, case_insensitive=False)


bot = commands.Bot(command_prefix=prefix, pm_help=None,
                   case_insensitive=False)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    serverid = "708101352890302475"
    channelid = "708132297563570227"
    server = bot.get_server(serverid)
    await bot.send_message(bot.get_channel(channelid), "Test")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!status'):
        await message.channel.send('Operational')

    if message.content.startswith('!hello'):
        await message.channel.send('You have my attention. Now what?')

    if message.content.startswith('!help'):
        await message.channel.send('If you would like to see a list of avalible commands, see the owner of this bot, or the Google Doc.')

    if message.content.startswith('why'):
        await message.channel.send('Why not?')


    if message.content.startswith('Why is the bot named that?'):
        await message.channel.send('Because my creator had a chicken at a friends house, but they ate it. I am named for that chicken.')
        

    if message.content.startswith('What does the bot do?'):
        await message.channel.send('Nothing. At all. Except reply with sarcastic comments.')

    if message.content.endswith('/sarc'):
        await message.channel.send('/sarc Means sarcasm intended, or is used to indicate that the writer of the comment in question intended for it to be spoken sarcastically, if it was to be spoken.')
        




    

client.run("INSERT YOUR TOKEN HERE")
