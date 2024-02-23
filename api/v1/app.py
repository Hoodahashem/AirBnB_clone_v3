#!/usr/bin/python3
from flask import Flask, blueprints
from models import storage
from views import app_views
import os
HBNB_API_HOST = os.getenv('HBNB_API_HOST')
HBNB_API_PORT = os.getenv('HBNB_API_PORT')


if HBNB_API_HOST is None:
    HBNB_API_HOST = '0.0.0.0'
if HBNB_API_PORT is None:
    HBNB_API_PORT = 5000


app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_db(exception):
    """teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
