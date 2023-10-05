#!/usr/bin/python3
"""
Python script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__, template_folder="templates")
app.url_map.strict_slashes = False


@app.route('/states')
def states():
    """
    Display a new HTML page
    """
    states = storage.all('State')
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def states_id(id):
    """
    Display a HTML page with all states
    """
    states = storage.all('State')
    if "State." + id in states:
        for key, value in states.items():
            if id in key:
                name = value.name
                city_dict = value.cities
    else:
        return render_template('9-states.html', els=True)
    return render_template('9-states.html', cities=city_dict,
                           id=id, name=name)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Remove the current session after each request
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
