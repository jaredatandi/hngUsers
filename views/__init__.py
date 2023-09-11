#!/usr/bin/env python3
"""Views intialization
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api")

from views.index import *