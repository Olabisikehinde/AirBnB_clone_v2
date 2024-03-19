#!/usr/bin/python3
"""This script start flask web application"""
from flask import Flask

hbnb_route = Flask(__name__)


@hbnb_route.route('/', strict_slashes=False)
def Hello_hbnb():
    """This function return "Hello HBNB!" to
    http client"""
    return "Hello HBNB!"


@hbnb_route.route('/hbnb', strict_slashes=False)
def hbnb():
    """This return "HBNB" to http client
    The decorator above convert this function to view function
    """
    return "HBNB"


if __name__ == "__main__":
    hbnb_route.run(host='0.0.0.0', port=5000, debug=True)
