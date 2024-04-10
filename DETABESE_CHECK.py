import sqlite3

conn = sqlite3.connect('play_situation.db')
cursor = conn.cursor()
cursor.execute(f'SELECT * FROM playing')
data = cursor.fetchall()
print(data)