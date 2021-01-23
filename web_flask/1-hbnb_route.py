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


if __name__ == '__main__':
    app.run(host='0.0.0.0')
