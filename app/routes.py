from __future__ import print_function # In python 2.7
from crypt import methods
from app import app
from flask import render_template, request, redirect, url_for
from app import get_db_connection
import sys

@app.route('/login', methods=['Get', 'POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['Get', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        # authenticate that username is unique and that passwords match
        conn = get_db_connection()
        users = conn.execute('SELECT * FROM users WHERE username = "{}";'.format(username)).fetchall()
        if len(users) == 0 and password1 == password2:
            conn.execute("INSERT INTO users (username, password) VALUES ('{}', '{}')".format(username, password1)).fetchall()
            conn.close()
            return redirect(url_for('main'))

    return render_template('register.html')

@app.route('/main')
def main():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users;').fetchall()
    conn.close()
    return render_template('main.html', users=users)