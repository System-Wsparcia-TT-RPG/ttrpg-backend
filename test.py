path = "docs/resources/spells.json"

import json
import requests



url = "http://localhost:8000/api/spell/create/"

# Define the JSON data
data = {
  "casting_time": "1 action",
  "classes": [
    "cleric",
    "paladin"
  ],
  "components": {
    "material": False,
    "raw": "V",
    "somatic": False,
    "verbal": True
  },
  "description": "You speak a one-word command to a creature you can see within range. The target must succeed on a Wisdom saving throw or follow the command on its next turn. The spell has no effect if the target is undead, if it doesn\u2019t understand your language, or if your command is directly harmful to it.\n\nSome typical commands and their effects follow. You might issue a command other than one described here. If you do so, the DM determines how the target behaves. If the target can\u2019t follow your command, the spell ends.\n\nApproach: The target moves toward you by the shortest and most direct route, Ending its turn if it moves within 5 feet of you.\nDrop: The target drops whatever it is holding and then ends its turn.\nFlee: The target spends its turn moving away from you by the fastest available means.\nGrovel: The target falls prone and then ends its turn.\nHalt: The target doesn't move and takes no Actions. A flying creature stays aloft, provided that it is able to do so. If it must move to stay aloft, it flies the minimum distance needed to remain in the air.",
  "duration": "1 round",
  "higher_levels": "When you cast this spell using a spell slot of 2nd level or higher, you can affect one additional creature for each slot level above 1st. The creatures must be within 30 feet of each other when you target them.",
  "level": "1",
  "name": "Command",
  "range": "60 feet",
  "ritual": False,
  "school": "enchantment",
  "tags": [
    "cleric",
    "paladin",
    "level1"
  ],
  "type": "1st-level enchantment"
}

# Convert the data to JSON format
json_data = json.dumps(data)

# Send the POST request
response = requests.post(url, data=json_data)

# Print the response
print(response.json())