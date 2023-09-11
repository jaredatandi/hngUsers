#!/usr/bin/env python3
"""Main views
"""
from flask import jsonify, abort
from views import app_views

@app_views.route('/stats', strict_slashes=False)
def stats():
    """GET /api/stats
    return:
       - the number of each objects
    """
    from models.person import Person 
    stats = {}
    stats['users'] = Person.count()
    return jsonify(stats)
