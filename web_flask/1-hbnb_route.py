#!/usr/bin/python3
"""
Python Script that prepares a Flask web app
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """
    Display message on the terminal
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
    Display HBNB
    """
    return 'HBNB'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
