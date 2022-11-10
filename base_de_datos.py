import sqlite3

conn = sqlite3.connect("database.sqlite")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS people (name TEXT, age NUMERIC, dni NUMERIC)")

cursor.execute('INSERT INTO people VALUES ("pedro" , 12, 23232323)')
cursor.execute('INSERT INTO people VALUES ("coco" , 12, 23232323)')
cursor.execute('INSERT INTO people VALUES ("papa" , 12, 23232323)')
conn.commit()
conn.close()

