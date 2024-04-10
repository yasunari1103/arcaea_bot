import discord
from discord.ext import commands
intents=discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)
from TOKEN import TOKEN

@client.command()
async def send_message(ctx):
    message_list = [
        '"[X]"',
        '"Chronicle"',
        '"Climax"',
        '"Crimson Throne"',
        '"Felis"',
        '"Garakuta Doll Play"',
        '"GIMME DA BLOOD"',
        '"怒槌"',
        '"Kissing Lucifer"',
        '"Lucid Traveler"',
        '"PUPA"',
        '"Rise of the World"',
        '"Tiferet"',
        '"Valhalla:0"',
        '"γuarδina"',
        '"IMPACT"',
        '"Singularity VVVIP[BYD]"',
    ]

    for i in message_list:
        await ctx.send(i)

client.run(TOKEN)