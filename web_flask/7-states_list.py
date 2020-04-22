#!/usr/bin/python3
""" Flask Script """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """ list the states in html"""
    list_s = storage.all('State')
    return render_template('7-states_list.html', list_s=list_s)


@app.teardown_appcontext
def storage_close(self):
    """ closes storage """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
