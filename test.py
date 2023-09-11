#!/usr/bin/env python3
import requests

# Replace with your API endpoint
url = 'http://localhost:5000/api/stats'

data = {
    "name": "Jane",
    "age": 28,
    "email": "jane@example.com"
}

response = requests.get(url, json=data)

if response.status_code == 201:
    print("Person created successfully.")
    print(response.json())
else:
    print("Failed to create person.")
    print(response.status_code, response.text)
