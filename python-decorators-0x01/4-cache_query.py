import sqlite3
import functools

query_cache = {}


def with_db_connection(func):
    """Decorator to open and close a database connection"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")

        result = func(conn, *args, **kwargs)
        conn.close()

        return result

    return wrapper


def cache_query(func):
    """Decorator to cache the results of queries based on SQL query string"""

    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        if query in query_cache:
            print("Using cached result for query:", query)
            return query_cache[query]

        result = func(conn, query, *args, **kwargs)

        query_cache[query] = result

        print("Query executed and cached:", query)
        return result

    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


users = fetch_users_with_cache(query="SELECT * FROM users")

users_again = fetch_users_with_cache(query="SELECT * FROM users")
