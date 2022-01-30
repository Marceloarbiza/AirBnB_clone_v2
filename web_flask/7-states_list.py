#!/usr/bin/python3
""" App Flask """

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_states():
    """Returns a html listing the states"""
    states = storage.all('State').values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
