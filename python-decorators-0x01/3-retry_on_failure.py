import time
import sqlite3
import functools


def with_db_connection(func):
    """Decorator to open and close a database connection"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")

        result = func(conn, *args, **kwargs)

        conn.close()

        return result

    return wrapper


def retry_on_failure(retries=3, delay=2):
    """Decorator to retry a function if it raises an exception"""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(
                        f"Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds..."
                    )
                    time.sleep(delay)  # Wait before retrying
            print(f"All {retries} attempts failed.")
            raise last_exception

        return wrapper

    return decorator


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


# Attempt to fetch users with automatic retry on failure
try:
    users = fetch_users_with_retry()
    print(users)
except Exception as e:
    print(f"Final error after retries: {e}")