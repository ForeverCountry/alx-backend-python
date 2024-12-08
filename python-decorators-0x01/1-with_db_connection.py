import sqlite3


def with_db_connection(func):
    """Decorator to open and close a database connection"""

    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")

        result = func(conn, *args, **kwargs)

        conn.close()

        return result

    return wrapper


@with_db_connection
def get_user_by_id(conn, user_id):
    """Fetch a user by ID from the database"""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()


# Fetch user by ID with automatic connection handling
user = get_user_by_id(user_id=1)
print(user)