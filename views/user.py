#!/usr/bin/env python3
"""Module of User views
"""
from flask import abort, jsonify, request
from views import app_views
from models.person import Person


@app_views.route('/<user_id>', methods=['GET'], strict_slashes=False)
def view_a_user(user_id):
    """GET /api/:id

    Path parameter:
        - User ID
    Return:
        - User object in JSON rep
        - 404 if not found
    """
    if user_id is None:
        abort(404)
    user = Person.get_person(user_id) 

@app_views.route('/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """DELETE /api/:id
    Path parameter:
        - User ID
    Return:
        - 404 if user not found
    """
    if user_id is None:
       abort(404) 
    user = Person.delete_person(user_id)

@app_views.route('/', methods=['POST'], strict_slashes=False)
def create_user():
    """POST /api/
    """
    user = Person.create_person()

@app_views.route('/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """PUT /api/:id
    Args:
        user_id (_type_): _description_
    """
    rj = None
    if user_id is None:
        abort(404)
    user = Person.get_person(user_id)
    if user is None:
        abort(404)
    # Request json (rj)
    try:
        rj = request.json()
    except Exception as e:
        rj = None
    if rj is None:
        return jsonify({'Error': "Wrong format"}), 400
    user = Person.update_person(user_id)
    