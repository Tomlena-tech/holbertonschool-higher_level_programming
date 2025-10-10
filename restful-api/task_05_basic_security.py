#!/usr/bin/env python3
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}
app.config['JWT_SECRET_KEY'] = 'votre-cle-secrete-super-securisee'
jwt = JWTManager(app)

auth = HTTPBasicAuth()

hashed_password = generate_password_hash("mysecretpassword")
print(f"Hashed password: {hashed_password}")

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None



@app.route("/basic-protected", methods=["GET"])
def basic_protected():
    return "Basic Auth: Access Granted"



@app.route("/login", methods=["POST"])
@jwt_required()
def log_user():
    return "Welcome to the Flask API!"











if __name__ == "__main__":
    PORT = 8000
    print(f'Server running on port {PORT}')
    app.run(host='', port=PORT)
