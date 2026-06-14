#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request

app = Flask(__name__)

#users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
         "bob": {"username": "bob"}}
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    usernames = []
    for u in users:
        usernames.append(users[u]["username"])
    return jsonify(usernames)

@app.route("/status")
def status():
    return make_response('OK')

@app.route("/users/<username>")
def user(username):
    if username not in users:
        return make_response(jsonify({"error": "User not found"}), 404)
    return jsonify(users[username])

@app.route("/add_user", methods=['POST'])
def add_user():
    try:
        data = request.get_json()
    except Exception:
        return make_response(jsonify({"error": "Invalid JSON"}), 400)
    if "username" not in data:
        return make_response(jsonify({"error": "Username is required"}), 400)
    if data["username"] in users:
        return make_response(jsonify({"error": "Username already exists"}), 409)
    users[data["username"]] = data
    return_data = {"message": "User added"}
    return_data["user"] = data
    return make_response(jsonify(data), 201)


if __name__ == "__main__":
    app.run()
