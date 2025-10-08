#!/usr/bin/env/python3
""" Develop a simple API using Python with the Flask framework"""


import json

from flask import Flask
app = Flask(__name__)

def home():
     if self.path == "/" or self.path == "":
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Welcome to the Flask API!")
        
if __name__ == "__main__": app.run()        
