#!/usr/bin/python3
from flask import Flask, Blueprint
from views import app_views

@app_views.route('/status', strict_slashes=False)
def status():
    """Return status"""
    return {"status": "OK"}
