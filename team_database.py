import sqlite3

def get_team_A_point(user_name):
    conn = sqlite3.connect("team_A_point.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_name TEXT PRIMARY KEY,
                    personal_score INTEGER
                )''')
    
    conn.commit()

    cursor.execute('SELECT personal_score FROM users WHERE user_name = ?',(user_name,))
    data = cursor.fetchone()

    return data

def get_team_B_point(user_name):
    conn = sqlite3.connect("team_B_point.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_name TEXT PRIMARY KEY,
                    personal_score INTEGER
                )''')
    
    conn.commit()

    cursor.execute('SELECT personal_score FROM users WHERE user_name = ?',(user_name,))
    data = cursor.fetchone()

    return data

def add_team_A_point(user_name, personal_score):
    conn = sqlite3.connect('team_A_point.db')
    cursor = conn.cursor()

    # ユーザーが既に存在するか確認
    existing_user = get_team_A_point(user_name)

    if existing_user:
        # ユーザーが既に存在する場合は更新
        update_team_A_point(user_name, existing_user[0] + personal_score)
    else:
        # ユーザーが存在しない場合は新しく追加
        cursor.execute('INSERT INTO users (user_name, personal_score) VALUES (?, ?)', (user_name, personal_score))
    conn.commit()
    conn.close()

def add_team_B_point(user_name, personal_score):
    conn = sqlite3.connect('team_B_point.db')
    cursor = conn.cursor()

    # ユーザーが既に存在するか確認
    existing_user = get_team_B_point(user_name)

    if existing_user:
        # ユーザーが既に存在する場合は更新
        update_team_B_point(user_name, existing_user[0] + personal_score)
    else:
        # ユーザーが存在しない場合は新しく追加
        cursor.execute('INSERT INTO users (user_name, personal_score) VALUES (?, ?)', (user_name, personal_score))
    conn.commit()
    conn.close()

def update_team_A_point(user_name, personal_score):
    conn = sqlite3.connect('team_A_point.db')
    cursor = conn.cursor()

    # ユーザー情報を更新
    cursor.execute('UPDATE users SET personal_score = ? WHERE user_name = ?', (personal_score, user_name))

    conn.commit()
    conn.close()

def update_team_B_point(user_name, personal_score):
    conn = sqlite3.connect('team_B_point.db')
    cursor = conn.cursor()

    # ユーザー情報を更新
    cursor.execute('UPDATE users SET personal_score = ? WHERE user_name = ?', (personal_score, user_name))

    conn.commit()
    conn.close()

def reset_team_A_database():
    conn = sqlite3.connect('team_A_point.db')
    cursor = conn.cursor()

    # テーブルが存在する場合、データを削除
    cursor.execute('DELETE FROM users')

    conn.commit()
    conn.close()

def reset_team_B_database():
    conn = sqlite3.connect('team_B_point.db')
    cursor = conn.cursor()

    # テーブルが存在する場合、データを削除
    cursor.execute('DELETE FROM users')

    conn.commit()
    conn.close()