#!/usr/bin/python3
"""This script start flask web application"""
from flask import Flask

hello_route = Flask(__name__)


@hello_route.route('/', strict_slashes=False)
def Hello_hbnb():
    """This function return "Hello HBNB!" to
    http client"""
    return "Hello HBNB!"


if __name__ == "__main__":
    hello_route.run(host='0.0.0.0', port=5000, debug=True)
