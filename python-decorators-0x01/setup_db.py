import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
"""
)

cursor.execute(
    """
INSERT INTO users (name, email) 
VALUES ('Maxy', 'maxy@example.com')
"""
)
cursor.execute(
    """
INSERT INTO users (name, email) 
VALUES ('Wongani', 'wongani@example.com')
"""
)

conn.commit()
conn.close()

print("Database 'users.db' set up successfully with the 'users' table!")
