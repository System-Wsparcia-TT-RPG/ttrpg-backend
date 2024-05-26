# Race API Endpoints

## GET /api/race/size/possible/

This endpoint retrieves all possible size combinations.

- Method: `GET`
- URL: `/api/race/size/possible/`
- Success Response:
  - Code: `200`
  - Content: List of all possible size values.

## GET /api/race/all/{depth}/

This endpoint retrieves all races.

- Method: `GET`
- URL: `/api/race/all/{depth}/`
- URL Parameters: `depth` (required) - The depth of serialization. Cannot be negative.
- Success Response:
  - Code: `200`
  - Content: List of all races with their details (all fields + id).

## GET /api/race/{identifier}/{depth}/

This endpoint retrieves a specific race by its ID.

- Method: `GET`
- URL: `/api/race/{identifier}/{depth}/`
- URL Parameters: `identifier` (required) - The ID of the race to retrieve, `depth` (required) - The depth of serialization. Cannot be negative.
- Success Response:
  - Code: `200`
  - Content: Details of the requested race (all fields + id).
- Error Response:
  - Code: `404`
  - Content: `{ "error": "Race not found" }`

## PATCH /api/race/{identifier}/

This endpoint updates a specific race by its ID.

- Method: `PATCH`
- URL: `/api/race/{identifier}/`
- URL Parameters: `identifier` (required) - The ID of the race to update.
- Data Parameters: JSON object with fields to update (HTTP Request Body - JSON).
- Success Response:
  - Code: `200`
  - Content: Updated details of the race (id).
- Error Response:
  - Code: `404`
  - Content: `{ "error": "Race not found" }`
  - Code: `400`
  - Content: `{ "error": "Invalid Race data", "details": error details }`

## PUT /api/race/{identifier}/

This endpoint replaces a specific race by its ID.

- Method: `PUT`
- URL: `/api/race/{identifier}/`
- URL Parameters: `identifier` (required) - The ID of the race to replace.
- Data Parameters: JSON object with new race data (HTTP Request Body - JSON).
- Success Response:
  - Code: `200`
  - Content: New details of the race (id).
  - Code: `201`
  - Content: New details of the race that has been created (id).
- Error Response:
  - Code: `400`
  - Content: `{ "error": "Invalid Race data", "details": error details }`

## DELETE /api/race/{identifier}/

This endpoint deletes a specific race by its ID.

- Method: `DELETE`
- URL: `/api/race/{identifier}/`
- URL Parameters: `identifier` (required) - The ID of the race to delete.
- Success Response:
  - Code: `200`
  - Content: `{ "deleted_objects": count }` where `count` is the number of deleted objects.
- Error Response:
  - Code: `404`
  - Content: `{ "error": "Race not found" }`

## POST /api/race/create/

This endpoint creates a new race.

- Method: `POST`
- URL: `/api/race/create/`
- Data Parameters: JSON object with new race data (HTTP Request Body - JSON).
- Success Response:
  - Code: `201`
  - Content: Details of the created race (id).
- Error Response:
  - Code: `400`
  - Content: `{ "error": "Invalid Race data", "details": error details }`