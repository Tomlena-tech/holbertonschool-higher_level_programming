#!/usr/bin/env/python3
""" Develop a simple API using Python with the Flask framework"""



from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}
  
@app.route('/')
def home():
    return 'Welcome to the Flask API!'

@app.route('/data')
def get_data():
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route('/users')
def get_all_users():
    return jsonify(users)

@app.route('/status')
def status():
    return jsonify({"status": "OK"})

@app.route('/users/<username>')
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404
    
@app.route('/add_user', methods=['POST'])
def add_user(): # New endpoint to add a user
    user_data = request.get_json()
    username = user_data.get('username')

    if not username:
        return jsonify({"error": "Username and info are required"}), 400
    
    users[username] = user_data # Add the new user to the dictionary
    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201
    



if __name__ == "__main__":
    app.run(debug=True, port= 8000)
