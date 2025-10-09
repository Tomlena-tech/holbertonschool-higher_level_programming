#!/usr/bin/env/python3
""" Develop a simple API using Python with the Flask framework"""



from flask import Flask, jsonify

app = Flask(__name__)
users = {"Thomas": "thomas", "Alice": "est", "Bob": "un", "Eve": "âne"}

@app.route('/')
def home():
    return 'Welcome to the Flask API!'

@app.route('/data')
def get_data():
    usernames = list(users.keys())
    return jsonify(usernames)



if __name__ == "__main__":
    app.run(debug=True, port=5001)
