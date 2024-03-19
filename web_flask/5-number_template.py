#!/usr/bin/python3
"""This script start a Flask web application
Listening on 0.0.0.0 on port 5000
with debugger on"""

from flask import Flask, render_template

number_template = Flask(__name__)


@number_template.route('/', strict_slashes=False)
def Hello_hbnb():
    """This function return "Hello HBNB!" to
    http client"""
    return "Hello HBNB!"


@number_template.route('/hbnb', strict_slashes=False)
def hbnb():
    """This return "HBNB" to http client
    The decorator above convert this function to view function
    """
    return "HBNB"


@number_template.route('/c/<text>', strict_slashes=False)
def cIsCool(text):
    """This function displasy C followed by the value of the text
    variable passed to the page"""
    return "C {}".format(text.replace("_", " "))


@number_template.route('/python', defaults={'text': 'is cool'},
                       strict_slashes=False)
@number_template.route('/python/<text>', strict_slashes=False)
def pythonRoute(text):
    """This function displays Python followed by the value of
    the text variable, replacing "_" with " ". """
    return "Python {}".format(text.replace("_", " "))


@number_template.route('/number/<int:n>', strict_slashes=False)
def number_route_page(n):
    """display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


@number_template.route('/number_template/<int:n>', strict_slashes=False)
def numTemplate(n):
    """display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY
    """
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    number_template.run(host="0.0.0.0", port=5000, debug=1)
