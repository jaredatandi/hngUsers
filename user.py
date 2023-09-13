#!/usr/bin/env python3
"""Module of User views
"""
from flask import abort,Flask, jsonify, request
import mysql.connector


# MySQL database configuration
db = mysql.connector.connect(
    host="172.17.0.2",
    user="db_user",
    password="db_password",
    database="Users"
)
cursor = db.cursor()
app = Flask(__name__)

# Endpoint to create a new person
@app.route('/api', methods=['POST'], strict_slashes=False)
def create_person():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Invalid data"}), 400

    insert_query = "INSERT INTO Users(name, age, email) VALUES (%s, %s, %s)"
    values = (data["name"], data["age"], data["email"])

    try:
        cursor.execute(insert_query, values)
        db.commit()
        new_person_id = cursor.lastrowid
        return jsonify({"id": new_person_id, "name": data["name"], "age": data["age"], "email": data["email"]}), 201
    except Exception as e:
        db.rollback()
        return jsonify({"message": "Failed to create person", "error": str(e)}), 500

# Endpoint to fetch details of a person by user ID
@app.route('/api/<int:user_id>', methods=['GET'])
def get_person(user_id):
    select_query = "SELECT * FROM Users WHERE id = %s"
    cursor.execute(select_query, (user_id,))
    person = cursor.fetchone()
    if person:
        person_data = {
            "id": person[0],
            "name": person[1],
            "age": person[2],
            "email": person[3],
        }
        return jsonify(person_data)
    return jsonify({"message": "Person not found"}), 404

# Endpoint to retrieve details of a person by name
@app.route('/api/name/<string:name>', methods=['GET'])
def get_person_by_name(name):
    if not isinstance(name, str):
        return jsonify({"Error": "name must be a string"}), 400
    select_query = "SELECT * FROM Users WHERE name = %s"
    cursor.execute(select_query, (name,))
    person = cursor.fetchone()
    if person:
        person_data = {
            "id": person[0],
            "name": person[1],
            "age": person[2],
            "email": person[3],
        }
        return jsonify(person_data)
    return jsonify({"message": "Person not found"}), 404

@app.route('/api/<string:name_or_id>', methods=['PUT'])
def update_person(name_or_id):
    data = request.get_json()
    if not data:
        return jsonify({"message": "Invalid data"}), 400

    if name_or_id.isnumeric():
        # If the name_or_id is numeric, assume it's a user_id
        user_id = int(name_or_id)
    else:
        # Otherwise, assume it's a name and perform a query to get the user_id
        select_query = "SELECT id FROM Users WHERE name = %s"
        cursor.execute(select_query, (name_or_id,))
        result = cursor.fetchone()
        if not result:
            return jsonify({"message": "Person not found"}), 404
        user_id = result[0]

    select_query = "SELECT * FROM Users WHERE id = %s"
    cursor.execute(select_query, (user_id,))
    existing_person = cursor.fetchone()

    if not existing_person:
        return jsonify({"message": "Person not found"}), 404

    update_query = "UPDATE Users SET name = %s, age = %s, email = %s WHERE id = %s"
    values = (data["name"], data["age"], data["email"], user_id)

    try:
        cursor.execute(update_query, values)
        db.commit()
        updated_person_data = {
            "id": user_id,
            "name": data["name"],
            "age": data["age"],
            "email": data["email"],
        }
        return jsonify(updated_person_data)
    except Exception as e:
        db.rollback()
        return jsonify({"message": "Failed to update person", "error": str(e)}), 500

@app.route('/api/<string:name_or_id>', methods=['DELETE'])
def delete_person(name_or_id):
    if name_or_id.isnumeric():
        # If the name_or_id is numeric, assume it's a user_id
        user_id = int(name_or_id)
    else:
        # Otherwise, assume it's a name and perform a query to get the user_id
        select_query = "SELECT id FROM Users WHERE name = %s"
        cursor.execute(select_query, (name_or_id,))
        result = cursor.fetchone()
        if not result:
            return jsonify({"message": "Person not found"}), 404
        user_id = result[0]

    select_query = "SELECT * FROM Users WHERE id = %s"
    cursor.execute(select_query, (user_id,))
    existing_person = cursor.fetchone()

    if not existing_person:
        return jsonify({"message": "Person not found"}), 404

    delete_query = "DELETE FROM Users WHERE id = %s"

    try:
        cursor.execute(delete_query, (user_id,))
        db.commit()
        return jsonify({"message": "Person deleted"})
    except Exception as e:
        db.rollback()
        return jsonify({"message": "Failed to delete person", "error": str(e)}), 500

# Close the DB connections 
@app.teardown_request
def teardown_request(exception):
    cursor.close()

if __name__ == "__main__":
    app.run(debug=True)