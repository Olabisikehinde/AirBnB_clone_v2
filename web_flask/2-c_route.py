#!/usr/bin/python3
"""This script start a Flask web application
Listening on 0.0.0.0 on port 5000
with debugger on"""

from flask import Flask

c_route = Flask(__name__)


@c_route.route('/', strict_slashes=False)
def Hello_hbnb():
    """This function return "Hello HBNB!" to
    http client"""
    return "Hello HBNB!"


@c_route.route('/hbnb', strict_slashes=False)
def hbnb():
    """This return "HBNB" to http client
    The decorator above convert this function to view function
    """
    return "HBNB"


@c_route.route('/c/<text>', strict_slashes=False)
def cIsCool(text):
    """This function displasy C followed by the value of the text
    variable passed to the page"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    c_route.run(host="0.0.0.0", port=5000, debug=1)
