import requests

# Define the base URL for your Flask API
base_url = 'http://localhost:5000/api'

# User ID of the user you want to update
user_id_to_update = 1

# Data to update the user with
update_data = {
    "name": "Updated Name",
    "age": 35,
    "email": "updated_email@example.com"
}

# Send a PUT request to update the user
update_response = requests.put(f'{base_url}/{1}', json=update_data)

if update_response.status_code == 200:
    print("User updated successfully.")
    updated_user = update_response.json()
    print("Updated User:")
    print(updated_user)
else:
    print("Failed to update user.")
    print(update_response.status_code, update_response.text)
