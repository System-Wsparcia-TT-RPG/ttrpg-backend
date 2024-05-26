# Character API Endpoints

## GET /api/character/all/{depth}/

This endpoint retrieves all characters.

- Method: `GET`
- URL: `/api/character/all/{depth}/`
- URL Parameters: `depth` (required) - The depth of serialization. Cannot be negative.
- Success Response:
  - Code: `200`
  - Content: List of all characters with their details (all fields + id).

## GET /api/character/{identifier}/{depth}/

This endpoint retrieves a specific character by its ID.

- Method: `GET`
- URL: `/api/character/{identifier}/{depth}/`
- URL Parameters: `identifier` (required) - The ID of the character to retrieve, `depth` (required) - The depth of serialization. Cannot be negative.
- Success Response:
  - Code: `200`
  - Content: Details of the requested character (all fields + id).
- Error Response:
  - Code: `404`
  - Content: `{ "error": "Character not found" }`

## PATCH /api/character/{identifier}/

This endpoint updates a specific character by its ID.

- Method: `PATCH`
- URL: `/api/character/{identifier}/`
- URL Parameters: `identifier` (required) - The ID of the character to update.
- Data Parameters: JSON object with fields to update (HTTP Request Body - JSON).
- Success Response:
  - Code: `200`
  - Content: Updated details of the character (id).
- Error Response:
  - Code: `404`
  - Content: `{ "error": "Character not found" }`
  - Code: `400`
  - Content: `{ "error": "Invalid Character data", "details": error details }`

## PUT /api/character/{identifier}/

This endpoint replaces a specific character by its ID.

- Method: `PUT`
- URL: `/api/character/{identifier}/`
- URL Parameters: `identifier` (required) - The ID of the character to replace.
- Data Parameters: JSON object with new character data (HTTP Request Body - JSON).
- Success Response:
  - Code: `200`
  - Content: New details of the character (id).
  - Code: `201`
  - Content: New details of the spell that has been created (id).
- Error Response:
  - Code: `400`
  - Content: `{ "error": "Invalid Character data", "details": error details }`

## DELETE /api/character/{identifier}/

This endpoint deletes a specific character by its ID.

- Method: `DELETE`
- URL: `/api/character/{identifier}/`
- URL Parameters: `identifier` (required) - The ID of the character to delete.
- Success Response:
  - Code: `200`
  - Content: `{ "deleted_objects": count }` where `count` is the number of deleted objects.
- Error Response:
  - Code: `404`
  - Content: `{ "error": "Character not found" }`

## POST /api/character/create/

This endpoint creates a new character.

- Method: `POST`
- URL: `/api/character/create/`
- Data Parameters: JSON object with new character data (HTTP Request Body - JSON).
- Success Response:
  - Code: `201`
  - Content: Details of the created character (id).
- Error Response:
  - Code: `400`
  - Content: `{ "error": "Invalid Character data", "details": error details }`