#!/usr/bin/env/python3
""" Develop a simple API using Python with the Flask framework"""



from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Flask API!'

@app.route('/data', methods=['GET'])
def get_data():
    data = users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
