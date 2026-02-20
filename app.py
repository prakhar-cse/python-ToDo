import sqlite3

# conn = sqlite3.connect("todo.db")
# cursor = conn.cursor()
# cursor.execute("""CREATE TABLE IF NOT EXISTS todos(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     task TEXT NOT NULL,
#     completed INTEGER DEFAULT 0
# )""")
# conn.commit()
# conn.close()
# print("Database is initialized")


def connect():
    return sqlite3.connect("todo.db")

def add_task(task):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO todos (task) VALUES (?)",
        (task,)
    )

    conn.commit()
    conn.close()

    print("Task is added")