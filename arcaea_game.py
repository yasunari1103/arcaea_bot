import discord
from discord.ext import commands
import math
import sqlite3
import time
import datetime
import asyncio
import team_database
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
    

A_team = ["yasudesu_"]
B_team = [""]

first_item_menber_list = ["kyomu1111","tns_disco","柑橘系は飲み物","fumen1024","柑橘系は飲み物","ryokuty4","bs_turtle13"]
second_item_menber_list = []
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
    now = datetime.datetime.now()
    format = '%Y/%m/%d %H:%M:%S'
    conn = sqlite3.connect('arcaea_bot/play_situation.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM playing WHERE user_name = ?',(user_name,))
    data = cursor.fetchone()    
    error_message_1 = "正確なスコアの値で入力してください"
    if data and  datetime.datetime.strptime(data[2],format) <= now <= datetime.datetime.strptime(data[3],format):
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
    else:
        await ctx.send('!start_game')
        await ctx.send('を実行してください。')

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
async def start_game(ctx):
    max_play_count = 3
    dt_now = datetime.datetime.now()
    dt_30late = dt_now + datetime.timedelta(minutes=30)
    user_name = ctx.author.name
    format = '%Y/%m/%d %H:%M:%S'
    conn = sqlite3.connect('arcaea_bot/play_situation.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS playing (
                    user_name TEXT PRIMARY KEY,
                    play_count INTEGER,
                    start_time TEXT,
                    end_time TEXT
    )""")
    conn.commit()
    cursor.execute("SELECT * FROM playing WHERE user_name = ?",(user_name,))
    data = cursor.fetchone()
    if data:
        db_now_str = data[2]
        db_later_str = data[3]
        if data[1] < max_play_count:
            if datetime.datetime.strptime(db_now_str,format) <= dt_now <= datetime.datetime.strptime(db_later_str,format):
                await ctx.send('実行中です。')
            else:
                await ctx.send(f'{user_name}さん、{dt_now}にデータベースを更新しました！\n{dt_30late}までスコアを受け付けます！')
                dt_now_str = dt_now.strftime('%Y/%m/%d %H:%M:%S')
                dt_30late_str = dt_30late.strftime('%Y/%m/%d %H:%M:%S')
                cursor.execute('UPDATE playing SET play_count = ?, start_time = ?, end_time = ? WHERE user_name = ?',(data[1]+1,dt_now_str,dt_30late_str,user_name))
                conn.commit()
                conn.close()
        if data[1] >= max_play_count:
            await ctx.send('実行可能回数に到達しています。')
    else:
        await ctx.send(f'{user_name}さん、{dt_now}にデータベースへ登録しました！\n{dt_30late}までスコアを受け付けます！')
        dt_now_str = dt_now.strftime('%Y/%m/%d %H:%M:%S')
        dt_30late_str = dt_30late.strftime('%Y/%m/%d %H:%M:%S')
        cursor.execute('INSERT INTO playing (user_name, play_count, start_time, end_time) VALUES (?,?,?,?)',(user_name,1,dt_now_str,dt_30late_str))
        conn.commit()
        conn.close()
        await ctx.send(f"{user_name}さん、データベースに登録、そして申請受け付けました！\n現在時刻{dt_now.hour}:{dt_now.minute}:{dt_now.second}から30分間、スコアを受け付けます！")
        

@client.command()
async def add_best_30(ctx,music,score):
    user_name = ctx.message.author.name
    conn = sqlite3.connect(f"{user_name}.db")
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {user_name}table (
                music TEXT PRIMARY KEY
                score INTEGER
                )''')

client.run(TOKEN)