import sqlite3


class ExecuteQuery:
    def __init__(self, db_name, query, params):
        self.db_name = db_name
        self.query = query
        self.params = params
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.params)
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()


if __name__ == "__main__":
    db_name = "User_data.db"
    query = "SELECT * FROM users WHERE age > ?"
    params = (25,)

    with ExecuteQuery(db_name, query, params) as cursor:
        results = cursor.fetchall()
        for row in results:
            print(row)
