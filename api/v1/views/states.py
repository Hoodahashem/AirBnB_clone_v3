#!/usr/bin/python3
"""State object view """
from flask import Flask, jsonify, request, Response
from flask import abort
from models.state import State
from models import storage
from api.v1.views import app_views


@app_views.route("/states", strict_slashes=False,  methods=['GET'])
def states():
    """retrieve State object(s)"""
    state_list = []
    all_states = storage.all(State)
    for k, v in all_states.items():
        state_list.append(v.to_dict())
    return jsonify(state_list)
