#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, render_template, url_for
from models import storage
import uuid


app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/0-hbnb')
def hbnb_filters(the_id=None):
    """ HBNB is alive! """
    state_objs = storage.all('State').values()
    states = dict([state.name, state] for state in state_objs)

    amenities = storage.all('Amenity').values()

    places = storage.all('Place').values()

    return render_template('0-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ FLASK """
    app.run(host=host, port=port)
