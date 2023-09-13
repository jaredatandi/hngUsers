# API Documentation

This document provides an overview of the endpoints available in my RESTful API.

## Base URL

The base URL for all API endpoints is `https://domain.com/api`.

## Endpoints

### 1. Create a new person

- **URL:** `/api`
- **HTTP Method:** POST
- **Description:** Create a new person with the provided data.
- **Request Format:**
  - JSON object with the following fields:
    - `name` (string, required): The name of the person.
    - `age` (integer): The age of the person.
    - `email` (string): The email address of the person.
- **Response Format:**
  - Successful response (HTTP status code 201):
    - JSON object with the created person's details.
  - Error response (HTTP status code 400):
    - JSON object with an error message if the request is invalid.

### 2. Retrieve details of a person by ID or name

- **URL:** `/api/<string:name_or_id>`
- **HTTP Method:** GET
- **Description:** Retrieve details of a person by their name or ID.
- **Request Format:**
  - URL parameter `<string:name_or_id>`: The name or ID of the person to retrieve.
- **Response Format:**
  - Successful response (HTTP status code 200):
    - JSON object with the person's details.
  - Error response (HTTP status code 404):
    - JSON object with an error message if the person is not found.

### 3. Update details of an existing person by ID or name

- **URL:** `/api/<string:name_or_id>`
- **HTTP Method:** PUT
- **Description:** Update details of an existing person by their name or ID.
- **Request Format:**
  - URL parameter `<string:name_or_id>`: The name or ID of the person to update.
  - JSON object with the following fields:
    - `name` (string, required): The updated name of the person.
    - `age` (integer): The updated age of the person.
    - `email` (string): The updated email address of the person.
- **Response Format:**
  - Successful response (HTTP status code 200):
    - JSON object with the updated person's details.
  - Error response (HTTP status code 404 or 400):
    - JSON object with an error message if the person is not found or the request is invalid.

### 4. Remove a person by ID or name

- **URL:** `/api/<string:name_or_id>`
- **HTTP Method:** DELETE
- **Description:** Remove a person by their name or ID.
- **Request Format:**
  - URL parameter `<string:name_or_id>`: The name or ID of the person to delete.
- **Response Format:**
  - Successful response (HTTP status code 200):
    - JSON object with a success message.
  - Error response (HTTP status code 404):
    - JSON object with an error message if the person is not found.

## Usage

You can use various HTTP clients, such as Postman or cURL, to interact with these endpoints. Ensure that you provide valid JSON data for POST and PUT requests.

## Notes

- All endpoints should be accessed over HTTPS for security.
- Error responses may include additional details about the specific error encountered.