#!/usr/bin/python3
"""
    /number/<n>: display “n is a number”
    only if n is an integer
"""


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_():
    """ close storage """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states():
    """ states """
    all_states = storage.all('State').values()
    all_states_sorted = sorted(all_states, key=lambda s: s.name)
    return render_template('7-states_list.html', all_states_sorted=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
