import sqlite3


class DBClient:

    def __init__(self):
        self.conn = sqlite3.connect("orders.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def insert_order(self, customer):
        self.cursor.execute("INSERT INTO orders (customer) VALUES (?)", (customer,))
        self.conn.commit()

    def order_exists(self, customer):
        self.cursor.execute("SELECT * FROM orders WHERE customer=?", (customer,))
        return self.cursor.fetchone() is not None

