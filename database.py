import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("tasks.db", check_same_thread=False)
        self.create_table()

    def create_table(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT)")

    def save_task(self, task):
        self.conn.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        self.conn.commit()

    def get_tasks(self):
        cursor = self.conn.execute("SELECT * FROM tasks")
        return [{"id": row[0], "task": row[1]} for row in cursor]
