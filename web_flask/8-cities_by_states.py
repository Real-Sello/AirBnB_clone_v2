#!/usr/bin/python3
"""
Python script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__, template_folder="templates")
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """
    Displays a new HTML page with all states
    """
    new_dict = storage.all('State')
    return render_template('8-cities_by_states.html', states=new_dict)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Removes the current session after each request
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
