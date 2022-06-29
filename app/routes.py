from __future__ import print_function
from crypt import methods
import sqlite3
from app import app
from flask import render_template, request, redirect, url_for, abort
import sys

def connect_to_db():
    conn = sqlite3.connect('app.db')
    return conn

current_user = None

@app.route('/login', methods=['Get', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # check if username exists, then check if password matches
        db = connect_to_db()
        cur = db.cursor()
        cur.execute(f"SELECT USERNAME FROM USERS WHERE USERNAME='{username}' AND PASSWORD='{password}';")
        if cur.fetchone():
            current_user = username
            return redirect(url_for('main'))
        else:
            abort(404)
    return render_template('login.html')

@app.route('/register', methods=['Get', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # authenticate that username is unique and that passwords match
        db = connect_to_db()
        cur = db.cursor()
        unique = db.execute("SELECT USERNAME FROM USERS WHERE USERNAME=?;", [username]).fetchall()
        if len(unique) == 0 and password1 == password2:
            cur.execute("INSERT INTO USERS (USERNAME, PASSWORD) VALUES(?,?)", (username, password1))
            db.commit()
            db.close()
            current_user = username
            return redirect(url_for('main'))
        else:
            abort(404)
    return render_template('register.html')

@app.route('/main', methods=['Get', 'POST'])
def main():
    if request.method == 'POST':
        url = request.form.get('url')
        title = request.form.get('title')
        
        # add song to my songs

    return render_template('main.html')