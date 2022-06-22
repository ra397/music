import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()


# to register a new user: 
cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
            ('rabi', 'secret')
            )

            
connection.commit()
connection.close()
