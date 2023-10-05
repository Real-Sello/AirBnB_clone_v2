#!/usr/bin/python3
"""
Python script that list all states
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__, template_folder="templates")
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnb_filters():
    """
    Displays a HTML page that lists all filters
    """
    states = storage.all('State')
    amenities = storage.all('Amenity')

    return render_template('10-hbnb_filters.html',
                           states=states, amens=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """
     Removes current session after each request
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
