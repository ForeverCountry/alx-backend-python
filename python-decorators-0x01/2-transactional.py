import sqlite3


def with_db_connection(func):
    """Decorator to open and close a database connection"""

    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")

        result = func(conn, *args, **kwargs)

        conn.close()

        return result

    return wrapper


def transactional(func):
    """Decorator to ensure the function is wrapped inside a transaction"""

    def wrapper(conn, *args, **kwargs):
        try:
            conn.isolation_level = None

            result = func(conn, *args, **kwargs)

            conn.commit()

            return result

        except Exception as e:
            print(f"Error: {e}. Rolling back transaction.")
            conn.rollback()
            raise

    return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)
    )


# Fetch user and update email with automatic transaction handling
update_user_email(user_id=1, new_email="Crawford_Cartwright@hotmail.com")
