import mysql.connector


def stream_users_in_batches(batch_size):
    """
    Fetch users from the database in batches.
    Yields each batch of users as a list of dictionaries.
    """
    cnx = mysql.connector.connect(
        user="root", password="root", database="ALX_prodev"
    )
    cursor = cnx.cursor()
    cursor.execute("SELECT user_id, name, email, age FROM user_data")

    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        yield [
            {
                "user_id": row[0],
                "name": row[1],
                "email": row[2],
                "age": int(row[3]),
            }
            for row in batch
        ]

    cursor.close()
    cnx.close()


def batch_processing(batch_size):
    """
    Processes each batch of users to filter those over age 25.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user["age"] > 25:
                print(user)
