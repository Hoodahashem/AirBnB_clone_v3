#!/usr/bin/python3
""" a script that starts a Flask web application"""
from flask import Flask, Blueprint
from api.v1.views import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
