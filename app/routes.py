from crypt import methods
from app import app
from flask import render_template, request

@app.route('/login', methods=['Get', 'POST'])
def login():
    return render_template('login.html')

@app.route('/login_validation', methods=['Get', 'POST'])
def login_validation():
    username = request.form.get('username')
    password = request.form.get('password')
    return '{} \n {}'.format(username, password)

@app.route('/register', methods=['Get', 'POST'])
def register():
    return render_template('register.html')

@app.route('/main')
def main():
    return render_template('main.html')