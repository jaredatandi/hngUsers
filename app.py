#!/usr/bin/env ptyhon3
"""Routing module for the api
"""
from views import app_views
from flask import  Flask

app = Flask(__name__)
app.register_blueprint(app_views)

if __name__ == "__main__":
    app.run()