import requests

# Replace with the actual URL of your API endpoint
url = 'http://localhost:5000/api/'

# Replace with the user ID you want to retrieve
user_id = 1  # Change this to the desired user ID

# Send a GET request to retrieve a person by user ID
response = requests.get(url + str(user_id))

if response.status_code == 200:
    print("Person retrieved successfully:")
    print(response.json())
elif response.status_code == 404:
    print("Person not found.")
else:
    print("Failed to retrieve person.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
