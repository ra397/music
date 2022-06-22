from distutils.log import debug
from flask import Flask
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

from app import routes

if __name__ == '__main__':
    app.run(debug=True)
