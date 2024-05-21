# Damage Dice API Endpoints

## GET /api/damage_dice/size/possible/

This endpoint retrieves all possible size combinations.

- Method: `GET`
- URL: `/api/damage_dice/size/possible/`
- Success Response:
  - Code: `200`
  - Content: List of all possible size values.

## GET /api/damage_dice/all/{depth}/

This endpoint retrieves all damage dices.

- Method: `GET`
- URL: `/api/damage_dice/all/{depth}/`
- URL Parameters: `depth` (required) - The depth of serialization. Cannot be negative.
- Success Response:
  - Code: `200`
  - Content: List of all damage dices with their details (all fields + id).

## GET /api/damage_dice/{identifier}/{depth}/

This endpoint retrieves a specific damage dice by its ID.

- Method: `GET`
- URL: `/api/damage_dice/{identifier}/{depth}/`
- URL Parameters: `identifier` (required) - The ID of the damage dice to retrieve, `depth` (required) - The depth of serialization. Cannot be negative.
- Success Response:
  - Code: `200`
  - Content: Details of the requested damage dice (all fields + id).
- Error Response:
  - Code: `404`
  - Content: `{ "error": "DamageDice not found" }`

## PATCH /api/damage_dice/{identifier}/

This endpoint updates a specific damage dice by its ID.

- Method: `PATCH`
- URL: `/api/damage_dice/{identifier}/`
- URL Parameters: `identifier` (required) - The ID of the damage dice to update.
- Data Parameters: JSON object with fields to update (HTTP Request Body - JSON).
- Success Response:
  - Code: `200`
  - Content: Updated details of the damage dice (id).
- Error Response:
  - Code: `404`
  - Content: `{ "error": "DamageDice not found" }`
  - Code: `400`
  - Content: `{ "error": "Invalid DamageDice data", "details": error details }`

## PUT /api/damage_dice/{identifier}/

This endpoint replaces a specific damage dice by its ID.

- Method: `PUT`
- URL: `/api/damage_dice/{identifier}/`
- URL Parameters: `identifier` (required) - The ID of the damage dice to replace.
- Data Parameters: JSON object with new damage dice data (HTTP Request Body - JSON).
- Success Response:
  - Code: `200`
  - Content: New details of the damage dice (id).
  - Code: `201`
  - Content: New details of the damage dice has been created (id).
- Error Response:
  - Code: `400`
  - Content: `{ "error": "Invalid DamageDice data", "details": error details }`

## DELETE /api/damage_dice/{identifier}/

This endpoint deletes a specific damage dice by its ID.

- Method: `DELETE`
- URL: `/api/damage_dice/{identifier}/`
- URL Parameters: `identifier` (required) - The ID of the damage dice to delete.
- Success Response:
  - Code: `200`
  - Content: `{ "deleted_objects": count }` where `count` is the number of deleted objects.
- Error Response:
  - Code: `404`
  - Content: `{ "error": "DamageDice not found" }`

## POST /api/damage_dice/create/

This endpoint creates a new damage dice.

- Method: `POST`
- URL: `/api/damage_dice/create/`
- Data Parameters: JSON object with new damage dice data (HTTP Request Body - JSON).
- Success Response:
  - Code: `201`
  - Content: Details of the created damage dice (id).
- Error Response:
  - Code: `400`
  - Content: `{ "error": "Invalid DamageDice data", "details": error details }`