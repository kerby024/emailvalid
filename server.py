from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector
import md5
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "secretsecretsecret"

mysql = MySQLConnector(app, 'emailvalid')

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/success', methods=["Get","post"])
def addMail():
    add_users_query = "INSERT INTO users (email, date) VALUES (:email, NOW())"
    data = {'email': request.form['email']}
    mysql.query_db(add_users_query, data)
    # is_valid = True
    if len(request.form["email"]) == 0:
        flash("Email field is required")
        # is_valid = False
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email")
        # is_valid = False
    else:
        flash ('You successfully logged in')
    
    all_query = "SELECT * FROM users"
    users = mysql.query_db(all_query)
    
    return render_template('success.html', context=users)

app.run(debug=True)