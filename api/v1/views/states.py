#!/usr/bin/python3
""" view for State objects that handles all default RestFul API actions """
from flask import jsonify, abort, request
from models import storage
from models.state import State
from api.v1.views import app_views

@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """ Retrieves the list of all State objects """
    states = storage.all(State)
    state_list = []
    for state in states.values():
        state_list.append(state.to_dict())
    return jsonify(state_list)
