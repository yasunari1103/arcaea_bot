import sqlite3

conn = sqlite3.connect(f'player_detabase/yasudesu..db')
cursor = conn.cursor()
cursor.execute(f'SELECT * FROM "yasudesu.table" ORDER BY music_potential')
data = cursor.fetchone()
print(data)