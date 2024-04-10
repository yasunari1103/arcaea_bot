import discord
from discord.ext import commands
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
import math
import sqlite3
import team_database
import random
import asyncio
from arcaea_music_list import music_list
from TOKEN import TOKEN
intents=discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)

async def get_username_by_user_id(guild, user_name):
    # ギルド内のメンバーを取得
    members = guild.members

    # ユーザーIDが一致するメンバーを検索
    for member in members:
        if member.id == user_name:
            return member.name

async def get_user_id_by_username(guild, username):
    # ギルド内のすべてのメンバーを取得
    members = guild.members

    # ユーザーネームが一致するメンバーを検索
    for member in members:
        if member.name == username:
            return int(member.id)


@client.command()
async def MC(ctx,song):
    for key,value in music_list.items():
        if key == song:
            await ctx.send(f"{song}の譜面定数は、{value}です！")
    if not song in music_list.keys():
        await ctx.send("正しい楽曲を入力してください！")

@client.command(
    name="APR",
    aliases=["add_play_result"]
)
async def add_play_result(ctx,music,score):
    if music in music_list:
        music_const: float = music_list[music]
        score = int(score)
        if score > 10000000:
            music_potential = music_const + 2.0
        if 10000000 >= score >= 9800000:
            music_potential = music_const + 2.0 -  ((10000000 - score)/200000)
        if 9800000 > score:
            music_potential = music_const + 1.0 -((9800000 - score)/300000)
        user_name: str = ctx.author.name
        conn = sqlite3.connect(f'player_detabase/{user_name}.db')
        cursor = conn.cursor()

        cursor.execute(f'''CREATE TABLE IF NOT EXISTS "{user_name}table" (
                            music TEXT UNIQUE,
                            score INTEGER,
                            music_potential REAL
                        )''')
        
        cursor.execute(f'SELECT * FROM "{user_name}table" WHERE music = ?',(music,))
        existing_data = cursor.fetchone()

        if not existing_data:
            cursor.execute(f'INSERT INTO "{user_name}table" (music, score, music_potential) VALUES (?,?,?)',(music,score,music_potential))
            await ctx.send(f"データベースに{music}:{score}を登録しました\n譜面別ポテンシャルは{music_potential}です")
        if existing_data and existing_data[1] < score:
            cursor.execute(f"DELETE FROM '{user_name}table' WHERE music = ?",(music,))
            cursor.execute(f'INSERT INTO "{user_name}table" (music, score, music_potential) VALUES (?,?,?)',(music,score,music_potential))
            await ctx.send(f'データベースの{music}を{score}に更新しました\n譜面別ポテンシャルは{music_potential}です')
        if existing_data and existing_data[1] >= score:
            await ctx.send(f'スコアが同じか下回っているのでデータを更新することができません')
    else:
        await ctx.send('正しい曲名を入力してください')

    conn.commit()
    conn.close()

@client.command()
async def check_best_30(ctx):
    user_name = ctx.message.author.name
    conn = sqlite3.connect(f'player_detabase/{user_name}.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM "{user_name}table" ORDER BY music_potential DESC')
    best_30_songs = cursor.fetchmany(30)
    best_30 = f"曲名=>スコア：譜面別ポテンシャル"
    best_botential = 0
    max_potential = 0
    c = 0
    for i in best_30_songs:
        best_botential += i[2]
        best_30 += f"\n{i[0]}=>{str(i[1])}：{str(round(i[2],6))}"
    for i in best_30_songs:
        max_potential += i[2]
        c += 1
        if c == 10:
            break
    await ctx.send(f"{best_30}\nベスト枠のポテンシャルは{round(best_botential / 30,6)}\nベスト更新無しで到達可能なポテンシャルは{round((best_botential + max_potential) / 40,6)}")

@client.command()
async def check_potential(ctx,music,score):
    music_const: float = music_list[music]
    score = int(score)
    if score > 10000000:
        music_potential = music_const + 2.0
    if 10000000 >= score >= 9800000:
        music_potential = music_const + 2.0 -  ((10000000 - score)/200000)
    if 9800000 > score:
        music_potential = music_const + 1.0 -((9800000 - score)/300000)
    await ctx.send(f'{music}で{score}を達成した場合、譜面別ポテンシャルは{music_potential}です！')

@client.command()
async def const_quiz(ctx):
    random_music = random.choice(list(music_list.keys()))
    correct_const = music_list[random_music]
    message = await ctx.send(f'{random_music}の定数はいくつでしょう？')
    def check(reply):
        return reply.channel == ctx.message.channel and reply.reference and reply.reference.message_id == message.id
    try:
        while True:
            reply = await client.wait_for('message', check=check, timeout=10)  # 30秒間リプライを待機
            try:
                guessed_const = float(reply.content.strip())
            except ValueError:
                await ctx.send('数字を入力してください。')
                continue

            if guessed_const == correct_const:
                await ctx.send(f'正解です！({correct_const})')
                break
            else:
                await ctx.send(f'不正解です。')
    except asyncio.TimeoutError:
        await ctx.send(f'時間切れです\n正解は {correct_const} です。')

client.run(TOKEN)