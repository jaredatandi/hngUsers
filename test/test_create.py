#!/usr/bin/env python3
import requests

# Replace with your API endpoint
url = 'http://localhost:5000/api'

# Data for creating a new person
data = {
    "name": "JDoe",
    "age": 85,
    "email": "johndoe@example.com"
}

try:
    # Send a POST request to create a new person
    response = requests.post(url, json=data)

    if response.status_code == 201:
        print("Person created successfully.")
        print(response.json())
    else:
        print("Failed to create person.")
        print(response.status_code, response.text)

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
