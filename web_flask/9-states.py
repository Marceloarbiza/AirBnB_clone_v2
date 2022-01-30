#!/usr/bin/python3
""" App Flask """

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def object_state(id=None):
    """ Discplay info each state by id """
    storage_states = storage.all('State')
    if id not None:
        storage_states = storage_states[f'State.{id}']
    else:
        storage_states = None
    return render_template('9-states.html', storage_states=states,
                           id=id)


@app.teardown_appcontext
def teardown(self):
    """ close storage """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
