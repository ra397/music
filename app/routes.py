from __future__ import print_function
from crypt import methods
from fileinput import close
import sqlite3
from app import app
from flask import render_template, request, redirect, url_for, abort, session
import sys

def connect_to_db():
    conn = sqlite3.connect('app.db')
    return conn

@app.route('/', methods=['Get', 'POST'])
@app.route('/login', methods=['Get', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        session['password'] = request.form.get('password')

        # check if username exists, then check if password matches
        db = connect_to_db()
        cur = db.cursor()
        cur.execute(f"SELECT USERNAME FROM USERS WHERE USERNAME='{session['username']}' AND PASSWORD='{session['password']}';")
        if cur.fetchone():
            return redirect(url_for('main'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/register', methods=['Get', 'POST'])
def register():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        session['password1'] = request.form.get('password1')
        session['password2'] = request.form.get('password2')

        # authenticate that username is unique and that passwords match
        db = connect_to_db()
        cur = db.cursor()
        unique = db.execute("SELECT USERNAME FROM USERS WHERE USERNAME=?;", [session['username']]).fetchall()
        if len(unique) == 0 and session['password1'] == session['password2']:
            cur.execute("INSERT INTO USERS (USERNAME, PASSWORD) VALUES(?,?)", (session['username'], session['password1']))
            db.commit()
            db.close()
            return redirect(url_for('main'))
        else:
            return redirect(url_for('register'))
    return render_template('register.html')


@app.route('/main', methods=['Get', 'POST'])
def main():
    # verify user is logged in before tring to access main
    if session.get('username') == None:
        return redirect(url_for('login'))
    if request.method == 'POST':
        url = request.form.get('url')
        title = request.form.get('title')
        db = connect_to_db()
        cur = db.cursor()
        cur.execute('INSERT INTO SONGS (USERNAME, TITLE, URL) VALUES(?,?,?)', (session['username'], title, url))
        db.commit()
        db.close()

    db = connect_to_db()
    cur = db.cursor()
    songs = cur.execute('SELECT TITLE, URL FROM SONGS WHERE USERNAME=?', [session['username']]).fetchall()
    db.close()
    return render_template('main.html', songs=songs)

@app.route('/logout')
def logout():
     # remove the username from the session if it's there
    session.pop('username', None)
    session.pop('password', None)
    session.pop('password1', None)
    session.pop('password2', None)

    return redirect(url_for('login'))