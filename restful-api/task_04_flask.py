#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"

@app.route("/data", methods=["GET"])
def data():
    return jsonify(list(users.keys()))

@app.route("/status", methods=["GET"])
def status():
    return "OK"

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json(silent=True) or {}
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    users[data["username"]] = data
    return jsonify({"message": "User added", "user": data}), 201

