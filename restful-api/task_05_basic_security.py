#!/usr/bin/python3
from flask import Flask
from flask import make_response
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

SECRET_KEY = 1

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
    }

@app.route('/basic_protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"
