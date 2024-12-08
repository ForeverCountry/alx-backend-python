import mysql.connector


def stream_user_ages():
    """
    Generator that yields user ages one by one from the database.
    """
    connection = mysql.connector.connect(
        user="root", password="root", database="ALX_prodev"
    )
    cursor = connection.cursor()

    cursor.execute("SELECT age FROM user_data")
    for age in cursor.fetchall():
        yield age[0]

    connection.close()


def calculate_average_age():
    """
    Function that calculates the average age using the stream_user_ages generator.
    """
    total_age = 0
    user_count = 0

    for age in stream_user_ages():
        total_age += age
        user_count += 1

    if user_count == 0:
        return 0

    return total_age / user_count


if __name__ == "__main__":
    average_age = calculate_average_age()
    print(f"Average age of users: {average_age:.2f}")
