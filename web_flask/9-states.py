#!/usr/bin/python3
""" App Flask """

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.rpute('/states/', strict_slashes=False)
@app.rpute('/states/<id>', strict_slashes=False)
def object_state(id=None):
    """ Discplay info each state by id """
    if id is None:
        storage_states = storage.all('State')
        return render_template('9-states.html', storage_states=states)
    else:
        storage_states = storage.all('State')
        for s in storage_states.values():
            if s.id == id:
                return render_template('9-states.html', s=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown(self):
    """ close storage """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
