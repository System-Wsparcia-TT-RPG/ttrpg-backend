# Spell API Endpoints

## GET /api/spell/all/{depth}/

This endpoint retrieves all spells.

- Method: `GET`
- URL: `/api/spell/all/{depth}/`
- URL Parameters: `depth` (required) - The depth of serialization. Cannot be negative.
- Success Response:
  - Code: `200`
  - Content: List of all spells with their details (all fields + id).

## GET /api/spell/{identifier}/{depth}/

This endpoint retrieves a specific spell by its ID.

- Method: `GET`
- URL: `/api/spell/{identifier}/{depth}/`
- URL Parameters: `identifier` (required) - The ID of the spell to retrieve, `depth` (required) - The depth of serialization. Cannot be negative.
- Success Response:
  - Code: `200`
  - Content: Details of the requested spell (all fields + id).
- Error Response:
  - Code: `404`
  - Content: `{ "error": "Spell not found" }`

## PATCH /api/spell/{identifier}/

This endpoint updates a specific spell by its ID.

- Method: `PATCH`
- URL: `/api/spell/{identifier}/`
- URL Parameters: `identifier` (required) - The ID of the spell to update.
- Data Parameters: JSON object with fields to update (HTTP Request Body - JSON).
- Success Response:
  - Code: `200`
  - Content: Updated details of the spell (id).
- Error Response:
  - Code: `404`
  - Content: `{ "error": "Spell not found" }`
  - Code: `400`
  - Content: `{ "error": "Invalid Spell data", "details": error details }`

## PUT /api/spell/{identifier}/

This endpoint replaces a specific spell by its ID.

- Method: `PUT`
- URL: `/api/spell/{identifier}/`
- URL Parameters: `identifier` (required) - The ID of the spell to replace.
- Data Parameters: JSON object with new spell data (HTTP Request Body - JSON).
- Success Response:
  - Code: `200`
  - Content: New details of the spell (id).
  - Code: `201`
  - Content: New details of the spell that has been created (id).
- Error Response:
  - Code: `400`
  - Content: `{ "error": "Invalid Spell data", "details": error details }`

## DELETE /api/spell/{identifier}/

This endpoint deletes a specific Spell by its ID.

- Method: `DELETE`
- URL: `/api/spell/{identifier}/`
- URL Parameters: `identifier` (required) - The ID of the spell to delete.
- Success Response:
  - Code: `200`
  - Content: `{ "deleted_objects": count }` where `count` is the number of deleted objects.
- Error Response:
  - Code: `404`
  - Content: `{ "error": "Spell not found" }`

## POST /api/spell/create/

This endpoint creates a new spell.

- Method: `POST`
- URL: `/api/spell/create/`
- Data Parameters: JSON object with new spell data (HTTP Request Body - JSON).
- Success Response:
  - Code: `201`
  - Content: Details of the created spell (id).
- Error Response:
  - Code: `400`
  - Content: `{ "error": "Invalid Spell data", "details": error details }`