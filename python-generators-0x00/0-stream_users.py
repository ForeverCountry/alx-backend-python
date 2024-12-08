#!/usr/bin/python3

"""
file: 0-stream_users.py
"""

import mysql.connector


def stream_users():
    cnx = mysql.connector.connect(
        user="root", password="root", database="ALX_prodev"
    )
    cursor = cnx.cursor()
    cursor.execute("SELECT user_id, name, email, age FROM user_data")

    while True:
        user = cursor.fetchone()
        if user is None:
            break
        yield {
            "user_id": user[0],
            "name": user[1],
            "email": user[2],
            "age": int(user[3]),
        }
