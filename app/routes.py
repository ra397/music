from flask import render_template, request, session, redirect, url_for
from app import app
from app.models import User

users = []
users.append(User(id=1, username='rabi', password='secret'))
users.append(User(id=2 ,username='lorena', password='secret'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        # get data from html elements
        username = request.form['username']
        password = request.form['password']
        
        # authenticate user
        try:
            user = [x for x in users if x.username == username][0]
        except:
            user = None
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('main'))

        return redirect(url_for('login'))

    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/main")
def main():
    return render_template('main.html')