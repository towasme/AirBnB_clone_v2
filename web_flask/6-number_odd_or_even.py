#!/usr/bin/python3
# script that starts a Flask web application
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ return message """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def just_hbnb():
    """ return message """
    return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def c_is(text):
    """ return input text """
    return 'C %s' % text.replace("_", " ")


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_text(text='is_cool'):
    """ return input text """
    return 'Python %s' % text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def is_num(n):
    """ return input text """
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    """ return html """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    """ return html """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
