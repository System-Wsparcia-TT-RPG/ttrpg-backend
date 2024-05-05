
from typing import Tuple
from typing import List
import json

def validate_character(character_json) -> bool:
    # Main method agregating all other helper methods for character validation

    return character_fields_exist(character_json)[0]

def character_fields_exist(character_json) -> Tuple[bool, List[str], List[str]]:
    # This method checks whether all the necessary keys are present in the JSON (we don't validate the actual data in the keys)
    # Returns: bool (json valid or not), missing_fields (which dict keys are missing), bad_field_types (which keys have wrong types)
    
    required_fields = [('nickname', str), ('player', dict), ('xp', int), ('race', dict), ('alignment', str), 
                       ('classes', list), ('background', dict), ('details', dict), ('weapon_proficiencies', list), ('armor_proficiencies', list),
                       ('tool_proficiencies', list), ('feats', list), ('spells', list), ('weapons', list), ('equipment', list), ('treasure', dict),
                       ('Ability Scores', dict), ('Skills', dict), ('Saving Throws', dict), ('Combat', dict)]
    
    return validate_json_keys(character_json, required_fields)

def validate_race(race_json) -> bool:
    # Validates "race" field of the character json

    # TODO: actually check if values stored in these fields corelate with expected values

    return race_fields_exist(race_json) and validate_race_actions(race_json['actions']) and validate_race_traits(race_json['traits'] and validate_source(race_json['source']))

def race_fields_exist(race_json) -> Tuple[bool, List[str], List[str]]:
    # Validate that all fields within the "race" key of the character are within spec.
    # Returns: bool (json valid or not), missing_fields (which dict keys are missing), bad_field_types (which keys have wrong types)
    required_fields = [('name', str), ('subtype', str), ('size', str), ('traits', list),
                       ('actions', list), ('senses', dict), ('source', dict)]
    
    return validate_json_keys(race_json, required_fields)

def validate_source(source_json) -> bool:
    # Validates a "source" field in the character json
    required_source_fields = [('text', str), ('note', str), ('href', str)]
    return validate_json_keys(source_json, required_source_fields)[0]

def validate_damage_dice(damage_dice_json) -> bool:
    # Validates a "damage_dice" field in character json
    required_damage_dice_fields = [('count', int), ('sides', int), ('mod', 0)]

    return validate_json_keys(damage_dice_json, required_damage_dice_fields)[0]

def validate_race_traits(traits: list) -> bool:
    # Check if every trait from the race trait list is valid
    required_trait_fields = [('name', str), ('description', str), ('source', dict)]

    for trait in traits:
        if validate_json_keys(trait, required_trait_fields)[0]:
            if not validate_source(trait['source']):
                return False
        else:
            return False
    return True

def validate_race_actions(actions: list) -> bool:
    # Check if every race action is valid
    required_action_fields = [('name', str), ('description', str), ('attack_bonus', int), ('damage_dice', dict),
                              ('damage_bonus', int), ('legendary', bool), ('reaction', bool), ('source', dict)]

    for action in actions:
        if validate_json_keys(action, required_action_fields)[0]:
            if not validate_damage_dice(action['damage_dice']) or not validate_source(action['source']):
                return False
        else: return False
    
    return True


def validate_json_keys(checked_json, required_fields : List[Tuple[str, type]]) -> Tuple[bool, List[str], List[str]]:
    # Validates that all fields and types within required_fields are present in checked_json
    missing_fields = []
    bad_field_types = []

    for field, field_type in required_fields:
        if checked_json.get(field) is None:
            missing_fields.append(field)
        elif type(checked_json.get(field)) is not field_type:
            bad_field_types.append(field)

    return (len(missing_fields) == 0 and len(bad_field_types) == 0, missing_fields, bad_field_types)


def expected_str_value(actual_value:str, expected_values:List[str], case_sensitive:bool = False) -> bool:
    if case_sensitive:
        return actual_value in expected_values
    else:
        return actual_value.lower() in [a.lower() for a in expected_values]
#     print(character_fields_exist(json_obj))
#     print(validate_race_traits(json_obj['race']['traits']))