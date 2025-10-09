#!/usr/bin/env python3
"""
API Flask minimaliste – réponse parfaite au sujet Holberton
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# 1. Stockage en mémoire : clé = username, valeur = dict complet
users = {}


# 2. Route racine
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


# 3. Route /data : liste des usernames
@app.route("/data", methods=["GET"])
def data():
    return jsonify(list(users.keys()))


# 4. Route /status
@app.route("/status", methods=["GET"])
def status():
    return jsonify("OK")


# 5. Route dynamique /users/<username>
@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


# 6. Route POST /add_user
@app.route("/add_user", methods=["POST"])
def add_user():
    payload = request.get_json(silent=True) or {}
    username = payload.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = payload
    return jsonify({"message": "User added", "user": payload}), 201


# 7. Point d’entrée (inutile si tu lances avec « flask --app task_04_flask.py run »,
# mais présent pour « python task_04_flask.py »)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
