#!/usr/bin/python3
"""
simple web  app
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """returning a message"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returning a mesg"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """returning a text"""
    spaced = text.replace("_", " ")
    return 'C {}'.format(spaced)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def text_python(text="is cool"):
    """returning a text"""
    spaced = text.replace("_", " ")
    return 'Python {}'.format(spaced)


@app.route('/number/<int:n>', strict_slashes=False)
def numb(n):
    """returning an int"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
