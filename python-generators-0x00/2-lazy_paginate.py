seed = __import__("seed")


def paginate_users(page_size, offset):
    """
    Function to fetch a page of users from the database.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}"
    )
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_paginate(page_size):
    """
    Generator that lazily loads pages of users from the database.
    It will only fetch the next page when needed.
    """
    offset = 0  # Start with the first page

    while True:
        users = paginate_users(page_size, offset)

        if not users:
            break

        yield users

        offset += page_size
