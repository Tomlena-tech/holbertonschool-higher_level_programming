#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/header')
def header():
    return render_template('header.html') 

@app.route('/footer')
def footer():
    return render_template('footer.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
