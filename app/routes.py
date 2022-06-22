from flask import render_template, request, session, redirect, url_for
from app import app, db
from app.models import User


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # get data from html elements
        username = request.form['username']
        password = request.form['password']
        
        # authenticate user
        
        
        return redirect(url_for('login'))

    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/main")
def main():
    return render_template('main.html')