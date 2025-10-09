#!/usr/bin/env/python3
""" Develop a simple API using Python with the Flask framework"""



from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}
  
@app.route('/', methods=['GET'])
def home():
    return 'Welcome to the Flask API!'

@app.route('/data', methods=['GET'])
def data():
    return jsonify(list(users.keys()))

@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(users)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})

@app.route('/users/<username>',methods=['GET'])
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404
    
@app.route('/add_user', methods=['POST'])
def add_user(): # New endpoint to add a user
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data['username']
    users[username] = data
    return jsonify({"message": "User added","user": data}), 201
    


if __name__ == "__main__":
    app.run(debug=True, port= 8000)
