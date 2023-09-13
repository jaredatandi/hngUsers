import requests

# Replace with the URL of your Flask API
api_url = 'http://localhost:5000/api'

def update_person_by_name(name, data):
    try:
        # Send a PUT request to update a person by name
        response = requests.put(f'{api_url}/{name}', json=data)

        if response.status_code == 200:
            # Successful response, print the updated person details
            updated_person = response.json()
            print(f"Person updated: {updated_person}")
        elif response.status_code == 404:
            # Person not found
            print(f"Person with name '{name}' not found.")
        else:
            # Handle other status codes as needed
            print(f"Failed to update person. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

def delete_person_by_name(name):
    try:
        # Send a DELETE request to remove a person by name
        response = requests.delete(f'{api_url}/{name}')

        if response.status_code == 200:
            # Successful response, print the deletion message
            deletion_message = response.json()
            print(deletion_message)
        elif response.status_code == 404:
            # Person not found
            print(f"Person with name '{name}' not found.")
        else:
            # Handle other status codes as needed
            print(f"Failed to delete person. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Replace 'John' with the name of the person you want to update or delete
    person_name = 'Jared'

    # Data for updating the person (modify as needed)
    update_data = {
        "name": "Updated Name",
        "age": 30,
        "email": "updated@example.com"
    }

    # Test updating the person
    update_person_by_name(person_name, update_data)

    # Test deleting the person
    delete_person_by_name("jane")
