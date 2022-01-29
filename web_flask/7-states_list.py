#!/usr/bin/python3
"""
    /number/<n>: display “n is a number”
    only if n is an integer
"""


from flask import Flask, render_template


app = Flask(__name__)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
