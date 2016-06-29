import sqlite3

conn = sqlite3.connect('flaskr.db')

cursor = conn.cursor()

cursor.execute('insert into entries (title, text) values (\'zhao\',\'yufei\' )')

cursor.close()
conn.commit()
conn.close()