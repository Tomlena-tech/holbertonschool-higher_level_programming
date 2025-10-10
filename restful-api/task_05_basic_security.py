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
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"



@app.route("/login", methods=["POST"])
def login():
    """Route de connexion pour obtenir un token JWT"""
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 401
    
    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401
    
    if not check_password_hash(users[username]['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401
    
    additional_claims = {"role": users[username]["role"]}
    access_token = create_access_token(
        identity=username,  # ← String uniquement !
        additional_claims={"role": users[username]["role"]}  # ← Dictionnaire avec les rôles
    )
    
    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()  
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()  
def admin_only():
    current_user = get_jwt_identity()
    user_role = users[current_user]['role']
    if user_role != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    
    return "Admin Access Granted"










if __name__ == "__main__":
    PORT = 5000
    print(f'Server running on port {PORT}')
    app.run(host='', port=PORT)
