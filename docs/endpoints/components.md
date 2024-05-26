# Components API Endpoints

## GET /api/components/all/{depth}/

This endpoint retrieves all components.

- Method: `GET`
- URL: `/api/components/all/{depth}/`
- URL Parameters: `depth` (required) - The depth of serialization. Cannot be negative.
- Success Response:
  - Code: `200`
  - Content: List of all components with their details (all fields + id).

## GET /api/components/{identifier}/{depth}/

This endpoint retrieves a specific components by its ID.

- Method: `GET`
- URL: `/api/components/{identifier}/{depth}/`
- URL Parameters: `identifier` (required) - The ID of the components to retrieve, `depth` (required) - The depth of serialization. Cannot be negative.
- Success Response:
  - Code: `200`
  - Content: Details of the requested components (all fields + id).
- Error Response:
  - Code: `404`
  - Content: `{ "error": "Components not found" }`

## PATCH /api/components/{identifier}/

This endpoint updates a specific components by its ID.

- Method: `PATCH`
- URL: `/api/components/{identifier}/`
- URL Parameters: `identifier` (required) - The ID of the components to update.
- Data Parameters: JSON object with fields to update (HTTP Request Body - JSON).
- Success Response:
  - Code: `200`
  - Content: Updated details of the components (id).
- Error Response:
  - Code: `404`
  - Content: `{ "error": "Components not found" }`
  - Code: `400`
  - Content: `{ "error": "Invalid Components data", "details": error details }`

## PUT /api/components/{identifier}/

This endpoint replaces a specific components by its ID.

- Method: `PUT`
- URL: `/api/components/{identifier}/`
- URL Parameters: `identifier` (required) - The ID of the components to replace.
- Data Parameters: JSON object with new components data (HTTP Request Body - JSON).
- Success Response:
  - Code: `200`
  - Content: New details of the components (id).
  - Code: `201`
  - Content: New details of the components that have been created (id).
- Error Response:
  - Code: `400`
  - Content: `{ "error": "Invalid Components data", "details": error details }`

## DELETE /api/components/{identifier}/

This endpoint deletes a specific Components by its ID.

- Method: `DELETE`
- URL: `/api/components/{identifier}/`
- URL Parameters: `identifier` (required) - The ID of the components to delete.
- Success Response:
  - Code: `200`
  - Content: `{ "deleted_objects": count }` where `count` is the number of deleted objects.
- Error Response:
  - Code: `404`
  - Content: `{ "error": "Components not found" }`

## POST /api/components/create/

This endpoint creates a new components.

- Method: `POST`
- URL: `/api/components/create/`
- Data Parameters: JSON object with new components data (HTTP Request Body - JSON).
- Success Response:
  - Code: `201`
  - Content: Details of the created components (id).
- Error Response:
  - Code: `400`
  - Content: `{ "error": "Invalid Components data", "details": error details }`