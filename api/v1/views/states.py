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

@app_views.route("/states/<state_id>", strict_slashes=False,  methods=['GET'])
def states_id(state_id):
    """retrieve State object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())

@app_views.route("/states/<state_id>", strict_slashes=False,  methods=['DELETE'])
def delete_state(state_id):
    """delete State object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200

@app_views.route("/states", strict_slashes=False,  methods=['POST'])
def create_state():
    """create State object"""
    state = request.get_json()
    if state is None:
        abort(400, 'Not a JSON')
    if 'name' not in state:
        abort(400, 'Missing name')
    new_state = State(**state)
    new_state.save()
    return jsonify(new_state.to_dict()), 201

@app_views.route("/states/<state_id>", strict_slashes=False,  methods=['PUT'])
def update_state(state_id):
    """update State object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    state_data = request.get_json()
    if state_data is None:
        abort(400, 'Not a JSON')
    for k, v in state_data.items():
        if k not in ['id', 'created_at', 'updated_at']:
            setattr(state, k, v)
    state.save()
    return jsonify(state.to_dict()), 200


