import discord
from discord.ext import commands
import math
import sqlite3
import team_database
from arcaea_music_list import music_list

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

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

def get_A(user_name):
    team_database.get_team_A_point(user_name)
def add_A(user_name,personal_score):
    team_database.add_team_A_point(user_name, personal_score)
def update_A(user_name, personal_score):
    team_database.update_team_A_point(user_name, personal_score)
def reset_A():
    team_database.reset_team_A_database()
def get_B(user_name):
    team_database.get_team_B_point(user_name)
def add_B(user_name,personal_score):
    team_database.add_team_B_point(user_name, personal_score)
def update_B(user_name, personal_score):
    team_database.update_team_B_point(user_name, personal_score)
def reset_B():
    team_database.reset_team_B_database()

A_team = [""]
B_team = [""]

item_menber_list = ["kyomu1111","tns_disco","柑橘系は飲み物","fumen1024","柑橘系は飲み物","ryokuty4","bs_turtle13"]
@client.command()
async def reset(ctx):
    if ctx.message.author.name == "yasudesu." or "yasudesu_":
        reset_A()
        reset_B()
        await ctx.send('データをリセットしました')


@client.command()
async def add_point(ctx,score,musical_score_constant):
    score = int(score)
    user_name = str(ctx.message.author.name)
    musical_score_constant = float(musical_score_constant)
    error_message_1 = "正確なスコアの値で入力してください"
    if user_name in A_team:
        team = "A"
        user_data = get_A(user_name)
        if user_data:
            user_name, personal_score = user_data
            if score < 0:
                await ctx.send(error_message_1)
            if score > 10002221:
                await ctx.send(error_message_1)
            if 10002221 >= score > 10000000:
                await ctx.send(f"{team}チームに{int(score * math.log(50, 20 - musical_score_constant))}ポイント加算されました！")
                personal_score += int(score * math.log(50, 20 - musical_score_constant))
                await ctx.send(f"# PMおめでとうございます！！！\n追加ポイント{5000000}ポイント獲得です！！！")
                add_A(user_name,personal_score + 5000000)
            else:
                await ctx.send(f"{team}チームに{int(score * math.log(50, 20 - musical_score_constant))}ポイント加算されました！")
                personal_score += int(score * math.log(50, 20 - musical_score_constant))
                add_A(user_name,personal_score)

        else:
            add_A(user_name,0) 
            personal_score = 0
            if score < 0:
                await ctx.send(error_message_1)
            if score > 10002221:
                await ctx.send(error_message_1)
            if 10002221 >= score > 10000000:
                await ctx.send(f"{team}チームに{int(score * math.log(50, 20 - musical_score_constant))}ポイント加算されました！")
                personal_score += int(score * math.log(50, 20 - musical_score_constant))
                await ctx.send(f"# PMおめでとうございます！！！\n# 追加ポイント{5000000}ポイント獲得です！！！")
                add_A(user_name,personal_score + 5000000)
            else:
                await ctx.send(f"{team}チームに{int(score * math.log(50, 20 - musical_score_constant))}ポイント加算されました！")
                add_A(user_name , int(score * math.log(50, 20 - musical_score_constant)))

    if user_name in B_team:
        team = "B"
        user_data = get_B(user_name)
        if user_data:
            user_name, personal_score = user_data
            if score < 0:
                await ctx.send(error_message_1)
            if score > 10002221:
                await ctx.send(error_message_1)
            if 10002221 >= score > 10000000:
                await ctx.send(f"{team}チームに{int(score * math.log(50, 20 - musical_score_constant))}ポイント加算されました！")
                personal_score += int(score * math.log(50, 20 - musical_score_constant))
                add_B(user_name,personal_score)
                await ctx.send(f"# PMおめでとうございます！！！\n追加ポイント{5000000}ポイント獲得です！！！")
                add_B(user_name,personal_score + 5000000)
            else:
                await ctx.send(f"{team}チームに{int(score * math.log(50, 20 - musical_score_constant))}ポイント加算されました！")
                personal_score += int(score * math.log(50, 20 - musical_score_constant))
                add_B(user_name,personal_score)

        else:
            add_B(user_name,0)
            personal_score = 0
            if score < 0:
                await ctx.send(error_message_1)
            if score > 10002221:
                await ctx.send(error_message_1)
            if 10002221 >= score > 10000000:
                await ctx.send(f"{team}チームに{int(score * math.log(50, 20 - musical_score_constant))}ポイント加算されました！")
                personal_score += int(score * math.log(50, 20 - musical_score_constant))
                await ctx.send(f"# PMおめでとうございます！！！\n追加ポイント{5000000}ポイント獲得です！！！")
                add_B(user_name,personal_score + 5000000)
            else:
                await ctx.send(f"{team}チームに{int(score * math.log(50, 20 - musical_score_constant))}ポイント加算されました！")
                add_B(user_name,int(score * math.log(50, 20 - musical_score_constant)))

@client.command()
async def all_score_check(ctx,team):
    if team == "A":
        conn = sqlite3.connect("team_A_point.db")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users ORDER BY personal_score DESC') 
        data = cursor.fetchall()
        send_message = []
        team_all_score = 0
        if data:
            for row in data:
                user_name = row[0]
                all_score = row[1]
                send_message.append(f"{user_name} => 総スコア:{all_score}")
                team_all_score += all_score
            # リストの要素を改行で結合して一つの文字列にする
            formatted_message = "\n".join(send_message)
            await ctx.send(formatted_message)
            await ctx.send(f"Aチームの合計点数は、{team_all_score}です！！！")
        else:
            await ctx.send('Aチームのデータが存在しません')
        # データベース接続を閉じる
        conn.close()
    
    if team == "B":
        conn = sqlite3.connect("team_B_point.db")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users ORDER BY personal_score DESC') 
        data = cursor.fetchall()
        send_message = []
        team_all_score = 0
        if data:
            for row in data:
                user_name = row[0]
                all_score = row[1]
                send_message.append(f"{user_name} => 総スコア:{all_score}")
                team_all_score += all_score
            # リストの要素を改行で結合して一つの文字列にする
            formatted_message = "\n".join(send_message)
            await ctx.send(formatted_message)
            await ctx.send(f"Bチームの合計点数は、{team_all_score}です！！！")
        else:
            await ctx.send('Bチームのデータが存在しません')
        # データベース接続を閉じる
        conn.close()

    if team == "all":
        conn = sqlite3.connect("team_A_point.db")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users ORDER BY personal_score DESC') 
        data = cursor.fetchall()
        send_message = []
        team_all_score = 0
        for row in data:
            user_name = row[0]
            all_score = row[1]
            send_message.append(f"{user_name} => 総スコア:{all_score}")
            team_all_score += all_score
        # リストの要素を改行で結合して一つの文字列にする
        formatted_message = "\n".join(send_message)
        await ctx.send(formatted_message)
        await ctx.send(f"Aチームの合計点数は、{team_all_score}です！！！")
        # データベース接続を閉じる
        conn.close()

        conn = sqlite3.connect("team_B_point.db")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users ORDER BY personal_score DESC') 
        data = cursor.fetchall()
        send_message = []
        team_all_score = 0
        for row in data:
            user_name = row[0]
            all_score = row[1]
            send_message.append(f"{user_name} => 総スコア:{all_score}")
            team_all_score += all_score
        # リストの要素を改行で結合して一つの文字列にする
        formatted_message = "\n".join(send_message)
        await ctx.send(formatted_message)
        await ctx.send(f"Bチームの合計点数は、{team_all_score}です！！！")
        # データベース接続を閉じる
        conn.close()


@client.command()
async def score_check(ctx,team):
    if team == "A":
        conn = sqlite3.connect("team_A_point.db")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users ORDER BY personal_score DESC') 
        data = cursor.fetchall()
        team_all_score = 0
        for row in data:
            user_name = row[0]
            all_score = row[1]
            team_all_score += all_score
        await ctx.send(f"Aチームの合計点数は、{team_all_score}です！！！")
        # データベース接続を閉じる
        conn.close()
    
    if team == "B":
        conn = sqlite3.connect("team_B_point.db")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users ORDER BY personal_score DESC') 
        data = cursor.fetchall()
        team_all_score = 0
        for row in data:
            user_name = row[0]
            all_score = row[1]
            team_all_score += all_score
        await ctx.send(f"Bチームの合計点数は、{team_all_score}です！！！")
        # データベース接続を閉じる
        conn.close()

    if team == "all":
        conn = sqlite3.connect("team_A_point.db")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users ORDER BY personal_score DESC') 
        data = cursor.fetchall()
        team_all_score = 0
        for row in data:
            user_name = row[0]
            all_score = row[1]
            team_all_score += all_score
        await ctx.send(f"Aチームの合計点数は、{team_all_score}です！！！")
        # データベース接続を閉じる
        conn.close()

        conn = sqlite3.connect("team_B_point.db")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users ORDER BY personal_score DESC') 
        data = cursor.fetchall()
        team_all_score = 0
        for row in data:
            user_name = row[0]
            all_score = row[1]
            team_all_score += all_score
        await ctx.send(f"Bチームの合計点数は、{team_all_score}です！！！")
        # データベース接続を閉じる
        conn.close()

@client.command()
async def MC(ctx,song):
    for key,value in music_list.items():
        if key == song:
            await ctx.send(f"{song}の譜面定数は、{value}です！")
    if not song in music_list.keys():
        await ctx.send("正しい楽曲を入力してください！")


TOKEN = 'MTEyMzY2NTU0MTgwMzAyMDMyOA.GPydZ3.BPoftKYXtUYWhvC4PYFJb3iTNmVuw3eRldCW-s'

client.run(TOKEN)