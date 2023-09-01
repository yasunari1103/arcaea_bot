import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
groupA = []
groupB = []

@client.command()
async def join_group(ctx,group):
    if group == "A":
        groupA.append(ctx.message.author.name)
        await ctx.send(f"{ctx.message.author.name}はAチームに所属されました")
    if group == "B":
        groupB.append(ctx.message.author.name)
        await ctx.send(f"{ctx.message.author.name}はBチームに所属されました")

@client.command()
async def AB_point(ctx,point,constant):
    new_constant = int(constant.replace(".","")) / 10
    new_point = int(point)
    A = 0
    B = 0
    if ctx.message.author.name in groupA:
        A += new_point * new_constant
        await ctx.send(f"Aチームに{new_point * new_constant}ポイント追加しました")
    if ctx.message.author.name in groupB:
        B += new_point * new_constant
        await ctx.send(f"Bチームに{new_point * new_constant}ポイント追加しました")

client.run('トークン')