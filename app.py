import sqlite3

conn = sqlite3.connect("todo.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS todos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    completed INTEGER DEFAULT 0
)""")

conn.commit()
conn.close()

print("Database is initialized")