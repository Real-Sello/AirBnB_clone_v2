#!/usr/bin/python3
"""
Python script that starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """
    display message on the terminal
    """
    return 'Hello HBNB!'


@app.route('/hbnb',)
def hbnb():
    """
    Display HBNB
    """
    return 'HBNB!'


@app.route('/c/<text>')
def c(text):
    """
    display c follow by the value
    """
    repla = text.replace('_', ' ')
    return 'C {}' .format(repla)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
