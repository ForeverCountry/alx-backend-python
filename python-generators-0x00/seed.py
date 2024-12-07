#!/usr/bin/python3

"""
file: seed.py
"""

import mysql.connector
import csv

DB_NAME = "ALX_prodev"
DB_USER = "root"
DB_PASS = "root"


def connect_db():
    """
    Desc: A function that connects to the database
    args: None
    returns: a connection
    """
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user=f"{DB_USER}",
            password=f"{DB_PASS}",
        )
    except mysql.connector.Error as err:
        print(f"Oops! failed to connect to mysql: {err.msg}")
    return connection


def create_database(connection):
    cur = connection.cursor()
    try:
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    except mysql.connector.Error as err:
        print(f"Failed to create database: {err.msg}")
    cur.close()


def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            user=f"{DB_USER}", password=f"{DB_PASS}", database=f"{DB_NAME}"
        )
    except mysql.connector.Error as err:
        print(f"Failed to establish connection: {err.msg}")

    return connection


def create_table(connection):
    cur = connection.cursor()
    user_data = """CREATE TABLE IF NOT EXISTS user_data (
        user_id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL(3, 0) NOT NULL
    )"""

    try:
        cur.execute(user_data)
    except mysql.connector.Error as err:
        print(err.msg)


def insert_data(connection, data):
    """
    Desc: A function to insert data into the user_data table.
    Args:
        connection: a MySQL connection object
        data: path to the CSV file containing user data
    Returns:
        None
    """
    cur = connection.cursor()

    try:
        with open(data, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]
                email = row["email"]
                age = row["age"]

                try:
                    cur.execute(
                        """
                        INSERT INTO user_data (name, email, age)
                        VALUES (%s, %s, %s)
                        """,
                        (name, email, age),
                    )
                except mysql.connector.Error as err:
                    print(f"Failed to insert row {row}: {err.msg}")
            connection.commit()
    except FileNotFoundError:
        print(f"File {data} not found.")
    except Exception as err:
        print(f"Unexpected error: {err}")
    finally:
        cur.close()
