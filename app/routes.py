from crypt import methods
from app import app
from flask import render_template, request
from app import get_db_connection

@app.route('/login', methods=['Get', 'POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['Get', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        return '{} \n {} \n {}'.format(username, password1, password2)
    # authenticate that username is unique and that 
    return render_template('register.html')

@app.route('/main')
def main():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()

    return render_template('main.html', users=users)