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
    if task != "":
        conn = connect()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO todos (task) VALUES (?)",
            (task,)
        )

        conn.commit()
        conn.close()

        print("Task is added")
    else:
        print("You can not add Null task")

def get_all_tasks():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM todos")
    tasks = cursor.fetchall()
    conn.close()

    print("***************ALL TASKS**************")
    for task in tasks:
        status = "Done" if task[2] else "---"
        print(f"{task[0]},      {task[1]},      {status}")

def mark_task_done(id):
    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute('UPDATE todos SET completed = 1 WHERE id = ?',
                       (id,))

        conn.commit()
        conn.close()
        print(f"Task with id- {id} is completed")

    except:
        conn.close()
        print(f"Task with id- {id} is not present")

def main():

    print("**********************************************")
    print("******************WELCOME*********************")
    print("**********************************************")

    while True:
        choice = input("Enter your action: ")
        if(choice == "1"):
            get_all_tasks()
        elif choice == "2":
            task = input("Enter task- ")
            add_task(task)
        elif choice == "3":
            get_all_tasks()
            task_id = input("Enter id of completed task: ")
            mark_task_done(task_id)
        else:
            print("Closing todo app")
            break


if __name__ == "__main__":
    main()