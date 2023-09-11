#!/usr/bin/env python3
"""
CRUD operation for user
"""
from flask import request, jsonify


persons = [
    {"id": 1, "name": "John", "age": 30, "email": "john@example.com"},
    {"id": 2, "name": "Joe", "age": 20, "email": "joe@example.com"},
]

class Person:
    def __init__(self, id, name, age, email) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.age = age
        
    def create_person():
        """CREATE person
           /api

        Returns:
            str: person create 
        """
        try:
            data = request.json
        except Exception as e:
            data = None
        if data is None:
            error_msg = "Wrong format"
        if error_msg is None and data.get("email", "") == "":
            error_msg = "email missin"
        if error_msg is None and data.get("password", "") == "":
            error_msg = "Password missing"
        if error_msg is None:
            try:
                new_person = {
                    "id": len(persons) + 1,
                    "name": data["name"],
                    "age": data["age"],
                "email": data["email"]
                }

                persons.append(new_person)
            except Exception as e:
                error_msg = "Can't create a new User: {}".format(e)
        return jsonify(new_person), 201
    
    def get_person(user_id):
        """GET person
           /api/user_id

        Args:
            user_id (int): id number on the db 

        Returns:
            str: fetched person 
        """
        person = next((p for p in persons if p["id"] == user_id), None)
        if person:
            return jsonify(person)
        return jsonify({"message": "Person does not exist"})

    def update_person(user_id):
        """UPDATE person
           /api/user_id

        Args:
            user_id (int): id number on DB 

        Returns:
            str: updated person 
        """
        data = request.json
        person = next((p for p in persons if p["id"] == user_id), None)
        if person:
            person["name"] = data["name"]
            person["age"] = data["age"]
            person["email"] = data["email"]
            return jsonify(person)
        return jsonify({"message": "Person not found"})

    def delete_person(user_id):
        """DELETE person
           /api/user_id

        Args:
            user_id (int): id of the person on DB 

        Returns:
            str: success message
        """
        person = next((p for p in persons if p["id"] == user_id), None)
        if person:
            person.remove(person)
            return jsonify({"message": "Person deleted successfully"})
       
        