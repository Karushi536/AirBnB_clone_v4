#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, render_template
import uuid

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints a Message when / is called """
    return 'Hello HBNB!'
def index():
    cache_id = uuid.uuid4()
    return render_template('1-hbnb.html', cache_id=cache_id)

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
