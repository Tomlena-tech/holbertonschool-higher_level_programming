#!/usr/bin/env python3
""" Develop a simple API using Python with the Flask framework"""

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}

@app.route('/')
def home():
    return 'Welcome to the Flask API!'

@app.route('/status')
def status():
    return jsonify({"status": "OK"})

@app.route('/data')
def data():
    return jsonify(list(users.keys()))

@app.route('/users')
def get_all_users():
    return jsonify(users)

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data['username']
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
