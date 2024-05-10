# Endpoints Documentation

## API

### Character

* ENDPOINT - `api/character/all/[GET]`
  * Description - Returns all known character objects as json with foreign keys present to related objects.
  * Request:
	```bash
	curl -X GET http://localhost:8000/api/character/all/
	```
  * Response POSITIVE(status=200):
	```json
	{
	  "characters": [
	    {
	      "id": 1,
	      "nickname": "John Baldur",
	      "player_id": 1,
	      "xp": 15200,
	      "race_id": 1,
	      "background_id": 1,
	      "details_id": 1,
	      "weapon_proficiencies": [
	        "Simple",
	        "Martial"
	      ],
	      "armor_proficiencies": [
	        "Light",
	        "Medium",
	        "Heavy",
	        "Shields"
	      ],
	      "tool_proficiencies": [
	        "Smith's Tools",
	        "Brewer's Supplies"
	      ],
	      "treasure_id": 1,
	      "ability_scores_id": 1,
	      "skills_id": 1,
	      "saving_throws_id": 1,
	      "combat_id": 1
	    }
	  ]
	}
	```
* ENDPOINT - `api/character/<int:character_id>/[GET]`
  * Description - Returns object of a character with given id as json with foreign keys present to related objects.
  * Request:
    ```bash
    curl -X GET http://localhost:8000/api/character/1/
    ```
  * Response POSITIVE(status=200):
    ```json
    {
      "character": {
        "id": 1,
        "nickname": "John Baldur",
        "player": 1,
        "xp": 15200,
        "race": 1,
        "background": 1,
        "details": 1,
        "weapon_proficiencies": [
          "Simple",
          "Martial"
        ],
        "armor_proficiencies": [
          "Light",
          "Medium",
          "Heavy",
          "Shields"
        ],
        "tool_proficiencies": [
          "Smith's Tools",
          "Brewer's Supplies"
        ],
        "treasure": 1,
        "ability_scores": 1,
        "skills": 1,
        "saving_throws": 1,
        "combat": 1
      }
    }
    ```
  * Request:
    ```bash
    curl -X GET http://localhost:8000/api/character/9999999999/
    ```
  * Response NEGATIVE(status=404):
    ```json
    {
      "error": "Character with specified id is not found!",
      "details": "Character matching query does not exist.",
      "error_data": {
        "id_not_found": 9999999999
      }
    }
    ```
  