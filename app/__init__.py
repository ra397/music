# set up flask app and database

from distutils.log import debug
from flask import Flask
import sqlite3

db = sqlite3.connect('app.db')

# create tables
db.execute(''' CREATE TABLE IF NOT EXISTS USERS (
        USERNAME   TEXT    NOT NULL,
        PASSWORD   TEXT    NOT NULL,
        PRIMARY KEY(USERNAME)
        );''')

db.execute(''' CREATE TABLE IF NOT EXISTS SONGS (
        USERNAME   TEXT    NOT NULL,
        TITLE   TEXT    NOT NULL,
        URL   TEXT    NOT NULL
        );''')

db.close()

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

from app import routes

if __name__ == '__main__':
    app.run(debug=True)
