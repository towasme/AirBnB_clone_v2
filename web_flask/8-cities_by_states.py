#!/usr/bin/python3
""" Write a script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def print_city_list():
    """ display html """
    list_of_city = storage.all('State')
    return render_template('8-cities_by_states.html',
                           list_of_city=list_of_city)


@app.teardown_appcontext
def close_storage(self):
    """ method to close and remove session
    """
    storage.close()


if __name__ == '__main__':
    """ Web app must be listening on 0.0.0.0 port 5000 """
    app.run(host='0.0.0.0', port=5000, debug=True)
