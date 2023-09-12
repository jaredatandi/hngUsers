import requests

# Replace with the appropriate URL and user_id you want to delete
base_url = 'http://localhost:5000/api'  # Update the URL
user_id_to_delete = 1  # Update with the user ID you want to delete

# Send a DELETE request to the API
delete_url = f'{base_url}/{user_id_to_delete}'

response = requests.delete(delete_url)

if response.status_code == 200:
    print(f"Person with ID {user_id_to_delete} deleted successfully.")
elif response.status_code == 404:
    print(f"Person with ID {user_id_to_delete} not found.")
else:
    print("Failed to delete person.")
    print(response.status_code, response.text)
