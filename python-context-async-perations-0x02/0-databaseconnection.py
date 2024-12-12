"""
.0-databaseconnection.py
"""

import sqlite3


class DatabaseConnection(object):
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()


# Example
db_name = "User_data"
with DatabaseConnection(db_name) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    for user in results:
        print(user)
